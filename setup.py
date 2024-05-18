import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='In Repository Markdown Migrator',
     version='0.1',
    entry_points={"mkdocs.plugins" : ["in-repo-markdown-migration = in-repo-markdown-migration.plugin:"
        ]},
     author="Kyle Mathews",
     author_email="sphenyspace@gmail.com",
     description="MkDocs plugin to migrate in repository markdown files into generated documentation.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     install_requires=['mkdocs'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
