import time
import shutil
import logging
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ============================================
# YOUR VAULT PATH (already set for you):
VAULT_PATH = Path("C:/Users/SK/OneDrive/Desktop/hachkathon-0-bronze-tier/AI_Employee_Vault")
# ============================================

INBOX = VAULT_PATH / "Inbox"
NEEDS_ACTION = VAULT_PATH / "Needs_Action"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger("FileWatcher")


class InboxHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        source = Path(event.src_path)

        # Skip temporary files
        if source.name.startswith('.') or source.name.endswith('.tmp'):
            return

        # Small delay to ensure file is fully written
        time.sleep(0.5)

        if not source.exists():
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"{timestamp}_{source.name}"

        # Move file to Needs_Action
        dest = NEEDS_ACTION / new_name
        try:
            shutil.move(str(source), str(dest))
            logger.info(f"Moved: {source.name} -> /Needs_Action/{new_name}")
        except Exception as e:
            logger.error(f"Error moving file: {e}")
            return

        # Create metadata file
        meta = NEEDS_ACTION / f"{new_name}.md"
        try:
            meta.write_text(f"""---
type: file_drop
original_name: {source.name}
size: {dest.stat().st_size} bytes
detected: {datetime.now().isoformat()}
priority: normal
status: pending
---

## New File for Processing
A file was dropped into Inbox and needs processing.

## Suggested Actions
- [ ] Review the file contents
- [ ] Summarize or process as needed
- [ ] Move to Done when complete
""")
            logger.info(f"Metadata created: {new_name}.md")
        except Exception as e:
            logger.error(f"Error creating metadata: {e}")


def main():
    INBOX.mkdir(exist_ok=True)
    NEEDS_ACTION.mkdir(exist_ok=True)

    handler = InboxHandler()
    observer = Observer()
    observer.schedule(handler, str(INBOX), recursive=False)
    observer.start()

    logger.info("=" * 50)
    logger.info("FILE WATCHER IS RUNNING")
    logger.info(f"Watching: {INBOX}")
    logger.info("Drop any file into /Inbox to process it.")
    logger.info("Press Ctrl+C to stop.")
    logger.info("=" * 50)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logger.info("Watcher stopped.")
    observer.join()


if __name__ == "__main__":
    main()
