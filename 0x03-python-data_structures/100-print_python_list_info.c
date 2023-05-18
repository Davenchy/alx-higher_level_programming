#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - a c function to print python list information
 * @p: the python list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
