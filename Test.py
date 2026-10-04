name = input("Enter your name: ")
charactername = input("Enter your character's name: ")
city = input ("Enter your city: ")
studentnumber = input("Enter your student number: ")
sentence = input("Enter your sentence: ")

print(f"""╔══════════════════════════════════════════╗
║           CHARACTER DATABASE             ║
╠══════════════════════════════════════════╣
║                                          ║
║ PLAYER                                   ║
║ Nguyễn Văn An                            ║
║                                          ║
║ DISPLAY NAME                             ║
║ {name}                                   ║
║                                          ║
║ CHARACTER                                ║
║ {charactername}                          ║
║                                          ║
║ CITY                                     ║
║ {city}                                   ║
║                                          ║
╠══════════════════════════════════════════╣
║               STATISTICS                 ║
╠══════════════════════════════════════════╣
║ Player length: {len(name)}               ║
║ Character length: {len(charactername)}   ║
║ Character first: {charactername[0]}      ║
║ Character last: {charactername[-1]}      ║
║                                          ║
║ Student year: {studentnumber[:4]}        ║
║ Student code: {studentnumber}            ║
║                                          ║
║ PLAYER TAG                               ║
║ {name}_{charactername}                   ║
║                                          ║
║ QUOTE                                    ║
║ {sentence}                               ║
║                                          ║
║ SKILL                                    ║
║ PYTHON PYTHON PYTHON                     ║
╚══════════════════════════════════════════╝""")
