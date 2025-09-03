from reportlab.lib.pagesizes import A4
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

# ---------- Resume Content (Update if needed) ----------
experience_content = [
    ("Armorcode Inc. / Cybersecurity SaaS platform", "Remote, India", "SDET-2", "Jan 2024 – Present", [
        "Spearheaded automation scaling for enterprise-grade clients, increasing test coverage by 30% and reducing regression cycle time.",
        "Migrated WireMock tests to AWS EC2 with secure credential management via Jenkins, enhancing security compliance and execution reliability.",
        "Optimized CI/CD test pipelines, reducing flakiness and cutting execution time by 15%.",
        "Owned feature-specific automation for workflows (e.g., Archive), improving release confidence and reducing post-deployment issues.",
        "Led CI/CD pipeline integration project by designing modular test execution stages in Jenkins & GitHub Actions, enabling parallel execution and environment-specific validations, reducing overall build feedback cycle by 40%.",
        "Built a Test Data Management and Generation System leveraging Java, AWS S3, and dynamic data factories to generate on-demand datasets, reducing manual preparation time by 60%."
    ]),
    ("Armorcode Inc.", "Remote, India", "SDET-1", "Oct 2022 – Dec 2023", [
        "Maintained and expanded automated test coverage across multiple microservices and UIs, increasing regression coverage by 25%.",
        "Collaborated with developers to integrate effective test hooks, reducing debugging time by 20%.",
        "Promoted to full-time based on exceptional internship performance.",
        "Received the “5H” Award for consistently exceeding performance targets."
    ]),
    ("Armorcode Inc.", "Remote, India", "Intern", "Feb 2022 – Sep 2022", [
        "Developed custom Java parsers for internal tool integrations, reducing manual effort by 2 hours/week.",
        "Contributed to automation scripts using Selenium, Cucumber, and Gherkin to streamline UI test cases.",
        "Built reusable automation code, accelerating new team member onboarding."
    ])
]

projects = [
    "CI/CD Pipeline Integration – Designed modular pipelines in Jenkins & GitHub Actions with quality gates, reducing deployment time by 40% while ensuring 95%+ test reliability.",
    "Test Data Management System – Built automated test data generation and management system using Java & AWS, reducing test data setup time by 70%.",
    "5H Award – Employee of the Month recognition for delivering scalable automation solutions improving regression efficiency by 25%."
]

skills_text = """
Programming: Java
Automation & Frameworks: Selenium WebDriver, TestNG, Cucumber, Rest Assured
CI/CD & Tools: Maven, Jenkins, GitHub Actions
Cloud & Platforms: AWS (EC2, S3, IAM)
Other: API Testing, WireMock, Postman
"""

# ---------- Styles ----------
styles = getSampleStyleSheet()
heading_style = ParagraphStyle(
    name="HeadingColored",
    parent=styles["Heading2"],
    textColor=colors.HexColor("#1f4e79"),  # Dark blue
    spaceAfter=10,
    spaceBefore=10
)
subheading_style = ParagraphStyle(
    name="SubHeadingColored",
    parent=styles["Heading3"],
    textColor=colors.HexColor("#2e75b6"),  # Lighter blue
    spaceAfter=6
)

# ---------- Header & Footer ----------
def add_header_footer(canvas, doc):
    canvas.saveState()
    # Header
    canvas.setFont('Helvetica-Bold', 10)
    canvas.setFillColor(colors.HexColor("#1f4e79"))
    canvas.drawString(inch, A4[1] - 0.5*inch, "Resume - Manan Girdhar")
    # Footer
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.grey)
    canvas.drawString(inch, 0.5*inch, f"Page {doc.page}")
    canvas.restoreState()

# ---------- Build Resume ----------
output_path = "Resume_Manan_Formatted_Colored.pdf"
doc = BaseDocTemplate(output_path, pagesize=A4)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height-0.5*inch, id='normal')
doc.addPageTemplates([PageTemplate(id='colored', frames=frame, onPage=add_header_footer)])

story = []

# Header Section
story.append(Paragraph("Manan Girdhar", heading_style))
story.append(Paragraph(
    "Gurgaon, India | manan.gir21@gmail.com | +91 8930983725 | "
    "LinkedIn: https://www.linkedin.com/in/manan-girdhar/ | "
    "GitHub: https://github.com/manangirdhar1", styles["Normal"]
))
story.append(Spacer(1, 12))

# Professional Experience
story.append(Paragraph("Professional Experience", heading_style))
for company, location, role, duration, bullets in experience_content:
    story.append(Paragraph(company, subheading_style))
    story.append(Paragraph(location, styles["Normal"]))
    story.append(Paragraph(f"{role} | {duration}", styles["Italic"]))
    for b in bullets:
        story.append(Paragraph(f"• {b}", styles["Normal"]))
    story.append(Spacer(1, 10))

# Education
story.append(Paragraph("Education", heading_style))
story.append(Paragraph("NIT Kurukshetra", subheading_style))
story.append(Paragraph("B.Tech in Computer Science Engineering | May 2019", styles["Normal"]))
story.append(Spacer(1, 10))

# Projects & Achievements
story.append(Paragraph("Projects & Achievements", heading_style))
for p in projects:
    story.append(Paragraph(f"• {p}", styles["Normal"]))
story.append(Spacer(1, 10))

# Skills
story.append(Paragraph("Skills", heading_style))
story.append(Paragraph(skills_text, styles["Normal"]))

# Build PDF
doc.build(story)
print(f"✅ Resume saved as {output_path}")
