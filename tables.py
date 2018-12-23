# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 12:06:03 2018

@author: Alexander von Lunen

Port of the table example for FPDF-PHP
see http://www.fpdf.org/en/tutorial/tuto5.htm
"""

from fpdf import FPDF

# Load data
def LoadData(file):
    # Read file lines
    lines = open(file, 'r')
    data = list()
    for line in lines:
        data.append(line.split(';'))
        
    lines.close()
    
    return data


# Simple table
def BasicTable(header, data, pdf):
    # Header
    for col in header:
        pdf.cell(40,7,col,1)
    pdf.ln()
    # Data
    for row in data:
        for col in row:
            pdf.cell(40,6,col,1)
        pdf.ln()

# Better table
def ImprovedTable(header, data, pdf):
    # Column widths
    w = list((40, 35, 40, 45))
    # Header
    for i in range(0,len(header)):
        pdf.cell(w[i], 7, header[i], 1, 0, 'C')
    pdf.ln()
    # Data
    for row in data:
        pdf.cell(w[0], 6, row[0], 'LR')
        pdf.cell(w[1], 6, row[1], 'LR')
        pdf.cell(w[2], 6, row[2], 'LR', 0, 'R')
        pdf.cell(w[3], 6, row[3], 'LR', 0, 'R')
        
        pdf.ln()
    # Closing line
    pdf.cell(sum(w), 0, '', 'T')


# Colored table
def FancyTable(header, data, pdf):
    # Colors, line width and bold font
    pdf.set_fill_color(255,0,0)
    pdf.set_text_color(255)
    pdf.set_draw_color(128,0,0)
    pdf.set_line_width(.3)
    pdf.set_font('','B')
    
    # Header
    w = list((40, 35, 40, 45))
    for i in range(0, len(header)):
        pdf.cell(w[i], 7, header[i], 1, 0, 'C', True)
    pdf.ln()
    
    # Color and font restoration
    pdf.set_fill_color(224,235,255)
    pdf.set_text_color(0)
    pdf.set_font('')

    # Data
    fill = False
    for row in data:
        pdf.cell(w[0], 6, row[0], 'LR', 0, 'L', fill)
        pdf.cell(w[1], 6, row[1], 'LR', 0, 'L', fill)
        pdf.cell(w[2], 6, row[2], 'LR', 0, 'R', fill)
        pdf.cell(w[3], 6, row[3], 'LR', 0, 'R', fill)
        pdf.ln()
        fill = not fill

    # Closing line
    pdf.cell(sum(w), 0, '', 'T')

pdf = FPDF()
# Column headings
header = list(('Country', 'Capital', 'Area (sq km)', 'Pop. (thousands)'))

# Data loading
data = LoadData('countries.txt')
pdf.set_font('Arial','',14)
pdf.add_page()
BasicTable(header, data, pdf)
pdf.add_page()
ImprovedTable(header, data, pdf)
pdf.add_page()
FancyTable(header, data, pdf)
pdf.output("countries.pdf", "F")