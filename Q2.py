def input_data():
    '''Asks swallow speed measurements as alphanumeric strings
     where initial charachter is E or U and returns them in KPH format. '''
   
    print("Swallow speed analysis : V1\n")
    data_list=[]
    while True:
        data=input("Enter the next reading:")
        if data=="":
            if len(data_list)==0: print("No readings entered. Nothing to do")
            break
        #storing initial alpha charachter to identify data type.
        first_str=data[0].upper()
        #checking if the input data is in correct format
        if first_str in "EU" and (not data[1:].isalnum()):
            # converting mile into kilometer
            if first_str=="U": data_list.append(float(data[1:])*1.609344)
            elif first_str=="E": data_list.append(float(data[1:]))
            print("Reading saved.") 
        else:
            print("Data format not recognized \n Reading discarded")
   #returning a list containing speed of swallows in KPH format
    return data_list


def display_data(data):
    '''Displays minimum, maximum and average speed of datas entered in a list.'''
    min_speed=min(data)
    max_speed=max(data)
    avg_speed=sum(data)/len(data)
    print("\nResults Summary:\n")
    print(f"minimum speed:{min_speed:.3f}KPH,  {min_speed/1.609344:.3f}MPH.")
    print(f"maximum speed:{max_speed:.3f}KPH,  {max_speed/1.609344:.3f}MPH.")
    print(f"average speed:{avg_speed:.3f}KPH,  {avg_speed/1.609344:.3f}MPH.")

if __name__=="__main__":
    
    final_list=input_data()
    count=""
    counter=len(final_list)
    if counter>0:
        #adding 's' in reading if cases more than one are analysed.
        if counter>1: count="s"
        print(counter,"reading"+count,"analysed")
        display_data(final_list)  
    