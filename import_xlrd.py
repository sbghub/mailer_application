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

    # row = xl_sheet.row(0)  # 1st row
    # print(60*'-' + 'n(Column #) value [type]n' + 60*'-')
    # for idx, cell_obj in enumerate(row):
    #     cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
    #     print('(%s) %s [%s]' % (idx, cell_obj.value, cell_type_str, ))
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
                # matchValues.append(row_idx)
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
              
                
         
                # combineVals.append(coordinates)
                # # combineVals = dict(zip())

                # print(coordinates)
                # print(list_key_value)
                # tupl = (coordinates, cell_obj.value)
                # print(tupl)
                # pp.pprint(dictionary)
                # print(combineVals)
                # allValues = dict(zip(combineVals, cellVals))
                # print(allValues)
                # matchValuesObj = {'Row Number': row_idx}


    pp.pprint(matchValues)
    # pp.pprint(matchValuesObj)

    
    for row_idx in range(130):
        print("SECOND ITERATION")
           
        
        print ('Row: %s' % row_idx)   # Print row number
        for col_idx in range(0, checkbox_cols):

            checkboxLogic =  checkboxes.cell(row_idx, col_idx)
            print ('Column: [%s] cell_obj: [%s]' % (col_idx, checkboxLogic))

            # if checkboxLogic.value != '':
    # row_vals = []
    # for row_idx in range(0, xl_sheet.nrows):
    #  for col_idx in range(0, num_cols):
    #     cell_obj = xl_sheet.cell(row_idx, col_idx)
    #     cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
    #     print ('(row %s) %s (type:%s)' % (row_idx, cell_obj.value, cell_type_str))
       
        # row_vals.append(cell_obj.value)
        



    # Retrieve non-empty rows
    # nonempty_row_vals = [x for x in row_vals if x]    
    # num_rows_missing_vals = xl_sheet.nrows - len(nonempty_row_vals)
    # print ('Vals: %d; Rows Missing Vals: %d' % (len(nonempty_row_vals), num_rows_missing_vals))


    # row_vals = []
    # for row_idx in range(0, xl_sheet.nrows):
    #     cell_obj = xl_sheet.cell(row_idx, col_idx)
    #     cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
    #     print ('(row %s) %s (type:%s)' % (row_idx, cell_obj.value, cell_type_str))
    #     row_vals.append(cell_obj.value)
    
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
  

    # pushArray.append(cols)
   
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

    # for col in cols:
    #  print ("COL VALUE")
    #  print(col.value)
    #  print("COLS")
    #  print(cols)
    # read a row slice
    # print("READING A ROW SLICE")
    # print(first_sheet.row_slice(rowx=0,
    #                             start_colx=0,
    #                             end_colx=2))
 


#----------------------------------------------------------------------
if __name__ == "__main__":
    path = "Global_Ordering.xlsm"
    open_file(path)