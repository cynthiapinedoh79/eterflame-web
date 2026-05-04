from django.db import migrations

ITEMS = [
    {
        'title': 'Brand Identity & Digital Presence',
        'kicker': 'Featured Project',
        'description': 'Visual system, interface direction, and premium digital execution.',
        'tags': '',
        'is_screenshot': False,
        'order': 1,
        'is_active': True,
    },
    {
        'title': 'Immersive Web Experience',
        'kicker': 'Web',
        'description': 'UI/UX architecture with seamless frontend development.',
        'tags': '',
        'is_screenshot': False,
        'order': 2,
        'is_active': True,
    },
    {
        'title': 'Visual Campaign Direction',
        'kicker': 'Creative',
        'description': 'Concept design, storytelling, and cinematic visual language.',
        'tags': '',
        'is_screenshot': False,
        'order': 3,
        'is_active': True,
    },
    {
        'title': 'Interface Architecture System',
        'kicker': 'System',
        'description': 'Design systems, components, and structured user flows.',
        'tags': '',
        'is_screenshot': False,
        'order': 4,
        'is_active': True,
    },
    {
        'title': 'Digital Marketing Conversion Predictor',
        'kicker': 'Data · ML',
        'description': 'ML pipeline — F1-score 0.8767. Interactive Streamlit dashboard with real-time predictions.',
        'tags': 'Python,Scikit-learn,Streamlit,Plotly',
        'is_screenshot': True,
        'order': 5,
        'is_active': True,
    },
]


def seed(apps, schema_editor):
    PortfolioItem = apps.get_model('design_app', 'PortfolioItem')
    for data in ITEMS:
        PortfolioItem.objects.get_or_create(title=data['title'], defaults=data)


def unseed(apps, schema_editor):
    PortfolioItem = apps.get_model('design_app', 'PortfolioItem')
    titles = [d['title'] for d in ITEMS]
    PortfolioItem.objects.filter(title__in=titles).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('design_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, reverse_code=unseed),
    ]
