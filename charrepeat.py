#find first repeating character in string. else return '/0'
def repchar(str1):
    visited={}
    for ch in str1:
        if visited.get(ch):
            return ch
        else:
            visited[ch]=True
    return '\0'        
   
str1=input("Enter string:")
print(repchar(str1))
