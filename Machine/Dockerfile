FROM ubuntu:20.04

# Install necessary tools
RUN apt-get update && apt-get install -y \
    netcat \
    sudo \
    steghide \
    openssh-server \
    && apt-get clean

# Add a user for the challenge
RUN useradd -m -s /bin/bash hacker && echo "hacker:hackme" | chpasswd

# Add an image and hide a base64 flag
COPY my_image.jpg /home/hacker/my_image.jpg
RUN echo "rtb{h1dd3n_1n_1m4g3}" | base64 > /home/hacker/hidden_flag.txt
RUN steghide embed -cf /home/hacker/my_image.jpg -ef /home/hacker/hidden_flag.txt -p "secret"
RUN rm /home/hacker/hidden_flag.txt
# Add flags
RUN echo "rtb{us3r_4cc3ss_gr4nt3d}" > /home/hacker/flag.txt && chmod 644 /home/hacker/flag.txt
RUN echo "rtb{r00t_4cc3ss_gr4nt3d}" > /root/root.txt && chmod 600 /root/root.txt
RUN echo "hacker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
# Set up SSH
RUN mkdir /var/run/sshd
EXPOSE 22

# Add a monitoring script
RUN echo '#!/bin/bash\n\
while true; do\n\
    if ! who | grep -q pts; then\n\
        echo "No active SSH sessions. Restarting container..."\n\
        kill -9 1\n\
    fi\n\
    sleep 5\n\
done' > /monitor.sh && chmod +x /monitor.sh

# Run the monitoring script and SSH service
CMD ["/bin/bash", "-c", "/monitor.sh & /usr/sbin/sshd -D"]

