def parse(s, v):
    """
    Parse identity data and return link object.
    """

    toret = []

    if s == 'wikidata':
        return {
            'name': 'Wikidata',
            'url': 'https://www.wikidata.org/wiki/' + v
        }
    elif s == 'niconicopedia':
        return {
            'name': 'ニコニコ大百科',
            'url': 'https://dic.nicovideo.jp/a/' + v
        }
    elif s == 'namuwiki':
        return {
            'name': 'Namuwiki',
            'url': 'https://namu.wiki/w/' + v
        }
    elif s == 'imdb':
        return {
            'name': 'IMDb',
            'url': 'https://www.imdb.com/name/' + v
        }
    elif s == 'personarchive-v1':
        return {
            'name': 'PersonArchive V1',
            'url': v
        }
    elif s == 'twitter':
        for i in v:
            if 'id' in i:
                toret.append({
                    'name': 'Twitter',
                    'url': 'https://twitter.com/i/user/' + str(i['id'])
                })
            elif 'username' in i:
                toret.append({
                    'name': 'Twitter',
                    'url': 'https://twitter.com/' + i['username']
                })
        return toret
    elif s == 'youtube':
        for i in v:
            if 'channelId' in i:
                toret.append({
                    'name': 'YouTube',
                    'url': 'https://www.youtube.com/channel/' + i['channelId']
                })
            elif 'userId' in i:
                toret.append({
                    'name': 'YouTube',
                    'url': 'https://www.youtube.com/user/' + i['userId']
                })
        return toret
    elif s == 'theaudiodb':
        return {
            'name': 'TheAudioDB',
            'url': 'https://www.theaudiodb.com/artist/' + str(v)
        }
    elif s == 'musicbrainz':
        return {
            'name': 'MusicBrainz',
            'url': 'https://musicbrainz.org/artist/' + v
        }
