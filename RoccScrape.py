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


def return_sheet_headers(sheet):
	num_cols = sheet.ncols
	num_rows = sheet.nrows

	for col in range(num_cols):
		header_value = sheet.cell(0, col).value
		if header_value == "Field #":
			for row in range(num_rows):
				value = sheet.cell(row, col).value
				if value: print("{}  coords: ({},{})".format(value, row, col))

			print("Super Key: {}".format(header_value))

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
			sheet = xl_workbook.sheet_by_name(sheet)
			return_sheet_headers(sheet)


if __name__ == "__main__":
    path = "roccStuff.xlsx"
    scrape_excel_file(path)