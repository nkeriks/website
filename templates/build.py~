import json
import jinja2
import re

def write_html(context, template, outfile):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(['.']))
    env.filters["boldnke"] = boldnke
    template = env.get_template(template)
    fp = open(outfile, 'w')
    fp.write(template.render(context).encode('utf8'))
    fp.close()

def parse_json(jfile):
    j = json.loads(open(jfile).read())
    return j

def boldnke(s):
    return re.sub("N. Eriksson", "<b>N. Eriksson</b>", s)

def main():
    context = parse_json('papers.json')
    write_html(context, 'papers.jtml', '../web/papers.html')
    write_html(context, 'index.jtml', '../web/index.html')

if __name__ == '__main__':
    main()
