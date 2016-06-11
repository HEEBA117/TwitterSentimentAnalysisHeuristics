import sys
import json


def calculate_score(curr_text,scores):

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
                #print ("{}:{}".format(actor,clean_wrd,scores[clean_wrd]))
    #print ("{}:{}".format(clean_text,sum))
    return sums

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    bottomList = []


    #TODO: Implement
    final_map={}
    scores={}
    st_score_map={}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = float(score) # Convert the score to a float.

    state_map={"AL":"Alabama",
    "AK":"Alaska",
    "AZ":"Arizona",
    "AR":"Arkansas",
    "CA":"California",
    "CO":"Colorado",
    "CT":"Connecticut",
    "DE":"Delaware",
    "DC":"District of Columbia",
    "FL":"Florida",
    "GA":"Georgia",
    "HI":"Hawaii",
    "ID":"Idaho",
    "IL":"Illinois",
    "IN":"Indiana",
    "IA":"Iowa",
    "KS":"Kansas",
    "KY":"Kentucky",
    "LA":"Louisiana",
    "ME":"Maine",
    "MT":"Montana",
    "NE":"Nebraska",
    "NV":"Nevada",
    "NH":"New Hampshire",
    "NJ":"New Jersey",
    "NM":"New Mexico",
    "NY":"New York",
    "NC":"North Carolina",
    "ND":"North Dakota",
    "OH":"Ohio",
    "OK":"Oklahoma",
    "OR":"Oregon",
    "MD":"Maryland",
    "MA":"Massachusetts",
    "MI":"Michigan",
    "MN":"Minnesota",
    "MS":"Mississippi",
    "MO":"Missouri",
    "PA":"Pennsylvania",
    "RI":"Rhode Island",
    "SC":"South Carolina",
    "SD":"South Dakota",
    "TN":"Tennessee",
    "TX":"Texas",
    "UT":"Utah",
    "VT":"Vermont",
    "VA":"Virginia",
    "WA":"Washington",
    "WV":"West Virginia",
    "WI":"Wisconsin",
    "WY":"Wyoming"}

    state_name=""
    #scores={}


    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = float(score)

    for tline in tweet_file: #iterating over each tweet
        tweets=json.loads(tline)
        if tweets['place']: # finding city
            place = tweets['place']
            country = place['country'] 

            if country == "United States": # restricting to US
                state_name = ""
                place_type = place['place_type']
                full_name = place['full_name']
                state_var = full_name.split(',')
                #print(place)

                #print ("{} : {}".format(place_type,full_name))
                if place_type == "city":
                    state_abb = state_var[1].strip()
                    #print (state_abb)
                    if state_abb in state_map:
                        state_name = state_map[state_abb]
                    else:
                        continue
                elif place_type == "admin":
                    state_name = state_var[0].strip()
                else:
                    continue

                if state_name == "":
                    continue

                tweet = tweets['text'].lower()
                #print (tweet)
                score=calculate_score(tweet,scores)
                #print (score)
                if state_name not in st_score_map:
                    st_score_map[state_name] = [0,0]

                curr_score,state_instance = st_score_map[state_name]
                state_instance = state_instance+1
                curr_score=curr_score + score
                st_score_map[state_name] = [curr_score,state_instance]



    for st in st_score_map:
        curr_score,state_instance = st_score_map[st]
        final_map [st] = curr_score/state_instance
        #print ("{} : {},{}".format(st,curr_score,state_instance))
    #     avg_sentiment = curr_score/actor_instance

                #score
    sorted_final_map =reversed(sorted (final_map,key = final_map.get))


    count = 0;
    for key in sorted_final_map:
        count +=1
        value = final_map[key]
        print("{} : {}".format(value,list(state_map.keys())[list(state_map.values()).index(key)]))
        if count==5:
            break

    sorted_final_map = sorted(final_map, key =final_map.get)

    count = 0
    for key in sorted_final_map:
        count +=1
        value =final_map[key]
        value = "{} : {}".format(value,list(state_map.keys())[list(state_map.values()).index(key)])
        bottomList[len(bottomList):] = [value]
        if count == 5:
            break

    bottomList.reverse()
    for item in bottomList:
        print (item)
    #print(bottomList)
    
                    


                
            #curr_text=tweets['text']





if __name__ == '__main__':
    main()
