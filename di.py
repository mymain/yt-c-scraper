from environs import Env


class UrlService:  # is depended on Env
    url = ''

    def __init__(self):
        self.env = Env()  # <-- the injected dependency


class YoutubeService:  # is depended on UrlService
    def __init__(self):
        self.client = UrlService()  # <-- the injected dependency
        self.client.env.read_env()
        self.url = self.client.env('youtube_url')


class InstagramService:  # is depended on UrlService
    def __init__(self):
        self.client = UrlService()  # <-- the injected dependency
        self.client.env.read_env()
        self.url = self.client.env('instagram_url')


if __name__ == '__main__':
    youtubeService = YoutubeService()
    instagramService = InstagramService()

    print(youtubeService.url)
    print(instagramService.url)

