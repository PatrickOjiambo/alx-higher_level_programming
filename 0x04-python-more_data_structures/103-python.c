#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size;
    Py_ssize_t i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);

    if (size > 10)
        size = 10;

    printf("  first %zd bytes: ", size);
    for (i = 0; i < size; i++) {
        printf("%02x", (unsigned char)str[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

