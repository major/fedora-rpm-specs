Name:           x11docker
Version:        7.6.0
Release:        %autorelease
Summary:        Run GUI applications and desktops in Linux containers

License:        MIT
URL:            https://github.com/mviereck/x11docker
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Default to the podman backend instead of docker
Patch0:         x11docker-podman-default.patch

BuildArch:      noarch

Requires:       bash
Requires:       (podman or /usr/bin/docker or /usr/bin/nerdctl)
Requires:       (xorg-x11-server-Xwayland or xorg-x11-server-Xorg)

Recommends:     nxagent
Recommends:     tini-static
Recommends:     xclip
Recommends:     xdotool
Recommends:     xdpyinfo
Recommends:     xhost
Recommends:     xorg-x11-server-Xephyr
Recommends:     xorg-x11-server-Xvfb
Recommends:     xorg-x11-xauth
Recommends:     xorg-x11-xinit
Recommends:     xpra
Recommends:     xrandr
Recommends:     (weston if libwayland-client)

%description
x11docker allows to run graphical desktop applications (and entire desktops) in
Linux containers.

%prep
%autosetup -p1

%install
install -Dpm0755 x11docker %{buildroot}%{_bindir}/x11docker
install -Dpm0644 x11docker.man %{buildroot}%{_mandir}/man1/x11docker.1

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md TODO.md paper.bib paper.md x11docker.png
%{_bindir}/x11docker
%{_mandir}/man1/x11docker.1*

%changelog
%autochangelog
