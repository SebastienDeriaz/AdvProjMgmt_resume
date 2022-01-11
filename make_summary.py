import glob
from markdown import markdown
import pdfkit

content = ""
output_file_pdf = "AdvProjMgmt_resume.pdf"
input_files = "Cours*.md"
HTML_template = "HTML_template.html"
title = "Résumé AdvProjMgmt 2021"

print(f"Saving as {output_file_pdf}")
for file in glob.glob(input_files):
    with open(file, "r", encoding='utf-8') as f:
        content += "\n\n" + f.read()
#output.write(content)


# .md -> .pdf
html_text = markdown(content, output_format='html4', encoding="utf-8")

with open(HTML_template, "r") as h:
    HTML = h.read()

    HTML = HTML.replace('{{body}}', html_text)
    HTML = HTML.replace('{{title}}', title)

    pdfkit.from_string(HTML, output_file_pdf)




