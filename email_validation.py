#email validation using string fruvtion 


#g@g.in -->> minimum 6 character 
#1st letter is alphabet(Index number 0 is always alphabet)
# Only one @ have to be present in the input email
# if "." present in the string from 3rd of 4th index from last or not , if present then pass , check using xor operator 
#check any space available or not in string using for loop
#check any capital letter available or not 
#check special char

email = input("Enter your email-Id which you want to check: ")
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ("_", ".", "@"):
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong email 5")
                else:
                    print("Valid email")
            else:
                print("Wrong input 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong e-mail 2")
else:
    print("Wrong e-mail 1")
