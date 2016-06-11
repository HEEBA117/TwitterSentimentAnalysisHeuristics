import sys
import json


def parse_tweets(stop_words,tweet_file):

	word_list=[]
	word_count_map={}

	for tline in tweet_file:
		#file_content+=tline.strip()
		#print (file_content)
		tweets=json.loads(tline)
		# if type(tweets).__name__ == "dict":
		# 	print("dict")
		# 	continue
		#for tweet in tweets:
		#	print(tweet)
		curr_text=tweets['text']
		clean_text=curr_text.split()
		for clean_wrd in clean_text:
			clean_wrd = clean_wrd.lower()
			#print (clean_wrd)
			
			if clean_wrd not in stop_words:
				if clean_wrd.startswith("@") == False and clean_wrd.startswith('#') == False and clean_wrd.startswith("http:") == False and clean_wrd.startswith("https:") == False:
					if clean_wrd. startswith("&") and clean_wrd.endswith(";") == True:
						continue
					if ('/' in clean_wrd) or ('&' in clean_wrd) or ("\'" in clean_wrd) or ("\\" in clean_wrd) or ('&' in clean_wrd)== True:
						continue
					#if 
					while len(clean_wrd) > 0 and (clean_wrd[0] < 'a' or clean_wrd[0] >'z'):
						clean_wrd = clean_wrd[1:]
					while len(clean_wrd) > 0 and (clean_wrd[-1] < 'a' or clean_wrd[-1] > 'z'):
						clean_wrd = clean_wrd[:-1]
						if clean_wrd not in word_list:
							word_list[len(word_list):]=[clean_wrd]
					if clean_wrd in word_count_map:
						count=word_count_map[clean_wrd]
						count += 1
						word_count_map[clean_wrd] = count
						prev=clean_wrd
					else:
						if clean_wrd != "" and len(clean_wrd) > 1 and clean_wrd not in stop_words:
							word_count_map[clean_wrd] = 1
				#else:
					#print (clean_wrd)

			# else:
			# 	print (clean_wrd)
	return (word_list,word_count_map)



def main():
	word_list=[]
	word_count_map={}
	stop_words=[]
	
	
	tweet_file = open(sys.argv[2])
	stop_word_file=open(sys.argv[1])



	for sline in stop_word_file:
		sword=sline.strip()
		stop_words[len(stop_words):]=[sword]

	#print(stop_words)


	word_list,word_count_map=parse_tweets(stop_words,tweet_file)
	total_count = len (word_list)
	#print (total_count)
	#print(word_count_map)

	sorted_count_map =reversed(sorted (word_count_map,key = word_count_map.get))
	for key in sorted_count_map:
		value = word_count_map[key]/total_count
		#print (key+" , "+value)
		print("{} {}".format(key,str(value)))
		

	#print (word_list)
	
	# 	for word in word_list
	# 		if word 

	# 	tweet_text+=tweets['text']
	# print (tweet_text)
if __name__ == '__main__':
	main()
