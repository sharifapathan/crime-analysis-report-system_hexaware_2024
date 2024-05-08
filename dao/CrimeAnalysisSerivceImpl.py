import mysql.connector
class DBContext():
    def __init__(self, connection):
        self.connection = connection

    def connect_to_mysql(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user=r'root',
                password=r'Riyaiscute',
                database=r'project1'
            )

            print("Connected to MySQL")
            return connection

        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def close_connection(connection):
        if connection:
            connection.close()
            print("Connection closed")

    def create_victim(self, connection, victim_data):
        try:
            cursor = connection.cursor()
            sql_query = "INSERT INTO Victims (FirstName, LastName, DateOfBirth, Gender, ContactInformation) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_query, victim_data)
            connection.commit()
            print("Victim created successfully")
        except Exception as e:
            print("Exception creating victim:", e)

        # Function to retrieve all victims

    def get_all_victims(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Victims")
            victims = cursor.fetchall()
            for victim in victims:
                print(victim)
        except Exception as e:
            print("Exception retrieving victims:", e)

        # Function to update a victim's information

    def update_victim(self, connection, victim_id, new_data):
        try:
            cursor = connection.cursor()
            sql_query = "UPDATE Victims SET FirstName=%s, LastName=%s, DateOfBirth=%s, Gender=%s, ContactInformation=%s WHERE VictimID=%s"
            new_data.append(victim_id)  # Append victim_id to the end of new_data
            cursor.execute(sql_query, new_data)
            connection.commit()
            print("Victim updated successfully")
        except Exception as e:
            print("Exception updating victim:", e)

        # Function to delete a victim

    def delete_victim(self, connection, victim_id):
        try:
            cursor = connection.cursor()
            sql_query = "DELETE FROM Victims WHERE VictimID=%s"
            cursor.execute(sql_query, (victim_id,))
            connection.commit()
            print("Victim deleted successfully")
        except Exception as e:
            print("Exception deleting victim:", e)

    def create_suspect(self, connection, suspect_data):
        try:
            cursor = connection.cursor()
            sql_query = "INSERT INTO Suspects (FirstName, LastName, DateOfBirth, Gender, ContactInformation) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_query, suspect_data)
            connection.commit()
            print("Suspect created successfully")
        except Exception as e:
            print("Exception creating suspect:", e)

        # Function to retrieve all suspects

    def get_all_suspects(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Suspects")
            suspects = cursor.fetchall()
            for suspect in suspects:
                print(suspect)
        except Exception as e:
            print("Exception retrieving suspects:", e)

        # Function to update a suspect's information

    def update_suspect(self, connection, suspect_id, new_data):
        try:
            cursor = connection.cursor()
            sql_query = "UPDATE Suspects SET FirstName=%s, LastName=%s, DateOfBirth=%s, Gender=%s, ContactInformation=%s WHERE SuspectID=%s"
            new_data.append(suspect_id)  # Append suspect_id to the end of new_data
            cursor.execute(sql_query, new_data)
            connection.commit()
            print("Suspect updated successfully")
        except Exception as e:
            print("Exception updating suspect:", e)

        # Function to delete a suspect

    def delete_suspect(self, connection, suspect_id):
        try:
            cursor = connection.cursor()
            sql_query = "DELETE FROM Suspects WHERE SuspectID=%s"
            cursor.execute(sql_query, (suspect_id,))
            connection.commit()
            print("Suspect deleted successfully")
        except Exception as e:
            print("Exception deleting suspect:", e)

    def create_agency(self, connection, agency_data):
        try:
            cursor = connection.cursor()
            sql_query = "INSERT INTO LawEnforcementAgencies (AgencyName, Jurisdiction, ContactInformation) VALUES (%s, %s, %s)"
            cursor.execute(sql_query, agency_data)
            connection.commit()
            print("Agency created successfully")
        except Exception as e:
            print("Exception creating agency:", e)

    def get_all_agencies(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM LawEnforcementAgencies")
            agencies = cursor.fetchall()
            for agency in agencies:
                print(agency)
        except Exception as e:
            print("Exception retrieving agencies:", e)

    def update_agency(self, connection, agency_id, new_data):
        try:
            cursor = connection.cursor()
            sql_query = "UPDATE LawEnforcementAgencies SET AgencyName=%s, Jurisdiction=%s, ContactInformation=%s WHERE AgencyID=%s"
            new_data.append(agency_id)  # Append agency_id to the end of new_data
            cursor.execute(sql_query, new_data)
            connection.commit()
            print("Agency updated successfully")
        except Exception as e:
            print("Exception updating agency:", e)

    def delete_agency(self, connection, agency_id):
        try:
            cursor = connection.cursor()
            sql_query = "DELETE FROM LawEnforcementAgencies WHERE AgencyID=%s"
            cursor.execute(sql_query, (agency_id,))
            connection.commit()
            print("Agency deleted successfully")
        except Exception as e:
            print("Exception deleting agency:", e)

    def create_officer(self, connection, officer_data):
        try:
            cursor = connection.cursor()
            sql_query = "INSERT INTO Officers (FirstName, LastName, BadgeNumber, OfficerRank, ContactInformation, AgencyID) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, officer_data)
            connection.commit()
            print("Officer created successfully")
        except Exception as e:
            print("Exception creating officer:", e)

    def get_all_officers(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Officers")
            officers = cursor.fetchall()
            for officer in officers:
                print(officer)
        except Exception as e:
            print("Exception retrieving officers:", e)

    def update_officer(self, connection, officer_id, new_data):
        try:
            cursor = connection.cursor()
            sql_query = "UPDATE Officers SET FirstName=%s, LastName=%s, BadgeNumber=%s, OfficerRank=%s, ContactInformation=%s, AgencyID=%s WHERE OfficerID=%s"
            new_data.append(officer_id)  # Append officer_id to the end of new_data
            cursor.execute(sql_query, new_data)
            connection.commit()
            print("Officer updated successfully")
        except Exception as e:
            print("Exception updating officer:", e)

    def delete_officer(self, connection, officer_id):
        try:
            cursor = connection.cursor()
            sql_query = "DELETE FROM Officers WHERE OfficerID=%s"
            cursor.execute(sql_query, (officer_id,))
            connection.commit()
            print("Officer deleted successfully")
        except Exception as e:
            print("Exception deleting officer:", e)

    def create_incident(self, connection, incident_data):
        try:
            cursor = connection.cursor()
            sql_query = "INSERT INTO Incidents (IncidentType, IncidentDate, LocationLatitude, LocationLongitude, Description, Status, VictimID, SuspectID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, incident_data)
            connection.commit()
            print("Incident created successfully")
        except Exception as e:
            print("Exception creating incident:", e)

    def get_all_incidents(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Incidents")
            incidents = cursor.fetchall()
            for incident in incidents:
                print(incident)
        except Exception as e:
            print("Exception retrieving incidents:", e)

    def update_incident(self, connection, incident_id, new_data):
        try:
            cursor = connection.cursor()
            sql_query = "UPDATE Incidents SET IncidentType=%s, IncidentDate=%s, LocationLatitude=%s, LocationLongitude=%s, Description=%s, Status=%s, VictimID=%s, SuspectID=%s WHERE IncidentID=%s"
            new_data.append(incident_id)  # Append incident_id to the end of new_data
            cursor.execute(sql_query, new_data)
            connection.commit()
            print("Incident updated successfully")
        except Exception as e:
            print("Exception updating incident:", e)

    def delete_incident(self, connection, incident_id):
        try:
            cursor = connection.cursor()
            sql_query = "DELETE FROM Incidents WHERE IncidentID=%s"
            cursor.execute(sql_query, (incident_id,))
            connection.commit()
            print("Incident deleted successfully")
        except Exception as e:
            print("Exception deleting incident:", e)

        # Example usage

    def create_evidence(self, connection, evidence_data):
        try:
            cursor = connection.cursor()
            sql_query = "INSERT INTO Evidence (Description, LocationFound, IncidentID) VALUES (%s, %s, %s)"
            cursor.execute(sql_query, evidence_data)
            connection.commit()
            print("Evidence created successfully")
        except Exception as e:
            print("Exception creating evidence:", e)

    def get_all_evidence(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Evidence")
            evidence = cursor.fetchall()
            for item in evidence:
                print(item)
        except Exception as e:
            print("Exception retrieving evidence:", e)

    def update_evidence(self, connection, evidence_id, new_data):
        try:
            cursor = connection.cursor()
            sql_query = "UPDATE Evidence SET Description=%s, LocationFound=%s, IncidentID=%s WHERE EvidenceID=%s"
            new_data.append(evidence_id)  # Append evidence_id to the end of new_data
            cursor.execute(sql_query, new_data)
            connection.commit()
            print("Evidence updated successfully")
        except Exception as e:
            print("Exception updating evidence:", e)

    def delete_evidence(self, connection, evidence_id):
        try:
            cursor = connection.cursor()
            sql_query = "DELETE FROM Evidence WHERE EvidenceID=%s"
            cursor.execute(sql_query, (evidence_id,))
            connection.commit()
            print("Evidence deleted successfully")
        except Exception as e:
            print("Exception deleting evidence:", e)

    def create_report(self, connection, report_data):
        try:
            cursor = connection.cursor()
            sql_query = "INSERT INTO Reports (IncidentID, ReportingOfficer, ReportDate, ReportDetails, Status) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_query, report_data)
            connection.commit()
            print("Report created successfully")
        except Exception as e:
            print("Exception creating report:", e)

    def get_all_reports(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Reports")
            reports = cursor.fetchall()
            for report in reports:
                print(report)
        except Exception as e:
            print("Exception retrieving reports:", e)

    def update_report(self, connection, report_id, new_data):
        try:
            cursor = connection.cursor()
            sql_query = "UPDATE Reports SET IncidentID=%s, ReportingOfficer=%s, ReportDate=%s, ReportDetails=%s, Status=%s WHERE ReportID=%s"
            new_data.append(report_id)  # Append report_id to the end of new_data
            cursor.execute(sql_query, new_data)
            connection.commit()
            print("Report updated successfully")
        except Exception as e:
            print("Exception updating report:", e)

    def delete_report(self, connection, report_id):
        try:
            cursor = connection.cursor()
            sql_query = "DELETE FROM Reports WHERE ReportID=%s"
            cursor.execute(sql_query, (report_id,))
            connection.commit()
            print("Report deleted successfully")
        except Exception as e:
            print("Exception deleting report:", e)

    # Example usage
