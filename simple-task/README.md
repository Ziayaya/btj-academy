1. Menambahkan custom port 5000 dan app route about
2. - untuk menyalin file ke file lain yang ada di dalam vm, dapat menggunakan command cp nama-file nama-folder
   - untuk build docker image yaitu dimulai dengan from python alpine yang diberi nama label simple task-safira, lalu melakukan WORKDIR setelah itu copy file requirements.txt. Setelah itu, run requirements.txt menggunakan pip install lalu expose port 5050 dan yang terakhir CMD app.py
   - Setelah membuat dockerfile, perlu membuat inventory.yaml yang mendefinisikan local path dan remote path yang diinginkan, docker image, container name dan docker tag yang diinginkan. Dikarenakan saya melakukan run melalui vm, maka saya menggunakan ansible host 10.184.0.100
     Untuk playbook sendiri, terdiri dari copy app.py ke remote server, requirements.txt ke remote server, membuat docker image flask dan container. Setelah itu run menggunakan cmd ansible-playbook -i inventory.yaml playbook.yaml
