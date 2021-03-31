# automatic-link-opener

Just a little thing that I wrote that automatically opens links at a certain time every day. Useful for things like school.

install.sh to install. Run "systemctl --user enable --now link-opener" to enable the service. Use config_editor to edit the configuration of when links open.

Depends on python-watchdog, python. Written in 3.9. Tested on Arch linux, though other people can try to use.
