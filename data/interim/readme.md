`an_jokes_direct.json`  
`an_jokes_inverted.json`  
`bash_jokes_direct.json`  
`bash_jokes_inverted.json`  
Direct and inverted indices for datasets with equalized lengths. Direct index include information on 
how many times ech word was used in the joke. Inverted index structure:
```
inverted = {
    ...
    'some_word': [[list of good jokes indices], [list of bad jokes indices]]
    ...
} 
```