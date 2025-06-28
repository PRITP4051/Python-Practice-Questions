# WAP to remove existing indentation from all the lines in a given text. 

text = """    This is line one.
        This is line two.
      This is line three.
    This is line four."""

# Split the text into lines and remove leading spaces from each line
lines = text.split('\n')
no_indent_lines = [line.lstrip() for line in lines]
result = '\n'.join(no_indent_lines)

print("Text after removing indentation:\n", result)