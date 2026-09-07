"""Traverse repositories and identify candidate source files."""

from __future__ import annotations

from os import walk
from pathlib import Path

from .file_filter import FileFilter
from .language_detector import LanguageDetector


class RepositoryScanner:
    def __init__(
        self,
        file_filter: FileFilter | None = None,
        language_detector: LanguageDetector | None = None,
    ) -> None:
        self.file_filter = file_filter or FileFilter()
        self.language_detector = language_detector or LanguageDetector()

    def scan(self, repository: str | Path) -> None:
        """Traverse every directory and file beneath ``repository``.

        Ignored directories are pruned from traversal, and unsupported or
        hidden files are skipped. Detected languages are intentionally not
        returned or processed yet.
        """
        root = Path(repository).expanduser()

        if not root.exists():
            raise FileNotFoundError(f"Repository does not exist: {root}")
        if not root.is_dir():
            raise NotADirectoryError(f"Repository is not a directory: {root}")

        for _directory, directories, files in walk(root, followlinks=False):
            directories[:] = [
                directory
                for directory in directories
                if not self.file_filter.should_skip_directory(directory)
            ]

            for file_name in files:
                file_path = Path(_directory) / file_name
                if not self.file_filter.should_include_file(file_path):
                    continue

                detected_language = self.language_detector.detect(file_path)
                if detected_language is None:
                    continue

                # Detection is wired into the scan, but the result is not used
                # until extraction and indexing are implemented.


def scan_repository(repository: str | Path) -> None:
    RepositoryScanner().scan(repository)
