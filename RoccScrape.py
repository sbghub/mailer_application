import xlrd
import json
import pprint
from os.path import join, dirname, abspath
from xlrd.sheet import ctype_text
from collections import OrderedDict


def return_sheet_headers(sheet):
	num_cols = sheet.ncols
	num_rows = sheet.nrows

	for col in range(num_cols):
		header_value = sheet.cell(0, col).value
		if header_value: print("cell param", header_value)
	
	print("Num-rows: ", num_rows)
	pass

def scrape_excel_file(path):

	fname = join(dirname(dirname(abspath(__file__))), 'mailer_application', 'roccStuff.xlsx')

	xl_workbook = xlrd.open_workbook(fname)
	book = xlrd.open_workbook("roccStuff.xlsx")
	sheet_names = xl_workbook.sheet_names()
	
	for sheet in sheet_names:
		print("SHEET NAMED", sheet)
		sheet = xl_workbook.sheet_by_name(sheet)
		return_sheet_headers(sheet)


if __name__ == "__main__":
    path = "roccStuff.xlsx"
    scrape_excel_file(path)