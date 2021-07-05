# FOR LEARNING PURPOSE
# BASICS OF STRINGS

def merge(string, k):
    for i in range(0, len(string), k):
        ans = "" # empty string to store sub_string
        for x in string[i : i+k]:
            if (x not in ans): #it will not allow repeated character in substring
                ans+=x
        print(ans)

string=input("Enter the sequencse : ") # remove the comment while trying it.
k=int(input()) # Length of each Sub-string

merge(string,k) # Calling the Function