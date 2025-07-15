from flask import Flask, request, render_template
import pandas as pd
import re

app = Flask(__name__)
PATTERN = r'^[A-Za-z0-9]+-[A-Za-z0-9]+$'

def controller_tags(colonna,tipologia):
    lista = set()
    for row in colonna:
        row = str(row).replace('_', '-')
        if tipologia in row:
            riga = row.split(',')
            if len(riga)>1:
                for parola in riga:
                    parola = str(parola).replace("R410-", "")
                    if re.match(PATTERN, str(parola)):
                        lista.add(parola)
    return lista

def crea_lista(colonna):
    lista = set()
    for row in colonna:
        row = str(row).replace("R410-", "")
        row = str(row).replace('_', '-')
        if re.match(PATTERN, str(row)):
            lista.add(row)
    return lista

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file1 = request.files['file1']
    file2 = request.files['file2']

    opzione = request.form.get('opzione')
    CT1 = request.form.get('CT1')
    CT2 = request.form.get('CT2')
    ifsegnali = request.form.get('ifsegnali')
    nr_colonna1 = request.form.get('colonna1_numero_scelta1')
    nr_colonna2 = request.form.get('colonna2_numero_scelta1')
    nr_colonna3 = request.form.get('colonna_numero_scelta2')
    nr_colonna4 = request.form.get('colonna_numero_scelta3')
    tipologia1 = request.form.get('valore1_scelta1')
    tipologia2 = request.form.get('valore2_scelta1')
    tipologia3 = request.form.get('valore_scelta2')
    
    tipologia1 = str(tipologia1).replace('_', '-')
    tipologia2 = str(tipologia2).replace('_', '-')
    tipologia3 = str(tipologia3).replace('_', '-')
    descrizione_colonna = request.form.get('descrizione_scelta3')
    priorita = request.form.get('scelta')

    if 'file1' not in request.files:
        return render_template('output.html', data='Nessun file1 selezionato'), 400
    try:
        fileA = pd.read_csv(file1, sep=';', header=None)
    except pd.errors.ParserError as e:
        return render_template('output.html', data='Errore nella lettura del primo file CSV:'), e

    if file1 and file1.filename.endswith('.csv'):
#----------------------------------------------------------------------------------------------------------------------------------------
        if opzione == 'opzione1':
            if 'file2' not in request.files:
                return render_template('output.html', data='Nessun file2 selezionato'), 400
            
            if file2 and file2.filename.endswith('.csv'):
                if priorita:
                    try:
                        fileB = pd.read_csv(file2, sep=';', header=None)
                    except pd.errors.ParserError as e:
                        return render_template('output.html', data='Errore nella lettura del secondo file CSV:'), e
                    
                    colonna1 = fileA.iloc[:, int(nr_colonna1)]
                    colonna2 = fileB.iloc[:, int(nr_colonna2)]

                    if CT1=='CT1':
                        lista1 = controller_tags(set(colonna1),tipologia1)
                    else:
                        lista1 = crea_lista(set(colonna1))

                    if CT2=='CT2':
                        lista2 = controller_tags(set(colonna2),tipologia2)
                    else:
                        lista2 = crea_lista(set(colonna2))

                    if  priorita == 'scelta1':
                        out = list(lista1 - lista2) #restituisce il contenuto che è presente in 1 ma non in 2
                        out.sort()
                    elif priorita == 'scelta2':
                        out = list(lista2 - lista1)
                        out.sort()

                    if len(out)==0:
                        return render_template('output.html', data='Tutti i valori sono presenti')
                    else:
                        return render_template('output.html', data=out)
                else:
                    return render_template('output.html', data='Errore priorità non scelta')
            else:
                return render_template('output.html', data='Il file2 non è un CSV valido'), 400
#----------------------------------------------------------------------------------------------------------------------------------------
        elif opzione == 'opzione2':
            colonna = fileA.iloc[:, int(nr_colonna3)]

            if CT1=='CT1':
                lista = list(controller_tags(set(colonna),tipologia3))
            else:
                lista = list(crea_lista(set(colonna)))

            lista.sort()
            return render_template('output.html', data=lista)
#----------------------------------------------------------------------------------------------------------------------------------------                        
        elif opzione == 'opzione3':
            colonna_segnali = fileA.iloc[:, int(nr_colonna4)]
            colonna_descrizioni = fileA.iloc[:, int(descrizione_colonna)]
            appoggio1 = []
            appoggio2 = []

            for row in colonna_segnali:
                row = str(row).replace("R410-", "")
                row = str(row).replace('_', '-')
                appoggio1.append(row)
            colonna_segnali = appoggio1
            
            for row in colonna_descrizioni:
                row = str(row).replace('_', '-')
                appoggio2.append(row)
            colonna_descrizioni = appoggio2

            if ifsegnali:
                dizionario = dict(zip(colonna_segnali, colonna_descrizioni))
                dizionario = dict(sorted(dizionario.items()))
                return render_template('output.html', data=dizionario)
            else:
                return render_template('output.html', data=colonna_descrizioni)
            
        else:
            return render_template('output.html', data='Devi selezionare una funzione!')
    else:
        return render_template('output.html', data='Il file1 non è un CSV valido'), 400
    
if __name__ == '__main__':
    app.run(debug=True)