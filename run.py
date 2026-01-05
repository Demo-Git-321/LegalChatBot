import os

# Create directory
os.makedirs('samples', exist_ok=True)

# 1. Council Resolution
doc1_content = """
COUNCIL RESOLUTION NO. 2024-08
SUBJECT: ADOPTION OF RENEWABLE ENERGY STANDARDS
DATE: December 12, 2024

WHEREAS, the Governing Body aims for 40% carbon reduction by 2030.
WHEREAS, municipal energy costs exceed $1.2M annually.
RESOLVED: All new construction must be solar-ready. Annual KPI audits are required every Q3.
"""

# 2. Planning Memo
doc2_content = """
MEMORANDUM: Urban Planning Update
FROM: Dept of Urban Planning
DATE: December 15, 2024

Status: Sector 7 Redevelopment.
Findings: Transit accessibility is low in Feature IDs 109-112. 
Budget: Project is 4.5% under the $450k allocation.
Recommendation: Increase high-density residential zoning for North District.
"""

# 3. Governance Procedures
doc3_content = """
PROCEDURAL MANUAL: GOVERNING BODY
SECTION 4: VOTING PROTOCOLS

A quorum consists of 5 members. Resolutions require a simple majority (50% + 1).
Urgent amendments to GeoJSON spatial zoning must be filed 48 hours before the session.
"""

# Save as text files (Gemini can read these as .txt just as well as .pdf)
# Or you can print these to PDF using your browser/Word.
with open('samples/1.txt', 'w') as f: f.write(doc1_content)
with open('samples/2.txt', 'w') as f: f.write(doc2_content)
with open('samples/3.txt', 'w') as f: f.write(doc3_content)

print("Created 3 sample documents in /samples folder.")