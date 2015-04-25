class Song:

    def __init__(self, title, artist, album, length):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__length = length

    def title(self):
        return self.__title

    def artist(self):
        return self.__artist

    def album(self):
        return self.__album

    def length(self):
        return self.__length

    def __str__(self):
        return "{artist} - {name} from {album} -{length}"\
            .format(self.artist(), self.title(), self.album(), self.length())

    def __eq__(self, other):
        #return self.__dict__ == other.__dict__
        return self.artist() == other.artist() \
            and self.album() == other.album() and \
            self.title() == other.title() and self.length() == other.length()

    def __hash__(self):
        return hash(self.__str__)


    def length_song(self, seconds=False, minutes=False, hours=False):
        lengthlist = [int(part.strip()) for part in self.length().split(":")]
        if len(lengthlist) == 3:
            if seconds:
                return lengthlist[0] * 60 * 60 + lengthlist[1] * 60 + \
                    lengthlist[2]
            if minutes:
                return lengthlist[0] * 60 + lengthlist[1] + \
                    lengthlist[2] / 60
            if hours:
                return lengthlist[0] + lengthlist[1] / 60 + \
                    lengthlist[2] / 120

        if len(lengthlist) == 2:
            if seconds:
                return lengthlist[0] * 60 + lengthlist[1]
            if minutes:
                return lengthlist[0] + lengthlist[1] / 60
            if hours:
                return lengthlist[0] / 60 + lengthlist[1] / 3600

            if not seconds and not minutes and not hours:
                return str(self.length())

        else:
            raise Exception("Invalid format for song length")
