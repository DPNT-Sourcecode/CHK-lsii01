from solutions.CHK import checkout_solution

class TestChk():
    def test_checkout(self):
        assert checkout_solution.checkout("D") == 15