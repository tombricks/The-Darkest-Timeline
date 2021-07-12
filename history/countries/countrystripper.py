import os
listfile = ""
for filename in os.listdir("."):
	filechanged = False
	if ".txt" not in filename or "EUR - Europe.txt" in filename:
		continue
	file = open("./"+filename, "r", encoding="utf8")
	filearr = file.readlines()
	capital = ""
	for x in filearr:
		if "capital" in x:
			for y in x:
				if y in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
					capital += str(y)
			break

	newfile = """# """+filename+"""
capital = """+capital+"""
set_stability = 0.6
set_war_support = 0.6

set_politics = {
		 ruling_party = neutrality
		last_election = "2012.1.1"
		election_frequency = 48
		elections_allowed = no
}"""

	print(newfile)
	file.close()
	file = open("./"+filename, "w", encoding="utf8")
	file.write(newfile)
	file.close()
