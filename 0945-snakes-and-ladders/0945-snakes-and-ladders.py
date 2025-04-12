class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def numPos(square):
            square -=1 # because the squares start from 1
            r = square//length
            c  = square % length
            if r % 2 !=0:
                c = length -1 - c
           
            return [r,c]
        
        q = deque()
        q.append((1, 0)) #[square, moves]
        visit = set()
        while q:
            
            square, moves = q.popleft()

            for i in range(1,7):
                nextsquare = square+i
                r,c = numPos(nextsquare)
                if board[r][c] != -1:
                    nextsquare = board[r][c]
                if nextsquare == length * length:
                    return moves+1
                if nextsquare not in visit:
                    visit.add(nextsquare)
                    q.append([nextsquare, moves+1])
        return -1
