import argparse
import subprocess

parser = argparse.ArgumentParser(description="test-tool")

parser.add_argument("-t", "--target", type=str, help="Target address")
parser.add_argument("-s", "--source", type=str, help="Source address")
parser.add_argument("-o", "--output", type=str, help="Output file name (optional)")

args = parser.parse_args()

source_var  = "Admin"           if args.source is None else args.source
target_var  = "them seleves"    if args.target is None else args.target
slap_string = f"{source_var} slaps {target_var} around a bit with a large trout"

if not args.output: #False being default state
    print(slap_string)
else:
    output_name = "results/date-n-time.txt"
    output_file = open(output_name,"w")
    output_file.write(slap_string + "\n")
    output_file.close()
    print(f"Results saved to {output_name}")