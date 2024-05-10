import time
import winsound
winsound.PlaySound('audio/Raining in Manila.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
time.sleep(1)
winsound.PlaySound(None, winsound.SND_NODEFAULT)
winsound.PlaySound('audio/Raining in Manila.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
time.sleep(1)
winsound.PlaySound(None, winsound.SND_NODEFAULT)