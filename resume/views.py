from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')
def about_view(request):
    context = {
        "firstname": "Farzam",
        "lastname": " Asadian",
        "email": "farzamasadian@gmail.com",
        "education": "Civil Engineering Graduate from Sharif University of Technology",
        "passions": "Backend Development, Data Science, and Network Security",
        "socials": {
            "linkedin": "https://linkedin.com/in/farzam-asadian-5b558b1b9",
            "github": "https://github.com/farzamasadian",
        },
    }
    return render(request, 'resume/about.html', context)

def base_view(request):
    return render(request, 'resume/base.html')
def education_view(request):
    context = {
        "education": {
            "institution": "Sharif University of Technology",
            "degree": "Bachelor of Science in Civil Engineering",
            "gpa": "3.5",
            "dates": "August 2019 - May 2024",
        }
    }
    return render(request, 'resume/education.html', context)
def interests_view(request):
    context = {
        "interests": (
            "I enjoy exploring backend development, data science, network security, blockchain and probability modeling. In my free time, I like reading, solving puzzles, and staying updated with technology advancements."
        ),
    }
    return render(request, 'resume/interests.html', context)
def languages_view(request):

    context = {
        "languages": [
            {"name": "Persian", "level": "Native"},
            {"name": "English", "level": "Proficient"},
        ]
    }
    return render(request, 'resume/languages.html', context)
    
def navbar_view(request):
    return render(request, 'resume/navbar.html')
def skills_view(request):
    context = {
        "skills": [
            "Python, C++, HTML, CSS, JavaScript, Matlab",
            "Django, Docker, Linux, PostgreSQL, MySQL",
            "Git, Containerization, Network Security",
            "Numpy, Pandas, Seaborn, Scikit Learn"
        ],
        }
    return render(request, 'resume/skills.html', context)
def biography_view(request):
    context = {
        "bio": (
            "Born in Ramsar and raised in Karaj, I graduated from Sharif University of Technology "
            "and am currently transitioning to IT for my master's degree. During my early university years, "
            "I discovered a profound passion for Python and coding. Creating applications feels like breathing life "
            "into a lifeless body with just lines of code. Now, post-graduation, I strive to enrich my intellectual "
            "repository with topics such as machine learning, backend development, network security, cryptography, "
            "blockchain, and even quantum computing."
        ),
    }
    return render(request, 'resume/biography.html', context)
def contact_view(request):
    context = {
        'email': 'farzamasadian@gmail.com',
        'phone': '+98 937 013 4528',
        'linkedin': 'https://linkedin.com/in/farzam-asadian-5b558b1b9',
        'github': 'https://github.com/farzamasadian',
    }
    return render(request, 'resume/contact.html', context)

def projects_view(request):
    context = {
        "projects": [
            {
                "name": "Resume Website",
                "description": "A personal portfolio website to showcase my skills and projects.",
                "link": "https://github.com/farzamasadian/resume-django",
            },
            {
                "name": "Machine Learning Practice",
                "description": "A machine learning model practice built with Python and scikit-learn.",
                "link": "https://github.com/farzamasadian/ml-practice",
            },
        ],
    }
    return render(request, 'resume/projects.html', context)