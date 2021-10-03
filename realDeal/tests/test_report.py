from Report.Report import Report

class TestReport():

    def setup(self):
        self.report = Report("Financial Report", "test.md")

    # def test_addLine_when_a_line_is_added_then_contents_will_get_the_new_line(self):
    #     content = ['Header', 'Revenue', 'Type', 'Utility', 'Item', 'Rental Income 20.0 50.0 40.0', 'Item', 'Parking 20.0 50.0 40.0', 'Type', 'Fee', 'Item', 'Test 10.0 100.0 20.0']
    #     expectedContent = ['# Revenue', '## Utility', 'Rental Income 20.0 50.0 40.0', 'Parking 20.0 50.0 40.0', '## Fee', 'Test 10.0 100.0 20.0']

    #     self.report.addContent(content)

    #     assert self.report.contents == expectedContent

    def test_generateMd_when_invoked_then_file_is_generated_with_content(self):
        content = ['Header', 'Revenue', 'Type', 'Utility', 'Item', 'Rental Income 20.0 50.0 40.0', 'Item', 'Parking 20.0 50.0 40.0', 'Type', 'Fee', 'Item', 'Test 10.0 100.0 20.0']
        self.report.addContent(content)
        self.report.generateMd()