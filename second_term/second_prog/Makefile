all:
	gcc -c -DBUILD_DLL parser.c
	gcc -shared -o parser.dll parser.o -Wl,--add-stdcall-alias

	python polish_notation.py


check:
	cppcheck --enable=all --suppress=missingIncludeSystem --platform=win64 *.c *.h
	clang-format -n *.c *.h
	gcc -Wall -Werror -Wextra *.c
clean:
	del *.o *.dll

rebuild:
	make clean
	make all
	make clean
	make check
	make clean