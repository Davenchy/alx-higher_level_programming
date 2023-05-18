#include <stdio.h>
#include <Python.h>

/**
 * get_pybytesobject_size - count the bytes inside the object
 * @obj: the bytes object
 * Return: the number of bytes stored in obj
 */
size_t get_pybytesobject_size(PyBytesObject *obj)
{
	char *data = obj->ob_sval;
	size_t size = 0;

	for (; *data; data++, size++)
		;
	return (size);
}

/**
 * print_pybytesobject_bytes - print first n bytes
 * @obj: the bytes object
 * @size: the number of bytes to print
 */
void print_pybytesobject_bytes(PyBytesObject *obj, Py_ssize_t size)
{
	char *data = obj->ob_sval;
	Py_ssize_t i;

	for (i = 0; i < size; i++)
		printf("%02hx%c", data[i] & 0xff, i < size - 1 ? ' ' : 0);
	putchar(10);
}

/**
 * print_python_bytes - A c function to print the python object bytes
 * @p: the python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size, bytes_to_print;
	PyBytesObject *obj = NULL;
	char *data;

	if (!PyBytes_Check(p))
	{
		puts("  [ERROR] Invalid Bytes Object");
		return;
	}

	obj = (PyBytesObject *)p;
	data = obj->ob_sval;
	for (size = 0; *data; data++, size++)
		;
	data = obj->ob_sval;

	bytes_to_print = size >= 10 ? 10 : size + 1;
	puts("[.] bytes object info");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", data);
	printf("  first %ld bytes: ", bytes_to_print);
	for (i = 0; i < bytes_to_print; i++)
		printf("%02hx%c", data[i] & 0xff, i < bytes_to_print ? ' ' : 0);
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
	size = PyList_Size(p);

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
