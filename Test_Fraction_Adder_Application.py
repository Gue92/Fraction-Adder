from Fraction_Adder_Application import add_frac

def test_add_frac():
    
    add_frac(35,5,5,125)
   
    assert add_frac.Zaehlerneu == 880
    assert add_frac.Nennerneu == 125
    assert add_frac.Z_short == 176
    assert add_frac.N_short == 25
    
    add_frac(2,3,-4,2)
   
    assert add_frac.Zaehlerneu == -8
    assert add_frac.Nennerneu == 6
    assert add_frac.Z_short == 4
    assert add_frac.N_short == -3



    
