# test_string_methods.py:

## test_upper()
This test tests the upper() method, which converts a string to all upper case characters. The test asserts that the upper() method on the string 'foo' returns the string 'FOO'.

## test_isupper()
This test tests the isupper() method, which returns True if a string is all upper case and False otherwise. The test asserts that the isupper() method returns True for the string 'FOO' and False for the string 'Foo'.

## test_split()
This test tests the split() method, which splits a string into a list of strings, using a specified separator. The test asserts that the split() method on the string 'hello world' with a separator of ' ' returns the list ['hello', 'world'].

## test_lower()
This test tests the lower() method, which converts a string to all lower case characters. The test asserts that the lower() method on the string 'FOO' returns the string 'foo'.

## test_startswith()
This test tests the startswith() method, which returns True if a string starts with a specified substring and False otherwise. The test asserts that the startswith() method on the string 'hello world' with the substring 'hello' returns True and the substring 'world' returns False.

## test_endswith()
This test tests the endswith() method, which returns True if a string ends with a specified substring and False otherwise. The test asserts that the endswith() method on the string 'hello world' with the substring 'world' returns True and the substring 'hello' returns False.

## test_strip()
This test tests the strip() method, which removes leading and trailing whitespace from a string. The test asserts that the strip() method on the string ' hello ' returns the string 'hello'.

## test_replace()
This test tests the replace() method, which replaces all occurrences of a specified substring in a string with another specified substring. The test asserts that the replace() method on the string 'hello world' with the substring 'world' and the replacement substring 'universe' returns the string 'hello universe'.

## test_join()
This test tests the join() method, which joins a list of strings into a single string, using a specified separator. The test asserts that the join() method on the list ['hello', 'world'] with the separator ' ' returns the string 'hello world'.

## test_find()
This test tests the find() method, which returns the index of the first occurrence of a specified substring in a string. The test asserts that the find() method on the string 'hello world' with the substring 'world' returns the index 6.

## test_rfind()
This test tests the rfind() method, which returns the index of the last occurrence of a specified substring in a string. The test asserts that the rfind() method on the string 'hello world' with the substring 'world' returns the index 6.

## test_count()
This test tests the count() method, which returns the number of occurrences of a specified substring in a string. The test asserts that the count() method on the string 'hello world' with the substring 'o' returns the number 2.


## To run the tests in the module, simply execute the following command in a terminal:
python test_string_methods.py
