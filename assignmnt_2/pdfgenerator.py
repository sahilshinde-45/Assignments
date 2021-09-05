from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica','B',20)
        self.cell(0,10,'Header',border=False,ln=1,align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica','I',10)
        self.cell(0,10,f'Page{self.page_no()}/{{nb}}',align='C')

    def withIndex(self,head,result_data):
        self.result_data = result_data
        self.head = head
        self.l =[]
        for i in self.result_data:
            self.l.append(i)
        index = self.l.index(self.l[0])
        self.l.insert(index,head)

    def output_table(self,result_data):
        self.add_page()
        self.alias_nb_pages()
        self.result_data = result_data
        self.set_font('helvetica',size=16)
        col_width = self.w/4
        line_height = self.font_size * 2.5
        for row in result_data:
            for item in row:
                print(item)
                self.multi_cell(col_width, line_height, str(item), border=1, ln=3, max_line_height=self.font_size)
            self.ln(line_height)

    def save_pdf(self,file_name):
        self.filename = file_name
        self.output(file_name)
