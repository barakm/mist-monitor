#
# Python script to monitor number of running instances across all clouds used by R&D for development.
# Does not scan test and production resources.
# Generates a file called output.xml with the details of the running VMs.
#
# Sample:
#
# <?xml version="1.0" ?>
# <machines>
#   <machine cloud="EC2 EU Ireland - ec2Demo" name="vagrant cloudify hubot" state="running"/>
#   <machine cloud="HP - US East - hpcloud-paid-dev2" name="ui-staging" state="running"/>
#   <machine cloud="HP - US West - hpcloud-paid-dev1" name="cloudify-management-server" state="running"/>
#   <machine cloud="HP - US East - hpcloud-paid-dev1" name="nightly-server_nodecellar_dep_nodejs_vm_ea760" state="running"/>
#   <machine cloud="HP - US East - hpcloud-paid-dev1" name="cloudify-management-server-itsik" state="running"/>
#   <machine cloud="HP - US East - hpcloud-paid-dev1" name="nightly-server_monitoring_dep_vm_70910" state="running"/>
#   <machine cloud="HP - US East - hpcloud-paid-dev1" name="nightly-server_nodecellar_dep_mongod_vm_36cf4" state="running"/>
#   <machine cloud="HP - US East - hpcloud-paid-dev3" name="cloudify-management-server-ranz" state="running"/>
# </machines>
__author__ = 'barakme'

from mistclient import MistClient
import sys


def print_usage():
    print "Usage:\n" \
          "======" \
          "python mist_monitor <username> <password>"

if len(sys.argv) != 3:
    print_usage()
    exit(1)

client = MistClient(email=sys.argv[1], password=sys.argv[2])

def print_metrics():
    print "Loading list of machines"
    machines = client.machines()
    running_machines = [machine for machine in machines if machine.info['state']=="running"]
    print "Total machines: %i" % len(machines)
    print "Running machines: %i" % len(running_machines)

    import xml.etree.ElementTree as ET
    import xml.dom.minidom

    machinesNode = ET.Element("machines")
    machinesNode.set("total", "%i" % len(machines))
    for running_machine in machines:
        machineNode = ET.SubElement(machinesNode, "machine")
        machineNode.set("name", running_machine.name)
        machineNode.set("cloud", running_machine.backend.title)
        machineNode.set("state", running_machine.info['state'])

    tree = ET.ElementTree(machinesNode)

    xml_string = ET.tostring(machinesNode)
    parsed_xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_string = parsed_xml.toprettyxml(indent="\t")

    print pretty_xml_string

    text_file = open("output.xml", "w")
    text_file.write(pretty_xml_string)
    text_file.close()

print_metrics()


