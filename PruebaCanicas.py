import unittest
import ProblemaCanicas
class Prueba_Canicas(unittest.TestCase):
    def test_Cani_real1(self):
        mat=[[0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,1,0,0,0,1],
             [0,0,0,1,0,0],
             [0,0,1,0,0,0],
             [1,0,0,0,1,0]]
        vec=[[6],[2],[1],[5],[3],[10]]
        toques=2
        res=[[0],[0],[1],[5],[9],[12]]
        resultado=ProblemaCanicas.canicas_real(mat,vec,toques)
        self.assertEqual(res,resultado)
    def test_Cani_real2(self):
        mat=[[0,0,0,0,0,0,0,0],
            [1/2,0,0,0,0,0,0,0],
            [1/2,0,0,0,0,0,0,0],
            [0,1/3,0,1,0,0,0,0],
            [0,1/3,0,0,1,0,0,0],
            [0,1/3,1/3,0,0,1,0,0],
            [0,0,1/3,0,0,0,1,0],
            [0,0,1/3,0,0,0,0,1]]
        vec=[[1],[0],[0],[1],[0],[0],[2],[0]]
        toques=3
        res=[[0.0], [0.0], [0.0], [1.1666666666666667], [0.16666666666666666], [0.3333333333333333], [2.1666666666666665], [0.16666666666666666]]
        resultado=ProblemaCanicas.canicas_real(mat,vec,toques)
        self.assertEqual(res,resultado)
    def test_Cani_imag(self):
        mat1=[[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
             [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
             [(0,0), (1,0), (0,0), (0,0), (0,0), (1,0)],
             [(0,0), (0,0), (0,0), (1,0), (0,0), (0,0)],
             [(0,0), (0,0), (1,0), (0,0), (0,0), (0,0)],
             [(1,0), (0,0), (0,0), (0,0), (1,0), (0,0)]]
        mat2=[[(9,4)],[(3,5)],[(2,1)],[(1,1)],[(6,7)],[(8,2)]]
        toques=4
        res=[[(0, 0)], [(0, 0)], [(15, 11)], [(1, 1)], [(11, 7)], [(2, 1)]]
        resultado=ProblemaCanicas.canicas_imaginario(mat1,mat2,toques)
        self.assertEqual(res,resultado)


if __name__=='__main__':
    unittest.main()
