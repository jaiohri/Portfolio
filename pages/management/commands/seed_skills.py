from django.core.management.base import BaseCommand
from pages.models import Skill

class Command(BaseCommand):
    help = 'Populates the database with skills based on the user provided list'

    def handle(self, *args, **kwargs):
        self.stdout.write('Adding skills...')

        # Skill data based on the image
        # Using a mapping for category -> list of skills
        # Since the model doesn't seem to have a category field yet, we'll just add them all
        # I'll assign icons and levels based on typical proficiency (you can adjust levels later in admin)
        
        skills_data = [
            # Languages
            {"name": "Python", "icon": "🐍", "level": 95, "order": 1, "category": "LANG"},
            {"name": "C", "icon": "🇨", "level": 80, "order": 2, "category": "LANG"},
            {"name": "C++", "icon": "➕", "level": 85, "order": 3, "category": "LANG"},
            {"name": "Java", "icon": "☕", "level": 85, "order": 4, "category": "LANG"},
            {"name": "Rust", "icon": "🦀", "level": 75, "order": 5, "category": "LANG"},
            {"name": "JavaScript", "icon": "📜", "level": 90, "order": 6, "category": "LANG"},
            {"name": "HTML/CSS", "icon": "🎨", "level": 95, "order": 7, "category": "LANG"},

            # Frameworks
            {"name": "Django", "icon": "🎸", "level": 95, "order": 1, "category": "FRAME"},
            {"name": "Flask", "icon": "⚗️", "level": 90, "order": 2, "category": "FRAME"},
            {"name": "React", "icon": "⚛️", "level": 85, "order": 3, "category": "FRAME"},
            {"name": "Tailwind", "icon": "🌬️", "level": 90, "order": 4, "category": "FRAME"},
            {"name": "HTMX", "icon": "🔄", "level": 85, "order": 5, "category": "FRAME"},
            {"name": "Framer", "icon": "🖼️", "level": 80, "order": 6, "category": "FRAME"},

            # AI/ML
            {"name": "ANN", "icon": "🧠", "level": 85, "order": 1, "category": "AIML"},
            {"name": "CNN", "icon": "👁️", "level": 85, "order": 2, "category": "AIML"},
            {"name": "RAG", "icon": "📚", "level": 90, "order": 3, "category": "AIML"},
            {"name": "LangChain", "icon": "🦜", "level": 90, "order": 4, "category": "AIML"},
            {"name": "LangGraph", "icon": "📊", "level": 85, "order": 5, "category": "AIML"},
            {"name": "NLP Pipelines", "icon": "🗣️", "level": 90, "order": 6, "category": "AIML"},

            # Backend/Databases
            {"name": "PostgreSQL", "icon": "🐘", "level": 90, "order": 1, "category": "BACK"},
            {"name": "MongoDB", "icon": "🍃", "level": 85, "order": 2, "category": "BACK"},
            {"name": "Redis", "icon": "🔴", "level": 80, "order": 3, "category": "BACK"},
            {"name": "Celery", "icon": "🥦", "level": 80, "order": 4, "category": "BACK"},

            # Cloud/DevOps
            {"name": "Docker", "icon": "🐳", "level": 85, "order": 1, "category": "CLOUD"},
            {"name": "AWS", "icon": "☁️", "level": 80, "order": 2, "category": "CLOUD"},
            {"name": "Pipedream", "icon": "🔗", "level": 85, "order": 3, "category": "CLOUD"},

            # Developer Tools
            {"name": "Git", "icon": "🌲", "level": 95, "order": 1, "category": "TOOL"},
            {"name": "VS Code", "icon": "📝", "level": 95, "order": 2, "category": "TOOL"},
            {"name": "Cursor", "icon": "🖱️", "level": 95, "order": 3, "category": "TOOL"},
            {"name": "Jira", "icon": "🎫", "level": 85, "order": 4, "category": "TOOL"},
            {"name": "LangSmith", "icon": "🛠️", "level": 85, "order": 5, "category": "TOOL"},

            # CS Fundamentals
            {"name": "Data Structures", "icon": "🌳", "level": 90, "order": 1, "category": "FUND"},
            {"name": "Algorithms", "icon": "🧮", "level": 90, "order": 2, "category": "FUND"},
            {"name": "OOP", "icon": "📦", "level": 95, "order": 3, "category": "FUND"},
            {"name": "System Design", "icon": "🏗️", "level": 85, "order": 4, "category": "FUND"},
        ]

        count = 0
        for s_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=s_data["name"],
                defaults={
                    "icon": s_data["icon"],
                    "level": s_data["level"],
                    "display_order": s_data["order"],
                    "category": s_data["category"]
                }
            )
            
            # Update existing
            skill.category = s_data["category"]  # Force update category
            skill.icon = s_data["icon"]
            skill.level = s_data["level"]
            skill.display_order = s_data["order"]
            skill.save()
                
            count += 1
            
        self.stdout.write(self.style.SUCCESS(f'Successfully processed {count} skills'))
