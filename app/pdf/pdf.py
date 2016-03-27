#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, json
from fpdf import FPDF

# page size
page_size = {
    'left': 10,
    'top': 10,
    'middle_x': 120,
    'end_x': 200,
    'section_indent': 10,
    'section_margin': 1
}
# page size
font_size = {
    'text': 10,
    'header_title': 28,
    'header_sub_title': 17,
    'section_title': 16
}

line_height = {
    'section': 9,
    'text': 5
}

# colors
grey = 120
blue = (0, 0, 255)
brown = (165, 42, 42)
black = 0

# list ellipse size
ellipse = {
    'margin': 3,
    'size': 1.5
}

# split column function
def apply_two_column (pdf_instance, arr, draw_func):
    is_end = False
    i = 0
    top = pdf_instance.get_y()
    while not is_end:
        if i + 2 >= len(arr):
            is_end = True
        # 2 projects one row
        two_element_arr = arr[i:i + 2]
        heights = [];
        for idx, item in enumerate(two_element_arr):
            left = page_size['middle_x'] if idx > 0 else page_size['left'] + page_size['section_indent']
            draw_func(pdf_instance, item, left, top)
            heights.append(pdf_instance.get_y())
        top = max(heights)
        i = i + 2

# draw function for employment
def draw_func_employment(pdf_instance, job, left, top):
    pdf_instance.set_y(top)
    pdf_instance.set_x(left)
    pdf_instance.set_font_size(font_size['text'] + 1)
    pdf_instance.set_text_color(*brown)
    pdf_instance.cell(1, line_height['text'], job['name'], ln=2)
    pdf_instance.set_font_size(font_size['text'])
    pdf_instance.set_text_color(black)
    pdf_instance.cell(1, line_height['text'] - 1, job['position'], ln=2)
    pdf_instance.set_text_color(grey)
    pdf_instance.cell(1, line_height['text'] + 1, job['year'], ln=2)
    pdf_instance.set_text_color(black)
    for desc in job['description']:
        pdf_instance.ellipse(pdf_instance.get_x() + 1, pdf_instance.get_y() + 1, 1.5, 1.5, 'F')
        pdf_instance.cell(ellipse['margin'])
        pdf_instance.cell(1, line_height['text'], desc, ln=2)
        pdf_instance.set_x(left)
    pdf_instance.ln(page_size['section_margin'])

# draw function for project
def draw_func_project(pdf_instance, proj, left, top):
    pdf_instance.set_y(top)
    pdf_instance.set_x(left)
    pdf_instance.set_font_size(font_size['text'] + 1)
    pdf_instance.set_text_color(*brown)
    pdf_instance.cell(1, line_height['text'] - 1, proj['name'] + u' (' + proj['year'] + ')', ln=2)
    pdf_instance.set_font_size(font_size['text'])
    pdf_instance.set_text_color(black)
    pdf_instance.cell(1, line_height['text'], u'[ ' + u', '.join(proj['library']) + ' ]', ln=2)
    for desc in proj['description']:
        pdf_instance.set_x(left)
        pdf_instance.ellipse(pdf_instance.get_x() + 1, pdf_instance.get_y() + 1, 1.5, 1.5, 'F')
        pdf_instance.cell(ellipse['margin'])
        pdf_instance.cell(1, line_height['text'], desc, ln=2)
    pdf_instance.ln(page_size['section_margin'])

# generate pdf for every language
all_langs = os.listdir('./app/i18n')
for lang in all_langs:
    # load json
    data = json.load(open('./app/i18n/' + lang))
    # create pdf
    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_margins(page_size['left'], page_size['top'])
    pdf.add_page()
    # set metadata
    # pdf.set_title(data['badge']['pdfName'])
    # pdf.set_author(data['header']['name'])
    # pdf.set_subject(data['html']['title'])
    # font defination
    title_font_data = data['pdf']['fonts']['title']
    text_font_data = data['pdf']['fonts']['text']
    # font for title
    if title_font_data['type'] == 'embeded':
        pdf.add_font(title_font_data['name'], '', os.path.abspath('.') + '/app/pdf/' + title_font_data['path'], uni=True)
    title_font = title_font_data['name']
    # font for plain text
    if text_font_data['type'] == 'embeded':
        pdf.add_font(text_font_data['name'], '', os.path.abspath('.') + '/app/pdf/' + text_font_data['path'], uni=True)
    text_font = text_font_data['name']
    # header section
    # left
    pdf.set_font(title_font, '', font_size['header_title'])
    pdf.cell(1, line_height['section'] + 1, data['header']['name'], ln=2)
    pdf.set_font_size(font_size['header_sub_title'])
    pdf.set_text_color(grey)
    pdf.cell(1, line_height['text'] + 1, data['header']['title'], ln=2)
    pdf.set_font_size(font_size['text'] + 2)
    online_text = data['pdf']['online']['text']
    pdf.cell(pdf.get_string_width(online_text), line_height['text'] + 1, online_text, ln=0)
    pdf.set_text_color(*blue)
    pdf.cell(1, line_height['text'] + 1, data['pdf']['online']['url'], ln=2, link=data['pdf']['online']['url'])
    header_y = pdf.get_y()
    # right
    pdf.set_y(page_size['top'] - 1)
    pdf.set_x(page_size['end_x'])
    pdf.set_font(text_font, '', font_size['text'])
    pdf.set_text_color(black)
    pdf.cell(1, line_height['text'] - 0.5, data['about']['location'], ln=2, align='R')
    pdf.cell(1, line_height['text'] - 0.5, data['about']['phone'], ln=2, align='R')
    pdf.cell(1, line_height['text'] - 0.5, data['about']['email'], ln=2, align='R')
    pdf.set_text_color(*blue)
    pdf.cell(1, line_height['text'] - 0.5, data['about']['socials']['blog']['url'], ln=2, align='R', link=data['about']['socials']['blog']['url'])
    pdf.cell(1, line_height['text'] - 0.5, data['about']['socials']['github']['url'], ln=2, align='R', link=data['about']['socials']['github']['url'])
    pdf.set_text_color(black)
    # hr
    pdf.set_line_width(0.4)
    pdf.dashed_line(page_size['left'] + 1, header_y, page_size['end_x'] + 1, header_y, 1, 1)
    pdf.ln(2)
    # about section
    pdf.set_font(title_font, '', font_size['section_title'])
    pdf.cell(1, line_height['section'] - 1, data['sections']['about'], ln=2)
    pdf.set_font(text_font, '', font_size['text'])
    col_1_count = len(data['about']['introduction']) / 2
    desc_y = pdf.get_y()
    for idx, desc in enumerate(data['about']['introduction']):
        if idx == col_1_count:
            pdf.set_y(desc_y)
        if idx < col_1_count:
            pdf.set_x(page_size['left'] + page_size['section_indent'])
        else:
            pdf.set_x(page_size['middle_x'])
        pdf.ellipse(pdf.get_x(), pdf.get_y() + 1, ellipse['size'], ellipse['size'], 'F')
        pdf.cell(ellipse['margin'])
        pdf.cell(1, line_height['text'] - 1, desc, ln=2)
    pdf.ln(page_size['section_margin'])
    # education section
    pdf.set_x(page_size['left'])
    pdf.set_font(title_font, '', font_size['section_title'])
    pdf.cell(1, line_height['section'] - 1, data['sections']['education'], ln=2)
    pdf.set_font(text_font, '', font_size['text'])
    for univ in data['education']['universities']:
        pdf.set_x(page_size['left'] + page_size['section_indent'])
        univ_y = pdf.get_y()
        pdf.set_font_size(font_size['text'] + 1)
        pdf.set_text_color(*brown)
        pdf.cell(1, line_height['text'], univ['name'], ln=2)
        pdf.set_font_size(font_size['text'])
        pdf.set_text_color(black)
        pdf.cell(1, line_height['text'] - 1, univ['major'], ln=2)
        pdf.set_text_color(grey)
        pdf.cell(1, line_height['text'] - 1, univ['location'] + u' -- ' + univ['year'], ln=2)
        pdf.set_text_color(black)

        pdf.set_y(univ_y)
        for item in univ['items']:
            pdf.set_x(page_size['middle_x'])
            pdf.ellipse(pdf.get_x(), pdf.get_y() + 1, ellipse['size'], ellipse['size'], 'F')
            pdf.cell(2)
            if 'link' in item:
                pdf.cell(pdf.get_string_width(item['textBefore']), line_height['text'] - 1, item['textBefore'], ln=0)
                pdf.set_text_color(*blue)
                pdf.cell(pdf.get_string_width(item['link']['text']), line_height['text'] - 1, item['link']['text'], ln=0, link=item['link']['url'])
                pdf.set_text_color(0)
                pdf.cell(1, line_height['text'], item['textAfter'], ln=2)
            else:
                pdf.cell(1, line_height['text'], item['text'], ln=2)
        pdf.ln(4)
    pdf.ln(page_size['section_margin'])
    # employment section
    pdf.set_x(page_size['left'])
    pdf.set_font(title_font, '', font_size['section_title'])
    pdf.cell(1, line_height['section'] - 1, data['sections']['employment'], ln=2)
    pdf.set_font(text_font, '', font_size['text'])
    apply_two_column(pdf, data['employment']['jobs'], draw_func_employment);
    # skill section
    pdf.set_x(page_size['left'])
    pdf.set_font(title_font, '', font_size['section_title'])
    pdf.cell(1, line_height['section'] - 1, data['sections']['skill'], ln=2)
    pdf.set_font(text_font, '', font_size['text'])
    for item in data['skill']['programming']['children']:
        pdf.set_x(page_size['left'] + page_size['section_indent'])
        pdf.ellipse(pdf.get_x(), pdf.get_y() + 1, ellipse['size'], ellipse['size'], 'F')
        pdf.cell(ellipse['margin'])
        skill_names = [i['name'] for i in item['skills']]
        pdf.cell(1, line_height['text'] - 1, item['text'] + u': ' + ', '.join(skill_names), ln=2)
    pdf.set_x(page_size['left'] + page_size['section_indent'])
    pdf.ellipse(pdf.get_x(), pdf.get_y() + 1, ellipse['size'], ellipse['size'], 'F')
    pdf.cell(ellipse['margin'])
    pdf.cell(1, line_height['text'] - 1, data['skill']['library']['text'] + u': ' + ', '.join(data['skill']['library']['children']), ln=2)
    pdf.ln(page_size['section_margin'])
    # project section
    pdf.set_x(page_size['left'])
    pdf.set_font(title_font, '', font_size['section_title'])
    pdf.cell(pdf.get_string_width(data['sections']['project']), line_height['section'] - 1, data['sections']['project'], ln=0)
    pdf.set_font(text_font, '', font_size['text'])
    pdf.set_text_color(grey)
    pdf.set_y(pdf.get_y() + 2)
    pdf.cell(30)
    pdf.cell(pdf.get_string_width(data['pdf']['github']['text']), line_height['text'] - 1, data['pdf']['github']['text'], ln=0)
    pdf.set_text_color(*blue)
    pdf.cell(1, line_height['text'] - 1, data['about']['socials']['github']['url'], ln=2, link=data['about']['socials']['github']['url'])
    pdf.set_y(pdf.get_y() + 3)
    pdf.set_text_color(black)
    projects = data['project']['col1'] + data['project']['col2']
    apply_two_column(pdf, projects, draw_func_project);
    # output file
    pdf.output('./dist/' + data['badge']['pdfLink'], 'F')