def bridge_keeper():
    """A function which simulates a bridge keeper from
                    Monty Python          """
    print("Stop! Who would cross the Bridge of Death \nMust answer me these questions three, 'ere the other side he see.")

    name=input("What is your name?")
    if "arthur" in name.lower(): return "My liege! You may pass!"

    quest=input("What is your quest?")
    if "grail" not in quest.lower(): return "Only those who seek grail may pass."

    colour=input("What is your favourite colour?")
    if colour[0].lower()==name[0].lower(): return "You may pass!"

    return "Incorrect! You must now face the Gorge of Eternal Peril."

if __name__=="__main__":
        
    print(bridge_keeper())
    