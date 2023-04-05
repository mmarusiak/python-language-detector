# Python language detector

It's simple project - actually refactored in one day project that I made for one of my classes. It uses statistics to detect language. 
Project uses:
* wikipedia API;
* numpy;

Project is made entirely for fun just to play with Python.

### Parameters/values:

``precision`` is amount of articles that are "read" for each language.  
``languages`` are languages that you provide to brain (language that brain needs to learn). Provide them in ``ISO-639-1`` format or by full name.  
``data_size`` is minimum size of single article (minimum amount of letters of article) to read it.  

### Usage:

Here's quick guide of usage:
* Clone repository to selcted directory;
* Import repository by adding ``import brain`` to start of your file;
* Now create new brain via ``brain.Brain(precision, languages, data_size (optional))`` *(Please note languages are in brain.Lanugages format!)*;
* Now you can guess the language by ``brain.guess(text)``;

### brain.Languages

brain.Languages is module for getting correct languages. It also has default languages stored in ``src\languages.txt`` (which you can modify. *Format is language name-ISO-639-1*). To create new languages set simply make new brain.Languages bia ``brain.Languages(languages)``, where languages that you pass doesn't need to exist - they can be incorrect, module will detect languages that only exists in ``src\languages.txt``.

### Collaborations

Feel free to collaborate, or to use that project!
