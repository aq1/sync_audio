import os
import tempfile
from typing import Tuple

from django.conf import settings


def convert_audio(audio_file) -> Tuple[str, bytes]:
    name = os.path.splitext(audio_file.name)[0] + settings.DEFAULT_AUDIO_FORMAT

    with tempfile.TemporaryDirectory() as temp_dir:
        new_path = os.path.join(temp_dir, name)
        with tempfile.NamedTemporaryFile() as audio_file_fp:
            audio_file_fp.write(audio_file.read())
            if os.system(f'ffmpeg -y -i "{audio_file_fp.name}" "{new_path}"'):
                return '', b''

            with open(new_path, 'rb') as f:
                return os.path.split(new_path)[-1], f.read()
