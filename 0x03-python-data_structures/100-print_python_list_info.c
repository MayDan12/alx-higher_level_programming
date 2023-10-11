#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - iThis function prints the
 * basic info about Python lists.
 * @p: The PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int sizes, allocs, ir;
	PyObject *objs;

	sizes = Py_SIZE(p);
	allocs = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sizes);
	printf("[*] Allocated = %d\n", allocs);

	for (ir = 0; ir < sizes; ir++)
	{
		printf("Element %d: ", ir);

		objs = PyList_GetItem(p, ir);
		printf("%s\n", Py_TYPE(objs)->tp_name);
	}
}
