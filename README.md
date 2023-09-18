# Repro

```
# get venv
python -m venv venv
source venv/bin/activate
# install deps
pip install -r requirements.txt
# run repro
python repro.py
# check highting in the doc out-pypdf.pdf out-pypdf2.pdf
```

Output
```
output-pypdf.pdf [549.1] [457.4]
/Users/sergei.vorobev/src/pypdf-highlighting-repro/repro.py:23: DeprecationWarning: AnnotationBuilder.rectangle is deprecated and will be removed in pypdf 4.0.0. Use pypdf.annotations.Rectangle instead.
  annotation = annotation_builder.rectangle(
output-pypdf2.pdf [315.3] [449.5]
```

`out-pypdf2.pdf` is much closer to the real position of the text in the document.