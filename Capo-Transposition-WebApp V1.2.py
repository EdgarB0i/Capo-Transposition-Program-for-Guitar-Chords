from flask import Flask, request
import re 

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <style>
                    body {{
                        background-image: url('https://wallpapers.com/images/featured/81wwq1khlwvotnx4.jpg');
                        background-size: cover;
                    }}
                    h2 {{
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <form action="display_inputs" method="post">
                    <h2 style="color:blue;">Enter the names of each chord separated by space. For example: Cmaj Amin Fmaj Gmaj</h2>
                    <h2>Please enter the chords you want to transpose: <input type="text" name="input1"><br></h2>
                    <h2>Enter the fret number capo is on: <input type="number" name="capo" min="0" max="100" step="1"><br></h2>
                    <h2><input type="submit" value="Submit"></h2>
                </form>
            </body>
        </html>
    '''

@app.route('/display_inputs', methods=['POST'])
def display_inputs():
    input1 = request.form['input1']
    capo = int(request.form['capo'])

    if capo > 12:
        return '''
            <html>
                <head>
                    <style>
                        body {{
                            background-image: url('https://www.pcclean.io/wp-content/uploads/2020/4/yu2i2m.jpg');
                            background-size: cover;
                        }}
                        h2 {{
                            text-align: center;
                        }}
                    </style>
                </head>
                <body>
                    <h2>Your inputs were: {}<br><br>Capo is on fret number {}!?<br><h2 style=color:red;>Capo is set too high!</h2></h2>
                </body>
            </html>
        '''.format(input1, capo)

    elif capo == 12:
        return '''
            <html>
                <head>
                    <style>
                        body {{
                            background-image: url('https://www.pcclean.io/wp-content/uploads/2020/4/yu2i2m.jpg');
                            background-size: cover;
                        }}
                        h2 {{
                            text-align: center;
                        }}
                    </style>
                </head>
                <body>
                    <h2>Your inputs were: {}<br><h2 style=color:red;>Just play the chords an octave higher!</h2></h2>
                </body>
            </html>
        '''.format(input1, capo)

    lst = input1.split(" ")
    lst_out = []

    all_notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'Ab', 'Bb', 'Db', 'Eb', 'Gb']
    
    for x in lst:
        chord_parts = re.match(r'([A-Ga-g#b]+)(.*)', x)
        if chord_parts:
            note = chord_parts.group(1).upper()
            rest = chord_parts.group(2)

            if note not in all_notes:
                return '<h2 style=color:red;>Invalid input of chords!</h2>'

            idx = (all_notes.index(note) + capo) % 12
            transposed = all_notes[idx]

            transposed_chord = transposed + rest
            lst_out.append(transposed_chord)
        else:
            # Handle the case where only individual notes are entered
            note = x.upper()
            if note in all_notes:
                idx = (all_notes.index(note) + capo) % 12
                transposed = all_notes[idx]

                lst_out.append(transposed)

    st_out = " ".join(lst_out)
    return '''
        <html>
            <head>
                <style>
                    body {{
                        background-image: url('https://www.teahub.io/photos/full/280-2808920_acoustic-guitar.jpg');
                        background-size: cover;
                    }}
                    .container {{
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        font-family: Arial, sans-serif;
                        font-size: 24px;
                        font-weight: bold;
                    }}
                    h2 {{
                        text-align: center;
                        font-size: 36px;
                        margin: 10px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Your inputs were:</h2>
                    <h2>{}</h2>
                    <h2>Capo is on fret number {}</h2>
                    <h2>Transposed chords are:</h2>
                    <h2>{}</h2>
                </div>
            </body>
        </html>
    '''.format(input1, capo, st_out)


if __name__ == '__main__':
    app.run()
