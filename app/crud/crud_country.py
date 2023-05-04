from peewee import Model

from app.db.connector import models


class CountryOperations:
    model: Model = models.get("geolocations_country")

    def all(self):
        return self.model.select()


Country = CountryOperations()
