# Makefile

all: trivium_32 trivium_64
	# gcc -fPIC -shared -o pythonConnector.so ./trivium-sw/trivium64.c

trivium_32:
	echo "Make trivium 32bit"
	gcc -fPIC -shared -o pythonConnector32.so ./trivium-sw/trivium32.c

trivium_64:
	echo "Make trivium 64bit"
	gcc -fPIC -shared -o pythonConnector64.so ./trivium-sw/trivium64.c


clean:
	rm *.so
