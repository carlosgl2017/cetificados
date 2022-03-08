from docxtpl import DocxTemplate
from datetime import date,datetime
today = date.today()
now = datetime.now() #hora
doc = DocxTemplate("plantilla.docx")
context = { 'monto_solicitado' : "10" }
context = { 'tasa' : "100" }
d1 = today.strftime("%d/%m/%Y")
context = { 'fecha' : d1 }
dt_string = now.strftime("%H:%M:%S")
context = { 'hora' : dt_string }
doc.render(context)
doc.save("acta_generado.docx")