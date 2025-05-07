#prog to reverse each word of a string
sentence="Python is Awesome"
words=sentence.split(' ')
reversed_sentence=' '.join(word[::-1] for word in words)
print(reversed_sentence)