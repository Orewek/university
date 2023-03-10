all:
	gcc -c -DBUILD_DLL parser_infix.c
	gcc -c -DBUILD_DLL parser_postfix.c
	move /y *.o object_files

	gcc -shared -o dll/parser_infix.dll object_files/parser_infix.o -Wl,--add-stdcall-alias
	gcc -shared -o dll/parser_postfix.dll object_files/parser_postfix.o -Wl,--add-stdcall-alias

run:
	python polish_notation.py
	python make_postfix.py

check:
	cppcheck --enable=all --suppress=missingIncludeSystem --platform=win64 *.c *.h
	clang-format -n *.c *.h

clean:
	del *.o *.dll *.exe *.txt
	del object_files\* dll \* /q 

rebuild:
	make clean all run clean check clean
