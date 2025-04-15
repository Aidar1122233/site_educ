from weasyprint import HTML
import os
from datetime import datetime

def generate_certificate(email, course_id):
    os.makedirs('certificates', exist_ok=True)
    html = f"""
    <h1 style="text-align: center;">Удостоверение</h1>
    <p>Выдано: {email}</p>
    <p>Курс ID: {course_id}</p>
    <p>Дата: {datetime.now().strftime('%Y-%m-%d')}</p>
    """
    pdf = HTML(string=html).write_pdf()
    filename = f'certificates/cert_{email}_{course_id}.pdf'
    with open(filename, 'wb') as f:
        f.write(pdf)