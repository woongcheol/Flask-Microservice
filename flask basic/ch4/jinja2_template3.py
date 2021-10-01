from jinja2 import Template
template = Template("number : {% for n in range(1, 10) %} {{n}} {% endfor %}")
template.render()