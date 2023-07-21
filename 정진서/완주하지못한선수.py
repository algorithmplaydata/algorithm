# def solution(participant, completion):

#     count_dict = {}
    
#     for name in completion:
#         count_dict[name] = count_dict.get(name, 0) + 1 # 있으면 + 1 없으면 0
    
#     for name in participant:
#         count_dict[name] = count_dict.get(name, 0) - 1
        
#         if count_dict[name] == 0:
#             del count_dict[name]

#     answer = ", ".join(count_dict.keys())
#     return answer

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# solution(participant, completion)


from collections import Counter
# Counter 는 키의 개수를 값으로 저장 (딕셔너리형태)
def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)

    answer_counter = participant_counter - completion_counter

    answer = ", ".join(answer_counter.keys())
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

solution(participant, completion)
