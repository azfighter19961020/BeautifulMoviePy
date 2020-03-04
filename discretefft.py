import numpy.fft as nf
import numpy as np
from moviepy.editor import *

def takeLoud(video_clip):
	audio = video_clip.audio
	x = audio.to_soundarray(fps=44100)
	sample_rate = 44100
	times = np.arange(len(x)) / sample_rate
	print(times)
	freqs = nf.fftfreq(times.size,1/sample_rate)
	noised_ffts = nf.fft(x)
	noised_pows = np.abs(noised_ffts)
	fund_freq = np.abs(freqs[noised_pows.argmax()])
	quit_indices = np.where(np.abs(freqs)==fund_freq)
	quit_pows = x[quit_indices]
	quit_times = times[quit_indices]
	VideoClip = []
	AudioClip = []
	for i in range(len(quit_times)-1):
		VideoClip.append(video_clip.subclip(quit_times[i],quit_times[i+1]))
		AudioClip.append(audio.subclip(quit_times[i],quit_times[i+1]))

	concateVideo = concatenate_videoclips(VideoClip)
	concateAudio = concatenate_audioclips(AudioClip)

	concateVideo.set_audio(concateAudio)
	return concateVideo