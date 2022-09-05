from jinja2 import Environment, FileSystemLoader

lookup = {}
for n in range(255):
  lookup[n] = chr(n)
stack = {}
for n in range(32):
  stack[n] = 0
code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

environment = Environment(loader=FileSystemLoader("./"))
template = environment.get_template("jinja.txt")

print(template.render(stack=stack, code=code, lookup=lookup))