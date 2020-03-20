#!/usr/bin/env python

start = 1  # column QTY can be found in
end = 5    # column with CREDIT - TOTAL
width = 4  # width of boat sizes across the top

sections = [
    "TRAILER",
    "FABRICATION",
    "CANVAS",
    "PAINT",
    "OUTFITTING"
]

##  TOP BAND        #########################################################

# top of sheet, absolute row, absolute column - not by boat size
# [0] title, [1] column, [2] row, [3] default
topSection = [
    ["OPTION NUMBER", 3, 1, ""],
    ["OPTION NAME", 3, 2, ""],
    ["OPTION NOTES", 3, 3, ""],
    ["TOTAL COST", 3, 6, "0"],
    ["CALCULATED RETAIL", 3, 7, "0"],
    ["ADVERTISED RETAIL", 3, 8, "0"],
    ["CONTRIBUTION MARGIN", 3, 9, "0"],
	["TRAILER/MOTOR OVERHEAD", 4, 11, "N"],
	["SMALLEST BOAT", 4, 12, "18.5"],
	["LARGEST BOAT", 4, 13, "37"],
    ["DESIGN LABOR RATE", 4, 22, "0"],
]

# need design labor codes here ....


# top of sheet, calculated column, absolute row - by boat size
# [0] title, [1] column, [2] row, [3] default
costSummary = [
    [" TOTAL COST", 16, 2, "0"],
    [" RETAIL CALCULATED", 16, 3, "0"],
    [" RETAIL ADVERTISED", 16, 4, "0"],
    [" CONTRIBUTION MARGIN", 16, 5, "0"],
	[" LABOR COST", 16, 8, "0"],
	[" MATERIAL COST", 16, 9, "0"],
    [" OVEHEAD CALCULATION COST", 16, 10, "0"],
	[" RETAIL CALCULATED COST", 16, 11, "0"],
	[" CALCULATED DEALER INVOICE", 16, 12, "0"],
	[" LABOR CREDIT", 16, 15, "0"],
	[" MATERIAL CREDIT", 16, 16, "0"],
	[" OVERHEAD CALCULATION CREDIT", 16, 17, "0"],
	[" TOTAL CREDIT", 16, 18, "0"],
	[" RETAIL CALCULATED CREDIT", 16, 19, "0"],
]

##  SECTION BANDS  ##########################################################

# top of section, absolute column, offset row - not by boat size
# [0] title, [1] column, [2] row, [3] default
startSections = [
    [" CONSUMABLES", 2, -1, "0"],
    [" LABOR RATE", 4, -1, "0"],
]

# top of section, calculated column, offset row - by boat size
# [0] title, [1] column, [2] row, [3] default
startSectionsSize = [
    [" HOURS", 15, -1, "0"],
	[" HOURS TOTAL", 16, -1, "0"],
]

# bottom of section, calculated column, offset row
# [0] title, [1] column, [2] row, [3] default
endSections = [
    [" CREDIT TOTAL", 16, 0, "0"],
    [" COST SUBTOTAL", 16, 1, "0"],
    [" COST CONSUMABLES", 16, 2, "0"],
    [" COST TOTAL", 16, 3, "0"],
]

endSectionsSize = [
    [" CREDIT TOTAL", 16, 0, "0"],
    [" COST SUBTOTAL", 16, 1, "0"],
    [" COST CONSUMABLES", 16, 2, "0"],
    [" COST TOTAL", 16, 3, "0"],
]


# 1/2 body of section, absolute column, offset row
# [0] title, [1] column, [2] row, [3] default
partSection = [
    ["QTY NUMBER", 1, 1, ""],
    ["PART NUMBER", 2, 1, ""],
    ["DESCRIPTION", 3, 1, ""],
    ["UOM", 4, 1, ""],
    ["PRICE", 5, 1, "0"],
    ["TOTAL", 6, 1, "0"],
    ["VENDOR", 11, 1, ""],
    ["VENDOR PART", 12, 1, ""],
    ['PICKLIST', 99, 1, ""],
]

# 2/2 body of section, calculated column, offset row
# [0] title, [1] column, [2] row, [3] default
partSectionByModel = [
    [" QTY", 13, 1, "0"],
    [" UOM", 14, 1, "0"],
    [" PRICE", 15, 1, "0"],
    [" TOTAL", 16, 1, "0"],
]


##  BOTTOM BAND    ##########################################################

# [0] title, [1] column, [2] row, [3] default
bottomSection = [
  ["EOS QUANTITY", 1, 1, ""],
  ["EOS LOCATION SELECTION", 2, 1, ""],
  ["EOS NOTES FIELD", 3, 1, ""],
  ["EOS CANVAS COLOR", 4, 1, ""],
  ["EOS CABIN OPTION", 5, 1, ""],

  ["EOS 1 PAINT COLOR", 1, 3, ""],
  ["EOS 2 PAINT COLOR", 2, 3, ""],
  ["EOS ZOLATONE", 3, 3, ""],
  ["EOS 1 VINYL", 4, 3, ""],
  ["EOS 2 VINYL", 5, 3, ""],

  ["SSOB", 2, 6, ""],
  ["SSOB CODE", 4, 6, ""],
  ["SSOB CATEGORY", 5, 6, ""],
  ["SSOB NO CHARGE/OVERRIDE", 6, 6, ""],
  
  ["LSOB", 2, 7, ""],
  ["LSOB CODE", 4, 7, ""],
  ["LSOB CATEGORY", 5, 7, ""],
  ["LSOB NO CHARGE/OVERRIDE", 6, 7, ""],
  
  ["SHHT", 2, 8, ""],
  ["SHHT CODE", 4, 8, ""],
  ["SHHT CATEGORY", 5, 8, ""],
  ["SSHT NO CHARGE/OVERRIDE", 6, 8, ""],
  
  ["SHFB", 2, 9, ""],
  ["SHFB CODE", 4, 9, ""],
  ["SHFB CATEGORY", 5, 9, ""],
  ["SHFB NO CHARGE/OVERRIDE", 6, 9, ""],
 
  ["23OS", 2, 10, ""],
  ["23OS CODE", 4, 10, ""],
  ["SHFB CATEGORY", 5, 10, ""],
  ["SHFB NO CHARGE/OVERRIDE", 6, 10, ""],
  
  ["SO", 2, 11, ""],
  ["SO CODE", 4, 11, ""],
  ["SHFB CATEGORY", 5, 11, ""],
  ["SHFB NO CHARGE/OVERRIDE", 6, 11, ""],
  
  ["WXL", 2, 12, ""],
  ["WXL CODE", 4, 12, ""],
  ["SHFB CATEGORY", 5, 12, ""],
  ["SHFB NO CHARGE/OVERRIDE", 6, 12, ""],

  ["25OS", 2, 13, ""],
  ["25OS CODE", 4, 13, ""],
  ["25OS CATEGORY", 5, 13, ""],
  ["25OS NO CHARGE/OVERRIDE", 6, 13, ""],

  ["27OS", 2, 14, ""],
  ["27OS CODE", 4, 14, ""],
  ["27OS CATEGORY", 5, 14, ""],
  ["27OS NO CHARGE/OVERRIDE", 6, 14, ""],

  ["29OS", 2, 15, ""],
  ["29OS CODE", 4, 15, ""],
  ["29OS CATEGORY", 5, 15, ""],
  ["29OS NO CHARGE/OVERRIDE", 6, 15, ""],

  ["31OS", 2, 16, ""],
  ["31OS CODE", 4, 16, ""],
  ["31OS CATEGORY", 5, 16, ""],
  ["31OS NO CHARGE/OVERRIDE", 6, 16, ""],

  ["33OS", 2, 17, ""],
  ["33OS CODE", 4, 17, ""],
  ["33OS CATEGORY", 5, 17, ""],
  ["33OS NO CHARGE/OVERRIDE", 6, 17, ""],

  ["35OS", 2, 18, ""],
  ["35OS CODE", 4, 18, ""],
  ["35OS CATEGORY", 5, 18, ""],
  ["35OS NO CHARGE/OVERRIDE", 6, 18, ""],
  
  ["WASO", 2, 19, ""],
  ["WASO CODE", 4, 19, ""],
  [" CATEGORY", 5, 19, ""],
  [" NO CHARGE/OVERRIDE", 6, 19, ""],
  
  ["DV", 2, 20, ""],
  ["DV CODE", 4, 20, ""],
  [" CATEGORY", 5, 20, ""],
  [" NO CHARGE/OVERRIDE", 6, 20, ""],
  
  ["C", 2, 21, ""],
  ["C CODE", 4, 21, ""],
  [" CATEGORY", 5, 21, ""],
  [" NO CHARGE/OVERRIDE", 6, 21, ""],
  
  ["OSP", 2, 22, ""],
  ["OSP CODE", 4, 22, ""],
  [" CATEGORY", 5, 22, ""],
  [" NO CHARGE/OVERRIDE", 6, 22, ""],
  
  ["S", 2, 23, ""],
  ["S CODE", 4, 23, ""],
  [" CATEGORY", 5, 23, ""],
  [" NO CHARGE/OVERRIDE", 6, 23, ""],
  
  ["EOS DEPARTMENT", 1, 26, ""],
  ["EOS OUTFITTING NOTES", 1, 26, ""],
]
