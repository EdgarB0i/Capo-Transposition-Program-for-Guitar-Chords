from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <style>
                    body {
                        background-image: url('https://wallpapers.com/images/featured/81wwq1khlwvotnx4.jpg');
                        background-size: cover;
                    }
                    h2 {
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <form action="display_inputs" method="post">
                    <h2 style="color:blue;">Enter the names of each chord separated by space. For example: Cmaj Amin Fmaj Gmaj
                    <h2>Please enter the chords you want to transpose: <input type="text" name="input1"><br>
                    <h2>Enter the fret number capo is on: <input type="number" name="capo" min="0" max="100" step="1"><br>
                    <h2><input type="submit" value="Submit">
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
                    <h2>Your inputs were: {}<br><br>Capo is on fret number {}!?<br><h2 style=color:red;>Capo is set too high!
                </body>
            </html>
        '''.format(input1,capo)

        
        
        
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
                    <h2>Your inputs were: {}<br><h2 style=color:red;>Just play the chords an octave higher!
                </body>
            </html>
        '''.format(input1,capo)

    lst=input1.split(" ")
    lst_out=[]
    notes=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    notes_flat=['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']

    chords=['AMAJ','A#MAJ','BBMAJ','BMAJ','CMAJ','C#MAJ','DBMAJ','DMAJ','D#MAJ','EBMAJ','EMAJ','FMAJ','F#MAJ','GBMAJ','GMAJ','G#MAJ','ABMAJ',
    'AMIN','A#MIN','BBMIN','BMIN','CMIN','C#MIN','DBMIN','DMIN','D#MIN','EBMIN','EMIN','FMIN','F#MIN','GBMIN','GMIN','G#MIN','ABMIN',
    'AADD9','A#ADD9','BBADD9','BADD9','CADD9','C#ADD9','DBADD9','DADD9','D#ADD9','EBADD9','EADD9','FADD9','F#ADD9','GBADD9','GADD9','G#ADD9','ABADD9',
    'AMAJ7','A#MAJ7','BBMAJ7','BMAJ7','CMAJ7','C#MAJ7','DBMAJ7','DMAJ7','D#MAJ7','EBMAJ7','EMAJ7','FMAJ7','F#MAJ7','GBMAJ7','GMAJ7','G#MAJ7','ABMAJ7',
    'AMIN7','A#MIN7','BBMIN7','BMIN7','CMIN7','C#MIN7','DBMIN7','DMIN7','D#MIN7','EBMIN7','EMIN7','FMIN7','F#MIN7','GBMIN7','GMIN7','G#MIN7','ABMIN7',
    'AM','A#M','BBM','BM','CM','C#M','DBM','DM','D#M','EBM','EM','FM','F#M','GBM','GM','G#M','ABM',
    'A','A#','BB','B','C','C#','DB','D','D#','EB','E','F','F#','GB','G','G#','AB',
    'AADD11','A#ADD11','BBADD11','BADD11','CADD11','C#ADD11','DBADD11','DADD11','D#ADD11','EBADD11','EADD11','FADD11','F#ADD11','GBADD11','GADD11','G#ADD11','ABADD11',
    'A5','A#5','BB5','B5','C5','C#5','DB5','D5','D#5','EB5','E5','F5','F#5','GB5','G5','G#5','AB5',
    'A7','A#7','BB7','B7','C7','C#7','DB7','D7','D#7','EB7','E7','F7','F#7','GB7','G7','G#7','AB7',
    'A9','A#9','BB9','B9','C9','C#9','DB9','D9','D#9','EB9','E9','F9','F#9','GB9','G9','G#9','AB9',
    'ASUS4','A#SUS4','BBSUS4','BSUS4','CSUS4','C#SUS4','DBSUS4','DSUS4','D#SUS4','EBSUS4','ESUS4','FSUS4','F#SUS4','GBSUS4','GSUS4','G#SUS4','ABSUS4',
    'ASUS2','A#SUS2','BBSUS2','BSUS2','CSUS2','C#SUS2','DBSUS2','DSUS2','D#SUS2','EBSUS2','ESUS2','FSUS2','F#SUS2','GBSUS2','GSUS2','G#SUS2','ABSUS2',
    'ADIM','A#DIM','BBDIM','BDIM','CDIM','C#DIM','DBDIM','DDIM','D#DIM','EBDIM','EDIM','FDIM','F#DIM','GBDIM','GDIM','G#DIM','ABDIM',
    'AADD13','A#ADD13','BBADD13','BADD13','CADD13','C#ADD13','DBADD13','DADD13','D#ADD13','EBADD13','EADD13','FADD13','F#ADD13','GBADD13','GADD13','G#ADD13','ABADD13']
    for x in lst:
        if x.upper() not in chords:
            return '<h2 style=color:red;>Invalid input of chords!'
        st=x
        stUp=st[0].upper()
        if st[1]=="#" or st[1]=="b" or st[1]=="B":
            stUp=st[0].upper()+st[1]

        if stUp in notes:
            idx=(notes.index(stUp)+capo)
        elif stUp in notes_flat:
            idx=(notes_flat.index(stUp)+capo)
        if idx>11:
            idx=idx-12
        stUp=(notes[idx])

        if st[1]=="#" or st[1]=="b":
            transposed=stUp+st[2:]
            lst_out.append(transposed)
        else:
            transposed=stUp+st[1:]
            lst_out.append(transposed)
    st_out=" ".join(lst_out)
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
    '''.format(input1,capo,st_out)



if __name__ == '__main__':
    app.run()