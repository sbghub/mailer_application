import xlrd
import json
import pprint
from os.path import join, dirname, abspath
from xlrd.sheet import ctype_text
from collections import OrderedDict

def open_file(path):

	fname = join(dirname(dirname(abspath(__file__))), 'Documents', 'roccStuff.xlsx')

	xl_workbook = xlrd.open_workbook(fname)
	book = xlrd.open_workbook("roccStuff.xlsx")
	sheet_names = xl_workbook.sheet_names()
	print("SHEET NAMES", sheet_names)
	xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
	checkboxes = xl_workbook.sheet_by_name(sheet_names[1])

if __name__ == "__main__":
    path = "roccStuff.xlsx"
    open_file(path)