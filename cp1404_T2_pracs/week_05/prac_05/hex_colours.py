HEX_COLORS = {"AliceBlue": "#fof8ff", "AcidGreen": "#b0bf1a", "Amaranth": "#e52b50", "Apricot": "	#fbceb1",
              "Beaver": "#9f8170", "Bitter Lime": "#bfff00", "Brilliant Rose": "#ff55a3"}
colour_name = input('Enter a colour: ')
while colour_name != "":
    print(f'The colour code for {colour_name} is {HEX_COLORS.get(colour_name)}')
    colour_name = input('Enter a colour: ')
