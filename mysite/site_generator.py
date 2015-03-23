from __future__ import print_function
import codecs
import os
from string import Template
import sys

import markdown

def split_metadata(text, split_str="--=--"):
    """
    Separate metadata from the body of the post

    Returns a dict of the metadata and the body text
    """
    metadata, markdown = text.split(split_str, 1)

    metadata = metadata.strip().split('\n')
    meta_dict = {}
    for line in metadata:
        key, val = line.split(': ')
        meta_dict[key] = val

    return meta_dict, markdown.strip()

def render_template(template, metadata, body):
    """
    Renders a metadata dictionary and html body into a template string
    """
    template = Template(template)
    rendered = template.safe_substitute(body=body, **metadata)
    return rendered

def generate_index(out_dir, index_template):
    # List the files, build links, put it into html, render.
    # use a link template to make the links? Will we need the RAX
    # cloud lib to do this?
    pass

def process_story(file_name):
    input_file = codecs.open(file_name, mode='r', encoding='utf-8')
    text = input_file.read()
    metadata, md_text = split_metadata(text)
    html = markdown.markdown(md_text)

    template_file = codecs.open('templates/story.html.tmpl',
                                mode='r',
                                encoding='utf-8')
    template = template_file.read()

    rendered_html = render_template(template, metadata, html)


    # Cut off the './' and '.md'
    if file_name.startswith('./'):
        out_file_name = file_name[2:-3]
    else:
        out_file_name = file_name[:-3]

    out_file_name= '_site/%s.html' % out_file_name

    out_file = codecs.open(out_file_name, mode='w', encoding='utf-8')
    out_file.write(rendered_html)

    print("Wrote %s" % out_file_name)

def main(file_name):
    process_story(file_name)
    generate_index(None, None)


if __name__ == '__main__':
    main(sys.argv[1])
