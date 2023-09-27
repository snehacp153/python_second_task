word_count ="sat cat hat hat cat hat"
counts =dict()
words = word_count.split()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(dict(sorted(counts.items(),reverse=True)))
