import setuptools

setuptools.setup(
    name="tts_webui_extension.riffusion",
    packages=setuptools.find_namespace_packages(),
    version="0.0.3",
    author="rsxdalv",
    description="Riffusion allows generating music from text.",
    url="https://github.com/rsxdalv/tts_webui_extension.riffusion",
    project_urls={},
    scripts=[],
    install_requires=[
        # "torch>=2.0.1",
        # "torchaudio>=2.0.2",
        "pydub",
        "scipy",
        "diffusers",
        "transformers",
        "accelerate",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
