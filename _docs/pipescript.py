"""
This file gets the pipescript documentation directly from the pipes executable, and generates the desired pages for documentation
"""

tpath = "./pipescript/transforms/"

import os
import shutil
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
    md = "# "+transform + "\n*"+o[transform]["description"] + "*\n\n" + o[transform]["documentation"] + "\n\n---\n\n"

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
md = "# List of Transforms\n\n*The following is a list of all transforms built into PipeScript & ConnectorDB. Click on a transform to see details and examples of use.*\n\n"

md+= '<div id="searchable"><input class="search search-query form-control" type="text" placeholder="Search"><br><table class="table table-striped table-bordered" id="ftable"><thead><tr><th>Name</th><th>Description</th></tr></thead><tbody class="list">'

for transform in o:
    t = o[transform]
    md += "<tr><td class='fname'><a href='./"+transform+".html'>" + transform + "</a></td><td class='fdesc'>" + t["description"] + "</td></tr>"

md += "</tbody></table></div>"
# Add list.js which will allow searching
md += '<script type="text/javascript" src="/assets/js/list.min.js"></script><script>var flist = new List("searchable",{valueNames:["fname","fdesc"]});</script>\n\n'
with open(tpath + "index.md","w") as f:
    f.write(md)
