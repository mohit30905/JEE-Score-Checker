from parsing import dict
from parsing_student import realdict
ques_id= dict
ans_id = realdict

correct_ans = []
wrong_ans = []
for key1,value1 in ques_id.items():
    for key2 , value2 in ans_id.items():
        if key1 == key2 and value1 == value2:
            correct_ans.append(value2)
            break
        elif key1 == key2 and value1!=value2:
            wrong_ans.append(value1)
            break

print('wrong ans is', wrong_ans )
print('correct_ans is', correct_ans )
score = len(correct_ans)*4 - len(wrong_ans)
print('corrct ans is',len(correct_ans),'wrong ans is',len(wrong_ans))
print(f"your score are {score} out of 300")
