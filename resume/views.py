from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')
def about_view(request):
    return render(request, 'resume/about.html')
def base_view(request):
    return render(request, 'resume/base.html')
def education_view(request):
    return render(request, 'resume/education.html')
def interests_view(request):
    context = {
        "interests": [
            "Machine Learning", 
            "Backend Development", 
            "Network Security", 
            "Cryptography", 
            "Blockchain", 
            "Quantum Computing"
        ],
    }
    return render(request, 'resume/interests.html', context)
def languages_view(request):
    context = {
        "languages": ["Persian (Native)", "English (Fluent)"],
    }
    return render(request, 'resume/languages.html', context)
def navbar_view(request):
    return render(request, 'resume/navbar.html')
def skills_view(request):
    return render(request, 'resume/skills.html')
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
        'phone': '+98 XXX XXX XXXX',
        'linkedin': 'https://linkedin.com/in/farzam-asadian-5b558b1b9',
        'github': 'https://github.com/farzamasadian',
    }
    return render(request, 'resume/contact.html', context)

def projects_view(request):
    context = {
        'projects': [
            {
                'name': 'Resume',
                'description': 'A simple django project.',
                'link': 'https://linktoyourproject.com',
            }
        ]
    }
    return render(request, 'projects.html', context)