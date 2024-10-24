import argparse
import os
from string import Template

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--APP')
    parser.add_argument('--NAME')
    parser.add_argument('--RELPATH_EXE')
    parser.add_argument('--VERSION')
    parser.add_argument('--template', default='default', type=str)

    args = parser.parse_args()

    if args.template == 'default':
        mf = '../templates/modulefile.template'
    elif args.template == 'venv':
        mf = '../templates/modulefile-venv.template'
    else:
        raise ValueError("'--template' must be 'default' or 'venv'.")

    modulefile_template_path = os.path.join(
        os.path.dirname(__file__), mf
    )
    with open(modulefile_template_path, 'r') as f:
        content = f.read()

    modulefile_template = Template(content)
    modulefile = modulefile_template.safe_substitute(**vars(args))

    with open(args.VERSION, 'w') as f:
        f.write(modulefile)

if __name__ == '__main__':
    main()