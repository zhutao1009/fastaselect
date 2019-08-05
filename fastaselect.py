# -*- coding: utf-8 -*-
#fastaselect
#version 0.1
#author Tao Zhu
#email zhutao@cau.edu.cn

import re
import argparse

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description = 'Extract fasta sequence')
parser.add_argument('-o','--output',help="The output file",type=str,required=True)
parser.add_argument('-i','--input',help="The input file",type=str,required=True)
parser.add_argument('-k','--keyword',help="Find special sequence compliance with your matching rules",type=str)
parser.add_argument('-n','--name',help="A file contain the sequence name you want to extract ",type=str)
parser.add_argument('-m','--min',help="Minimum length",type=int)
args = parser.parse_args()

def readfasta(input):
	with open(input,'r') as f:
		fasta={}
		for line in f:
			line = line.strip()
			if line[0] == '>':
				header = line[1:]
			else:
				sequence = line
				fasta[header] = fasta.get(header,'') + sequence
	return fasta 

def readfastahead(seqhead):
	seq=open(seqhead)
	seqname=[]
	for i in seq:
		seqname.append(i.strip("\n"))
	return seqname

def fastawrit(list,listname,file):
	f=open(file,"a+")
	a=0
	f.write(">"+str(listname)+"\n")
	while a < len(list):
		cache=list[a:(a+80)]
		a+=80
		f.write(cache+'\n')
	f.close()

def findfasta(seqhead,seq,file):
	for i in seqhead:
		fastawrit(seq[i],str(i),file)


def length(seq,min,file):
	for i in seq:
		if len(seq[i]) >= min:
			fastawrit(seq[i],str(i),file)

def findbykword(keyword,seq,file):
	for i in seq:
		if bool(re.search(keyword, str(i))):
			fastawrit(seq[i],str(i),file)


if __name__ == '__main__':
	if args.output and args.input != None :
		inputfasta=readfasta(args.input)
		if args.keyword!= None:
			findbykword(args.keyword,inputfasta,args.output)
		if args.name != None:
			name=readfastahead(args.name)
			findfasta(name,inputfasta,args.output)
		if args.min != None:
			length(inputfasta,args.min,args.output)
	else:
		print ("Missing necessary parameters -i or -o")