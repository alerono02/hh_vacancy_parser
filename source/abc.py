from abc import ABC, abstractmethod


class Employer(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_employers(self):
        pass

    @abstractmethod
    def get_vacancies(self, url_vac):
        pass
