# genomicutils
genomicutils is a light python tool to rename a bulk of VCF and BAM files by reading the barcode within their header.

### Quick start
```
git clone https://github.com/gianlucavozza/genomicutils.git
cd genomicutils
singularity pull docker://biocontainers/samtools:v1.9-4-deb_cv1
```
To rename a bulk of VCF files, type:
```
python bulkRename.py -p $VCF_FOLDER
```

To rename a bulk of bam files, first bam files must have been put into a ***folder/bam/*** folder structure. Then, type:
```
python bam_rename.py -p folder/ -s path/to/samtools.simg -b path/to/bind
```
***-b*** is actually not required. It has to be used if the user need to mount an other path than the one with the BAMs.

### Additional information
To report bugs or any kind of issue, please contact drgianluca.vozza@gmail.com
