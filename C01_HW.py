import csv
import datetime
class Submission:
    def __init__(self, subid, stuid, prob, status, score, codelen, subtime):
        self.subid = subid
        self.stuid = stuid
        self.prob = prob
        self.status = status
        self.score = score
        self.codelen = codelen
        self.subtime = subtime
class problem:
    def __init__(self, accepted, compile_time, runtime_error, time_limite_exceeded, wrong_answer):
        self.accepted = accepted
        self.compile_time = compile_time
        self.runtime_error = runtime_error
        self.time_limit_exceeded = time_limite_exceeded
        self.wrong_answer = wrong_answer
midterm_path = "/Users/shawn/Desktop/GitHub/Python-in-Business/midterm2.csv"
with open(midterm_path, 'r', encoding='utf-8') as midterm:
    header = midterm.readline()
    print("HEADER:", header)
    count = 0
    body = midterm.readlines()
    submissions = []
    for line in body:
        count += 1
        subid, stuid, prob, status, score, codelen, subtime = line.split(",")
        sub = Submission(subid, stuid, prob, status, score, codelen, subtime)
        # print(f"Submission {count}: {sub.subid}, {sub.stuid}, {sub.prob}, {sub.status}, {sub.score}, {sub.codelen}, {sub.subtime}")
        submissions.append(sub)
    submissions = list(reversed(submissions))
    str = input("Enter start and end time: ")
    start, end = str.replace.split()
    problems = []

    for sub in submissions:
        if sub.subtime >= start and sub.subtime <= end:
            if sub.prob not in problems:
                problems.append(sub.prob)
            if sub.status not in 

            
