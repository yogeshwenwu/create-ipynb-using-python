from nbformat import v4 as nbf
from nbformat import reads
from nbformat import writes

class Notebook:
    def new_notebook(filename: str):
        notebook = nbf.new_notebook()
        with open(filename, 'w') as f:
            f.write(writes(notebook))


    def add_markdown_cell(text:str):
        with open(filename,'r') as f:
            content = f.read()
            notebook = reads(content, as_version= 4)
        mark_down = nbf.new_markdown_cell(text)
        notebook['cells'].append(mark_down)
        with open(filename,'w')as f:
            f.write(writes(notebook))

    def add_code_cell():
        with open(filename,'r') as f:
            content = f.read()
            notebook = reads(content, as_version=4)
        code_cell = nbf.new_code_cell()
        notebook['cells'].append(code_cell)
        with open(filename,'w') as f:
            f.write(writes(notebook))



name = str(input("Name the file:"))
filename = name + ".ipynb"
Notebook.new_notebook(filename)
Notebook.add_markdown_cell("Write a program to print even numbers upto 10") 
Notebook.add_code_cell()