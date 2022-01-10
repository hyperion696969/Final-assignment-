from random import choice 

def email_validity(email):
    '''Checks validity of Email address and returns true or false. 
        For returning true: number of @ must be exactly 1, length of characters
        before @ must minimum be 2,
        domain name must be "pop.ac.uk" only.'''
    
    return True if email.count("@")==1 and email.index("@")>=2 and email[-9:]=="pop.ac.uk" else False

def word_check(sentence):
    keywords=["wifi","library","deadline","service","payment","1234"]
    for word in keywords:
        if word in sentence: return word

input_string=""
operator_list=["Sam","Jamie","Jenny","Ken","Tony","Bruce"]
random_response=["Hmmmm.........","Ohhhh.....","Tell me more","Oh,yes, I see","Yes?"]
keywords=["wifi","library","deadline","service","payment","1234"]
exit_commands=["exit","bye","help"]

success_sample=9
failure_sample=10-success_sample
network_modes=([1]*success_sample)+([0]*failure_sample)

print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.\n")
user_email=input("Please enter your Poppleton email address:")

if email_validity(user_email):
    
    user=user_email[:(user_email.index("@"))]
    
    print(f"Hi, {user}! Thank you, and Welcome to PopChat!")
    print(f"My name is {choice(operator_list)}, and it will be my pleasure to help you.\n")
    
    while True:
        
        network_status=choice(network_modes)
        if network_status==0:
            print("*****NETWORK ERROR*****")
            break
        input_string=input()
        if input_string.lower() in exit_commands:break
            
        keyword_dict={"wifi":["WiFi is excellent across the campus.",
                              "The local campus WiFi is of 50-60 GBps.",
                              "We are proud to announce that our Wifi is very stable." ],

                    "library":["The library is closed today.",
                              "Library is opposite of our college cafe.",
                              "We also have a E-library. For more info search our official site."  ],

                   "deadline":["Your deadline has been extended by two working days.",
                               "Deadline cannot be negotitated by fellow students."],

                   "service":["We have lab for each faculties near library.",
                              "Our college cafe is open 24/7."  ],

                   "payment":["Please contact college recption for details.",
                              "Payment for each semester must be paid in the same semester."],

                   "1234":["get on the dance floor!"]
                   }
        
        try:
            print(choice(keyword_dict[word_check(input_string)]))
        except:
            print(choice(random_response))
        print("\n")    
    
    print(f"Thanks, {user}, for using PopChat. See you again soon!")

else:
    print("Invalid user email.")