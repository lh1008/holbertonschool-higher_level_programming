#include "holberton.h"

/**
 * _isupper - Continue point
 * Desc: function that checks for uppercase character
 * @c: int c
 * Return: Always 0 (Success)
 */
int _isupper(int c)
{
	if (c >=65 && c <= 90)
		return (1);
	else
		return (0);
}
