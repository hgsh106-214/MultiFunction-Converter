import ffmpy
from pydub import AudioSegment
from tkinter import *
from tkinter import filedialog
from kivy.app import App
from kivy.core.window import Window
# kivy.require("1.10.1")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.write()


class MainScreen(Screen):
    pass


class AudioScreen(Screen):
    pass


class VideoScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main.kv")


class MainApp(App):

    def build(self):
        return presentation

    class AudioFunction(App):
        def to_mp3(self):
            root = Tk()
            try:
                fileName = filedialog.askopenfilename(
                    filetypes=(('WAV files', "*.wav"), ('OGG files', "*.ogg"), ('AAC files', "*.aac"),
                               ('M4A files', "*.m4a"), ('FLV files', "*.flv"),
                               ('MP4 files', "*.mp4"), ('WMV files', "*.wmv"), ("All files", "*.*")),
                    title='Please select a file you want to convert')
                dirname = filedialog.asksaveasfilename(filetypes=(('MP3 files', "*.mp3"), ("All files", "*.*")),
                                                        title='Please select a directory to save')
                if fileName[-3:] == "wav":
                    AudioSegment.from_wav(fileName, "wav").export(dirname+".mp3", format="mp3")
                elif fileName[-3:] == "ogg":
                    AudioSegment.from_ogg(fileName, "ogg").export(dirname+".mp3", format="mp3")
                elif fileName[-3:] == "m4a":
                    AudioSegment.from_file(fileName, "m4a").export(dirname+".mp3", format="mp3")
                elif fileName[-3:] == "aac":
                    AudioSegment.from_file(fileName, "aac").export(dirname+".mp3", format="mp3")
                elif fileName[-3:] == "mp4":
                    AudioSegment.from_file(fileName, "mp4").export(dirname+".mp3", format="mp3")
                elif fileName[-3:] == "flv":
                    AudioSegment.from_file(fileName, "flv").export(dirname+".mp3", format="mp3")
                elif fileName[-3:] == "wmv":
                    AudioSegment.from_file(fileName, "wmv").export(dirname+".mp3", format="mp3")
            except:
                print("Convert failed")
            root.destroy()

        def to_wav(self):
            root = Tk()
            try:
                fileName = filedialog.askopenfilename(
                    filetypes=(('MP3 files', "*.mp3"), ('OGG files', "*.ogg"), ('AAC files', "*.aac"),
                               ('M4A files', "*.m4a"), ('FLV files', "*.flv"),
                               ('MP4 files', "*.mp4"), ('WMV files', "*.wmv"), ("All files", "*.*")),
                    title='Please select a file you want to convert')
                dirname = filedialog.asksaveasfilename(filetypes=(('WAV files', "*.wav"), ("All files", "*.*")),
                                                       title='Please select a directory to save')
                if fileName[-3:] == "mp3":
                    AudioSegment.from_mp3(fileName, "mp3").export(dirname + ".wav", format="wav")
                elif fileName[-3:] == "ogg":
                    AudioSegment.from_ogg(fileName, "ogg").export(dirname + ".wav", format="wav")
                elif fileName[-3:] == "m4a":
                    AudioSegment.from_file(fileName, "m4a").export(dirname + ".wav", format="wav")
                elif fileName[-3:] == "aac":
                    AudioSegment.from_file(fileName, "aac").export(dirname + ".wav", format="wav")
                elif fileName[-3:] == "mp4":
                    AudioSegment.from_file(fileName, "mp4").export(dirname + ".wav", format="wav")
                elif fileName[-3:] == "flv":
                    AudioSegment.from_file(fileName, "flv").export(dirname + ".wav", format="wav")
                elif fileName[-3:] == "wmv":
                    AudioSegment.from_file(fileName, "wmv").export(dirname + ".wav", format="wav")
            except:
                print("Convert failed")
            root.destroy()

        def to_ogg(self):
            root = Tk()
            try:
                fileName = filedialog.askopenfilename(
                    filetypes=(('MP3 files', "*.mp3"), ('WAV files', "*.wav"), ('AAC files', "*.aac"),
                               ('M4A files', "*.m4a"), ('FLV files', "*.flv"),
                               ('MP4 files', "*.mp4"), ('WMV files', "*.wmv"), ("All files", "*.*")),
                    title='Please select a file you want to convert')
                dirname = filedialog.asksaveasfilename(filetypes=(('ogg files', "*.ogg"), ("All files", "*.*")),
                                                       title='Please select a directory to save')
                if fileName[-3:] == "mp3":
                    AudioSegment.from_mp3(fileName, "mp3").export(dirname + ".ogg", format="ogg")
                elif fileName[-3:] == "wav":
                    AudioSegment.from_wav(fileName, "wav").export(dirname + ".ogg", format="ogg")
                elif fileName[-3:] == "m4a":
                    AudioSegment.from_file(fileName, "m4a").export(dirname + ".ogg", format="ogg")
                elif fileName[-3:] == "aac":
                    AudioSegment.from_file(fileName, "aac").export(dirname + ".ogg", format="ogg")
                elif fileName[-3:] == "mp4":
                    AudioSegment.from_file(fileName, "mp4").export(dirname + ".ogg", format="ogg")
                elif fileName[-3:] == "flv":
                    AudioSegment.from_file(fileName, "flv").export(dirname + ".ogg", format="ogg")
                elif fileName[-3:] == "wmv":
                    AudioSegment.from_file(fileName, "wmv").export(dirname + ".ogg", format="ogg")
            except:
                print("Convert failed")
            root.destroy()

        def to_aac(self):
            root = Tk()
            try:
                fileName = filedialog.askopenfilename(
                    filetypes=(('MP3 files', "*.mp3"), ('WAV files', "*.wav"), ('M4A files', "*.m4a"),
                               ('OGG files', "*.ogg"), ('FLV files', "*.flv"),
                               ('MP4 files', "*.mp4"), ('WMV files', "*.wmv"), ("All files", "*.*")),
                    title='Please select a file you want to convert')
                dirname = filedialog.asksaveasfilename(filetypes=(('AAC files', "*.aac"), ("All files", "*.*")),
                                                       title='Please select a directory to save')
                if fileName[-3:] == "mp3":
                    AudioSegment.from_mp3(fileName, "mp3").export(dirname + ".aac", format="aac")
                elif fileName[-3:] == "wav":
                    AudioSegment.from_wav(fileName, "wav").export(dirname + ".aac", format="aac")
                elif fileName[-3:] == "ogg":
                    AudioSegment.from_ogg(fileName, "ogg").export(dirname + ".aac", format="aac")
                elif fileName[-3:] == "m4a":
                    AudioSegment.from_file(fileName, "m4a").export(dirname + ".aac", format="aac")
                elif fileName[-3:] == "mp4":
                    AudioSegment.from_file(fileName, "mp4").export(dirname + ".aac", format="aac")
                elif fileName[-3:] == "flv":
                    AudioSegment.from_file(fileName, "flv").export(dirname + ".aac", format="aac")
                elif fileName[-3:] == "wmv":
                    AudioSegment.from_file(fileName, "wmv").export(dirname + ".aac", format="aac")
            except:
                print("Convert failed")
            root.destroy()

    class VideoFunction(App):
        def to_avi(self):
            root = Tk()
            try:
                fileName = filedialog.askopenfilename(filetypes=(
                ('FLV files', "*.flv"), ('MP4 files', "*.mp4"), ('WMV files', "*.wmv"), ("All files", "*.*")),
                                                      title='Please select a file you want to convert')
                dirname = filedialog.asksaveasfilename(filetypes=(('AVI files', "*.avi"), ("All files", "*.*")),
                                                       title='Please select a directory to save')
                ffmpy.FFmpeg(inputs={fileName: None}, outputs={dirname + ".avi": None}).run()
            except:
                print("Convert failed")
            root.destroy()

        def to_mp4(self):
            root = Tk()
            try:
                fileName = filedialog.askopenfilename(filetypes=(
                ('FLV files', "*.flv"), ('AVI files', "*.avi"), ('WMV files', "*.wmv"), ("All files", "*.*")),
                                                      title='Please select a file you want to convert')
                dirname = filedialog.asksaveasfilename(filetypes=(('MP4 files', "*.mp4"), ("All files", "*.*")),
                                                       title='Please select a directory to save')
                ffmpy.FFmpeg(inputs={fileName: None}, outputs={dirname + ".mp4": None}).run()
            except:
                print("Convert failed")
            root.destroy()

        def to_wmv(self):
            root = Tk()
            try:
                fileName = filedialog.askopenfilename(filetypes=(
                ('FLV files', "*.flv"), ('AVI files', "*.avi"), ('MP4 files', "*.mp4"), ("All files", "*.*")),
                                                      title='Please select a file you want to convert')
                dirname = filedialog.asksaveasfilename(filetypes=(('WMV files', "*.wmv"), ("All files", "*.*")),
                                                       title='Please select a directory to save')
                ffmpy.FFmpeg(inputs={fileName: None}, outputs={dirname + ".wmv": None}).run()
            except:
                print("Convert failed")
            root.destroy()

        def to_flv(self):
            root = Tk()
            try:
                fileName = filedialog.askopenfilename(filetypes=(
                ('AVI files', "*.avi"), ('MP4 files', "*.mp4"), ('WMV files', "*.wmv"), ("All files", "*.*")),
                                                      title='Please select a file you want to convert')
                dirname = filedialog.asksaveasfilename(filetypes=(('FLV files', "*.flv"), ("All files", "*.*")),
                                                       title='Please select a directory to save')
                ffmpy.FFmpeg(inputs={fileName: None}, outputs={dirname + ".flv": None}).run()
            except:
                print("Convert failed")
            root.destroy()
if __name__ == "__main__":
    Window.clearcolor = (0.674, 0.796, 0.882, 1)
    MainApp().run()
