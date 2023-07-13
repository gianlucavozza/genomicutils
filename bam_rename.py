'''
Author: Gianluca Vozza
v.0.1
'''
import os
import argparse
import subprocess

# Parse path file argument
parser = argparse.ArgumentParser(
    prog='bam_reader.py',
    description='This script reads the bam files in a folder and renames them with the appropriate barcode'
)

parser.add_argument(
    "-p",
    "--path",
    type=str,
    default=None,
    required=True,
    help="Path to the bam folder"
),
parser.add_argument(
    "-s",
    "--singularity",
    type=str,
    default=None,
    required=True,
    help="Path to the singularity image of samtools"
),

parser.add_argument(
    "-b",
    "--bind",
    type=str,
    default=None,
    required=True,
    help="Path to the folder to bind"
),
args = parser.parse_args()

# Specify the path to your BAM file
folder = args.path + '/bam/'
file_list = os.listdir(folder)

# Path to the Samtools Singularity image
singularity_image = args.singularity 

# Folder to bind inside the Singularity container
bind_folder = args.bind

for filename in file_list:
    if filename.endswith('.bam'):
        # Use subprocess to call samtools view with the -H option to get the header
        command = [
            "singularity",
            "exec",
            "--bind",
            f"{bind_folder}:{bind_folder}",
            singularity_image,
            "samtools",
            "view",
            "-H",
            os.path.join(folder, filename)
        ]

        header_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = header_process.communicate()

        # Decode the header bytes to a string
        header = stdout.decode()

        # Find the SM tag in the header
        for line in header.split("\n"):
            if line.startswith("@RG"):
                tokens = line.split("\t")
                for token in tokens:
                    if token.startswith("SM:"):
                        sample_name = token[3:]

                        # Rename bam and bai
                        new_bam_filename = os.path.join(folder, sample_name + '.bam')
                        new_bai_filename = os.path.join(folder, sample_name + '.bam.bai')

                        os.rename(os.path.join(folder, filename), new_bam_filename)
                        os.rename(os.path.join(folder, filename + '.bai'), new_bai_filename)

                        break
                break

