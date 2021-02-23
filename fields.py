#!/usr/bin/env python

# [0] title, [1] column, [2] row, [3] default
topSection = [
    ["OPTION NUMBER", 3, 1, ""],
    ["OPTION NAME", 3, 2, ""],
    ["OPTION NOTES", 3, 3, ""],
    ["TOTAL COST", 3, 6, "0"],
    ["CALCULATED RETAIL", 3, 7, "0"],
    ["ADVERTISED RETAIL", 3, 8, "0"],
    ["CONTRIBUTION MARGIN", 3, 9, "0"],
    ["DESIGN LABOR RATE", 4, 22, "0"],
    
    ["18 TOTAL COST", 16, 2, "0"],
    ["18 RETAIL CALCULATED", 16, 3, "0"],
    ["18 RETAIL ADVERTISED", 16, 4, "0"],
    ["18 CONTRIBUTION MARGIN", 16, 5, "0"],

    ["19 TOTAL COST", 20, 2, "0"],
    ["19 RETAIL CALCULATED", 20, 3, "0"],
    ["19 RETAIL ADVERTISED", 20, 4, "0"],
    ["19 CONTRIBUTION MARGIN", 20, 5, "0"],
    
    ["20 TOTAL COST", 24, 2, "0"],
    ["20 RETAIL CALCULATED", 24, 3, "0"],
    ["20 RETAIL ADVERTISED", 24, 4, "0"],
    ["20 CONTRIBUTION MARGIN", 24, 5, "0"],
    
    ["21 TOTAL COST", 28, 2, "0"],
    ["21 RETAIL CALCULATED", 28, 3, "0"],
    ["21 RETAIL ADVERTISED", 28, 4, "0"],
    ["21 CONTRIBUTION MARGIN", 28, 5, "0"],
    
    ["22 TOTAL COST", 32, 2, "0"],
    ["22 RETAIL CALCULATED", 32, 3, "0"],
    ["22 RETAIL ADVERTISED", 32, 4, "0"],
    ["22 CONTRIBUTION MARGIN", 32, 5, "0"],
    
    ["23 TOTAL COST", 36, 2, "0"],
    ["23 RETAIL CALCULATED", 36, 3, "0"],
    ["23 RETAIL ADVERTISED", 36, 4, "0"],
    ["23 CONTRIBUTION MARGIN", 36, 5, "0"],
    
    ["24 TOTAL COST", 40, 2, "0"],
    ["24 RETAIL CALCULATED", 40, 3, "0"],
    ["24 RETAIL ADVERTISED", 40, 4, "0"],
    ["24 CONTRIBUTION MARGIN", 40, 5, "0"],
    
    ["25 TOTAL COST", 44, 2, "0"],
    ["25 RETAIL CALCULATED", 44, 3, "0"],
    ["25 RETAIL ADVERTISED", 44, 4, "0"],
    ["25 CONTRIBUTION MARGIN", 44, 5, "0"],
    
    ["26 TOTAL COST", 48, 2, "0"],
    ["26 RETAIL CALCULATED", 48, 3, "0"],
    ["26 RETAIL ADVERTISED", 48, 4, "0"],
    ["26 CONTRIBUTION MARGIN", 48, 5, "0"],
    
    ["27 TOTAL COST", 52, 2, "0"],
    ["27 RETAIL CALCULATED", 52, 3, "0"],
    ["27 RETAIL ADVERTISED", 52, 4, "0"],
    ["27 CONTRIBUTION MARGIN", 52, 5, "0"],
    
    ["28 TOTAL COST", 56, 2, "0"],
    ["28 RETAIL CALCULATED", 56, 3, "0"],
    ["28 RETAIL ADVERTISED", 56, 4, "0"],
    ["28 CONTRIBUTION MARGIN", 56, 5, "0"],
    
    ["29 TOTAL COST", 60, 2, "0"],
    ["29 RETAIL CALCULATED", 60, 3, "0"],
    ["29 RETAIL ADVERTISED", 60, 4, "0"],
    ["29 CONTRIBUTION MARGIN", 60, 5, "0"],
    
    ["30 TOTAL COST", 64, 2, "0"],
    ["30 RETAIL CALCULATED", 64, 3, "0"],
    ["30 RETAIL ADVERTISED", 64, 4, "0"],
    ["30 CONTRIBUTION MARGIN", 64, 5, "0"],
    
    ["31 TOTAL COST", 68, 2, "0"],
    ["31 RETAIL CALCULATED", 68, 3, "0"],
    ["31 RETAIL ADVERTISED", 68, 4, "0"],
    ["31 CONTRIBUTION MARGIN", 68, 5, "0"],
    
    ["32 TOTAL COST", 72, 2, "0"],
    ["32 RETAIL CALCULATED", 72, 3, "0"],
    ["32 RETAIL ADVERTISED", 72, 4, "0"],
    ["32 CONTRIBUTION MARGIN", 72, 5, "0"],
    
    ["33 TOTAL COST", 76, 2, "0"],
    ["33 RETAIL CALCULATED", 76, 3, "0"],
    ["33 RETAIL ADVERTISED", 76, 4, "0"],
    ["33 CONTRIBUTION MARGIN", 76, 5, "0"],
    
    ["34 TOTAL COST", 80, 2, "0"],
    ["34 RETAIL CALCULATED", 80, 3, "0"],
    ["34 RETAIL ADVERTISED", 80, 4, "0"],
    ["34 CONTRIBUTION MARGIN", 80, 5, "0"],
    
    ["35 TOTAL COST", 84, 2, "0"],
    ["35 RETAIL CALCULATED", 84, 3, "0"],
    ["35 RETAIL ADVERTISED", 84, 4, "0"],
    ["35 CONTRIBUTION MARGIN", 84, 5, "0"],
    
    ["36 TOTAL COST", 88, 2, "0"],
    ["36 RETAIL CALCULATED", 88, 3, "0"],
    ["36 RETAIL ADVERTISED", 88, 4, "0"],
    ["36 CONTRIBUTION MARGIN", 88, 5, "0"],
    
    ["37 TOTAL COST", 72, 2, "0"],
    ["37 RETAIL CALCULATED", 72, 3, "0"],
    ["37 RETAIL ADVERTISED", 72, 4, "0"],
    ["37 CONTRIBUTION MARGIN", 72, 5, "0"],
    
    ["18 DESIGN HOURS", 15, 22, "0"],
    ["19 DESIGN HOURS", 19, 22, "0"],
    ["20 DESIGN HOURS", 23, 22, "0"],
    ["21 DESIGN HOURS", 27, 22, "0"],
    ["22 DESIGN HOURS", 31, 22, "0"],
    ["23 DESIGN HOURS", 35, 22, "0"],
    ["24 DESIGN HOURS", 39, 22, "0"],
    ["25 DESIGN HOURS", 43, 22, "0"],
    ["26 DESIGN HOURS", 47, 22, "0"],
    ["27 DESIGN HOURS", 51, 22, "0"],
    ["28 DESIGN HOURS", 55, 22, "0"],
    ["29 DESIGN HOURS", 59, 22, "0"],
    ["30 DESIGN HOURS", 63, 22, "0"],
    ["31 DESIGN HOURS", 67, 22, "0"],
    ["32 DESIGN HOURS", 71, 22, "0"],
    ["33 DESIGN HOURS", 75, 22, "0"],
    ["34 DESIGN HOURS", 79, 22, "0"],
    ["35 DESIGN HOURS", 83, 22, "0"],
    ["36 DESIGN HOURS", 87, 22, "0"],
    ["37 DESIGN HOURS", 91, 22, "0"],
]

# [0] title, [1] column, [2] row, [3] default
startSections = [
    [" CONSUMABLES", 1, -1, "0"],
    [" LABOR RATE", 4, -1, "0"],
    [" 18 HOURS", 15, -1, "0"],
    [" 19 HOURS", 19, -1, "0"],
    [" 20 HOURS", 23, -1, "0"],
    [" 21 HOURS", 27, -1, "0"],
    [" 22 HOURS", 31, -1, "0"],
    [" 23 HOURS", 35, -1, "0"],
    [" 24 HOURS", 39, -1, "0"],
    [" 25 HOURS", 43, -1, "0"],
    [" 26 HOURS", 47, -1, "0"],
    [" 27 HOURS", 51, -1, "0"],
    [" 28 HOURS", 55, -1, "0"],
    [" 29 HOURS", 59, -1, "0"],
    [" 30 HOURS", 63, -1, "0"],
    [" 31 HOURS", 67, -1, "0"],
    [" 32 HOURS", 71, -1, "0"],
    [" 33 HOURS", 75, -1, "0"],
    [" 34 HOURS", 79, -1, "0"],
    [" 35 HOURS", 83, -1, "0"],
    [" 36 HOURS", 87, -1, "0"],
    [" 37 HOURS", 91, -1, "0"],
]

# [0] title, [1] column, [2] row, [3] default
endSections = [
    [" 18 CREDIT TOTAL", 16, 0, "0"],
    [" 19 CREDIT TOTAL", 20, 0, "0"],
    [" 20 CREDIT TOTAL", 24, 0, "0"],
    [" 21 CREDIT TOTAL", 28, 0, "0"],
    [" 22 CREDIT TOTAL", 32, 0, "0"],
    [" 23 CREDIT TOTAL", 36, 0, "0"],
    [" 24 CREDIT TOTAL", 40, 0, "0"],
    [" 25 CREDIT TOTAL", 44, 0, "0"],
    [" 26 CREDIT TOTAL", 48, 0, "0"],
    [" 27 CREDIT TOTAL", 52, 0, "0"],
    [" 28 CREDIT TOTAL", 56, 0, "0"],
    [" 29 CREDIT TOTAL", 60, 0, "0"],
    [" 30 CREDIT TOTAL", 64, 0, "0"],
    [" 31 CREDIT TOTAL", 68, 0, "0"],
    [" 32 CREDIT TOTAL", 72, 0, "0"],
    [" 33 CREDIT TOTAL", 76, 0, "0"],
    [" 34 CREDIT TOTAL", 80, 0, "0"],
    [" 35 CREDIT TOTAL", 84, 0, "0"],
    [" 36 CREDIT TOTAL", 88, 0, "0"],
    [" 37 CREDIT TOTAL", 92, 0, "0"],
    
    [" 18 COST TOTAL", 16, 1, "0"],
    [" 19 COST TOTAL", 20, 1, "0"],
    [" 20 COST TOTAL", 24, 1, "0"],
    [" 21 COST TOTAL", 28, 1, "0"],
    [" 22 COST TOTAL", 32, 1, "0"],
    [" 23 COST TOTAL", 36, 1, "0"],
    [" 24 COST TOTAL", 40, 1, "0"],
    [" 25 COST TOTAL", 44, 1, "0"],
    [" 26 COST TOTAL", 48, 1, "0"],
    [" 27 COST TOTAL", 52, 1, "0"],
    [" 28 COST TOTAL", 56, 1, "0"],
    [" 29 COST TOTAL", 60, 1, "0"],
    [" 30 COST TOTAL", 64, 1, "0"],
    [" 31 COST TOTAL", 68, 1, "0"],
    [" 32 COST TOTAL", 72, 1, "0"],
    [" 33 COST TOTAL", 76, 1, "0"],
    [" 34 COST TOTAL", 80, 1, "0"],
    [" 35 COST TOTAL", 84, 1, "0"],
    [" 36 COST TOTAL", 88, 1, "0"],
    [" 37 COST TOTAL", 92, 1, "0"],

    [" 18 CONSUMABLES", 16, 2, "0"],
    [" 19 CONSUMABLES", 20, 2, "0"],
    [" 20 CONSUMABLES", 24, 2, "0"],
    [" 21 CONSUMABLES", 28, 2, "0"],
    [" 22 CONSUMABLES", 32, 2, "0"],
    [" 23 CONSUMABLES", 36, 2, "0"],
    [" 24 CONSUMABLES", 40, 2, "0"],
    [" 25 CONSUMABLES", 44, 2, "0"],
    [" 26 CONSUMABLES", 48, 2, "0"],
    [" 27 CONSUMABLES", 52, 2, "0"],
    [" 28 CONSUMABLES", 56, 2, "0"],
    [" 29 CONSUMABLES", 60, 2, "0"],
    [" 30 CONSUMABLES", 64, 2, "0"],
    [" 31 CONSUMABLES", 68, 2, "0"],
    [" 32 CONSUMABLES", 72, 2, "0"],
    [" 33 CONSUMABLES", 76, 2, "0"],
    [" 34 CONSUMABLES", 80, 2, "0"],
    [" 35 CONSUMABLES", 84, 2, "0"],
    [" 36 CONSUMABLES", 88, 2, "0"],
    [" 37 CONSUMABLES", 92, 2, "0"],

    [" 18 TOTAL", 16, 3, "0"],
    [" 19 TOTAL", 20, 3, "0"],
    [" 20 TOTAL", 24, 3, "0"],
    [" 21 TOTAL", 28, 3, "0"],
    [" 22 TOTAL", 32, 3, "0"],
    [" 23 TOTAL", 36, 3, "0"],
    [" 24 TOTAL", 40, 3, "0"],
    [" 25 TOTAL", 44, 3, "0"],
    [" 26 TOTAL", 48, 3, "0"],
    [" 27 TOTAL", 52, 3, "0"],
    [" 28 TOTAL", 56, 3, "0"],
    [" 29 TOTAL", 60, 3, "0"],
    [" 30 TOTAL", 64, 3, "0"],
    [" 31 TOTAL", 68, 3, "0"],
    [" 32 TOTAL", 72, 3, "0"],
    [" 33 TOTAL", 76, 3, "0"],
    [" 34 TOTAL", 80, 3, "0"],
    [" 35 TOTAL", 84, 3, "0"],
    [" 36 TOTAL", 88, 3, "0"],
    [" 37 TOTAL", 92, 3, "0"],
]


partSection = [
    ["PART NUMBER", 2, 1, ""],
    ["DESCRIPTION", 3, 1, ""],
    ["UOM", 4, 1, ""],
    ["PRICE", 5, 1, "0"],
    ["VENDOR", 11, 1, ""],
    ["VENDOR PART", 12, 1, ""],

    ["18 QTY", 13, 1, "0"],
    ["19 QTY", 17, 1, "0"],
    ["20 QTY", 21, 1, "0"],
    ["21 QTY", 25, 1, "0"],
    ["22 QTY", 29, 1, "0"],
    ["23 QTY", 33, 1, "0"],
    ["24 QTY", 37, 1, "0"],
    ["25 QTY", 41, 1, "0"],
    ["26 QTY", 45, 1, "0"],
    ["27 QTY", 49, 1, "0"],
    ["28 QTY", 53, 1, "0"],
    ["29 QTY", 57, 1, "0"],
    ["30 QTY", 61, 1, "0"],
    ["31 QTY", 65, 1, "0"],
    ["32 QTY", 69, 1, "0"],
    ["33 QTY", 73, 1, "0"],
    ["34 QTY", 77, 1, "0"],
    ["35 QTY", 81, 1, "0"],
    ["36 QTY", 82, 1, "0"],
    ["37 QTY", 85, 1, "0"],

    ["18 TOTAL", 13, 1, "0"],
    ["19 TOTAL", 17, 1, "0"],
    ["20 TOTAL", 21, 1, "0"],
    ["21 TOTAL", 25, 1, "0"],
    ["22 TOTAL", 29, 1, "0"],
    ["23 TOTAL", 33, 1, "0"],
    ["24 TOTAL", 37, 1, "0"],
    ["25 TOTAL", 41, 1, "0"],
    ["26 TOTAL", 45, 1, "0"],
    ["27 TOTAL", 49, 1, "0"],
    ["28 TOTAL", 53, 1, "0"],
    ["29 TOTAL", 57, 1, "0"],
    ["30 TOTAL", 61, 1, "0"],
    ["31 TOTAL", 65, 1, "0"],
    ["32 TOTAL", 69, 1, "0"],
    ["33 TOTAL", 73, 1, "0"],
    ["34 TOTAL", 77, 1, "0"],
    ["35 TOTAL", 81, 1, "0"],
    ["36 TOTAL", 85, 1, "0"],
    ["37 TOTAL", 89, 1, "0"],
]

# [0] title, [1] column, [2] row, [3] default
bottomSection = [
  ["EOS QUANTITY", 1, 1, ""],
  ["EOS LOCATION SELECTION", 2, 1, ""],
  ["EOS NOTES FIELD", 3, 1, ""],
  ["EOS	EOS CANVAS COLOR", 4, 1, ""],

  ["EOS 1 PAINT COLOR", 1, 3, ""],
  ["EOS 2 PAINT COLOR", 2, 3, ""],
  ["EOS ZOLATONE", 3, 3, ""],
  ["EOS 1 VINYL", 4, 3, ""],
  ["EOS 2 VINYL", 5, 3, ""],

  ["SSOB", 2, 6, ""],
  ["SSOB CODE", 4, 6, ""],
  
  ["LSOB", 2, 7, ""],
  ["LSOB CODE", 4, 7, ""],
  
  ["SHHT", 2, 8, ""],
  ["SHHT CODE", 4, 8, ""],
  
  ["23OS", 2, 9, ""],
  ["23OS CODE", 4, 9, ""],
  
  ["SO", 2, 10, ""],
  ["SO CODE", 4, 10, ""],
  
  ["WXL", 2, 11, ""],
  ["WXL CODE", 4, 11, ""],
  
  ["25OS", 2, 12, ""],
  ["25OS CODE", 4, 12, ""],
  
  ["27OS", 2, 13, ""],
  ["27OS CODE", 4, 13, ""],
  
  ["29OS", 2, 14, ""],
  ["29OS CODE", 4, 14, ""],
  
  ["31OS", 2, 15, ""],
  ["31OS CODE", 4, 15, ""],
  
  ["33OS", 2, 16, ""],
  ["33OS CODE", 4, 16, ""],
  
  ["35OS", 2, 17, ""],
  ["35OS CODE", 4, 17, ""],
  
  ["WASO", 2, 18, ""],
  ["WASO CODE", 4, 18, ""],
  
  ["DV", 2, 19, ""],
  ["DV CODE", 4, 19, ""],
  
  ["C", 2, 20, ""],
  ["C CODE", 4, 20, ""],
  
  ["OSP", 2, 21, ""],
  ["OSP CODE", 4, 21, ""],
  
  ["S", 2, 22, ""],
  ["S CODE", 4, 22, ""],
  
  ["EOS DEPARTMENT", 1, 23, ""],
  
  ["OUTFITTING NOTES", 1, 25, ""],
]
