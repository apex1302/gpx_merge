import argparse
import xml.etree.ElementTree as ET

def combine_gpx_files(file1, file2, output_file):
    # Load the first GPX file
    tree1 = ET.parse(file1)
    root1 = tree1.getroot()

    # Load the second GPX file
    tree2 = ET.parse(file2)
    root2 = tree2.getroot()

    # Specify the XML namespace for GPX
    namespace = "http://www.topografix.com/GPX/1/1"

    # Append all track segments from the second GPX file to the first GPX file
    for trkseg in root2.findall(f'.//{{{namespace}}}trkseg'):
        root1.append(trkseg)

    # Save the combined GPX file with the correct namespace
    ET.register_namespace('', namespace)  # Register the namespace with an empty prefix
    tree1.write(output_file, xml_declaration=True, encoding='utf-8', method="xml")

    print(f"Combined GPX file saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Combine two GPX files into one.')
    parser.add_argument('--file1', required=True, help='Path to the first GPX file')
    parser.add_argument('--file2', required=True, help='Path to the second GPX file')
    parser.add_argument('--output', required=True, help='Output file name')
    args = parser.parse_args()

    combine_gpx_files(args.file1, args.file2, args.output)

