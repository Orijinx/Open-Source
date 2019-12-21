from synthesizer import Player, Synthesizer, Waveform
chord = [261.626,  329.628, 391.996]

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
# Play A4
#player.play_wave(synthesizer.generate_constant_wave(440.0, 3.0))

player.play_wave(synthesizer.generate_chord(chord,3.0))

#Player.play_wave(synthesizer.generate_chord(chord, 3.0))