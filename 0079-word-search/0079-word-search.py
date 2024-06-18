class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, word_index):
            if word_index == len(word):
                return True
            if (x<0 or y<0 or x>len(board)-1 or y>len(board[0]) -1 or board[x][y] != word[word_index]):
                return False

            temp = board[x][y]
            board[x][y] = "#"

            found = (dfs(x-1, y, word_index+1) or 
                    dfs(x, y+1, word_index+1) or 
                    dfs(x+1, y, word_index+1) or 
                    dfs(x, y-1, word_index+1))

            board[x][y] = temp
            return found
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # Start DFS only if the first character matches
                    if dfs(i, j, 0):
                        return True
