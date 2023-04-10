<h2 align="center">
Python language detector
</h2>
<h4 align="center">
Project made entirely for fun.  

![textdetect](https://user-images.githubusercontent.com/20907620/230876982-855a69db-b618-432d-9d3b-3adf86ab0fd7.gif)
</h4>

### Parameters/values:

``precision`` is amount of articles that are "read" for each language.  
``languages`` are languages that you provide to brain (language that brain needs to learn). Provide them as ``brain.Language``.  
``data_size`` is minimum size of single article (minimum amount of letters of article) to read it.  

### Usage:

Here's quick guide of usage:
* Clone repository to selcted directory;
* Import repository by adding ``import brain`` to start of your file;
* Now create new brain via ``brain.Brain(precision, languages, data_size (optional))`` *(Please note languages are in brain.Lanugages format!)*;
* Now you can guess the language by ``brain.guess(text)``;

Project *(probably)* works only on latin based languages.

Project uses wiki API and numpy.


### brain.Languages

brain.Languages is module for getting correct languages. It also has default languages stored in ``src\languages.txt`` (which you can modify. *Format is language name-ISO-639-1*). To create new languages set simply make new brain.Languages via ``brain.Languages(languages)``, where languages that you pass *(in ``ISO-639-1`` format or by full name)* doesn't need to exist - they can be incorrect, module will detect languages that only exists in ``src\languages.txt``.

### Collaborations

Feel free to collaborate, or to use that project!
