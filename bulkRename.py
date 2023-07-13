#coding=utf-8
'''
Author: G. Vozza
v. 0.1
'''
#modules
import os
import argparse

#check if path is correctly inserted
def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser(description='This program rename VCF files') #program description
parser.add_argument('--path', type=dir_path,
                    help='the path to vcf directory', required=True)# create the argument
args = parser.parse_args()

#VCF indexes
sample_index = 9

for file in os.listdir(args.path): #list all files in the directory
    if file.endswith(".vcf"): #select only vcf files
        with open(args.path +file, 'r') as f: #read the file
             for line in f: 
                if '##' in line:                
                    continue
                elif '#' in line: #take only the header line (#CHROM, POS, etc.)
                    name = line.strip().split("\t")[sample_index] #split the line and take only sample name
                    os.rename(args.path + file, args.path + name + ".vcf") #rename file with sample name and add vcf extension
                    
        
