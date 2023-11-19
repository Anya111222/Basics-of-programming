# -- coding: utf-8 --
#3-var
def main(stroke):
      words = stroke.split()
      lst = []
      for i in words:
          lst.append(''.join(sorted(i)))
      return ' '.join(lst)

stroke = str(input())
print(main(stroke))