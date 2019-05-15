from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
import pandas as pd

def postprocess(candidate_keyword_list_final):
	candidate_keyword_dict={}
	candidate_keyword_list_indexwise=[]
	matrix_index=0
	
	for phrase in candidate_keyword_list_final:
		words=word_tokenize(phrase)
		temp_list=[]
		for word in words:
			if word not in candidate_keyword_dict:
				candidate_keyword_dict[word]=matrix_index
				matrix_index+=1
			temp_list.append(candidate_keyword_dict[word])
		candidate_keyword_list_indexwise.append(temp_list)
	
	matrix=np.zeros((matrix_index,matrix_index),dtype=int)
	for each_list in candidate_keyword_list_indexwise:
		each_list.sort()
		length=len(each_list)
		for i in range(length):
			for j in range(i,length):
				matrix[each_list[i],each_list[j]]+=1
				if each_list[i]!=each_list[j]:
					matrix[each_list[j],each_list[i]]+=1
	
	word_score=np.zeros((matrix_index,3))
	for i in range(matrix.shape[0]):
		word_score[i][0]=matrix[i].sum()
		word_score[i][1]=matrix[i,i]
		word_score[i][2]=word_score[i][0]/word_score[i][1]
	
	'''removing candidate keywords that are a part of other candidate keywords'''
	temp_list=[]
	for i in range(len(candidate_keyword_list_indexwise)-1):
		for j in range(i+1,len(candidate_keyword_list_indexwise)):
			if set(candidate_keyword_list_indexwise[i]).issubset(set(candidate_keyword_list_indexwise[j])):
				temp_list.append(i)
	
	temp_list=set(temp_list)
	for i in temp_list:
		candidate_keyword_list_indexwise[i]='-'
	del(temp_list)
	
	final_keywords_score_index=[]
	for i in range(len(candidate_keyword_list_indexwise)):
		if candidate_keyword_list_indexwise[i]=='-':
			final_keywords_score_index.append(0)
			continue
		temp_sum=0
		for each_index in candidate_keyword_list_indexwise[i]:
			temp_sum+=word_score[each_index][2]
		final_keywords_score_index.append(temp_sum)
		
	word_score_frame=pd.DataFrame({'candidate_keyword':candidate_keyword_list_final,'score':final_keywords_score_index})
	word_score_frame.drop_duplicates('candidate_keyword',inplace=True)
	word_score_frame.sort_values('score',ascending=False,inplace=True)
	#threshold=word_score_frame['score'].mean()
	print(word_score_frame)
	threshold=0.4
	threshold_value=word_score_frame['candidate_keyword'].count()*threshold
	keywords=word_score_frame.head(int(threshold_value))
	return keywords['candidate_keyword'].values.tolist()