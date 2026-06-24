import sys
import os

# Add the backend directory to sys.path so we can import database and models
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models.job import Job
from models.application import Application

def seed_jobs():
    db = SessionLocal()
    
    # 1. Clear existing applications and jobs
    print("Clearing existing applications and jobs...")
    try:
        db.query(Application).delete()
        db.query(Job).delete()
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error clearing existing data: {e}")
        db.close()
        return
    
    # 2. Add 10 new jobs
    jobs = [
        Job(
            title="Senior Full-Stack Developer (MERN)",
            company="PixelCraft Studio",
            location="Bengaluru",
            salary="₹12L - ₹18LPA",
            description="Looking for a Full-Stack developer experienced in MongoDB, Express, React, and Node.js. You will lead the design and development of our primary SaaS product. Experience with AWS deployment and serverless architectures is highly valued.",
            deadline="2026-09-15",
            active=True
        ),
        Job(
            title="AI/Machine Learning Engineer",
            company="Cognitive Systems Ltd",
            location="Chennai (Hybrid)",
            salary="₹18L - ₹25LPA",
            description="Join our AI research team to build and optimize large language models and computer vision applications. Must have strong python coding skills, experience with PyTorch/TensorFlow, and familiarity with fine-tuning open-source models.",
            deadline="2026-08-30",
            active=True
        ),
        Job(
            title="Cloud Infrastructure & DevOps Engineer",
            company="SkyHigh Cloud Solutions",
            location="Hyderabad",
            salary="₹15L - ₹22LPA",
            description="We are seeking a DevOps engineer to design and maintain our secure, scalable Kubernetes clusters on AWS. Skills required: Terraform, Docker, CI/CD pipelines (GitHub Actions/Jenkins), and monitoring tools (Prometheus/Grafana).",
            deadline="2026-10-01",
            active=True
        ),
        Job(
            title="Product Designer (UI/UX)",
            company="Vivid Digital Agency",
            location="Delhi (Hybrid)",
            salary="₹10L - ₹15LPA",
            description="Seeking a creative Product Designer to design beautiful, intuitive user interfaces for mobile and web platforms. Experience in Figma, creating design systems, user research, wireframing, and interactive prototyping is required.",
            deadline="2026-08-15",
            active=True
        ),
        Job(
            title="Data Scientist",
            company="FinTrend Analytics",
            location="Bengaluru",
            salary="₹14L - ₹20LPA",
            description="Apply statistics, machine learning, and data mining techniques to analyze financial datasets and build predictive models. Proficiency in Python/R, SQL, and data visualization tools (Tableau/PowerBI) is essential.",
            deadline="2026-09-05",
            active=True
        ),
        Job(
            title="Go Backend Engineer",
            company="Microservice Masters",
            location="Hyderabad",
            salary="₹16L - ₹24LPA",
            description="Looking for a Go (Golang) developer to build high-performance microservices. You will work on designing robust APIs, optimizing database queries (PostgreSQL), and integrating real-time messaging queues like Kafka.",
            deadline="2026-08-25",
            active=True
        ),
        Job(
            title="iOS Developer (Swift)",
            company="AppStream Media",
            location="Chennai (Hybrid)",
            salary="₹12L - ₹18LPA",
            description="Looking for an iOS developer with 3+ years of experience to create native apps using Swift and SwiftUI. Must have experience with Git, consuming RESTful APIs, and publishing applications to the Apple App Store.",
            deadline="2026-10-15",
            active=True
        ),
        Job(
            title="Cybersecurity Analyst",
            company="Shield Guard Security",
            location="Delhi",
            salary="₹11L - ₹16LPA",
            description="Responsible for monitoring our network infrastructure, identifying security vulnerabilities, and responding to incidents. Certifications like CISSP, CEH, or CompTIA Security+ are highly desirable.",
            deadline="2026-09-20",
            active=True
        ),
        Job(
            title="Product Manager",
            company="SaaSify Technologies",
            location="Bengaluru (Hybrid)",
            salary="₹15L - ₹22LPA",
            description="We are looking for a Product Manager to define the product roadmap and translate user feedback into clear requirements. You will collaborate closely with engineering, design, and marketing teams.",
            deadline="2026-08-20",
            active=True
        ),
        Job(
            title="QA Automation Engineer",
            company="BugFree Systems",
            location="Remote (India)",
            salary="₹8L - ₹12LPA",
            description="Join our QA team to design, write, and execute automated test scripts for web applications. Key tools: Selenium, Cypress, Playwright, and Python/JS. Experience with load and performance testing is a plus.",
            deadline="2026-09-10",
            active=True
        )
    ]
    
    try:
        db.add_all(jobs)
        db.commit()
        print("Successfully deleted old entries and seeded 10 new jobs!")
    except Exception as e:
        db.rollback()
        print(f"Error seeding new jobs: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_jobs()
