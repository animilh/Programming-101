from histogram import Histogram
import matplotlib.pyplot as plt

h = Histogram()

f = open('servers.txt', 'r')
content = f.read().split('\n')
for line in content:
    if line in ('Apache', 'nginx', 'Microsoft-IIS','lighttpd'):
        h.add(line)



h = h.get_dict()
print(h)
keys = list(h.keys())
values = list(h.values())

X = list(range(len(keys)))

plt.bar(X, list(h.values()), align="center")
plt.xticks(X, keys)

plt.title(".bg servers")
plt.xlabel("Server")
plt.ylabel("Count")

plt.savefig("histogram.png")
