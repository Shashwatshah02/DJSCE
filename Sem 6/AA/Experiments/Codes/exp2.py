import random
candidates = [0,1,2,3,4,5,6,7,8,9]
interview = []
hire = []

for i in range(0,len(candidates)):
    x = random.choice(candidates)
    interview.append(x)
    candidates.remove(x)
print(interview)

for i,num in enumerate(interview, 1):
    largest_num = max(interview[:i])
    print("Hired Candidate: ", largest_num, " in interview ", i)
    hire.append(largest_num)

print(set(hire))
print("Candidates fired are : ", len(set(hire))-1)