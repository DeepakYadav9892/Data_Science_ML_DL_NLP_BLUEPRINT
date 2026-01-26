spice_mix=set()
print(f"Iniial spice mix id:{id(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("cardomom")
print(f"Intail spice mix id:{id(spice_mix)}")

##id of the object remains same as we are modifying the existing object 
print(spice_mix)