import xlrd
import json
import pprint
from os.path import join, dirname, abspath
from xlrd.sheet import ctype_text
from collections import OrderedDict
 
#----------------------------------------------------------------------
def open_file(path):
    """
    Open and read an Excel file

    """
    pp = pprint.PrettyPrinter(indent=4)
    fname = join(dirname(dirname(abspath(__file__))), 'Documents', 'Global_Ordering.xlsm')

    xl_workbook = xlrd.open_workbook(fname)
    book = xlrd.open_workbook("Global_Ordering.xlsm")
    sheet_names = xl_workbook.sheet_names()
    print("SHEET NAMES", sheet_names)
    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
    checkboxes = xl_workbook.sheet_by_name(sheet_names[1])




    num_cols = xl_sheet.ncols 
    checkbox_cols = checkboxes.ncols

    matchValues = []
    rowVals = []
    colVals = []
    cellVals = []
    combineVals = []
    ValsArray = []
    matchValuesObj = {}

    for row_idx in range(145):    # Iterate through rows
        print("FIRST ITERATION")
        print ('-'*40)

        print ('Row: %s' % row_idx)   # Print row number
        for col_idx in range(0, num_cols):  # Iterate through columns
           
            cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col

            matchValuesObj = {'Row Number': row_idx}

            print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj.value))
            if cell_obj.value != '':

                matchValues.append(cell_obj.value)
                rowVals.append(row_idx)
                colVals.append(col_idx)
                cellVals.append(cell_obj.value)
                coordinates = dict(zip(rowVals, colVals ))
                list_key_value = [ [k,v] for k, v in coordinates.items() ]
                ValsArray.append(coordinates.items())
                combineVals = (list_key_value[-1], cellVals[-1])
                # print("COMBINE VALS")
                # print(combineVals)

                print("LIST KEY VALUE")
                print(combineVals)


    pp.pprint(matchValues)
    # pp.pprint(matchValuesObj)

    
    for row_idx in range(130):
        print("SECOND ITERATION")
           
        
        print ('Row: %s' % row_idx)   # Print row number
        for col_idx in range(0, checkbox_cols):

            checkboxLogic =  checkboxes.cell(row_idx, col_idx)
            print ('Column: [%s] cell_obj: [%s]' % (col_idx, checkboxLogic))

            # if checkboxLogic.value != '':
    
    # print number of sheets
    # print(book.nsheets)
 
    # print sheet names
    # print(book.sheet_names())
 
    # get the first worksheet
    # print("SHEET BY INDEX")
    first_sheet = book.sheet_by_index(0)
    # print("YO")
    # print(first_sheet)
 
    # read a row
    # print("FIRST ROW OVER HERE")
    first_sheet.row_values(rowx=0, start_colx=0, end_colx=9)
 
    # read a cell
    # print("CELL")
   
    cell = first_sheet.cell(0,0)
    cells = first_sheet.row_slice(rowx=0, start_colx=0, end_colx=9)
    col = first_sheet.cell(0,0)
    cols = first_sheet.col_slice(colx=2,  start_rowx=0, end_rowx=145)
   
    n = 0
    for cell in cells:
     n += 1
    
     # print(n)

     # print ("CELL ValUE")
     # print(cell.value)
     # print("CELLS")
     # print(cols)
     # print(json.dumps(col))
   
    # mapp = first_sheet.cell_note_map()
    # print("MAPP", mapp)

if __name__ == "__main__":
    path = "Global_Ordering.xlsm"
    open_file(path)