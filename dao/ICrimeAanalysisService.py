from abc import ABC, abstractmethod
from datetime import date
from typing import List




class ICrimeAnalysisService(ABC):
    """Interface for Crime Analysis and Reporting System service."""

    @abstractmethod
    def createIncident(self, incident) -> bool:
        """Create a new incident."""
        pass

    @abstractmethod
    def updateIncidentStatus(self, status, incident_id) -> bool:
        """Update the status of an incident."""
        pass

    @abstractmethod
    def getIncidentsInDateRange(self, start_date: date, end_date: date) -> List:
        """Get a list of incidents within a date range."""
        pass

    @abstractmethod
    def searchIncidents(self, criteria) -> List:
        """Search for incidents based on various criteria."""
        pass

    @abstractmethod
    def generateIncidentReport(self, incident) -> Report:
        """Generate incident reports."""
        pass

    @abstractmethod
    def createCase(self, case_description: str, incidents: List) -> Case:
        """Create a new case and associate it with incidents."""
        pass

    @abstractmethod
    def getCaseDetails(self, case_id: int) -> Case:
        """Get details of a specific case."""
        pass

    @abstractmethod
    def updateCaseDetails(self, case: Case) -> bool:
        """Update case details."""
        pass

    @abstractmethod
    def getAllCases(self) -> List:
        """Get a list of all cases."""
        pass