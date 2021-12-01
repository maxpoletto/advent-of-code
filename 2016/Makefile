CC=/usr/local/opt/llvm/bin/clang
CFLAGS=-Wall -Wno-deprecated-declarations -O3

LIB=-L/usr/local/opt/openssl@3/lib -L/usr/local/opt/gnutls/lib
INC=-I/usr/local/opt/openssl@3/include

TARGETS=day05

day05: day05.cc
	$(CC) $(CFLAGS) -o $@ $^ $(INC) $(LIB) -lstdc++ -lcrypto

day14: day14.cc
	$(CC) $(CFLAGS) -o $@ $^ $(INC) $(LIB) -lstdc++ -lcrypto

clean:
	@rm -f $(TARGETS) *~
