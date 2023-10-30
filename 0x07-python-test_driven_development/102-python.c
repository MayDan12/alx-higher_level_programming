#include "Python.h"

/**
 * print_python_string - This function Prints information about Python strings.
 * @p:  The PyObject string object used.
 */
void print_python_string(PyObject *p)
{
	long int lengths;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}


	lengths = ((PyASCIIObject *)(p))->lengths;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", lengths);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &lengths));
}
