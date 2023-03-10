all:
	gcc -c -DBUILD_DLL parser.c
	move /y *.o object_files

	gcc -shared -o dll/parser.dll object_files/parser.o -Wl,--add-stdcall-alias

run:
	python polish_notation.py
	python check2.py

check:
	cppcheck --enable=all --suppress=missingIncludeSystem --platform=win64 *.c *.h
	clang-format -n *.c *.h

clean:
	del *.o *.dll *.exe *.txt
	del object_files\* dll \* /q 

rebuild:
	make clean all run clean check clean
