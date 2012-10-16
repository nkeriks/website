import json
import jinja2
import re

def parse_json(jfile):
    j = json.loads(open(jfile).read())

    papers = j['papers'].keys()
    from collections import defaultdict

    peer_years =  defaultdict(list)
    other_years = defaultdict(list)
    firstlast = 0
    for k in papers:
        year = k[:4]
        cat = j['papers'][k]["category"]
        if "book" in cat:
            other_years[year].append(k)
        elif "preprints" in cat:
            peer_years['submitted'].append(k)
        else:
            peer_years[year].append(k)
            if "flc" in cat or 'math' in cat:
                firstlast += 1
    j['years'] = dict(peer_years.items())
    j['notreviewedyears'] = dict(other_years.items())
    j['pr'] = sum(map(len,peer_years.values()))
    j['npr'] = sum(map(len,other_years.values()))
    j['firstlast'] = firstlast
    return j

    
def boldnke(s):
    return re.sub("N. Eriksson", r"\\textbf{N. Eriksson}", s)

def tolatex(string):
    #replace <i></i> with \textit{ }
    s2 = re.sub("<i>", r"\\textit{", string)
    s3 = re.sub("</i>", "}", s2)
    return s3

LATEX_SUBS = (
    #(re.compile(r'\\'), r'\\textbackslash'),
    (re.compile(r'([{}_#%&$])'), r'\\\1'),
    (re.compile(r'~'), r'\~{}'),
    (re.compile(r'\^'), r'\^{}'),
    (re.compile(r'"'), r"''"),
    (re.compile(r'\.\.\.+'), r'\\ldots'),
)

def escape_tex(value):
    newval = value
    for pattern, replacement in LATEX_SUBS:
        newval = pattern.sub(replacement, newval)
    return newval

def main():
    context = parse_json('../templates/papers.json')
    latex_jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(['../cv']), 
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '\VAR{',
        variable_end_string = '}',
        comment_start_string = '\#{',
        comment_end_string = '}',
        line_statement_prefix = '%-',
        line_comment_prefix = '%#',
        trim_blocks = True,
        autoescape = False,
    )
    latex_jinja_env.filters["htmltolatex"] = tolatex
    latex_jinja_env.filters["boldnke"] = boldnke
    latex_jinja_env.filters["escapetex"] = escape_tex

    template = latex_jinja_env.get_template('template.tex')
    fp = open('../cv/cv.tex', 'w')
    fp.write(template.render(context).encode('utf8'))
    fp.close()

if __name__ == '__main__':
    main()
