# pickle
# 파이썬에서는 객체를 바이트 단위로 저장하고, 그 바이트들을 다시 불러오는 방식으로 동작한다.

import pickle
# profile_file = open("profile_pickle", "wb") 
# # wb : 바이트 단위로 파일을 쓰기 모드로 열어주는 역할
# # 피클에서는 항상 바이너리로 정의해줘야 한다
# # 따로 인코딩을 할 필요는 없다. 
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장해주는 역할을 한다.
# profile_file.close()


profile_file = open("profile_pickle", "rb") 
profile = pickle.load(profile_file) #profile_file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()