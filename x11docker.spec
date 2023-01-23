Name:           x11docker
Version:        6.9.0
Release:        6%{?dist}
Summary:        Run GUI applications and desktops in Linux containers

License:        MIT
URL:            https://github.com/mviereck/x11docker
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Default to the podman backend instead of docker
Patch0:         x11docker-podman-default.patch
# Use /usr/bin/tini-static for tini if available
Patch1:         %{url}/pull/369.patch

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
# x11docker-gui depends on kaptain, which is not packaged yet

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md TODO.md paper.bib paper.md x11docker.png
%{_bindir}/x11docker

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 6.9.0-2
- Make weston dependency conditional on Wayland being installed
- Fix binary install

* Sun Jun 13 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 6.9.0-1
- Initial package
