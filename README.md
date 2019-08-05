# fastaselect
Find sequences from a large fasta file by names，length and keywords  
usage: fastaselect.py [-h] -o OUTPUT -i INPUT [-k KEYWORD] [-n NAME] [-m MIN]  

Extract fasta sequence  

optional arguments:  
  -h, --help            show this help message and exit  
  -o OUTPUT, --output OUTPUT  
                        The output file  
  -i INPUT, --input INPUT  
                        The input file  
  -k KEYWORD, --keyword KEYWORD  
                        Find special sequence compliance with your matching
                        rules  
  -n NAME, --name NAME  A file contain the sequence name you want to extract  
  -m MIN, --min MIN     Minimum length  
  
Example:  
Find sequence longer than 500bp  
fastaselect.py -o output.fasta -i input.fasta -m 500  
  
Find sequence by keywords or regular expression  
fastaselect.py -o output.fasta -i input.fasta -k ^\w.*\d  

Find squence by sequence name  
fastaselect.py -o output.fasta -i input.fasta -n name.txt  
  
$cat name.txt  
seq1  
seq2  
seq3  
seq4  
######################################################################################
Please note that the file path is differenc in windows and linux:  
Windows: C:\\your\\file\\path\\file.fasta  
Linux: /home/your/file/path/file.fasta  
zhutao@cau.edu.cn for help  
#######################################################################################
