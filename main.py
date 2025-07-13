# main.py
# Entry point for SmallPDF Clone app

import os
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, SlideTransition, Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.utils import platform
from kivy.clock import Clock
from plyer import storagepath
from kivy.lang import Builder
Builder.load_file("screens/home.kv")

from config import (
    THEME, APP_NAME, ANDROID_PERMISSIONS, ASSETS_DIR, OUTPUT_DIR, FILE_ERROR_MESSAGES
)

# Configure Kivy settings for mobile
Config.set('graphics', 'resizable', 0)  # Disable window resizing on mobile
Config.set('kivy', 'exit_on_escape', 0)  # Prevent accidental exit
Config.write()

class HomeScreen(Screen):
    """Home screen with feature buttons (defined in home.kv)."""
    pass

class PlaceholderScreen(Screen):
    """Generic placeholder screen for unimplemented features."""
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.add_widget(
            MDLabel(
                text=f"{name.replace('_', ' ').title()} (Coming Soon)",
                halign="center",
                theme_text_color="Primary",
            )
        )

class SmallPDFCloneApp(MDApp):
    """Main app class for SmallPDF Clone."""
    
    def build(self):
        """Initialize the app with theme and screen manager."""
        # Apply theme settings
        self.theme_cls.theme_style = THEME["theme_style"]
        self.theme_cls.primary_palette = THEME["primary_palette"]
        self.theme_cls.accent_palette = THEME["accent_palette"]

        # Initialize screen manager
        self.screen_manager = ScreenManager(transition=SlideTransition())
        
        # Add home screen and placeholder screens for each feature
        self.screen_manager.add_widget(HomeScreen(name="home"))
        feature_screens = [
            "merge", "split", "compress", "reorder", "protect",
            "img2pdf", "scan", "ocr", "pdf2img"
        ]
        for screen_name in feature_screens:
            self.screen_manager.add_widget(PlaceholderScreen(name=screen_name))
        
        return self.screen_manager

    def on_start(self):
        """Run startup tasks like directory creation and permission checks."""
        # Create necessary directories
        self.create_directories()
        
        # Request Android permissions
        if platform == "android":
            Clock.schedule_once(self.request_permissions, 0)

    def create_directories(self):
        """Create assets and output directories if they don't exist."""
        try:
            # Get Android-compatible paths
            app_dir = storagepath.get_application_dir()
            assets_path = os.path.join(app_dir, ASSETS_DIR)
            output_path = os.path.join(app_dir, OUTPUT_DIR)
            
            # Create directories
            for path in [assets_path, output_path]:
                if not os.path.exists(path):
                    os.makedirs(path)
        except Exception as e:
            print(f"Error creating directories: {e}")
            self.show_error(FILE_ERROR_MESSAGES["permission_denied"])

    def request_permissions(self, dt):
        """Request Android permissions for storage and camera."""
        # TODO: Implement permissions when building for Android
        # For now, just print a message
        print("Permissions would be requested on Android")
        # for permission in ANDROID_PERMISSIONS:
        #     permissions.request_permission(
        #         permission,
        #         callback=lambda perm, granted: print(f"{perm}: {'Granted' if granted else 'Denied'}")
        #     )

    def show_error(self, message):
        """Placeholder for displaying error messages in UI."""
        print(f"Error: {message}")  # Replace with UI dialog later

if __name__ == "__main__":
    SmallPDFCloneApp().run()