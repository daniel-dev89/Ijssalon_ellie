def presenteer(data: dict, totaal):

    for key, value in data.items():
        print(f"{key} : {value} euro")
    
    print("=" * 20)  
    print(f"totaal : {totaal} euro")  

mijn_dict = {
        'vis' : 10, 
        'vlees' : 25,
        'overig' : 15
    }
totaal = 50
presenteer(mijn_dict, totaal)
