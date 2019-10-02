#!/usr/bin/env python3

import __pystruct_internals__
import fractions
import decimal

class frac:
  def __init__(self, num=None, den=None, whl=None):
    if num is not None and den is None and whl is None:
      if isinstance(num, int):
        whl = num
        den = 1
        num = 0
      elif isinstance(num, float):
        whl = int(num)

        frac = fractions.Fraction(decimal.Decimal(str(num))%1)

        den = frac.denominator
        num = frac.numerator
      elif isinstance(num, str):
        num = num.strip()

        frac = fractions.Fraction(decimal.Decimal(num))

        den = frac.denominator
        num = frac.numerator % den
        whl = int(frac.numerator / den)
      else:
        raise TypeError('Expected one of int, float, or string for argument.')
    elif num is not None and den is not None and whl is None:
      whl = 0

      if not (isinstance(num, int) or isinstance(num, float)) or not (isinstance(den, int) or isinstance(den, float)):
        raise TypeError('Expected type int or float for both arguments.')
    elif num is not None and den is not None and whl is not None:
      if not (isinstance(num, int) or isinstance(num, float)) or not (isinstance(den, int) or isinstance(den, float)) or not (isinstance(whl, int) or isinstance(whl, float)):
        raise TypeError('Expected type int or float for all arguments.')
    else:
      # All are none
      num = 0
      den = 1
      whl = 0

    if den == 0:
      raise ZeroDivisionError('Denominator of fraction cannot be zero.')

    self.num = int(num)
    self.den = int(den)
    self.whl = int(whl)

  def toMixed(self, iweiz=False):
    if iweiz or (not iweiz and self.whl != 0):
      res = '%i %i/%i' % (self.whl, self.num, self.den)
    else:
      res = '%i/%i' % (self.num, self.den)

    return res

  def toImproper(self):
    new_num = (self.whl*self.den) + self.num

    return '%i/%i' % (new_num, self.den)

  def reciprocate(self):
    new_num = (self.whl*self.den) + self.num
    self.num = den
    self.den = new_num

    return self

  def reciprocal(self):
    new_num = (self.whl*self.den) + self.num

    return frac(self.den, new_num)

  def copy(self):
    return frac(self.num, self.den, self.whl)

  def __repr__(self):
    return 'frac(\'%s\')' % (self.toImproper())

  def __str__(self):
    return self.toImproper()
