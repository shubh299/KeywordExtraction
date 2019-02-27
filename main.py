import sys
import read
import preprocessing
import postprocessing

def main(file_path):
	#file_path=sys.argv[1]
	input_content=read.text_from_txt(file_path)
	candidate_keyword_list_final=preprocessing.preprocess(input_content)
	keywords=postprocessing.postprocess(candidate_keyword_list_final)
	return keywords
	#for word in keywords:
	#	print(word)
	
if __name__=="__main__":
	main()