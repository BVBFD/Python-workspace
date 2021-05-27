import pickle

profile_file = open("profile_file.f", "wb")
profile = {"이름": "이성은", "나이": 20, "취미": ["축구", "배구", "피구"]}
pickle.dump(profile, profile_file)

profile_file = open("profile_file.f", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
