import string, random
import operator
goal = 'abcdefghijklmnopqrstuvwxyzaaaaaaaaadsafasdfasdaaaa'


class indiv:
	def __init__(self,str,score):
		self.str = str
		self.score = 0

class group:
	def __init__(self, mutation, generation):
		self.mutation = 20
		self.generation = 0
		self.list = []
		self.finish = 0
	def fitness(self):
		for indivdual in self.list:
			i = 0
			score_ = 0
			indivdual.score = 0
			for letter in indivdual.str:
				if (letter == goal[i]):
					score_+=1
				i+=1
			indivdual.score = pow(2,int(score_))
			#print('score', score_, 'str = ',indivdual.str)


	def overcross(self):
		self.fitness()
		self.list = sorted(self.list, key=lambda indiv: indiv.score, reverse = True)
		print(self.list[0].str)
		newlist = []
		for i in range(8000):
			index1 = random.randrange(1, 100)
			index2 = random.randrange(1, 100)
			parent1 = self.list[index1].str
			parent2 = self.list[index2].str
			newstr = ''

			for letter in range(len(goal)):
				seed = random.randrange(0, 50)
				if(seed < 23):
					newstr = newstr + parent1[letter]
				elif(seed >= 23 & seed <= 43):
					newstr = newstr + parent2[letter]
				else:
					newstr = newstr + randomString(1) #getting random letter

			if(newstr == goal):
				self.finish = 1
				print(newstr)
				break
			newlist.append(indiv(newstr,0))

		for i in range(2000):
			newlist.append(self.list[i])

		self.fitness()
		self.list = newlist
		self.generation+=1


def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

creature = group(0,0)

for i in range(10000):
	new_str = randomString(len(goal))
	creature.list.append(indiv(new_str,0))

while creature.finish == 0:
	creature.overcross()

print(creature.generation,'generations')

			


	

		

