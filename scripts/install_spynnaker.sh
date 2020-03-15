#!/bin/bash


: '
This script is used to install pip-based SPyNNaker based on the information in
http://spinnakermanchester.github.io/latest/spynnaker_install.html

It covers the parts of
- Python Dependencies (for Debian-based Linux systems e.g. Ubuntu, LinuxMint etc.)
- Standard Central Installation
- User-Only Installation
- Virtualenv Installation
from the link above.

It is written to install SPyNNaker8 which is the newest version for now with PyNN 0.9 support - Python 2.7.
'


############################################ FUNCTIONS ############################################


set_virtualenv()
{
  read -p "The name of the virtual environmet: " V_ENV_NAME
  until [[ -n $V_ENV_NAME ]] ; do # virtual environmet name control
    echo "Invalid environment name."
    read -p "The name of the virtual environmet: " V_ENV_NAME
  done

  read -p "The path of the virtual environmet (Type . for the current path ): " V_ENV_PATH
  while [[ -z $V_ENV_PATH || !( -d $V_ENV_PATH ) ]] ; do # virtual environmet path control
    echo "Invalid path."
    read -p "The path of the virtual environmet (Type . for the current path ): " V_ENV_PATH
  done

  if [[ $V_ENV_PATH = "." ]] ; then
    V_ENV_PATH=$(pwd)"/${V_ENV_NAME}"
  else
    V_ENV_PATH=$V_ENV_PATH"/"$V_ENV_NAME
  fi

  echo "* Full path for the virtual environmet: $V_ENV_PATH"

  # Set the virtual environment
  pip install virtualenv
  virtualenv -p `which python2.7` $V_ENV_PATH # 2.7 is the version for now, the version part might be changed or dismissed in the (near) future.
  source $V_ENV_PATH/bin/activate
  [ $? -eq 0 ] && echo "* Environment is set and activated for further installation."
}


install_spynnaker()
{
  ## This part stands for user-only installation ##
  if [[ -n $1 ]]; then
    USER_INFO="--user" # because it will be used in this format during the installation below
    echo "* Installing SPyNNaker for the current user..."
  else
    USER_INFO=""
    echo "* Installing SPyNNaker..."
  fi
  ## -- ##


  # If you'd like to change the SpyNNaker version you are going to install,
    # here is the place to do that.
      # In time it might be updated in order to get the newest version automatically from the pip repository.
  pip install spynnaker8 $USER_INFO
  [ $? -eq 0 ] && echo "* spynnaker8 is installed."
  pip install SpyNNaker-Visualisers $USER_INFO
  [ $? -eq 0 ] && echo "* SpyNNaker-Visualisers is installed."
  python -m spynnaker8.setup-pynn
  pip install matplotlib $USER_INFO
  [ $? -eq 0 ] && echo "* matplotlib is installed."
  [ $? -eq 0 ] && echo "* Done."
}


############################################ MAIN SCRIPT ############################################


# Python dependencies for SpiNNaker on Debian-based Linux systems
echo "* Installing Python2.7..."
sudo apt-get install python2.7
echo "* Installing pip, setuptools, and wheel..."
sudo apt-get install python-pip
pip install --upgrade pip setuptools wheel
echo "* Installing necessary OpenGL libraries to be used for the visualiser..."
sudo apt-get install freeglut3-dev

echo $'\nPlease choose your preferred SPyNNaker installation from the list below.'
echo "1) Standard Central Installation"
echo "2) (Current) User-Only Installation"
echo "3) Virtual Environment Installation"
echo "Type 1, 2, or 3 for selection; q to quit."

while :
do
  read ANSWER
  case $ANSWER in
    2 )
      install_spynnaker "user-only"
      exit
      ;;

    3 )
      set_virtualenv
      ;&

    1 )
      install_spynnaker
      ;&

    q|Q )
      exit
      ;;

    * ) echo "Please type either one of the choices {1, 2, 3; q|Q}: " ;;
  esac
done
