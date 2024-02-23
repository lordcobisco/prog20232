from pylsl import StreamInlet, resolve_stream

print("looking for an stream...")
streams = resolve_stream()
inlet = StreamInlet(streams[1])

while True:
    sample, timestamp = inlet.pull_sample()
    print(timestamp, sample)
