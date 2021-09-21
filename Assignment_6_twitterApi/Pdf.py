import fpdf as fpdf
from fpdf import FPDF



class PDF(FPDF):
    def header(self):
        self.set_font('helvetica','B',20)
        self.set_text_color(128,0,128)
        pdf_width=self.w
        title_width=self.get_string_width("HEADING")+ 10
        self.set_x((pdf_width-title_width)/2)
        self.cell(title_width,10,"HEADING",border=1,ln=1,align='C')
        self.set_text_color(220, 50, 50)
        self.ln(20)



    def maketable(self,header,value):

        self.set_font('times','',10.0)
        epw=self.w-2.5*self.l_margin
        cw=epw/5              #columnwidth
        rh=self.font_size  #rowheight
        for h in header:
            self.set_fill_color(244, 245, 173)
            self.cell(cw,2.5*rh,txt=h,border=1,align='C',fill=True)
        self.ln(2.5*rh)
        for element in value:
            for j in element:
                self.cell(cw,2.5*rh,str(j),border=1,align='C')
            self.ln(2.5*rh)

    def footer(self):
        self.set_font("helvetica","I",10)
        self.set_text_color(88,88,88)
        self.set_y(-15)
        self.cell(0,10,f'Page{self.page_no()}/{{nb}}',align='C')



"""
    def setHeader(self):
        self.set_font('helvetica', 'B', 20)
        self.cell(0, 10, 'Header', border=False, ln=1, align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.cell(0, 10, f'Page{self.page_no()}/{{nb}}', align='C')

    def output_table(self, result_data, no_of_column):
        self.add_page()
        self.alias_nb_pages()
        self.no_of_column = no_of_column
        self.result_data = result_data

        self.set_font('helvetica', size=8)
        col_width = self.epw / self.no_of_column
        line_height = self.font_size * 12

        for row in self.l:
            for item in row:
                self.multi_cell(col_width, line_height, str(item), border=1, ln=3, max_line_height=self.font_size)
            self.ln(line_height)

    def save_pdf(self, file_name):
        self.filename = file_name
        self.output(file_name)
        print('File Created Sucessfully')

    def withIndex(self, head, retrieve_data):
        self.retrieve_data = retrieve_data
        self.head = head
        self.l = []
        for i in self.retrieve_data:
            self.l.append(i)
        index = self.l.index(self.l[0])
        self.l.insert(index, head)

    '''
    def createHeader(self):
        self.set_font('times', 'B', size=15)
        self.set_text_color(0, 0, 0)
        pdf_width = self.w
        title_width = self.get_string_width("Global warming") + 10
        self.set_x((pdf_width - title_width) / 2)
        self.cell(title_width, 12, "Global warming", border=1.5, ln=2, align='C')
        self.set_text_color(0, 0, 0)
        self.ln(20)

    def renderTable(self, data,header):

        self.set_font("Times", size=10)
        line_height = self.font_size * 2.5
        col_width = self.epw / 4  # distribute content evenly
        for h in header:
            self.set_fill_color(135,206,235)
            self.multi_cell(col_width,line_height,str(h),border=1,ln=3,align='C',max_line_height=self.font_size,fill=True)
        self.ln(line_height)
        for element in data:
            for j in element:
                self.multi_cell(col_width,line_height,str(j),border=1,ln=3,align='C',max_line_height=self.font_size)
            self.ln(line_height)

    def setFooter(self):
        self.set_font = ("helvetica", 'I', 10)
        self.set_text_color(88, 88, 88)
        self.set_y(-15)
        self.cell(0, 10, f'Page{self.page_no()}/{{nb}}', align='C')
"""
