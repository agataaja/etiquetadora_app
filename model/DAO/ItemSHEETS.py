from connection import SHEETDB


class ItemSheets:

    def insert(self, object):

        self.sheet_objct = SHEETDB.setup_google_sheet(0)

        self.sheet_objct.append_row(object)


class PersonSheet:

    def get_last_id(self):

        sheet = SHEETDB.setup_google_sheet(1)
        # Assume the ID is in the first column (A)
        col_values = sheet.col_values(2)

        print(col_values)
        if len(col_values) > 1:  # Che
            # ck if there are rows beyond the header
            print('last_id =', int(col_values[-1]))
            return int(col_values[-1])
        return 0  # Return 0 if no persons are registered yet

    def insert(self, object):

        self.sheet_objct = SHEETDB.setup_google_sheet(1)

        self.sheet_objct.append_row(object)

