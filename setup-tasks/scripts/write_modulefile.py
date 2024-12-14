import argparse
import os
from string import Template

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--APP')
    parser.add_argument('--VERSION')
    parser.add_argument('--template', default='default', type=str)
    
    # TODO: Separate argparse sections (per template)
    
    # default
    parser.add_argument('--RELPATH_EXE', required=False)
    
    # venv
    parser.add_argument('--NAME', required=False)
    
    # container
    parser.add_argument('--APPTAINER_MODULE', required=False, default='apptainer/1.3.2')
    parser.add_argument('--CMD', required=False)
    parser.add_argument('--FUNC', required=False)
    parser.add_argument('--IMAGE_NAME', required=False)

    args = parser.parse_args()

    if args.template == 'default':
        mf = '../templates/modulefile.template'
    elif args.template == 'venv':
        mf = '../templates/modulefile-venv.template'
    elif args.template == 'container':
        mf = '../templates/modulefile-container.template'
    else:
        raise ValueError("'--template' must be 'default' or 'venv' or 'container'.")

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