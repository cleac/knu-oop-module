# Modular work on Object Oriented Programming course

### About

This project implements a plain data manager in Python 3, where
 - data can be built from several files
 - the access level of users is implemented:
   - users can get data from files
   - moderators can edit data from files 
   - admins can create and delete data nodes
   - superadmins can create users
 - files are saved in /var/data (no windows support)

### Control questions

1. Which principles of SOLID was used in this project?

        SRP - fully
        OCP - partially, 'cause it can't be implemented fully in Python
        LSP - fully
        ISP - partially, 'cause Python doesn't need such thing as interface

2. Which design patterns were used in the project?

        Object oriented: Singleton, Facade
        Functional: decorator, context call (file interactions using with operator of Python)

3. Which patterns would be used if another programming language would be used?

        Strategy and (maybe)Builder would be used in static typed languages, like C++ for file i/o.

___

The MIT License (MIT)

Copyright (c) 2016 Alexander Nesterenko

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
