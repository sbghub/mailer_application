import xlrd
import json
import pprint
from os.path import join, dirname, abspath
from xlrd.sheet import ctype_text
from collections import OrderedDict

def open_file(path):

	fname = join(dirname(dirname(abspath(__file__))), 'mailer_application', 'roccStuff.xlsx')

	xl_workbook = xlrd.open_workbook(fname)
	book = xlrd.open_workbook("roccStuff.xlsx")
	sheet_names = xl_workbook.sheet_names()
	
	for sheet in sheet_names:
		print("SHEET NAMED", sheet)
		sheet = xl_workbook.sheet_by_name(sheet)
		num_cols = sheet.ncols


		for col in range(num_cols):
			print("cell param", sheet.cell(0, col))
		print("-----end-sheet-----"*3)

if __name__ == "__main__":
    path = "roccStuff.xlsx"
    open_file(path)