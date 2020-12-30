CC=/opt/local/bin/clang-mp-11
CFLAGS=-Wall -O3
INC=-I/opt/local/include
LIB=-L/opt/local/lib

TARGETS=day04

day04: day04.cc
	$(CC) $(CFLAGS) -o $@ $^ $(INC) $(LIB) -lstdc++ -lgnutls-openssl

clean:
	@rm -f $(TARGETS) *~
