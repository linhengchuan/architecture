# (L)iskov-substitution principle(LSP)

- Objects should be replaceable with their subtype without affecting the correctness of the program.
- For example a class penguine inherits class bird. Penguine (is-a) bird.
- Bird object has fly method while penguine has no fly method(overwrite and unimplemented).
- If we replace bird object with penguine object, the code fails when fly is called.
- LSP is failed in this case.

### LSP is a more strict test than IS-A test

### Solution

- Breaking the hierachy method: Create a new base class which is even more generic to be implement/inherited by the other 2 classes.
- Tell, dont ask method: The utils class, that are operating on the class and its subtypes, should not need to ask them what are they before operating on them. The class and subtype should tell the utils information needed directly.
