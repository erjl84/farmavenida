from flask import Flask
from flask import render_template, request, redirect, url_for
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    _consulta = request.form['txtConsulta'].upper()
    if request.method == 'POST' and _consulta != "":        
        archivo = open('VISUAL.TXT', 'r')
        listaProductos = archivo.readlines()[1:]        
        nLista = []
        margenU = 0
        pattern = re.compile(_consulta)
        str_match = [x for x in listaProductos if re.search(pattern, x)]
        for linea in str_match:
            #nomProductos.append(linea[0:32])
            #existenciaProd.append(int(linea[32:37].strip()))
            precioPublico = float(linea[37:47].strip())
            precioFarmacia = float(linea[47:57].strip())
            margenU = 100 - (precioFarmacia / precioPublico * 100)            
            #labProducto.append(linea[66:75])
            #codBarras.append(linea[75:88])
            #codProv.append(linea[89:95])
            nLista+= [f"{linea[0:32]}{linea[32:37]}{linea[37:47]}{linea[47:57]}{linea[66:75]}{linea[75:88]}{linea[89:95]}{str(margenU)}"]
        nLista.sort()            
    return render_template('resultado.html', datos = nLista)

if __name__ == '__main__':
    app.run(debug=True)

