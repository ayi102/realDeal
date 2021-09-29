from Report.Report import Report

class TestReport():

    def setup(self):
        self.report = Report("Test")

    def test_addLine_when_a_line_is_added_then_contents_will_get_the_new_line(self):
        expectedContents = ["Test Line 1",
                            "Test Line 2",
                            "Test Line 3"]

        for line in expectedContents:
            self.report.addLine(line)

        self.report.print()
        assert self.report.contents == expectedContents