from solutions.CHK import checkout_solution


    
class TestChk():
    def test_checkout_5A(self):
        assert checkout('AAAAA') == 200
    def test_checkout_3A(self):
         assert checkout('AAA') == 130
    def test_checkout_4A(self):
         assert checkout('AAAA') == 180
    def test_checkout_2B(self):
         assert checkout('BB') == 45
    def test_checkout_2E_0B(self):
         assert checkout('EE') == 80
    def test_checkout_2E_1B(self):
         assert checkout('EEB') == 80
    def test_checkout_2B_2E(self):
         assert checkout('BBEE') == 110
    def test_checkout_2E_2B(self):
         assert checkout('EEBB') == 110
    def test_checkout_BEBEEE(self):
        assert checkout('BEBEEE') == 160
    def test_checkout_ABCDECBAABCABBAAAEEAA(self):
        assert checkout('ABCDECBAABCABBAAAEEAA') == 665
    def test_checkout_2F(self):
        assert checkout('FF') == 20
    def test_checkout_3F(self):
        assert checkout('FFF') == 20
    def test_checkout_4F(self):
        assert checkout('FFFF') == 30
    def test_checkout_5F(self):
        assert checkout('FFFFF') == 40
    def test_checkout_6F(self):
        assert checkout('FFFFFF') == 40
    def test_checkout_13H(self):
        assert checkout('HHHHHHHHHHHHH') == 110
    def test_checkout_3U(self):
        assert checkout('UUU') == 120
    def test_checkout_3R_1Q(self):
        assert checkout('RRRQ') == 150
    def test_checkout_6R_2Q(self):
        assert checkout('RRRRRRQQ') == 300
    def test_checkout_3R_1Q_1R_1Q_2R(self):
        assert checkout('RRRQRQRR') == 300
    def test_checkout_3N_1M(self):
        assert checkout('NNNM') == 120
    def test_checkout_6N_2M(self):
        assert checkout('NNNNNNMM') == 240
    def test_checkout_3N_1M_1N_1M_2N(self):
        assert checkout('NNNMNMNN') == 240
    def test_checkout_3V(self):
        assert checkout('VVV') == 130   
    def test_checkout_2V(self):
        assert checkout('VV') == 90
    def test_checkout_3V_2V(self):
        assert checkout('VVVVV') == 220
    def test_checkout_3V_3V_1V(self):
        assert checkout('VVVVVVV') == 310
    def test_checkout_3S(self):
        assert checkout('SSS') == 45
    def test_checkout_4S(self):
        assert checkout('SSSS') == 65
    def test_checkout_5S(self):
        assert checkout('SSSSS') == 85
    def test_checkout_6S(self):
        assert checkout('SSSSSS') == 90
    def test_checkout_1T_1S_1Y(self):
        assert checkout('TSY') == 45
    def test_checkout_1T(self):
        assert checkout('T') == 20
    def test_checkout_1K(self):
        assert checkout('K') == 70
    def test_checkout_alphabet(self):
        assert checkout('ABCDEFGHIJKLMNOPQRSTUVW') == 795
    def test_checkout_1S_1T_1X(self):
        assert checkout('STX') == 45
    def test_checkout_1S_1T_1X_1S_1T_1X(self):
        assert checkout('STXSTX') == 90
    def test_checkout_3S_1Z(self):
        assert checkout('SSSZ') == 65
