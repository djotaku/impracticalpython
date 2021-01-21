# What I Learned

## Crypto

## Python

### python-docx module

At least at the time this book was published, there is a hierarchy to the way python-docx reads docx files.

- document - this contains paragraphs

- paragraphs - this contains runs

- run - a connected string of text with the same Style. That is, "Style" as in the style you can pick in MS Word.

- Interestingly, when the created document is opened in LibreOffice Writer 7.0.4.2, highlighting does not reveal the message. (Also using Fedora 32, KDE, and LibreOffice from Flatpak - if it matters) must actually change the font to a different color. That's pretty neat! That said, unlike MS Word, it does show squiggly lines for the mispelt words. (author points this out in figure 6-13 after I saw it)
