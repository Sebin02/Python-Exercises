#prog to reverse each word of a string with case
sentence="Python is Awesome"
words=sentence.lower().split(' ')
reversed_sentence=' '.join(word[::-1].capitalize() for word in words)
print(reversed_sentence)