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
         


