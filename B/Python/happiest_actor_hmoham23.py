import sys
import csv

def calculate_score(curr_text,scores,actor):

    clean_text=curr_text.split()

    sums=0
    flag = True
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
                sums += scores[clean_wrd]
                #print ("{} : {}:{}".format(actor,clean_wrd,scores[clean_wrd]))
    #print ("{}:{}".format(clean_text,sum))
    return sums

def main():
    sent_file = open(sys.argv[1])
    csv_file = open(sys.argv[2])
    file_reader = csv.reader(csv_file, delimiter = ',')

    actor_map={}
    final_map={}
    #prev_actor=""

    actor_instance=0
    scores={}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = float(score) # Convert the score to a float.

    for row in file_reader:
        actor = row[0]
        tweet = row[1].lower()
        score=calculate_score(tweet,scores,actor)

        if actor in actor_map:
            curr_score,actor_instance = actor_map[actor]
            actor_instance = actor_instance+1
            curr_score=curr_score + score
            actor_map[actor] = [curr_score,actor_instance]
        else:
            actor_map[actor] = [score,1]


    final_map = {}
    for actor in actor_map:
        curr_score,actor_instance = actor_map[actor]
        value = curr_score / actor_instance
        final_map [actor] = value
     
    final_sorted_map = reversed( sorted(final_map,key=final_map.get))  

    for key in final_sorted_map:
        value = final_map[key]
        print ("{} : {}".format(value,key))
    #     avg_sentiment = curr_score/actor_instance
    #     if avg_sentiment in final_map:
    #         final_map[avg_sentiment].append(actor)
    #     else:
    #         final_map[avg_sentiment]=[actor]

    # sorted_final_map = reversed (sorted(final_map))


    
    # for key in sorted_final_map:
    #     valueArray = final_map[key]
    #     for value in valueArray:
    #         print ("{} : {}".format(key,value))








        #print("{} : {}".format(actor,tweet))


    #TODO: Implement

if __name__ == '__main__':
    main()
