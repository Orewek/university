build: all
ALLFILES=stack.c stack.h build.c
FILES= stack.c build.c
all:
	gcc $(FILES) -o task

check:
	cppcheck --enable=all --suppress=missingIncludeSystem --platform=win64 $(ALLFILES)