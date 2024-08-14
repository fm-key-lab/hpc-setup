import argparse
import os
from string import Template

parser = argparse.ArgumentParser()
parser.add_argument('--APP')
parser.add_argument('--VERSION')
parser.add_argument('--RELPATH_EXE')

args = parser.parse_args()

modulefile_template_path = os.path.join(
    os.path.dirname(__file__),
    '../templates/modulefile.template'
)
with open(modulefile_template_path, 'r') as f:
    content = f.read()

modulefile_template = Template(content)
modulefile = modulefile_template.safe_substitute(**vars(args))

with open(args.VERSION, 'w') as f:
    f.write(modulefile)