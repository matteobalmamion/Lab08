import flet as ft

from model.nerc import Nerc


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()

    def handleWorstCase(self, e):
        lista=self._model.worstCase(self._idMap[self._view._ddNerc.value],int(self._view._txtYears.value), int(self._view._txtHours.value))
        self._view._txtOut.controls.clear()

        self._view._txtOut.controls.append(ft.Text(f"Total people affected: {self._model.sommaBestPop}"))
        self._view._txtOut.controls.append(ft.Text(f"Total people affected: {self._model.sommaBestH}"))

        for v in lista:
            self._view._txtOut.controls.append(ft.Text(f"{v}"))
        self._view.update_page()

    def fillDD(self):
        nercList = self._model.listNerc
        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v
