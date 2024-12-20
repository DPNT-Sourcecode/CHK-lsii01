from solutions.CHK import checkout_solution


    
class TestChk():
    def test_checkout_solution_5A(self):
        assert checkout_solution('AAAAA') == 200
    def test_checkout_solution_3A(self):
         assert checkout_solution('AAA') == 130
    def test_checkout_solution_4A(self):
         assert checkout_solution('AAAA') == 180
    def test_checkout_solution_2B(self):
         assert checkout_solution('BB') == 45
    def test_checkout_solution_2E_0B(self):
         assert checkout_solution('EE') == 80
    def test_checkout_solution_2E_1B(self):
         assert checkout_solution('EEB') == 80
    def test_checkout_solution_2B_2E(self):
         assert checkout_solution('BBEE') == 110
    def test_checkout_solution_2E_2B(self):
         assert checkout_solution('EEBB') == 110
    def test_checkout_solution_BEBEEE(self):
            assert checkout_solution('BEBEEE') == 160
    def test_checkout_solution_ABCDECBAABCABBAAAEEAA(self):
            assert checkout_solution('ABCDECBAABCABBAAAEEAA') == 665
         

