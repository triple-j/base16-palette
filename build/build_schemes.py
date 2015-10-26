#!/usr/bin/env python 

import os
from git import Repo
from shutil import rmtree
from glob import glob
import xml.etree.ElementTree as etree
import re

git_url = "https://github.com/chriskempson/base16.git"
repo_dir = "./base16"
scss_dir = "../scss/color-schemes"

labels = [
    "base00",
    "base01",
    "base02",
    "base03",
    "base04",
    "base05",
    "base06",
    "base07",
    "base08",
    "base09",
    "base0A",
    "base0B",
    "base0C",
    "base0D",
    "base0E",
    "base0F"
    ]

if os.path.isdir(repo_dir):
    # delete repo_dir
    rmtree(repo_dir)

# clone repo
Repo.clone_from(git_url, repo_dir)

# find all svg palettes
palettes = glob(repo_dir+"/scheme-previews/*.svg")

for palette in palettes:
    tree = etree.parse(palette)
    root = tree.getroot()
    
    filename = os.path.basename(palette)
    filename = re.sub(r'^base16-', '', filename, flags=re.IGNORECASE)
    filename = re.sub(r'\.svg$', '', filename, flags=re.IGNORECASE)
    filename = "_" + filename + ".scss"
    filepath = scss_dir + "/" + filename
    
    text = "";
    
    title = root.find(".//{http://www.w3.org/2000/svg}title").text
    
    text += "// " + title + "\n\n"
    
    colors = {}
    for label in labels:
        colors[label] = root.find(".//*[@id='" + label + "']").attrib['stroke']
        
        text += "$" + label + ": " + colors[label] + " !default;\n"
    
    print "Writing: " + title + " (" + filepath + ")"
    
    f = open(filepath, 'w')
    f.write(text)
    f.close()
