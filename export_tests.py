from fpdf import FPDF
import json, re, base64, html

with open('data.json') as f:
  data = json.load(f)

name = data['data']['test']['name']
test = data['data']['sections'][0]['questions']

def parse(string):
    if "data:image/png;base64" in string:
        string = string.replace('<p><img src="data:image/png;base64,', '')
        string = string.replace('" alt="" /></p>', '')
        image = base64.b64decode(string) 
    elif "https://cdn-test-assets.classplus.co" in string:
        arr = re.findall(r'(https?://[^\s]+)', string)
        return arr[0]
    elif "https://cms-cdn.classplus.co" in string:
        arr = re.findall(r'(https?://[^\s]+)', string)
        return arr[0]
    else:
        dat = html.unescape(string)
        return dat
        
for i in range(len(test)):
    print(f"Q{i}. - {parse(test[i]['solution'])}")
    

year = 2022
test_id = 7
subject = 'C-Prog'
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Arial', 'BU', 13)
def qa():
    for i in range(len(test)):
        pdf.cell(10, 10, f'Q{i+1}:', ln=True)
        question = parse(test[i]['name'])
        solution = parse(test[i]['solution'])
        pdf.image(question[:-1], x = None, y = None, w = 175, h = 0, type = '', link = '')
        pdf.cell(0,5, ln=True)
        pdf.cell(10, 10, f'Solution:', ln=True)
        if solution.startswith("<p>"):
            pdf.cell(10, 10, solution, ln=True)
        else:
            pdf.image(solution[:-1], x = None, y = None, w = 175, h = 0, type = '', link = '')
    pdf.output(f'{year}_{test_id}_{subject}_QA.pdf')

def q():
    for i in range(len(test)):
        pdf.cell(10, 10, f'Q{i+1}:', ln=True)
        question = parse(test[i]['name'])
        solution = parse(test[i]['solution'])
        pdf.image(question[:-1], x = None, y = None, w = 175, h = 0, type = '', link = '')
        pdf.cell(0,5, ln=True)
#         pdf.cell(10, 10, f'Sol{}:', ln=True)
#         pdf.image(solution[:-1], x = None, y = None, w = 175, h = 0, type = '', link = '')
    pdf.output(f'{year}_{test_id}_{subject}_Q.pdf')

def a():
    for i in range(len(test)):
#         pdf.cell(10, 10, f'Q{i+1}:', ln=True)
        question = parse(test[i]['name'])
        solution = parse(test[i]['solution'])
#         pdf.image(question[:-1], x = None, y = None, w = 175, h = 0, type = '', link = '')
#         pdf.cell(0,5, ln=True)
        pdf.cell(10, 10, f'Sol {i+1}:', ln=True)
        pdf.image(solution[:-1], x = None, y = None, w = 175, h = 0, type = '', link = '')
    pdf.output(f'{year}_{test_id}_{subject}_A.pdf')
    
qa()
# q()
# a()
