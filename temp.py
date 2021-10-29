import numpy as np
def randomSM (n, file_name):    
      
    Men_pref_list = []    
    Women_pref_list = []    
    for i in range(n): 
	print(i)       
        Ordered_list = [i+1 for i in range(n)]       
        np.random.shuffle(Ordered_list)       
        Men_pref_list.append(Ordered_list)     
        Ordered_list = [i+1 for i in range(n)]       
        np.random.shuffle(Ordered_list)       
        Women_pref_list.append(Ordered_list)      
        with open(file_name, "w") as f:      
            f.write(str(n)+'\n')      
            for Lst in Men_pref_list:          
                new_line = ""        
                for elem in Lst:              
                    new_line += str(elem)+' '      
                    f.write(new_line[:-1]+'\n')        
                    f.write(' \n')      
                    for Lst in Women_pref_list:    
                        new_line = ""         
                        for elem in Lst:        
                            new_line += str(elem)+' '  
                            f.write(new_line[:-1]+'\n')
                            
                            

randomSM(1000,"P1.txt")        

