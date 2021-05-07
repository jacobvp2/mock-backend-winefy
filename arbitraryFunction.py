def definePersonality(username):
    personalityList = ['INFP', 'INTJ', 'INFJ', 'INTP',
                        'ENFP', 'ENTJ', 'ENFJ', 'ENTP',
                        'ISFJ', 'ISFP', 'ISTJ', 'ISTP',
                        'ESFJ', 'ESFP', 'ESTJ', 'ESTP' ]
    index = len(username) % len(personalityList)
    return personalityList[index]
