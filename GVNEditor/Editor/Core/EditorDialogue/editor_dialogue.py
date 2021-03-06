"""
    This file is part of GVNEditor.

    GVNEditor is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GVNEditor is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with GVNEditor.  If not, see <https://www.gnu.org/licenses/>.
"""
import copy
from Editor.Interface.EditorDialogue.editor_dialogue import EditorDialogueUI
from Editor.Interface.EditorDialogue.dialogue_entry import DialogueEntry
from PyQt5 import QtWidgets

class EditorDialogue():
    def __init__(self, settings, logger):
        self.settings = settings
        self.logger = logger

        self.logger.Log("Initializing Dialogue Editor...")

        # Build the Dialogue Editor UI
        self.ed_ui = EditorDialogueUI(self)

    def UpdateActiveEntry(self):
        """ Makes the selected entry the active one, refreshing the details panel """
        print("Changing active entry")

        selection = self.GetSelectedEntry()

        # Refresh the details panel to reflect the newly chosen row
        self.UpdateDetails(selection)

    # ****** TOOLBAR BUTTON FUNCTIONS ******

    def AddEntry(self, action_data: dict, specific_row: int = None) -> DialogueEntry:
        """ Given a block of action data from the action database, create a new entry in the dialogue sequence """
        print("Adding new dialogue entry")

        # Create a new, empty row. Allow optional row position specification, but default to the end of the sequence
        new_entry_row = self.ed_ui.dialogue_sequence.rowCount()
        if specific_row is not None:
            new_entry_row = specific_row
            self.ed_ui.dialogue_sequence.insertRow(new_entry_row)
        else:
            self.ed_ui.dialogue_sequence.insertRow(new_entry_row)

        # Create a new dialogue entry object, and add it to the sequence widget
        new_entry = DialogueEntry(action_data, self.settings, self.UpdateActiveEntry)

        # Assign the entry widget to the row
        self.ed_ui.dialogue_sequence.setCellWidget(new_entry_row, 0, new_entry)
        self.ed_ui.dialogue_sequence.selectRow(new_entry_row)

        # Resize the row to fit any contents it has
        self.ed_ui.dialogue_sequence.resizeRowToContents(new_entry_row)

        self.logger.Log(f"Adding new dialogue sequence entry")

        return new_entry

    def RemoveEntry(self):
        """ If an entry is selected, delete it from the table """
        selection = self.GetSelectedRow()

        if selection is not None:
            self.ed_ui.dialogue_sequence.removeRow(self.GetSelectedRow())


    def CopyEntry(self):
        """ If an entry is selected, clone it and add it to the sequence """
        selection = self.GetSelectedEntry()

        if selection:
            self.AddEntry(selection.action_data)

    def MoveEntryUp(self):
        """ If an entry is selected, move it up one row """

        if self.ed_ui.dialogue_sequence.rowCount():
            selection = self.GetSelectedRow()

            # Only allow moving up if we're not already at the top of the sequence
            if selection == 0:
                self.logger.Log("Warning: Can't move entry up as we're at the top of the sequence")
            else:
                # 'cellWidget' returns a pointer which becomes invalid once we override it's row. Given this, instead
                # of gently moving the row, we recreate it by transferring it's data to a newly created entry
                taken_entry = self.ed_ui.dialogue_sequence.cellWidget(selection, 0)

                # Delete the origin row
                self.ed_ui.dialogue_sequence.removeRow(selection)

                # Add a new entry two rows above the initial row
                new_row_num = selection - 1
                new_entry = self.AddEntry(taken_entry.action_data, new_row_num)

                # Transfer the data from the original entry to the new one, before refreshing the details
                new_entry.cache_data = taken_entry.cache_data
                self.UpdateActiveEntry()

    def MoveEntryDown(self):
        """ If an entry is selected, move it down one row """

        if self.ed_ui.dialogue_sequence.rowCount():
            selection = self.GetSelectedRow()

            # Only allow moving down if we're not already at the bottom of the sequence
            if selection + 1 >= self.ed_ui.dialogue_sequence.rowCount():
                self.logger.Log("Warning: Can't move entry down as we're at the bottom of the sequence")
            else:
                # 'cellWidget' returns a pointer which becomes invalid once we override it's row. Given this, instead
                # of gently moving the row, we recreate it by transferring it's data to a newly created entry
                taken_entry = self.ed_ui.dialogue_sequence.cellWidget(selection, 0)

                # Delete the origin row
                self.ed_ui.dialogue_sequence.removeRow(selection)

                # Add a new entry two rows above the initial row
                new_row_num = selection + 1
                new_entry = self.AddEntry(taken_entry.action_data, new_row_num)

                # Transfer the data from the original entry to the new one, before refreshing the details
                new_entry.cache_data = taken_entry.cache_data
                self.UpdateActiveEntry()

    def UpdateDetails(self, selected_entry):
        """ Refreshes the details panel with the details from the selected dialogue entry """
        if selected_entry:
            self.ed_ui.details.PopulateDetails(selected_entry)

        # No entries left to select. Wipe remaining details
        else:
            self.ed_ui.details.Clear()

    def GetSelectedEntry(self) -> DialogueEntry:
        """ Returns the currently selected dialogue entry. If there isn't one, returns None """
        selected_entry = self.ed_ui.dialogue_sequence.selectedIndexes()

        if selected_entry:
            selected_row = selected_entry[0].row()
            return self.ed_ui.dialogue_sequence.cellWidget(selected_row, 0)
        else:
            return None

    def GetSelectedRow(self) -> int:
        """ Returns the currently selected row. If there isn't one, returns None """
        selected_row = self.ed_ui.dialogue_sequence.selectedIndexes()

        if selected_row:
            return selected_row[0].row()
        else:
            return None



