import glob

content = ""

output_file = "AdvProjMgmt_resume.md"
input_files = "Cours*.md"

with open(output_file, "w") as output:
    print(f"Saving in {output_file}")
    for file in glob.glob(input_files):
        with open(file, "r") as f:
            content += "\n\n" + f.read()
    output.write(content)




