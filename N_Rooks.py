
def get_rook_attack(i,j,mat):
    path = []
    for n in range(len(mat)):path.append([i,n])
    for m in range(len(mat)):path.append([m,j])
    return path

def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j],end=" ")
            print(" " , end=" ")
        print("")

mat = []
m_len = 3
for i in range(m_len):
    to_app = []
    for j in range(m_len):
        to_app.append(0)
    mat.append(to_app)


def n_rook(mat,mat_att=[],i=0,j=0,rook=0):
    if rook == len(mat):
        print_mat(mat)
        print(" ")
        return

    if i >= len(mat) or j>= len(mat):return

    for k in range(len(mat)):
        if [i,j] not in mat_att:
            mat[i][j] = 1
            att = get_rook_attack(i,j,mat)
            n_rook(mat,mat_att+att,k,j,rook+1)
        else:
            n_rook(mat, mat_att, k , j+1, rook)

n_rook(mat)