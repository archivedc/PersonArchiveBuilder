import glob
import os
import shutil

from jinja2 import Environment, FileSystemLoader
import yaml

import parser.identityParser as identityParser

# Delete output directory if exists
if (os.path.isdir("./output")):
    shutil.rmtree("./output")

# Copy Static Directory
shutil.copytree("./templates/static", "./output")

for f in glob.glob("input/*.yaml"):
    data = {}

    with open(f, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('person.html')

    if 'primaryDisplayLanguage' in data:
        data['defaultName'] = data['name'][data['primaryDisplayLanguage']]

    if 'links' not in data:
        data['links'] = []

    if 'identity' in data:
        for k, v in data['identity'].items():
            ilink = identityParser.parse(k, v)
            if isinstance(ilink, list):
                data['links'] += ilink
            elif (ilink != None):
                data['links'].append(ilink)

    with open('output/' + os.path.basename(f).split('.')[0] + '.html', 'w', encoding="utf-8") as file:
        file.write(template.render(data))
