
import re
from itertools import chain

n, m = map(int, input().split())

matrix = [input() for _ in range(n)]

print(re.subn(r'(\w)[^\w]+(\w)',r'\1 \2', ''.join(chain.from_iterable([*zip(*matrix)])))[0])