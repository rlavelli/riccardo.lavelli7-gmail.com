import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from collections import Counter

stop_words = set(stopwords.words('english'))

wordstring = 'it was the best of times, it was the worst of times!! but best times'
wordstring_clean = re.sub(r'[^\w\s]','', wordstring)

text = word_tokenize(wordstring_clean)

new_sentence =[]

for w in text:
    if w not in stop_words: new_sentence.append(w)

counts = Counter(new_sentence)
counts_high = {x : counts[x] for x in counts if counts[x] >= 3}
x_labels = counts.keys()
y_values = counts.values()
counts_df = pd.DataFrame.from_dict(counts_high, orient='index', columns=['Freq'])
counts_df = counts_df.reset_index()
counts_df.columns = ['Word', 'N']

print(wordstring)
print('')
print(new_sentence)
print('')
print(counts)
print('')
print(counts_high)
print('')
print(counts_df)


# nitems = len(y_values)
# x_values = np.arange(0, nitems)    # set up a array of x-coordinates

# fig, ax = plt.subplots(1)
# ax.bar(x_values, y_values, align='center')
# ax.set_xticks(x_values);
# ax.set_xticklabels(x_labels, rotation=90);
# plt.show()

