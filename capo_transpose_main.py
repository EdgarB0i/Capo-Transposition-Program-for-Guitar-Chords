#capo transpose program
num=int(input("Enter how many chords do you want to transpose: "))
lst=[]
lst_out=[]
for i in range(num):
    lst.append(input("Enter name of the chord: "))
capo=int(input("Enter the fret number capo is on: "))
for x in lst:
    st=x
    stUp=st[0].upper()
    if st[1]=="#" or st[1]=="b":
        stUp=st[0].upper()+st[1]
    #---------------------------------for A--------------------------------------
    if stUp=="A":
        if capo==0:
            stUp="A"
        elif capo==1:
            stUp="A#"
        elif capo==2:
            stUp="B"
        elif capo==3:
            stUp="C"
        elif capo==4:
            stUp="C#"
        elif capo==5:
            stUp="D"
        elif capo==6:
            stUp="D#"
        elif capo==7:
            stUp="E"
        elif capo==8:
            stUp="F"
#--------------------------------for B--------------------------------------
    elif stUp=="B":
        if capo==0:
            stUp="B"
        elif capo==1:
            stUp="C"
        elif capo==2:
            stUp="C#"
        elif capo==3:
            stUp="D"
        elif capo==4:
            stUp="D#"
        elif capo==5:
            stUp="E"
        elif capo==6:
            stUp="F"
        elif capo==7:
            stUp="F#"
        elif capo==8:
            stUp="G"  
#----------------------------------for C-----------------------------------       
    elif stUp=="C":
        if capo==0:
            stUp="C"
        elif capo==1:
            stUp="C#"
        elif capo==2:
            stUp="D"
        elif capo==3:
            stUp="D#"
        elif capo==4:
            stUp="E"
        elif capo==5:
            stUp="F"
        elif capo==6:
            stUp="F#"
        elif capo==7:
            stUp="G"
        elif capo==8:
            stUp="G#" 

#----------------------------------for D-----------------------------------       
    elif stUp=="D":
        if capo==0:
            stUp="D"
        elif capo==1:
            stUp="D#"
        elif capo==2:
            stUp="E"
        elif capo==3:
            stUp="F"
        elif capo==4:
            stUp="F#"
        elif capo==5:
            stUp="G"
        elif capo==6:
            stUp="G#"
        elif capo==7:
            stUp="A"
        elif capo==8:
            stUp="A#" 
        
#----------------------------------for E-----------------------------------       
    elif stUp=="E":
        if capo==0:
            stUp="E"
        elif capo==1:
            stUp="F"
        elif capo==2:
            stUp="F#"
        elif capo==3:
            stUp="G"
        elif capo==4:
            stUp="G#"
        elif capo==5:
            stUp="A"
        elif capo==6:
            stUp="A#"
        elif capo==7:
            stUp="B"
        elif capo==8:
            stUp="C" 
        
#----------------------------------for F-----------------------------------       
    elif stUp=="F":
        if capo==0:
            stUp="F"
        elif capo==1:
            stUp="F#"
        elif capo==2:
            stUp="G"
        elif capo==3:
            stUp="G#"
        elif capo==4:
            stUp="A"
        elif capo==5:
            stUp="A#"
        elif capo==6:
            stUp="B"
        elif capo==7:
            stUp="C"
        elif capo==8:
            stUp="C#" 

#----------------------------------for G-----------------------------------       
    elif stUp=="G":
        if capo==0:
            stUp="G"
        elif capo==1:
            stUp="G#"
        elif capo==2:
            stUp="A"
        elif capo==3:
            stUp="A#"
        elif capo==4:
            stUp="B"
        elif capo==5:
            stUp="C"
        elif capo==6:
            stUp="C#"
        elif capo==7:
            stUp="D"
        elif capo==8:
            stUp="D#" 

#----------------------------------for A#-----------------------------------       
    elif stUp=="A#" or stUp=="Bb":
        if capo==0:
            stUp="A#"
        elif capo==1:
            stUp="B"
        elif capo==2:
            stUp="C"
        elif capo==3:
            stUp="C#"
        elif capo==4:
            stUp="D"
        elif capo==5:
            stUp="D#"
        elif capo==6:
            stUp="E"
        elif capo==7:
            stUp="F"
        elif capo==8:
            stUp="F#" 
        
#----------------------------------for C#-----------------------------------       
    elif stUp=="C#" or stUp=="Db":
        if capo==0:
            stUp="C#"
        elif capo==1:
            stUp="D"
        elif capo==2:
            stUp="D#"
        elif capo==3:
            stUp="E"
        elif capo==4:
            stUp="F"
        elif capo==5:
            stUp="F#"
        elif capo==6:
            stUp="G"
        elif capo==7:
            stUp="G#"
        elif capo==8:
            stUp="A"   

#----------------------------------for D#-----------------------------------       
    elif stUp=="D#" or stUp=="Eb":
        if capo==0:
            stUp="D#"
        elif capo==1:
            stUp="E"
        elif capo==2:
            stUp="F"
        elif capo==3:
            stUp="F#"
        elif capo==4:
            stUp="G"
        elif capo==5:
            stUp="G#"
        elif capo==6:
            stUp="A"
        elif capo==7:
            stUp="A#"
        elif capo==8:
            stUp="B" 

#----------------------------------for F#-----------------------------------       
    elif stUp=="F#" or stUp=="Gb":
        if capo==0:
            stUp="F#"
        elif capo==1:
            stUp="G"
        elif capo==2:
            stUp="G#"
        elif capo==3:
            stUp="A"
        elif capo==4:
            stUp="A#"
        elif capo==5:
            stUp="B"
        elif capo==6:
            stUp="C"
        elif capo==7:
            stUp="C#"
        elif capo==8:
            stUp="D" 
        
#----------------------------------for G#-----------------------------------       
    elif stUp=="G#" or stUp=="Ab":
        if capo==0:
            stUp="G#"
        elif capo==1:
            stUp="A"
        elif capo==2:
            stUp="A#"
        elif capo==3:
            stUp="B"
        elif capo==4:
            stUp="C"
        elif capo==5:
            stUp="C#"
        elif capo==6:
            stUp="D"
        elif capo==7:
            stUp="D#"
        elif capo==8:
            stUp="E" 


    if st[1]=="#" or st[1]=="b":
        transposed=stUp+st[2:]
        lst_out.append(transposed)
    else:
        transposed=stUp+st[1:]
        lst_out.append(transposed)

print("Transposed chords are: ",*lst_out,sep=" ")
    
    
    


