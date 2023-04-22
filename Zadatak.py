from psycopg2 import *
import psycopg2 as pg
import openpyxl as op
import pandas as pd

class Maratonac:
    def __init__(self,redni_broj,ime_prezime,godiste,zemlja,kategorija):
        self.redni_broj=redni_broj
        self.ime_prezime=ime_prezime
        self.godiste=godiste
        self.zemlja=zemlja
        self.kategorija=kategorija
    def __str__ (self):
        return('{} {} {}'.format(self.redni_broj,self.ime_prezime,self.zemlja))

class Ucitaj_maratonac:
    def __init__(self):
        self.maraton=[]
        self.l_m=pd.Series()

    def puni_bazu(self):
        try:
            con=pg.connect (
                database='maraton', 
                user='postgres', 
                password='itoip', 
                host='localhost', 
                port='5432' ) 
            cursor_obj=con.cursor() 
            cursor_obj.execute('SELECT * FROM MARATONCI')
            result=cursor_obj.fetchall()
            #r=pd.Series(result)
            r=result
            for i in r:
                m=Ucitaj_maratonac(i[0],i[1],i[2],i[3],i[4])
                self.l_m[len(self.l_m)]=m
        except(Exception,pg.Error) as e:
            return "Error",e
        finally:
            cursor.close()
            con.close()
        
        for x in result:
            redni_broj=x[0]
            ime_prezime=x[1]
            godiste=x[2]
            zemlja=x[3]
            kategorija=x[4]
            ln=Maratonac(redni_broj,ime_prezime,godiste,zemlja,kategorija)
            self.maraton.append(ln)

        def search_listbox(self,imeprezime):
            l=[]
            for i in self.l_m:
                if i.ime_prezime
            
            pass
        def export_maratonac(self,maratonac):
            pass
        def export_sve_excel(self):
            pass
        def export_ime_zemalja(self):
            pass





A=Ucitaj_maratonac()
A.puni_bazu()
for x in A.maraton:
    print(x)

M=Ucitaj_maratonac()
for i in M.l_m:
    print(i)
