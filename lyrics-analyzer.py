text = """ They didn’t think they could bear it if anyone found out about the Potters. Mrs. Potter was Mrs. Dursley’s sister, but they hadn’t met for several years; in fact, Mrs. Dursley pretended she didn’t have a
sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be.  e Dursleys shuddered to think what the neighbors would say if the Potters arrived in the street.  e Dursleys knew that the Potters had a small son, too, but they had never even seen him.  is boy was another good reason
for keeping the Potters away; they didn’t want Dudley mixing with a child like that. When Mr. and Mrs. Dursley woke up on the dull, gray Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr. Dursley hummed as he picked out his most boring tie for work, and Mrs. Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair. None of them noticed a large, tawny owl fl utter past the window.
"""
#print(len(text.split()))

word_count = {}

for word in text.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1
print(word_count)    