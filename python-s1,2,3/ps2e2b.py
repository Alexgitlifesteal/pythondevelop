lista = ['Hydrogen' , 'Helium' , 'Lithium', 'Beryllium' , 'Boron' , 'Carbon' , 'Nitrogen' , 'Oxygen' , 'Flourine', 'Neon']
listb = ['Sodium' , 'Magnesium', 'Aluminium' , 'Silicon' , 'Phosphorus' , 'Sulpher' , 'Chlorine' , 'Argon' , 'Potassium' , 'Calcium']
c = lista+listb
c.append('Scandium')
c.append('Titanium') 
c.append('Vanadium') 
c.append('Chromium') 
c.append('Manganese') 
c.append('Iron') 
c.append('Cobalt') 
c.append('Nickel') 
c.append('Copper') 
c.append('Zinc')
#print elements in new list startign with S using compressions method
d = [word for word in c if word.startswith('S')]
print d
 
#print elements with 4 letters using compressions method
e = [word for word in c if len(word) == 4]
print e