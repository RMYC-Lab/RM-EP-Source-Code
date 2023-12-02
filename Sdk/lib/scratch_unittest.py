class TestResult:

    def __init__(self):
        self.test_finished = False
        self.test_result = False
        self.test_exit = False

    def set_test_finished(self):
        self.test_finished = True

    def get_test_finished(self):
        return self.test_finished

    def set_test_result(self, result):
        self.test_result = result

    def get_test_result(self):
        return self.test_result

    def set_test_exit(self):
        self.test_exit = True

    def get_test_exit(self):
        return self.test_exit