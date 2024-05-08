
from entity.Incidents import Incidents
from entity.Victims import Victims
from entity.Suspects import Suspects
from entity.LawEnforcementAgencies import LawEnforcementAgencies
from entity.Officers import Officers
from entity.Evidence import Evidence
from entity.Reports import Reports
from util.DBConnUtil import DBConnUtil


class CrimeAnalysisServiceImpl(ICrimeAnalysisService):
    def __init__(self):
        self.db_conn = DBConnUtil.get_connection()  # Assuming DBConnUtil has a static method to get DB connection

    # Implement methods for Incidents
    def create_incident(self, incident: Incidents):
        pass

    def get_incident_by_id(self, incident_id: int) -> Incidents:
        pass

    def update_incident(self, incident: Incidents):
        pass

    def delete_incident(self, incident_id: int):
        pass

    # Implement methods for Victims
    def create_victim(self, victim: Victims):
        pass

    def get_victim_by_id(self, victim_id: int) -> Victims:
        pass

    def update_victim(self, victim: Victims):
        pass

    def delete_victim(self, victim_id: int):
        pass

    # Implement methods for Suspects
    def create_suspect(self, suspect: Suspects):
        pass

    def get_suspect_by_id(self, suspect_id: int) -> Suspects:
        pass

    def update_suspect(self, suspect: Suspects):
        pass

    def delete_suspect(self, suspect_id: int):
        pass

    # Implement methods for Law Enforcement Agencies
    def create_agency(self, agency: LawEnforcementAgencies):
        pass

    def get_agency_by_id(self, agency_id: int) -> LawEnforcementAgencies:
        pass

    def update_agency(self, agency: LawEnforcementAgencies):
        pass

    def delete_agency(self, agency_id: int):
        pass

    # Implement methods for Officers
    def create_officer(self, officer: Officers):
        pass

    def get_officer_by_id(self, officer_id: int) -> Officers:
        pass

    def update_officer(self, officer: Officers):
        pass

    def delete_officer(self, officer_id: int):
        pass

    # Implement methods for Evidence
    def create_evidence(self, evidence: Evidence):
        pass

    def get_evidence_by_id(self, evidence_id: int) -> Evidence:
        pass

    def update_evidence(self, evidence: Evidence):
        pass

    def delete_evidence(self, evidence_id: int):
        pass

    # Implement methods for Reports
    def create_report(self, report: Reports):
        pass

    def get_report_by_id(self, report_id: int) -> Reports:
        pass

    def update_report(self, report: Reports):
        pass

    def delete_report(self, report_id: int):
        pass