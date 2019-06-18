#!/usr/bin/env python

# [0] title, [1] column, [2] row
topSection = [
    ["OPTION NUMBER", 2, 1],
    ["OPTION NAME", 2, 2],
    ["OPTION NOTES", 2, 3],
    ["TOTAL COST", 2, 9],
    ["CALCULATED RETAIL", 2, 10],
    ["ADVERTISED RETAIL", 2, 11],
    ["CONTRIBUTION MARGIN", 2, 12],
    ["DESIGN LABOR RATE", 2, 15],
    
    ["18 LABOR TOTAL", 13, 2],
    ["18 MATERIAL TOTAL", 13, 3],
    ["18 OVERHEAD CALCULATION", 13, 4],
    ["18 TOTAL COST", 13, 5],

    ["19 LABOR TOTAL", 17, 2],
    ["19 MATERIAL TOTAL", 17, 3],
    ["19 OVERHEAD CALCULATION", 17, 4],
    ["19 TOTAL COST", 17, 5],

    ["20 LABOR TOTAL", 21, 2],
    ["20 MATERIAL TOTAL", 21, 3],
    ["20 OVERHEAD CALCULATION", 21, 4],
    ["20 TOTAL COST", 21, 5],
    
    ["21 LABOR TOTAL", 25, 2],
    ["21 MATERIAL TOTAL", 25, 3],
    ["21 OVERHEAD CALCULATION", 25, 4],
    ["21 TOTAL COST", 25, 5],
    
    ["22 LABOR TOTAL", 29, 2],
    ["22 MATERIAL TOTAL", 29, 3],
    ["22 OVERHEAD CALCULATION", 29, 4],
    ["22 TOTAL COST", 29, 5],
    
    ["23 LABOR TOTAL", 33, 2],
    ["23 MATERIAL TOTAL", 33, 3],
    ["23 OVERHEAD CALCULATION", 33, 4],
    ["23 TOTAL COST", 33, 5],
    
    ["24 LABOR TOTAL", 37, 2],
    ["24 MATERIAL TOTAL", 37, 3],
    ["24 OVERHEAD CALCULATION", 37, 4],
    ["24 TOTAL COST", 37, 5],
    
    ["25 LABOR TOTAL", 41, 2],
    ["25 MATERIAL TOTAL", 41, 3],
    ["25 OVERHEAD CALCULATION", 41, 4],
    ["25 TOTAL COST", 41, 5],
    
    ["26 LABOR TOTAL", 45, 2],
    ["26 MATERIAL TOTAL", 45, 3],
    ["26 OVERHEAD CALCULATION", 45, 4],
    ["26 TOTAL COST", 45, 5],
    
    ["27 LABOR TOTAL", 49, 2],
    ["27 MATERIAL TOTAL", 49, 3],
    ["27 OVERHEAD CALCULATION", 49, 4],
    ["27 TOTAL COST", 49, 5],
    
    ["28 LABOR TOTAL", 53, 2],
    ["28 MATERIAL TOTAL", 53, 3],
    ["28 OVERHEAD CALCULATION", 53, 4],
    ["28 TOTAL COST", 53, 5],
    
    ["29 LABOR TOTAL", 57, 2],
    ["29 MATERIAL TOTAL", 57, 3],
    ["29 OVERHEAD CALCULATION", 21, 4],
    ["29 TOTAL COST", 57, 5],
    
    ["30 LABOR TOTAL", 61, 2],
    ["30 MATERIAL TOTAL", 61, 3],
    ["30 OVERHEAD CALCULATION", 61, 4],
    ["30 TOTAL COST", 61, 5],
    
    ["31 LABOR TOTAL", 65, 2],
    ["31 MATERIAL TOTAL", 65, 3],
    ["31 OVERHEAD CALCULATION", 65, 4],
    ["31 TOTAL COST", 65, 5],
    
    ["32 LABOR TOTAL", 69, 2],
    ["32 MATERIAL TOTAL", 69, 3],
    ["32 OVERHEAD CALCULATION", 69, 4],
    ["32 TOTAL COST", 69, 5],
    
    ["33 LABOR TOTAL", 73, 2],
    ["33 MATERIAL TOTAL", 73, 3],
    ["33 OVERHEAD CALCULATION", 73, 4],
    ["33 TOTAL COST", 73, 5],
    
    ["34 LABOR TOTAL", 77, 2],
    ["34 MATERIAL TOTAL", 77, 3],
    ["34 OVERHEAD CALCULATION", 77, 4],
    ["34 TOTAL COST", 77, 5],
    
    ["35 LABOR TOTAL", 81, 2],
    ["35 MATERIAL TOTAL", 81, 3],
    ["35 OVERHEAD CALCULATION", 81, 4],
    ["35 TOTAL COST", 81, 5],
    
    ["36 LABOR TOTAL", 85, 2],
    ["36 MATERIAL TOTAL", 85, 3],
    ["36 OVERHEAD CALCULATION", 85, 4],
    ["36 TOTAL COST", 85, 5],
    
    ["37 LABOR TOTAL", 89, 2],
    ["37 MATERIAL TOTAL", 89, 3],
    ["37 OVERHEAD CALCULATION", 89, 4],
    ["37 TOTAL COST", 89, 5],
    
    ["18 DESIGN HOURS", 13, 15],
    ["19 DESIGN HOURS", 17, 15],
    ["20 DESIGN HOURS", 21, 15],
    ["21 DESIGN HOURS", 25, 15],
    ["22 DESIGN HOURS", 29, 15],
    ["23 DESIGN HOURS", 33, 15],
    ["24 DESIGN HOURS", 37, 15],
    ["25 DESIGN HOURS", 41, 15],
    ["26 DESIGN HOURS", 45, 15],
    ["27 DESIGN HOURS", 49, 15],
    ["28 DESIGN HOURS", 53, 15],
    ["29 DESIGN HOURS", 57, 15],
    ["30 DESIGN HOURS", 61, 15],
    ["31 DESIGN HOURS", 65, 15],
    ["32 DESIGN HOURS", 69, 15],
    ["33 DESIGN HOURS", 73, 15],
    ["34 DESIGN HOURS", 77, 15],
    ["35 DESIGN HOURS", 81, 15],
    ["36 DESIGN HOURS", 85, 15],
    ["37 DESIGN HOURS", 89, 15],
]

partSection = [
]

# [0] title, [1] column, [2] row
bottomSection = [
  ["EOS QUANTITY", 1, 1],
  ["EOS LOCATION SELECTION", 2, 1],
  ["EOS NOTES FIELD", 3, 1],
  ["E71	EOS CANVAS COLOR", 4, 1],

  ["EOS 1 PAINT COLOR", 1, 3],
  ["EOS 2 PAINT COLOR", 2, 3],
  ["EOS ZOLATONE", 3, 3],
  ["EOS 1 VINYL", 4, 3],
  ["EOS 2 VINYL", 5, 3],

  ["SSOB", 2, 6],
  ["SSOB CODE", 4, 6],
  
  ["LSOB", 2, 7],
  ["LSOB CODE", 4, 7],
  
  ["SSHT", 2, 8],
  ["SSHT CODE", 4, 8],
  
  ["23OS", 2, 9],
  ["23OS CODE", 4, 9],
  
  ["SO", 2, 10],
  ["SO CODE", 4, 10],
  
  ["WXL", 2, 11],
  ["WXL CODE", 4, 11],
  
  ["WASO", 2, 12],
  ["WASO CODE", 4, 12],
  
  ["DV", 2, 13],
  ["DV CODE", 4, 13],
  
  ["C", 2, 14],
  ["C CODE", 4, 14],
  
  ["OSP", 2, 15],
  ["OSP CODE", 4, 15],
  
  ["S", 2, 16],
  ["S CODE", 4, 16],
  
  ["EOS DEPARTMENT", 1, 19],
]

# ["OUTFITTING NOTE", 21, 1],
