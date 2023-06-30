import xml.etree.ElementTree as ET
import argparse

def find_zone_names(root):
    zone_name_dict = []
    zone_id_dict = []
    for child in root:
        if child.tag == 'zones':
            id = child
            break
    for id_tag in id:
        if id_tag.tag == 'zone':
            for child in id_tag:
                if child.tag == 'name':
                    zone_name_dict.append(child.text)
            for child_id in id_tag:
                if child_id.tag == 'id':
                    zone_id_dict.append(child_id.text)
    print("De volgende zones zijn gevonden: ")
    for i in range(len(zone_name_dict)):
        print("\t Zone name: ", zone_name_dict[i] + ", met volgende zone id: ", zone_id_dict[i])

def find_zone(root, zone_id):
    for child in root:
        if child.tag == 'zones':
            id = child
            break
    for id_tag in id:
        if id_tag.tag == 'zone':
            for child in id_tag:
                if child.tag == 'id' and child.text == zone_id:
                    return child
                    
def change_zone_id(id, new_id):
    id.text = new_id

def do_zone_swap(id1, id2):
    temp = id1.text
    id1.text = id2.text
    id2.text = temp

def main(arg_input_file, arg_output_file, arg_zone1, arg_zone2):
    print("From: " + arg_input_file + " is zone " + arg_zone1 + " swapped with zone " + arg_zone2 + " and saved to " + arg_output_file)
    tree = ET.parse(arg_input_file)
    root = tree.getroot()
    do_zone_swap(find_zone(root, arg_zone1), find_zone(root, arg_zone2))
    tree.write(arg_output_file)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Swaps two zones in a Brightsign BPF file')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    parser.add_argument('-z1', '--zone1', help='Zone 1', required=True)
    parser.add_argument('-z2', '--zone2', help='Zone 2', required=True)
    args = parser.parse_args()
    print("Starting Brightsign BPF zone swapper")
    main(args.input, args.output, args.zone1, args.zone2)