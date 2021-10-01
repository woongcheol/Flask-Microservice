from jinja2 import Template
template = Template("Hello {{something}} !")
template.render(something = "김말똥")