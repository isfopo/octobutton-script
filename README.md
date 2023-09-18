# Octobutton Script

An Ableton Live Remote Script for the teensy-based [Octobutton MIDI device](https://github.com/isfopo/octobutton-embed) that provides the pedal with looper functionality using clips.

## Resources

[Structure Void's Live API version 11 Documentation](https://structure-void.com/PythonLiveAPI_documentation/Live11.0.xml),
[nsuspray API Documentation](https://nsuspray.github.io/Live_API_Doc/)
[Hanz Petrov's "Introduction to the Ableton Framework Classes"](http://remotescripts.blogspot.com/2010/03/introduction-to-framework-classes.html).
[Push2UserModeScript by jzgdev](https://github.com/jzgdev/Push2UserModeScript)
[Push 2 Midi Mappings](https://i2.wp.com/www.joshuacasper.com/contents/uploads/MidiMapping.png?ssl=1)

## Development Notes

Folders that start with a `_`, like `_Framework`, and `ableton` are included in this repo for convenience, but they should not be modified here. These are modules that will be exposed to your remote script within the Ableton environment, meaning the modules in this folder are never actually used. Having them in this folder prevents import error warnings and allows for auto-complete in your editor. These modules where downloaded from <https://github.com/gluon/AbletonLive11_MIDIRemoteScripts>, which has a number of other scripts that can be referenced in your script. These script are subject to change when Ableton releases an update, so it is possible that the code that is in this repo will become outdated. If that is the case, add an Issue or a PR to fix the problem.

If you are getting some kind of import error for the `Live` module, like `Warning: Import "Live" could not be resolved`, that can be ignored. Again, this is a module that will be used in the Ableton environment.
