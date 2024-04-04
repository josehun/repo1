from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def get_ar(self):
        pass

class EgyagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar

class KetagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar * 1.5