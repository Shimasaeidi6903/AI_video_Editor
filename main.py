import os
import shutil

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup


class VideoEditorApp(App):

    def build(self):

        self.selected_videos = []

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="AI VIDEO EDITOR",
            font_size=28,
            size_hint_y=None,
            height=70
        )

        select_button = Button(
            text="SELECT VIDEOS",
            size_hint_y=None,
            height=60
        )

        select_button.bind(
            on_press=self.open_file_chooser
        )

        self.selected_label = Label(
            text="No videos selected",
            size_hint_y=None,
            height=50
        )

        self.instruction = TextInput(
            hint_text="Describe the edit you want...",
            multiline=True
        )

        edit_button = Button(
            text="START EDITING",
            size_hint_y=None,
            height=60
        )

        edit_button.bind(
            on_press=self.start_editing
        )

        layout.add_widget(title)
        layout.add_widget(select_button)
        layout.add_widget(self.selected_label)
        layout.add_widget(self.instruction)
        layout.add_widget(edit_button)

        return layout

    def open_file_chooser(self, instance):

        chooser = FileChooserListView(
            multiselect=True,
            filters=[
                "*.mp4",
                "*.mov",
                "*.avi",
                "*.mkv",
                "*.webm"
            ]
        )

        select_button = Button(
            text="SELECT",
            size_hint_y=None,
            height=60
        )

        cancel_button = Button(
            text="CANCEL",
            size_hint_y=None,
            height=60
        )

        buttons = BoxLayout(
            size_hint_y=None,
            height=60
        )

        buttons.add_widget(select_button)
        buttons.add_widget(cancel_button)

        content = BoxLayout(
            orientation="vertical"
        )

        content.add_widget(chooser)
        content.add_widget(buttons)

        popup = Popup(
            title="Select Videos",
            content=content,
            size_hint=(0.95, 0.9)
        )

        select_button.bind(
            on_press=lambda x:
            self.confirm_selection(
                chooser,
                popup
            )
        )

        cancel_button.bind(
            on_press=popup.dismiss
        )

        popup.open()

    def confirm_selection(self, chooser, popup):

        self.selected_videos = chooser.selection

        if self.selected_videos:

            count = len(self.selected_videos)

            self.selected_label.text = (
                str(count)
                + " video(s) selected"
            )

            info = (
                str(count)
                + " VIDEOS SELECTED\n\n"
            )

            for video in self.selected_videos:

                filename = os.path.basename(video)

                size = os.path.getsize(video)

                size_mb = size / (1024 * 1024)

                info += (
                    "🎬 "
                    + filename
                    + "\n"
                    + "Size: "
                    + str(round(size_mb, 2))
                    + " MB\n\n"
                )

            self.show_popup(info)

        else:

            self.selected_label.text = (
                "No videos selected"
            )

        popup.dismiss()

    def start_editing(self, instance):

        if not self.selected_videos:

            self.show_popup(
                "Please select a video first."
            )

            return

        try:

            video = self.selected_videos[0]

            filename = os.path.basename(video)

            output_folder = os.path.join(
                os.path.dirname(video),
                "AI_VIDEO_EDITOR"
            )

            os.makedirs(
                output_folder,
                exist_ok=True
            )

            output_file = os.path.join(
                output_folder,
                "edited_" + filename
            )

            shutil.copy2(
                video,
                output_file
            )

            self.show_popup(
                "SUCCESS!\n\n"
                "Output created:\n\n"
                + output_file
            )

        except Exception as e:

            self.show_popup(
                "ERROR:\n\n"
                + str(e)
            )

    def show_popup(self, message):

        popup = Popup(
            title="AI VIDEO EDITOR",
            content=Label(
                text=message
            ),
            size_hint=(0.85, 0.6)
        )

        popup.open()


VideoEditorApp().run()
