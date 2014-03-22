from helper import *
from operator import itemgetter

def splitDNA(dna_string):
	'''
	Splits the dna by ID
	'''
	l = dna_string.split('>')

	return l[1:]
	 
	
def GCContent(dna_list):
	'''
	Returns a list of DNA IDs and their GC content
	'''
	GC_content_list = []
	for i in dna_list:
		DNA_s = i.split('\n', 1)
		DNA_s[1] = DNA_s[1].replace('\n', '')
		GC_count = 0.0
		for l in DNA_s[1]:
			if l == 'G' or l == 'C':
				GC_count += 1.0
		GC_content = float(GC_count)/len(DNA_s[1])*100
		GC_content_list.append((DNA_s[0], GC_content))

	return GC_content_list


def highestGCContent(GC_content_list):
	'''
	Returns the DNA ID and the GC content of the DNA with the highest GC content
	'''
	winner = max(GC_content_list, key=itemgetter(1))
	return str(winner[0]) + '\n' + str(winner[1])



print highestGCContent(GCContent(splitDNA(txtToString('test.txt'))))