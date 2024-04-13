class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def build_trie(dictionary):
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    return root

def boggle_solver(board, dictionary):
    def is_valid_move(x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

    def dfs(x, y, node, current_word):
        char = board[x][y]

        if char in node.children:
            current_word += char
            node = node.children[char]

            if node.is_end_of_word:
                found_words.add(current_word)

            visited.add((x, y))

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue

                    new_x, new_y = x + dx, y + dy
                    if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                        dfs(new_x, new_y, node, current_word)

            visited.remove((x, y))

    root = build_trie(dictionary)
    found_words = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited = set()
            dfs(i, j, root, board[i][j])

    return list(found_words)

board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]

dictionary = ["START", "NOTE", "SAND", "STONED"]

valid_words = boggle_solver(board, dictionary)
print(valid_words)
