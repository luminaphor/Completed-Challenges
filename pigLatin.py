sentence=input(' ')
print('Original:',sentence)

sentence=sentence.split(' ')
translated=''

for word in sentence:
    translated+=(word[1:]+word[0])+'ay '

print('Translated:',translated)
