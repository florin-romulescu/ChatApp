
# ChatApp

Proiect realizat de:  
 * [Enescu Horia](https://github.com/HoriaTG)
 * [Romulescu Florin](https://github.com/florin-romulescu)

Acest proiect consta in realizarea unei aplicatii web care permite comunicarea la distanta intre 2 sau mai multi useri pe un chat global.

### Configurare dispozitiv

Pentru a rula proiectul pe dispozitivul tau ca server trebuie ca pc-ul sa contina python 3.10 cu flask instalat. Urmatoarele comenzi functioneaza pe sisteme linux sau terminal de linux in Windows (WSL).

1. Verificare versiune python:
```bash
python3 --version
```
Output:
```bash
Python 3.10.6
```

2. Instalare pip (package manager pentru python):
```bash
sudo apt install python3-pip
```

3. Instalare flask:
```bash
pip3 install flask
```

### Rulare aplicatie:

```
flask --app main run
```

### Structura directoare

Aici este explicata cum arata structura de directoare si ce se intampla in fiecare fisier:

- `README.md`: documentatia proiectului
- `.gitignore`: contine fisierele care vor fi ignorate de commit
- `app.py`: fisierul principal de la care porneste executia serverului
- `views.py`: contine functiile pentru fiecare pagina
- `img/`: in acest director vor fi puse toate imaginile folosite
- `js/`: in acest director vor fi puse toate scripturile de JavaScript
- `style/`: in acest director vor fi puse toate fisierele .css
- `templates/`: in acest director vor fi puse toate fisierele .html

<div style='color:red'><b>In cazul in care directoarele nu apar in repo inseamna ca momentan nu sunt fisiere in ele!</b></div>