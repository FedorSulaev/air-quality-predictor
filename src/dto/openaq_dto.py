from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class Meta:
    name: str
    website: str
    page: int
    limit: int
    found: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Meta":
        return cls(
            name=data.get("name"),
            website=data.get("website"),
            page=data.get("page"),
            limit=data.get("limit"),
            found=data.get("found"),
        )

@dataclass
class Country:
    id: int
    code: str
    name: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Country":
        return cls(id=d["id"], code=d["code"], name=d["name"])

@dataclass
class Owner:
    id: int
    name: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Owner":
        return cls(id=d["id"], name=d["name"])

@dataclass
class Provider:
    id: int
    name: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Provider":
        return cls(id=d["id"], name=d["name"])

@dataclass
class Instrument:
    id: int
    name: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Instrument":
        return cls(id=d["id"], name=d["name"])

@dataclass
class Parameter:
    id: int
    name: str
    units: str
    displayName: Optional[str]

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Parameter":
        return cls(
            id=d["id"],
            name=d["name"],
            units=d["units"],
            displayName=d.get("displayName"),
        )

@dataclass
class Sensor:
    id: int
    name: str
    parameter: Parameter

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Sensor":
        return cls(
            id=d["id"],
            name=d["name"],
            parameter=Parameter.from_dict(d["parameter"])
        )

@dataclass
class Coordinates:
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Coordinates":
        return cls(latitude=d["latitude"], longitude=d["longitude"])

@dataclass
class Attribution:
    name: str
    url: Optional[str]

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Attribution":
        return cls(name=d.get("name", ""), url=d.get("url"))

@dataclass
class License:
    id: int
    name: str
    attribution: Attribution
    dateFrom: Optional[str]
    dateTo: Optional[str]

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "License":
        return cls(
            id=d["id"],
            name=d["name"],
            attribution=Attribution.from_dict(d["attribution"]),
            dateFrom=d.get("dateFrom"),
            dateTo=d.get("dateTo"),
        )

@dataclass
class DateTimePair:
    utc: str
    local: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "DateTimePair":
        return cls(utc=d["utc"], local=d["local"])

@dataclass
class LocationResult:
    id: int
    name: str
    locality: Optional[str]
    timezone: Optional[str]
    country: Country
    owner: Owner
    provider: Provider
    isMobile: bool
    isMonitor: bool
    instruments: List[Instrument]
    sensors: List[Sensor]
    coordinates: Coordinates
    licenses: List[License]
    bounds: Optional[List[float]]
    distance: Optional[float]
    datetimeFirst: Optional[DateTimePair]
    datetimeLast: Optional[DateTimePair]

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "LocationResult":
        return cls(
            id=d["id"],
            name=d["name"],
            locality=d.get("locality"),
            timezone=d.get("timezone"),
            country=Country.from_dict(d["country"]),
            owner=Owner.from_dict(d["owner"]),
            provider=Provider.from_dict(d["provider"]),
            isMobile=d.get("isMobile", False),
            isMonitor=d.get("isMonitor", False),
            instruments=[Instrument.from_dict(x) for x in d.get("instruments", [])],
            sensors=[Sensor.from_dict(x) for x in d.get("sensors", [])],
            coordinates=Coordinates.from_dict(d["coordinates"]),
            licenses=[License.from_dict(x) for x in d.get("licenses", [])],
            bounds=d.get("bounds"),
            distance=d.get("distance"),
            datetimeFirst=DateTimePair.from_dict(d["datetimeFirst"]) if d.get("datetimeFirst") else None,
            datetimeLast=DateTimePair.from_dict(d["datetimeLast"]) if d.get("datetimeLast") else None,
        )
    
@dataclass
class Period:
    label: str
    interval: str
    datetimeFrom: DateTimePair
    datetimeTo: DateTimePair

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Period":
        return cls(
            label=d["label"],
            interval=d["interval"],
            datetimeFrom=DateTimePair.from_dict(d["datetimeFrom"]),
            datetimeTo=DateTimePair.from_dict(d["datetimeTo"]),
        )

@dataclass
class Coverage:
    expectedCount: int
    expectedInterval: str
    observedCount: int
    observedInterval: str
    percentComplete: float
    percentCoverage: float
    datetimeFrom: DateTimePair
    datetimeTo: DateTimePair

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Coverage":
        return cls(
            expectedCount=d["expectedCount"],
            expectedInterval=d["expectedInterval"],
            observedCount=d["observedCount"],
            observedInterval=d["observedInterval"],
            percentComplete=d["percentComplete"],
            percentCoverage=d["percentCoverage"],
            datetimeFrom=DateTimePair.from_dict(d["datetimeFrom"]),
            datetimeTo=DateTimePair.from_dict(d["datetimeTo"]),
        )

@dataclass
class FlagInfo:
    hasFlags: bool

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "FlagInfo":
        return cls(hasFlags=d["hasFlags"])

@dataclass
class Measurement:
    value: float
    flagInfo: FlagInfo
    parameter: Parameter
    period: Period
    coordinates: Optional[Dict[str, float]]
    summary: Optional[str]
    coverage: Coverage

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Measurement":
        return cls(
            value=d["value"],
            flagInfo=FlagInfo.from_dict(d["flagInfo"]),
            parameter=Parameter.from_dict(d["parameter"]),
            period=Period.from_dict(d["period"]),
            coordinates=d.get("coordinates"),
            summary=d.get("summary"),
            coverage=Coverage.from_dict(d["coverage"]),
        )

__all__ = [
    "Meta",
    "Country",
    "Owner",
    "Provider",
    "Instrument",
    "Parameter",
    "Sensor",
    "Coordinates",
    "Attribution",
    "License",
    "DateTimePair",
    "LocationResult",
    "Period",
    "Coverage",
    "FlagInfo",
    "Measurement",
]
