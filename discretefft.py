import numpy.fft as nf
import numpy as np
from moviepy.editor import *
def takeLoud(video_clip):
	audio = video_clip.audio
	x = audio.to_soundarray(fps=44100)
	sample_rate = 44100
	times = np.arange(len(x)) / sample_rate
	print(times)
	freqs = nf.fftfreq(times.size,1 / sample_rate)
	noised_ffts = nf.fft(x)
	noised_pows = np.abs(noised_ffts)
	quit_indices = np.where(noised_pows > np.mean(noised_pows)*10)
	quit_pows = x[quit_indices[0]]
	quit_times = times[quit_indices[0]]
	timeList = []
	VideoClip,AudioClip = [],[]
	for i in range(len(quit_times)-1):
		if quit_times[i+1] - quit_times[i] < 1:
			continue
		timeList.append(quit_times[i])
	for i in range(len(timeList)-1):
		VideoClip.append(video_clip.subclip(timeList[i],timeList[i+1]))
		AudioClip.append(audio.subclip(timeList[i],timeList[i+1]))
		print("append complete")	
	concateVideo = concatenate_videoclips(VideoClip)
	concateAudio = concatenate_audioclips(AudioClip)

	concateVideo.set_audio(concateAudio)
	return concateVideo