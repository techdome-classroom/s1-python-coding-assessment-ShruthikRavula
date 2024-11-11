class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        arr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        first_neib = [[(r, c) for c in range(cols)] for r in range(rows)]

        def plummate(row, col):
            while first_neib[row][col] != (row, col):
                temp_row, temp_col = first_neib[row][col]
                first_neib[row][col] = first_neib[temp_row][temp_col]
                row, col = temp_row, temp_col
            return row, col
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':
                    for dr, dc in arr:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 'L':
                            r1, c1 = plummate(r, c)
                            r2, c2 = plummate(new_r, new_c)
                            mn = min((r1, c1), (r2, c2))
                            first_neib[r1][c1] = mn
                            first_neib[r2][c2] = mn
                            plummate(r, c)
                            plummate(new_r, new_c)
        
        st = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':
                    row, col = plummate(r, c)
                    st.add((row, col))
        
        return len(st)