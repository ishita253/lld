import os

r, w = os.pipe()  # Create pipe (r = read end, w = write end)

# Process A (writer)
pid = os.fork()

if pid == 0:
    os.close(r)  # Close read end
    os.write(w, b"Hello from process A\n")
    os.close(w)
else:
    os.close(w)  # Close write end
    print("Process B received:", os.read(r, 100).decode())
    os.close(r)
