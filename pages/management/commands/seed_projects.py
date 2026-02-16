from django.core.management.base import BaseCommand
from pages.models import Project, Technology

class Command(BaseCommand):
    help = 'Populates the database with initial portfolio projects'

    def handle(self, *args, **kwargs):
        self.stdout.write('Adding projects...')

        # Helper function to get or create techs
        def get_techs(names):
            tech_objs = []
            for name in names:
                tech, created = Technology.objects.get_or_create(name=name.strip())
                tech_objs.append(tech)
            return tech_objs

        # Define the projects data
        projects_data = [
            {
                "title": "Generative AI - Dean's Research",
                "technologies": ["Python", "Hugging Face"],
                "description": "Built an end-to-end NLP pipeline for smart-city text, including scraping, normalization, zero-shot topic classification, and interactive ranking UI. Benchmarked BERT/GPT/BART models; deployed a BART-MNLI inference pipeline with 0.7 confidence routing and semantic retrieval to improve precision; presented results in a DRA poster.",
                "display_order": 1
            },
            {
                "title": "Arcane Events – Lottery-Based Android Event Platform",
                "technologies": ["Java", "Android Studio", "Firebase", "GitHub Projects", "Figma", "QR Scanning", "Geolocation APIs"],
                "description": "Developed a production-scale Android application enabling lottery-based event registration with multi-role access (entrant, organizer, admin), real-time notifications, QR code scanning, and Firebase-backed data persistence. Executed the full software engineering lifecycle in a 7-person team, including requirements gathering, UML/CRC design, sprint planning, backlog management, and iterative delivery with documented agile workflows.",
                "display_order": 2
            },
            {
                "title": "Portfolio Website",
                "technologies": ["Python", "Django", "HTML", "CSS", "JavaScript", "Tailwind CSS", "PostgreSQL", "Docker"],
                "description": "Developed a production-grade full-stack Django platform with a custom CMS, Dockerized PostgreSQL, and modular Tailwind/HTMX frontend architecture. Implemented interactive features (cursor effects, partial page loads, admin dashboards) to improve UX and maintainability.",
                "display_order": 3
            },
            {
                "title": "Autonomous Game AI Controller",
                "technologies": ["Python", "NumPy", "SciPy", "scikit-fuzzy", "Genetic Algorithms"],
                "description": "Built a fuzzy-logic autonomous game controller integrating real-time targeting, collision avoidance, and motion control using multi-sensor inputs (bullet time, angular error, collision risk, ship dynamics). Optimized controller behavior using a genetic algorithm, tuning fuzzy parameters to maximize hit rate while minimizing deaths through simulation-based fitness evaluation.",
                "display_order": 4
            }
        ]

        # Loop through and create them
        for p_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=p_data["title"],
                defaults={
                    "description": p_data["description"],
                    "display_order": p_data["display_order"],
                    "featured": True
                }
            )
            
            # Update existing projects
            if not created:
                project.description = p_data["description"]
                project.display_order = p_data["display_order"]
                project.save()

            # Add technologies
            techs = get_techs(p_data["technologies"])
            project.technologies.set(techs)
            
            self.stdout.write(self.style.SUCCESS(f'Successfully processed: {project.title}'))
