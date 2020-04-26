from geoalchemy2 import Geometry
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class Airline(Base):
    id = Column(Integer, index=True, primary_key=True)
    airline_id = Column(Integer, index=True, unique=True)
    name = Column(String, index=True)
    alias = Column(String, index=True)
    iata = Column(String(2), index=True)
    icao = Column(String(3), index=True)
    callsign = Column(String)
    active = Column(Boolean, index=True)

    country_id = Column(Integer, ForeignKey("country.id"))
    country = relationship("Country", back_populates="airlines")

    route = relationship("Route", back_populates="airline")


class Airport(Base):
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    iata = Column(String(3), index=True)
    icao = Column(String(4), index=True)
    location = Column(Geometry("POINT"))
    altitude = Column(Integer)
    tz = Column(Integer)
    dst = Column(String(1))
    tz_db = Column(String)
    type = Column(String)
    source = Column(String)

    country_id = Column(Integer, ForeignKey("country.id"))
    country = relationship("Country", back_populates="airport")

    source_route = relationship("Route", back_populates="source_airport")
    destination_route = relationship("Route", back_populates="destination_airport")


class Country(Base):
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, index=True)
    iso = Column(String(2), index=True)
    dafif = Column(String(2), index=True)

    airlines = relationship("Airline", back_populates="country")
    airports = relationship("Airport", back_populates="country")


class Plane(Base):
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, index=True)
    iata = Column(String(3), index=True)
    icao = Column(String(4), index=True)

    plane = relationship("Route", back_populates="plane")


class Route(Base):
    id = Column(Integer, index=True, primary_key=True)
    airline = Column(String)
    codeshare = Column(Boolean)
    stops = Column(Integer)

    airline_id = Column(Integer, ForeignKey("airline.id"))
    airline = relationship("Airline", back_populates="route")

    source_airport_id = Column(Integer, ForeignKey("airport.id"))
    source_airport = relationship("Airport", back_populates="source_airport")

    destination_airport_id = Column(Integer, ForeignKey("airport.id"))
    destination_airport = relationship("Airport", back_populates="destination_airport")

    plane_id = Column(Integer, ForeignKey("plane.id"))
    plane = relationship("Plane", back_populates="route")
