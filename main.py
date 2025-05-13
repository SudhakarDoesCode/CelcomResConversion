from docx import Document
import sys
import os

def merge_documents(template_path, resume_path, output_path):
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found: {template_path}")
    if not os.path.exists(resume_path):
        raise FileNotFoundError(f"Resume not found: {resume_path}")

    template = Document(template_path)
    resume = Document(resume_path)

    # Append resume content to template
    for element in resume.element.body:
        template.element.body.append(element)

    template.save(output_path)
    print(f"✅ Resume merged into template. Saved as: {output_path}")

if __name__ == "__main__":
    template_file = sys.argv[1]
    resume_file = sys.argv[2]
    output_file = sys.argv[3]

    merge_documents(template_file, resume_file, output_file)
