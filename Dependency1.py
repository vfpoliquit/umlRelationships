class Printer:

    def print_page(self, text: str):
        print(f"Printing: {text}")


class ReportGenerator:

    def __init__(self, content: str):
        self.content = content

    # ReportGenerator depends on Printer strictly during this call execution
    def output_report(self, printer_device: Printer):
        printer_device.print_page(self.content)


# Usage
my_printer = Printer()
quarter_report = ReportGenerator("Q1 Academic Performance: Excellent!")
quarter_report.output_report(my_printer)