#include <ctype.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - A c function to print the python object bytes
 * @p: the python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	PyBytesObject *obj = NULL;

	fflush(stdout);
	puts("[.] bytes object info");
	if (!PyBytes_Check(p)) /* if not bytes object then print error */
	{
		puts("  [ERROR] Invalid Bytes Object");
		return;
	}

	obj = (PyBytesObject *)p;
	size = ((PyVarObject *)p)->ob_size; /* get the used object size */

	printf("  size: %ld\n", size);
	for (i = 0; i < size; i++)
		if (!obj->ob_sval[i]) /* if end of string break */
			break;
		else if (isprint(obj->ob_sval[i])) /* print  character if printable */
			putchar(obj->ob_sval[i]);
	putchar(10); /* add new line */
	if (++size > 10) /* recalculate the size to be less than 10 with NULL char */
		size = 10;
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++) /* print each byte in formated hex with spaces */
		printf("%02hhx%c", obj->ob_sval[i], i < size - 1 ? 32 : 10);
}

/**
 * print_python_list - a c function to print python list information
 * @p: the python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyListObject *obj;

	fflush(stdout);
	puts("[*] Python list info");
	if (!PyList_Check(p)) /* if not a list object then stop execuation */
		return;

	obj = (PyListObject *)p;
	size = ((PyVarObject *)p)->ob_size; /* get the list used size */

	printf("[*] Size of the Python List = %ld\n", size);
	/* the allocated list size */
	printf("[*] Allocated = %ld\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = obj->ob_item[i]; /* get item from the list */

		/* the item's type name */
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item)) /* if item of type bytes the print info */
			print_python_bytes(item);
	}
}
