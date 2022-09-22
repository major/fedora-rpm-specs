# Force out of source build
%undefine __cmake_in_source_build

# % global snap       20200911
# % global gitcommit  9b383805b7967884a8b602c5a43be415c3427fe4
# % global shortcommit % (c=% {gitcommit}; echo $ {c:0:5})

%global appname io.github.antimicrox.antimicrox
%global libname libantilib

Name:         antimicrox
Version:      3.2.4
Release:      2%{?snap:.%{snap}git%{shortcommit}}%{?dist}
Summary:      Graphical program used to map keyboard buttons and mouse controls to a gamepad

License:  GPLv3+
URL:      https://github.com/AntiMicroX/%{name}

%if 0%{?snap}
%global archivename %{name}-%{gitcommit}
%else
%global archivename %{name}-%{version}
%endif

%if 0%{?snap}
Source0:        %{url}/archive/%{gitcommit}/%{archivename}.tar.gz
%else
Source0:        %{url}/archive/%{version}/%{archivename}.tar.gz
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  SDL2-devel
BuildRequires:  itstool
BuildRequires:  gettext
# For desktop file & AppData
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  systemd

Requires:       systemd-udev

%description
%{name} is a graphical program used to map keyboard keys and mouse controls
to a gamepad. This program is useful for playing PC games using a gamepad that
do not have any form of built-in gamepad support. %{name} is a fork of
AntiMicro which was inspired by QJoyPad but has additional features.

%prep
%setup -n %{archivename} -q

%build
%cmake3
%cmake3_build

%install
%cmake3_install

%find_lang %{name} --with-qt

%post
%udev_rules_update

%postun
%udev_rules_update

%files -f %{name}.lang
# Redundant
%exclude %{_datadir}/%{name}/CHANGELOG.md
%exclude %dir %{_datadir}/%{name}/translations
%exclude %{_datadir}/%{name}/translations/*
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/*/*/apps/*
%{_metainfodir}/%{appname}.appdata.xml
%{_datadir}/mime/packages/%{appname}.xml
%{_mandir}/man1/%{name}.1*
%{_udevrulesdir}/60-antimicrox-uinput.rules

%check
%{_bindir}/desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appname}.desktop
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{appname}.appdata.xml

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Gergely Gombos <gombosg@disroot.org> - 3.2.4-1
- 3.2.4

* Sun May 22 2022 Gergely Gombos <gombosg@disroot.org> - 3.2.3-1
- 3.2.3

* Mon Apr 11 2022 Gergely Gombos <gombosg@disroot.org> - 3.2.2-1
- 3.2.2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Gergely Gombos <gombosg@disroot.org> - 3.2.1-1
- 3.2.1

* Tue Nov 30 2021 Gergely Gombos <gombosg@disroot.org> - 3.2.0-1
- 3.2.0

* Fri Sep 17 2021 Gergely Gombos <gombosg@disroot.org> - 3.1.7-1
- 3.1.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Gergely Gombos <gombosg@disroot.org> - 3.1.4-1
- 3.1.4, remove libantilib subpackage

* Sun Nov 15 2020 Gergely Gombos <gombosg@disroot.org> - 3.1.3-1
- 3.1.3, remove icons dependency, add % {arm} arch

* Fri Oct 2 2020 Gergely Gombos <gombosg@disroot.org> - 3.1.2-1
- 3.1.2

* Fri Sep 11 2020 Gergely Gombos <gombosg@disroot.org> - 3.1-1.20200911git9b383
- Initial package
