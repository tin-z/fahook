
TARGET=test1
SOURCES=test1.c

$(TARGET): $(SOURCES)
	$(CC) $(LMFLAGS) -o $@ $^


clean:
	rm $(TARGET)
