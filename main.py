import datrie
import string

# setup
trie = datrie.Trie(string.ascii_uppercase)
with open('dictionary.txt', 'r') as fin:
    eng_words = [x.strip() for x in list(fin)]

for i, x in enumerate(eng_words):
    trie[x] = i

# inp: a grid of cells
def solve(grid):
    result = set()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            result.update(find_words(grid, [(r, c)], []))
    return sorted([x for x in list(result) if len(x) > 2])

def get_neighbors(grid, r, c):
    directions_r = [0]
    directions_c = [0]
    if r > 0:
        directions_r.append(-1)
    if r < len(grid) - 1:
        directions_r.append(1)
    if c > 0:
        directions_c.append(-1)
    if c < len(grid[0]) - 1:
        directions_c.append(1)
    neighbors = []
    for r_diff in directions_r:
        for c_diff in directions_c:
            if not (r_diff == 0 and c_diff == 0):
                neighbors.append((r + r_diff, c + c_diff))
    return neighbors

def generate_word(grid, path):
    return ''.join([grid[r][c] for (r, c) in path])

def is_word(word):
    return word in trie

def has_words(prefix):
    suffixes = trie.suffixes(prefix)
    return len(suffixes) > 0 or suffixes == ['']

def find_words(grid, path, words_gathered):
    prefix = generate_word(grid, path)
    r, c = path[-1]
    if is_word(prefix):
        words_gathered.append(prefix)
    if not has_words(prefix):
        return words_gathered
    neighbors = get_neighbors(grid, r, c)
    for neighbor in neighbors:
        if neighbor not in path:
            words_gathered = find_words(grid, path + [neighbor], words_gathered)
    return words_gathered
