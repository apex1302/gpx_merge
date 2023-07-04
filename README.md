# gpx_merge

GPX Merge Tool - Combine Two GPX Files into One

Usage: python gpx_merge.py --file1 <file1.gpx> --file2 <file2.gpx> --output <output.gpx>

Description:
The GPX Merge Tool allows you to combine two GPX (GPS Exchange Format) files into a single GPX file. It appends all track segments from the second GPX file to the first GPX file, creating a merged output file.

Arguments:
  --file1 <file1.gpx>    Path to the first GPX file.
  --file2 <file2.gpx>    Path to the second GPX file.
  --output <output.gpx>  Output file name for the merged GPX file.

Example:
  python gpx_merge.py --file1 path/to/file1.gpx --file2 path/to/file2.gpx --output path/to/output.gpx

Notes:
- Ensure that you have Python installed on your system before running the tool.
- Make sure you have valid GPX files to merge. The tool will append all track segments from the second file to the first file.
- The output file should have the ".gpx" extension.
- Provide the correct paths to the input files and specify the desired output file path when running the tool.

