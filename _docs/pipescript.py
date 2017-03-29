"""
This file gets the pipescript documentation directly from the pipes executable, and generates the desired pages for documentation
"""

ipath = "./pipescript/"
tpath = "./pipescript/transforms/"

import os
import shutil
if os.path.exists(tpath):
    shutil.rmtree(tpath)
os.makedirs(tpath)

# http://stackoverflow.com/questions/706989/how-to-call-an-external-program-in-python-and-retrieve-the-output-and-return-cod
from subprocess import Popen, PIPE
import json
process = Popen(["pipes", "transforms"], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()

#print(str(output))
# The documentation is loaded as a large json file
o =json.loads(output.decode('utf-8'))

# First generate the transform files
for transform in o:
    t = o[transform]
    md = "<!-- THIS FILE IS AUTO-GENERATED. Edits can be made at https://github.com/connectordb/pipescript/tree/master/resources/docs/transforms -->\n\n"
    md += "# "+transform + "\n*"+o[transform]["description"] + "*\n\n" + o[transform]["documentation"] + "\n\n---\n\n"

    if not "ischema" in t:
        t["ischema"] = ""
    if not "oschema" in t:
        t["oschema"] = ""

    md += "#### Transform Details\n<table class='pipescriptargs'><thead><tr><th>One-To-One</th><th>Stateless</th><th>Peek</th><th>Input Schema</th><th>Output Schema</th></tr></thead>"
    md += "<tr><td>" + str(t["one_to_one"])+"</td><td>" +str(t["stateless"])+"</td><td>" + str(t["peek"])+"</td><td>" + str(t["ischema"])+"</td><td>"  + str(t["oschema"])+"</td></tr></table>\n\n"

    args = t["args"]
    if args!=None and len(args) > 0:
        md += "### Arguments\n<table class='pipescriptargs'><thead><tr><th>#</th><th>Description</th><th>Optional</th><th>Constant</th><th>Hijacked</th><th>Default</th></tr></thead>"
        for i in range(len(args)):
            """
            [{'description': "The time zone to use for determining timestamps, in IANA timezone database format (ex: 'America/New_York'). 'Local' uses the server time zone. 'UTC' uses UTC.", 'constant': True, 'default': 'Local', 'hijacked': False, 'optional': True}]
            """
            arg = args[i]
            if not "default" in arg:
                arg["default"] = ""

            md += "<tr><td>" + str(i+1)+ "</td><td>" + arg["description"]  + "</td><td>" + str(arg["optional"]) + "</td><td>"+ str(arg["constant"]) + "</td><td>" + str(arg["hijacked"]) + "</td><td>" + str(arg["default"]) + "</td></tr>"
        md += "</table>\n"

    with open(tpath + transform + ".md","w") as f:
        f.write(md)

# And finally, we write the index page, which holds the list of transforms
def mkindex(prepend="./"):
    md = "## List of Transforms\n\n*The following is a list of all transforms built into PipeScript & ConnectorDB. Click on a transform to see details and examples of use.*\n\n"

    md+= '<div id="searchable"><input class="search search-query form-control" type="text" placeholder="Search"><br><table class="table table-striped table-bordered" id="ftable"><thead><tr><th>Name</th><th>Description</th></tr></thead><tbody class="list">'

    for transform in o:
        t = o[transform]
        md += "<tr><td class='fname'><a href='"+ prepend+transform+".html'>" + transform + "</a></td><td class='fdesc'>" + t["description"] + "</td></tr>"

    md += "</tbody></table></div>"
    # Add list.js which will allow searching
    md += '<script type="text/javascript" src="/assets/js/list.min.js"></script><script>var flist = new List("searchable",{valueNames:["fname","fdesc"]});</script>\n\n'
    return md

md = mkindex()

# First we write the PipeScript online try-it editor
with open(tpath + "index.md","w") as f:
    f.write("<!-- THIS FILE IS AUTO-GENERATED. Modify pipescript.py in /_docs -->\n\n# Try PipeScript\n\n*You can try PipeScript online here. Paste whatever data you'd like to the box on the left, and the result of your transform will appear in the box on the right!*\n\n")
    f.write('<link href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.25.0/codemirror.min.css" rel="stylesheet"><style type="text/css">.CodeMirror {border: 1px solid black;height: 650px;}</style>'
    + '<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.25.0/codemirror.min.js"></script>'
    + '<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.25.0/mode/javascript/javascript.min.js"></script>'
    + '<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.25.0/addon/edit/matchbrackets.min.js"></script>'
    + '<div class="row"><div class="col-md-12" style="margin-bottom: 10px;"><form><div class="input-group">'
    + '<input type="text" class="form-control" id="script" style="font-family:monospace;font-size: 150%;" value="map(d(\'activity\'),d(\'steps\'):sum)">'
    + '<span class="input-group-btn"><input type="submit" class="btn btn-default" id="scriptbtn" type="button">Go!</button></span></div></form></div></div>'
    + '<div class="row"><div class="col-md-6"><textarea id="input"></textarea></div><div class="col-md-6"><textarea id="output"></textarea></div></div>'
    + '<script src="/assets/js/pipescript_tryit.js"></script>\n\n')
    
    f.write(md)
    f.write('\n\n<script type="text/javascript" src="https://demo.connectordb.io/app/pipescript.js"></script><script>runScript();</script>\n\n')

# Next we write the main transform page
md = mkindex("./transforms/")
with open(ipath + "index.md","w") as f:
    f.write("<!-- THIS FILE IS AUTO-GENERATED. Modify index_start.md for text, and pipescript.py for table.-->\n\n")
    with open(ipath + "index_start.md","r") as r:
        f.write(r.read())
    f.write("\n\n")
    f.write(md)