from pydub import AudioSegment


folder = 'samples/'

def crop(audio_file, intervals):
    song = AudioSegment.from_mp3(folder + audio_file)
    new_inters = [0] + list(map(lambda x: x * 1000, intervals)) + [-1]
    segments = [song[new_inters[i]: new_inters[i+1]]
                for i in range(len(new_inters) - 1)]
    for i, segment in enumerate(segments):
        segment.export('{}{}_segment{}.mp3'.format(folder, audio_file[:-4], i),
                       format='mp3')


def concatenate(audio_files, filename):
    segments = [AudioSegment.from_mp3(folder + f) for f in audio_files]
    res = AudioSegment.empty()
    for segment in segments:
        res += segment
    res.export(folder + filename, format='mp3')


def reverse(audio_file, filename):
    song = AudioSegment.from_mp3(folder + audio_file)
    backwards = song.reverse()
    backwards.export(folder + filename, format='mp3')
