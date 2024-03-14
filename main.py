import argparse

source_var = "admin"
target_var = "them selves"
slap_string = f"{source_var} slaps {target_var} around a bit with a large trout"
rtfm_var = """rtfm:
--host host-address
--target target-address
--output file-name (optional)
"""

parser = argparse.ArgumentParser(description="slap target around a bit with a large trout")

parser.add_argument("-t", "--target", type=str, help="Target address")
parser.add_argument("-s", "--source", type=str, help="Source address")
parser.add_argument("-o", "--output", type=str, help="Output file name (optional)")

args = parser.parse_args()



if args.target:
    target_var = args.target

if args.source:
    source_var = args.source


if not args.output: #False being default state
    print(slap_string)
else:
    pass