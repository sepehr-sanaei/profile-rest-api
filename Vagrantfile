Vagrant.configure("2") do |config|
  # Set the box to Ubuntu 18.04 (Bionic)
  config.vm.box = "ubuntu/bionic64"

  # Update and upgrade the packages on VM startup
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update && sudo apt-get upgrade -y

    # Install Python 3 if it's not already installed
    sudo apt-get install -y python3 python3-pip

    # Create an alias file to set Python 3 as the default
    echo 'alias python=python3' | sudo tee -a /home/vagrant/.bashrc

    # Reload .bashrc to apply alias
    source /home/vagrant/.bashrc
  SHELL

  # Forward port 8000 from guest to host
  config.vm.network "forwarded_port", guest: 8000, host: 8000
end
