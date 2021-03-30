name = "Manu"
position = 2
score = 99.79

print("Hello " + name + ". You have got " + str(score) + " score and your position is " + str(position) + ".")

print("Hello",name,". You have got ",str(score),"score and your position is",str(position),".")

print("Hello",name,". You have got ",score,"score and your position is",position,".") # while using "," for concatenation, we don't have to use "str"

print("Hello",name,". You have got "+str(score),"score and your position is",position,".") # a mix of "+" and "," can be used for concatenation

print("Hello",name,". You have got ",str(score)+" score and your position is",position,".")

print(f"Hello {name}. You have got {score} score and your position is {position}.")