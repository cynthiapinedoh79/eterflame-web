from django.db import migrations

SLUGS = {
    'Canva Pro': 'canva',
    'DistroKid': 'distrokid',
    'ElevenLabs': 'elevenlabs',
    'Framer': 'framer',
    'Hostinger': 'hostinger',
    'Notion': 'notion',
    'Spotify': 'spotify',
    'Suno AI': 'suno',
}


def seed_slugs(apps, schema_editor):
    AffiliateLink = apps.get_model('works', 'AffiliateLink')
    for link in AffiliateLink.objects.all():
        slug = SLUGS.get(link.name)
        if slug and not link.simpleicons_slug:
            link.simpleicons_slug = slug
            link.save()


def unseed_slugs(apps, schema_editor):
    AffiliateLink = apps.get_model('works', 'AffiliateLink')
    AffiliateLink.objects.filter(simpleicons_slug__in=SLUGS.values()).update(simpleicons_slug='')


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_affiliatelink_simpleicons_slug'),
    ]

    operations = [
        migrations.RunPython(seed_slugs, reverse_code=unseed_slugs),
    ]
