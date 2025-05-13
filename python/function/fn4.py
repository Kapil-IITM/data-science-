# write a function to print the element of a list in a single line 

cities = ["Alwar","jaipur","Kota","delhi","lucknow","hydrabad"]
name = ["Kapil","vijay","Vinay","Prince"]

def el_list(list):
    for el in list:
        print(el,end =" ")
    
el_list(cities)
el_list(name)
