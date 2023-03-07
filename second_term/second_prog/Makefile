all:
	gcc parser.c  stack.c -o task

	gcc -c -DBUILD_DLL parser.c
	gcc -shared -o parser.dll parser.o -Wl,--add-stdcall-alias

	python polish_notation.py

clean:
	del *.o

rebuild:
	make clean
	make all
	make clean