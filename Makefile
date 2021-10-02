.PHONY: all

NAME = brainfuck

all:
	python $(NAME).py | python compressor.py > $(NAME).bf
