#from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
import nltk

#import nltk
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('stopwords')

def get_wordnet_pos(treebank_tag):

		if treebank_tag.startswith('J'):
			return wordnet.ADJ
		elif treebank_tag.startswith('V'):
			return wordnet.VERB
		elif treebank_tag.startswith('N'):
			return wordnet.NOUN
		elif treebank_tag.startswith('R'):
			return wordnet.ADV
		else:
			return wordnet.NOUN

def preprocess(input_text):
	input_text=input_text.lower()
	stop_tags=['CC','CD','DT','EX','IN','LS','MD','PDT','PRP','PRP$','TO','UH','WDT','WP','WP$','WRB','VB','VBD','VBG','VBN','VBP',',','.',':',';','(',')','[',']','{','}']
	#stop_words=list(stopwords.words('english'))+['also','usually','however','enable','give','type','use','mixed','consider']
	stop_words=[word.rstrip("\n") for word in open("stopWords.txt",mode="r")]
	#stop_words=['enable','i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'be', 'do', 'until', 'about', 'against', 'between', 'into', 'through', 'during', 'again', 'further', 'then', 'once', 'here', 'there', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 'give', 'type', 'use', 'mixed', 'consider']
	#print(stop_words)
	lemmatizer = WordNetLemmatizer()
	sentences=sent_tokenize(input_text)
	candidate_keyword_string=''
	candidate_keyword_list=''
	for a in sentences:
		sentence_tags=nltk.pos_tag(word_tokenize(a))
		for index in range(len(sentence_tags)):
			if sentence_tags[index][1] in stop_tags:    ###Replacing stop words with --
				sentence_tags[index]="-"
			else:
				sentence_tags[index]=lemmatizer.lemmatize(sentence_tags[index][0],get_wordnet_pos(sentence_tags[index][1]))
				if sentence_tags[index] in stop_words:
					sentence_tags[index]="-"
		#print(sentence_tags)
		candidate_keyword_list=' '.join(sentence_tags)
		candidate_keyword_string+=candidate_keyword_list

	candidate_keyword_list_final=candidate_keyword_string.split('-')
	candidate_keyword_list_final=list(filter(lambda a: a!=' ',candidate_keyword_list_final))
	candidate_keyword_list_final=list(filter(lambda a: a!='',candidate_keyword_list_final))
	for index in range(len(candidate_keyword_list_final)):
		candidate_keyword_list_final[index]=candidate_keyword_list_final[index].strip(" ")
	#print(candidate_keyword_list_final)
	return candidate_keyword_list_final




