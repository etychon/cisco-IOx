FROM multiarch/qemu-user-static:x86_64-aarch64 as qemu
FROM arm64v8/alpine
COPY --from=qemu /usr/bin/qemu-aarch64-static /usr/bin
RUN apk add --no-cache python
COPY test.py /test.py
ENTRYPOINT /usr/bin/python /test.py
