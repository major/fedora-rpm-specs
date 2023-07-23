# -*-Mode: rpm-spec -*-

Name:      azote
Version:   1.12.3
Release:   1%{?dist}
BuildArch: noarch
Summary:   Wallpaper and color manager for Sway, i3 and some other WMs

# GPLv3: main program
# BSD: colorthief.py
License:   GPL-3.0-only and BSD-1-Clause

URL:       https://github.com/nwg-piotr/azote
Source0:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: 0001-fedora-36-library-path.patch

BuildRequires: desktop-file-utils
BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-devel

Requires: python3-pillow
Requires: python3-gobject
Requires: ((feh and xrandr) if Xserver)
Requires: ((swaybg and wlr-randr) if wayfire)
Requires: python3-cairo

Recommends: python3-send2trash
Recommends: ImageMagick
Recommends: ((maim and slop) if Xserver)

Provides: bundled(python3-colorthief) = 0.2.1

%description
Azote is a GTK+3 - based picture browser and background setter, as the
front-end to the swaybg (sway/Wayland) and feh (X windows) commands. It
also includes several color management tools.

The program is confirmed to work on sway, i3, Openbox, Fluxbox and dwm
window managers, on Arch Linux, Void Linux, Debian and Fedora.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install
# not sure why setup.py doesn't do this, but:
install -p -D dist/%{name} %{buildroot}/%{_bindir}/%{name}
#desktop-file-edit --set-icon %{_datadir}/pixmaps/%{name}.svg dist/%{name}.desktop
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/applications dist/%{name}.desktop
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/%{name} dist/*.png dist/*.svg
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/pixmaps dist/azote.svg
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
for lib in %{buildroot}%{python3_sitelib}/%{name}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%files
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%doc README.md

%license LICENSE LICENSE-COLORTHIEF

%changelog
* Fri Jul 21 2023 Bob Hepple <bob.hepple@gmail.com> - 1.12.3-1
- new version
- migrated to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.11.0-2
- Rebuilt for Python 3.12

* Thu Mar 30 2023 Bob Hepple <bob.hepple@gmail.com> - 1.11.0-1
- new version

* Sat Mar 11 2023 Bob Hepple <bob.hepple@gmail.com> - 1.10.1-1
- new version

* Mon Feb 13 2023 Bob Hepple <bob.hepple@gmail.com> - 1.9.7-3
- added azote.svg to /usr/share/pixmaps RHBZ#2169207

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Bob Hepple <bob.hepple@gmail.com> - 1.9.7-1
- new version
- remove shebangs from library files

* Wed Jul 13 2022 James Harmison <jharmison@gmail.com> - 1.9.5-2
- Fix for Python library path

* Wed Jun 01 2022 Bob Hepple <bob.hepple@gmail.com> - 1.9.5-1
- new version

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Bob Hepple <bob.hepple@gmail.com> - 1.9.3-1
- new version

* Tue Nov 30 2021 Bob Hepple <bob.hepple@gmail.com> - 1.9.2-2
- send2trash is only recommended
- add other recommended packages

* Sun Oct 31 2021 Bob Hepple <bob.hepple@gmail.com> - 1.9.2-1
- new version

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 13 2021 Bob Hepple <bob.hepple@gmail.com> - 1.9.1-4
- depend on xrandr rather than xorg-x11-server-utils (required for f34+; OK for f33-)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.1-3
- Rebuilt for Python 3.10

* Wed May 26 2021 Bob Hepple <bob.hepple@gmail.com>
- added dependency on feh and xlr-xrandr if Xserver is installed

* Wed May 26 2021 Bob Hepple <bob.hepple@gmail.com> - 1.9.1-1
- new version

* Sat Mar 13 2021 Bob Hepple <bob.hepple@gmail.com> - 1.9.0-1
- new version

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Bob Hepple <bob.hepple@gmail.com> - 1.8.2-1
- new version

* Tue Oct 06 2020 Bob Hepple <bob.hepple@gmail.com> - 1.8.1-1
- new version

* Mon Sep 28 2020 Bob Hepple <bob.hepple@gmail.com> - 1.8.0-1
- new version

* Sun Sep 20 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.15-1
- new version

* Mon Sep 14 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.14-1
- new version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.12-1
- new release

* Mon Jun 01 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-7
- rebuilt to fix runpath error in f32

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.10-6
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-5
- update per RHBZ#1813737

* Tue Mar 17 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-4
- update per RHBZ#1813737

* Tue Mar 17 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-3
- update per RHBZ#1813737

* Mon Mar 16 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-2
- update per RHBZ#1813737

* Mon Mar 16 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.10-1
- new release

* Mon Feb 24 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.9-2.fc31.wef
- fix location of icons to what the .desktop expects

* Mon Feb 24 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7.9-1.fc31.wef
- Initial version of the package
