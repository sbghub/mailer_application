import xlrd
import json
import pprint
from os.path import join, dirname, abspath
from xlrd.sheet import ctype_text
from collections import OrderedDict

'''
The bottom of the file has the block where the 
main methods get called when calling this file.
'''

data = {}


def return_sheet_headers(sheet, sheet_name, sheet_obj):
	num_cols = sheet.ncols
	num_rows = sheet.nrows

	for col in range(num_cols):
		header_value = sheet.cell(0, col).value
		
		if header_value == "Field #":
			print("Super Key: {}".format(header_value))

			for row in range(num_rows):
				value = sheet.cell(row, col).value
				if value and value != "Field #": 
					sheet_obj[value] = {}
					print("{}  coords: ({},{})".format(value, row, col))

		elif header_value: 
			print("Key: {}".format(header_value))
	
	print("Num-rows: {}".format(num_rows))
	pass


def scrape_excel_file(path):
	fname = join(dirname(dirname(abspath(__file__))), 'mailer_application', 'roccStuff.xlsx')
	xl_workbook = xlrd.open_workbook(fname)
	book = xlrd.open_workbook("roccStuff.xlsx")
	sheet_names = xl_workbook.sheet_names()
	
	for sheet in sheet_names:
		if xl_workbook.sheet_by_name(sheet).nrows == 0:
			print("{} is blank.".format(sheet))
		else:
			print("SHEET NAMED : {}".format(sheet))
			data[sheet] = {}
			sheet_info = xl_workbook.sheet_by_name(sheet)
			return_sheet_headers(sheet_info, sheet, data[sheet])
	
	print()
	print("Data: {}".format(data))
	print()


if __name__ == "__main__":
    path = "roccStuff.xlsx"
    scrape_excel_file(path)