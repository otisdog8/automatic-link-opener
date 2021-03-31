#!/bin/bash
mkdir ~/.config/link_opening/
chmod +x opening/config_editor.py
cp opening/daemon.py ~/.config/link_opening/daemon.py
sudo cp opening/config_editor.py /usr/bin/config_editor
cp link-opener.service ~/.config/systemd/user/link-opener.service