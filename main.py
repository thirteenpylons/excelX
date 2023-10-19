"""
Streamline extracting data from excel

Having all of the excel files that you want to extract this data from in
the same directory and calling that dir within the method.

TODO:
    Add file parameter to all methods. Figure out if bulk or single... 
        if single couldn't that be done manually?

Author: Christian M. Fulton
Date: 19.Oct.2023
"""

class ExcelX:
    def __init__(self):
        pass

    def extract_cell(self, directory: str, cell: str):
        """
        extract from a single cell

        parameters:
            directory: the directory that has all of the excel docs
            cell: define the cell to extract from, "D15"

        preconditions:
            cell: Must be a string leading with a letter and tailed by integers.
        """
    
    def extract_range(self, directory: str, cell_letter: str, min: int, max: int):
        """
        Extract from a range of cells

        parameters: 
            directory: the directory that has all of the excel docs
            cell_letter: letters [a-z] designating cell
            min: minimum integer where to start extraction row
            max: maximum integer where to end. This will include a +1
        """
    
    def extract_cell_add_string_tail(self, cell: str):
        """
        Extract cell and add string to tail.
        """
