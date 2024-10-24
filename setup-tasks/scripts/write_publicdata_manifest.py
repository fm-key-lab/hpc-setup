import argparse
import os
from string import Template

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--GROUP_DATA')
    parser.add_argument('--output')

    args = parser.parse_args()

    publicdata_template_path = os.path.join(
        os.path.dirname(__file__), '../templates/publicdata_json.template'
    )
    with open(publicdata_template_path, 'r') as f:
        content = f.read()

    publicdata_template = Template(content)
    publicdata = publicdata_template.safe_substitute(**vars(args))

    with open(args.output, 'w') as f:
        f.write(publicdata)

if __name__ == '__main__':
    main()