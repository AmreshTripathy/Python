def alternatingCharacters(s):
    s = list(s)
    deletion = 0
    
    for i in range(len(s)):
        if ((i+1) < len(s)):
            if (s[i] == "A"):
                if(s[i+1] == "A"):
                    
                    deletion += 1
                    
                
            
            elif(s[i] == "B"):
                if(s[i+1] == "B"):
                   
                    deletion += 1
                    
                
    return deletion

  
    
if __name__ == '__main__':
    

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print (result)