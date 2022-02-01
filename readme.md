# Publishing a Workflow

1. Create an entry in the project that you want to publish, or
   edit an existing entry. The two files to edit are `commit.yaml`
   and `pantheon.yaml`. The `commit.yaml` file contains metadata
   about the commit of this entry. The data includes the url of the
   workflow and the commit ID of the published workflow. For example:

```
repository: https://github.com/cinemascienceworkflows/2021-04_Nyx-Ascent
commit:     39b6c8831ae68ed89f449eea0dc0ecc828d03fab
```

1. Now you create the public entry for the project, by running the publish script 
   from the top level directory:

```
python publish.py <project> <workflow>
```

This will create a `<entry>.md` file in the top level directory. This entry should be
pasted into the appropriate page in the `pantheonscience.org` website, or other place 
you want to publish the entry.
