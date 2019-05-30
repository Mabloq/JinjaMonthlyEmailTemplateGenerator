import os
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
import glob


def get_filepaths(path):
    result = []

    for root, dirs, files in os.walk(path):
        files = glob.glob(os.path.join(root, '*.html'))
        for f in files:

            result.append(os.path.abspath(f))
    return result


def main():
    htmlfiles = get_filepaths('./Emails')
    results = []
    for path in htmlfiles:
        page = open(path, "r")
        soup = BeautifulSoup(page, 'html.parser')

        for keep in soup.select('.keep'):
            print(keep.tr)
            keep.img['align'] = "right"
            keep.img['style'] = "border-style: none;margin-left: 20px"
            print('====================================')
            keep.br.extract()
            print(keep)
            results.append(keep)
        page.close()

    template_loader = FileSystemLoader(searchpath="./")
    template_env = Environment(loader=template_loader)
    template = template_env.get_template('monthly_template.jinja2')
    output_from_parsed_template = template.render(keepers=results)
    with open("output1.html", "w") as file:
        file.write(output_from_parsed_template)


if __name__ == "__main__":
    main()
