import pandas as pd

def txttocsv(filename):
    temp = open(filename,'r').read().splitlines()
    characters = ['Claire', 'Phil', 'Haley', 'Luke', 'Alex', 'Gloria', 
              'Jay', 'Manny', 'Mitchell', 'Cameron', 'Lily']
    
    # Getting rid of the empty str
    for line in temp:
        if line == '':
            temp.remove(line)
            
    # Merging str with less than 2 words to the previous sent
    for line in enumerate(temp):
        if len(line[1].split()) < 2:
            temp[line[0]-1] = temp[line[0]-1] + ' ' + line[1]
            
    # Getting rid of the str with less than 2
    new_temp = []
    for line in temp:
        if len(line.split()) > 2:
            new_temp.append(line)
            
    # Removing irrelevant characters txt
    for line in new_temp:
        if (":" in line.split()) and (line.split()[0] not in characters):
            new_temp.remove(line)
            
    for line in enumerate(new_temp): 
        if (line[1].split()[0] not in characters):
            new_temp[line[0]-1] = new_temp[line[0]-1] + ' ' + line[1]
            new_temp.remove(line[1])
            
    Phil = []
    Claire = []
    Haley = []
    Alex = []
    Luke = []
    Gloria = []
    Manny = []
    Jay = []
    Cam = []
    Mitchell = []
    Lily = []
    
    for line in new_temp:
        if line.split()[1] == ":":
            if line.split()[0] == 'Phil':
                Phil.append(line)
            elif line.split()[0] == 'Claire':
                Claire.append(line)
            elif line.split()[0] == 'Haley':
                Haley.append(line)
            elif line.split()[0] == 'Alex':
                Alex.append(line)
            elif line.split()[0] == 'Luke':
                Luke.append(line)
            elif line.split()[0] == 'Gloria':
                Gloria.append(line)
            elif line.split()[0] == 'Manny':
                Manny.append(line)
            elif line.split()[0] == 'Jay':
                Jay.append(line)
            elif line.split()[0] == 'Cameron':
                Cam.append(line)
            elif line.split()[0] == 'Mitchell':
                Mitchell.append(line)
            elif line.split()[0] == 'Lily':
                Lily.append(line)
    
    dict = {
        'Phil': Phil,
        'Claire' : Claire,
        'Haley' : Haley,
        'Alex' : Alex,
        'Luke' : Luke,
        'Gloria' : Gloria,
        'Jay' : Jay,
        'Manny' : Manny,
        'Cam' : Cam, 
        'Mitch' : Mitchell,
        'Lily' : Lily
    }
    
    df = pd.DataFrame.from_dict(dict, orient='index')
    
    df.to_csv(filename[:4]+'CSV.csv')
    
    return "New CSV created named " + filename[:4]+'CSV.csv'