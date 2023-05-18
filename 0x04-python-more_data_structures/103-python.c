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

	if (!PyBytes_Check(p))
	{
		puts("  [ERROR] Invalid Bytes Object");
		return;
	}

	obj = (PyBytesObject *)p;
	size = ((PyVarObject *)p)->ob_size;

	fflush(stdout);
	puts("[.] bytes object info");
	printf("  size: %ld\n", size);

	if (++size > 10)
		size = 10;
	printf("  trying string: %s\n", obj->ob_sval);
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
		printf("%02hx%c", obj->ob_sval[i] & 0xff, i < size - 1 ? ' ' : 0);
	putchar(10);
}

/**
 * print_python_list - a c function to print python list information
 * @p: the python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyListObject *obj;

	if (!PyList_Check(p))
		return;

	obj = (PyListObject *)p;
	size = ((PyVarObject *)p)->ob_size;

	fflush(stdout);
	puts("[*] Python list info");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = obj->ob_item[i];

		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
