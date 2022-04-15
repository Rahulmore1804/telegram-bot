from datetime import datetime
from this import d
import wikipedia as wiki
wiki.set_lang("en")
def exampleinput(input1):
    a = str(input1).lower()


    if a in ('hello','hi'):
        return "hey, mate"
    
    if "search//" in a:
        
        a = a.replace('search//','')
        wiki.set_lang("en")
         
         
        return wiki.summary(a,sentences=4)
        #  wiki.set_lang("fr")
        #  print(wiki.summary("Python"))
        #  wiki.set_lang("en")
        #  x1 = wiki.page("Python")
         
        #  print(x1.content)
         

    if a in ('time','time?'):
       now = datetime.now()
 
       dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # print("date and time =", dt_string)

       return str(dt_string)
    
    return "i don't understand what you have said"