import sys
import json


def calculate_score(curr_text,scores):
    clean_text=curr_text.split()
    sum=0
    for clean_wrd in clean_text:
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
            if clean_wrd in scores:
                sum += scores[clean_wrd]
    #print ("{}:{}".format(clean_text,sum))
    return (clean_text,sum)




def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #TODO: Implement
    final_score=0
    score_map={}

    afinnfile = sent_file

    scores={}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = float(score) # Convert the score to a float.

    for tline in tweet_file:
        tweets=json.loads(tline)
        curr_text=tweets['text']
        curr_text = curr_text.replace("\n"," ")
        tweet,score=calculate_score(curr_text,scores)
        #print ("score : {}".format(score))
        #print ("score: {}:{}".format(tweet,score))
        if score in score_map:
            score_map[score].append(curr_text)
        else:
            score_map[score] = [curr_text]

    sorted_score_map = reversed (sorted(score_map))

    firstTen=0
    flag = False
    tweet_text = ""
    for key in sorted_score_map:
        
        #print (key)
        valueArray = score_map[key]
        for value in valueArray:
            firstTen += 1
            
            #print("count = {}".format(firstTen))
            print ("{} : {}".format(key,value))
            

            if firstTen == 10:
                flag = True
                break
        if flag == True:
            break

    #print ("\n\n")

    firstTen=0
    flag = False
    bottomList=[]
    sorted_score_map = sorted(score_map)

    for key in sorted_score_map:
        #print (key)
        valueArray = score_map[key]
        for value in valueArray:
            firstTen += 1
            
            value = "{} : {}".format(key,value)
            bottomList[len(bottomList):] = [value]
            #print ("{} : {}".format(key,str(value)))
            if firstTen == 10:
                flag = True
                break
        if flag == True:
            break

    bottomList.reverse()

    for item in bottomList:
        print (item)





if __name__ == '__main__':
    main()
