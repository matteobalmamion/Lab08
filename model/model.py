import datetime

from database.DAO import DAO


class Model:
    def __init__(self):
        self._solBest = []
        self._listNerc = None
        self._listEvents = None
        self.sommaBestPop=0
        self.sommaBestH=0
        self.dataMax=datetime.datetime.now()
        self.dataMin=datetime.datetime(1900,1,1)
        self.loadNerc()



    def worstCase(self, nerc, maxY, maxH):
        self._listEvents= DAO.getAllEvents(nerc)
        parziale=[]
        pos=0
        self.ricorsione(parziale, maxY, maxH, pos)
        print(self._solBest)
        return self._solBest

    def ricorsione(self, parziale, maxY, maxH, pos):
        sommaPop=self.sommaPeople(parziale)
        sommaH=self.sommaOrari(parziale)
        if sommaH==maxH or pos==len(self._listEvents):
            if self.sommaBestPop<sommaPop:
                self.sommaBestPop=sommaPop
                self.sommaBestH=sommaH
                self._solBest = parziale.copy()
            return
        else:
            for element in self._listEvents[pos:]:
                if not (element.date_event_began.year < (self.dataMax.year - maxY) and element.date_event_began.year>(self.dataMin.year+maxY)):
                        pos+=1
                        continue
                if (((element.date_event_finished-element.date_event_began).total_seconds())/3600)>(maxH-sommaH):
                    pos+=1
                    continue
                parziale.append(element)
                if self.sommaOrari(parziale)>maxH:
                    if len(parziale)==1:
                        parziale.remove(element)
                        continue
                    parziale.remove(element)
                    return
                pos=pos+1
                self.ricorsione(parziale, maxY, maxH, pos)
                parziale.remove(element)

    def sommaPeople(self,events):
        somma=0
        for event in events:
            somma+=event.customers_affected
        return somma
    def sommaOrari(self, events):
        somma=0
        for event in events:
            somma+=((event.date_event_finished-event.date_event_began).total_seconds())/3600
        return somma

    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc