# main.py
# Entry point for SmallPDF Clone app

import os
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.utils import platform
from kivy.clock import Clock
from plyer import storagepath, permissions

from config import (
    THEME, APP_NAME, ANDROID_PERMISSIONS, ASSETS_DIR, OUTPUT_DIR, FILE_ERROR_MESSAGES
)

# Configure Kivy settings for mobile
Config.set('graphics', 'resizable', 0)  # Disable window resizing on mobile
Config.set('kivy', 'exit_on_escape', 0)  # Prevent accidental exit
Config.write()

class HomeScreen(Screen):
    """Placeholder for the home screen."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(
            MDLabel(
                text="Welcome to SmallPDF Clone",
                halign="center",
                theme_text_color="Primary",
                font_style="H5"
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
        self.theme_cls.font_styles.update({
            "H5": [THEME["font_name"], THEME["font_size"]["title"], True]
        })

        # Initialize screen manager
        self.screen_manager = ScreenManager(transition=SlideTransition())
        self.screen_manager.add_widget(HomeScreen(name="home"))
        
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
            # Handle in UI later
            self.show_error(FILE_ERROR_MESSAGES["permission_denied"])

    def request_permissions(self, dt):
        """Request Android permissions for storage and camera."""
        for permission in ANDROID_PERMISSIONS:
            permissions.request_permission(
                permission,
                callback=lambda perm, granted: print(f"{perm}: {'Granted' if granted else 'Denied'}")
            )

    def show_error(self, message):
        """Placeholder for displaying error messages in UI."""
        print(f"Error: {message}")  # Replace with UI dialog later

if __name__ == "__main__":
    SmallPDFCloneApp().run()