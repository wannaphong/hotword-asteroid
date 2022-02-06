import os
from eff_word_net.streams import SimpleMicStream
from eff_word_net.engine import HotwordDetector
from eff_word_net import samples_loc

mycroft_hw = HotwordDetector(
        hotword="mobile",
        reference_file = os.path.join(samples_loc,"mobile_ref.json"),
        activation_count=3
    )

mic_stream = SimpleMicStream()
mic_stream.start_stream()

print("Say mobile ")
while True :
    frame = mic_stream.getFrame()
    result = mycroft_hw.checkFrame(frame)
    if(result):
        print("Wakeword uttered")
