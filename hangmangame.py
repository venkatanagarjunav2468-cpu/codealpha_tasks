import random
words=["ram","nagarjuna","king","code","apple","banana"]

while True:
	word=random.choice(words)
	gussed=[]
	attempts=6
	while attempts>0:
		display=""
		for letter in word:
			if letter in gussed:
				display+=letter+""
			else:
				display+=" _ "
		print("\n word:",display)
		
		if " _ " not in display:
			print("YOU WIN THE MAT CH ")
			break
		guess=input("Enter a single letter:")
		if guess in word:
			gussed.append(guess)
			print(" Correct")
		else:
			attempts-=1
			print(f"Wrong letter,remains you have only {attempts} chencess")
	if attempts==0:
		print("Game Over! Good byee")
	agine=input("play agine say (yes/no) ?").lower()
	if agine!="yes":
		print("thanks for plying ,you exit the game")
		break