import glob
import yaml
from datetime import datetime
import sys

if (len(sys.argv) != 3):
    print("ERROR: incorrect number of arguments")
    print("")
    print("Usage: python publish.py <project> <entry>")

# command line arguments
project = sys.argv[1]
entry   = sys.argv[2]

# other variables
pantheon_url = "github.com/pantheonscience/workflows"
mdfname      = entry + ".md"
dtime        = datetime.today() 
date         = dtime.strftime("%d %b %Y %H:%M:%S MDT")

with open(mdfname, "w") as mfile:

    fullpath = "entry/" + project + "/" + entry
    with open(fullpath + "/pantheon.yaml", "r") as pfile, open(fullpath + "/commit.yaml", "r") as cfile:
        pdata = yaml.load(pfile, Loader=yaml.FullLoader)
        cdata = yaml.load(cfile, Loader=yaml.FullLoader)

        with open(fullpath + "/pantheon_workflow.bib", "w") as bfile:
            bfile.write("@online{\n")
            bfile.write("  author    = {{{}}},\n".format(pdata["contact"]["contact_name"]))
            bfile.write("  title     = {{Pantheon/{}/{}}},\n".format(
                                                pdata["project"]["project_name"],
                                                pdata["workflow"]["workflow_name"]))
            bfile.write("  publisher = {pantheon.org},\n")
            bfile.write("  date      = {{{}}},\n".format(date))
            bfile.write("  url       = {{{}}},\n".format(cdata["repository"]))
            bfile.write("  commit    = {{{}}},\n".format(cdata["commit"]))
            bfile.write("  note      = {Citation is for workflow only. For other citations, see attribution in workflow documentation.}\n")
            bfile.write("}\n")

    mfile.write("|||\n")
    mfile.write("|-|-|\n")
    mfile.write("|name|[{}]({}/tree/{})|\n".format(
                        pdata["workflow"]["workflow_name"],
                        cdata["repository"], cdata["commit"] ))
    mfile.write("|desc|{}|\n".format(pdata["workflow"]["workflow_desc"]))
    mfile.write("|state|{}|\n".format(pdata["pantheon"]["pantheon_state"]))
    mfile.write("|repository|{}|\n".format(cdata["repository"]))
    mfile.write("|commit|{}|\n".format(cdata["commit"]))
    mfile.write("|date|{}|\n".format(date))
    mfile.write("|citation|[citation](https://{}/blob/master/entry/{}/{}/pantheon_workflow.bib)|\n".format(pantheon_url, project, entry))
    mfile.write("\n")


