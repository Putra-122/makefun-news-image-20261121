"""Entry program for news-image-20261121.

Copies the pre-rendered entry.png (built by make_image.py in this
repository) to the grader's output directory. Standard library only,
no network, deterministic: both runs write identical bytes.
"""
import os
import shutil


def main():
    # The grader sets MAKEFUN_OUTPUT_DIR; default is the sandbox /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(
        os.path.join(here, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
