class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        box9x9 = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                digit = board[r][c]
                
                if digit == ".":
                    continue
                
                if digit in ROWS[r] or \
                digit in COLS[c] or \
                digit in box9x9[(r//3, c//3)]:
                    return False
                
                ROWS[r].add(digit)
                COLS[c].add(digit)
                box9x9[(r // 3, c // 3)].add(digit)
        return True