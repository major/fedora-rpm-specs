%global provider org.rncbc.qpwgraph

Name:           qpwgraph
Version:        0.3.9
Release:        1%{?dist}
Summary:        PipeWire Graph Qt GUI Interface
# Main license is GPLv2+ in sources,
License:        GPLv2+
URL:            https://gitlab.freedesktop.org/rncbc/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       shared-mime-info

%description
qpwgraph is a graph manager dedicated to PipeWire, using the Qt C++ framework,
based and pretty much like the same of QjackCtl.

%prep
%autosetup -p0 -n %{name}-v%{version}

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{provider}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%{provider}.desktop
%{_metainfodir}/%{provider}.metainfo.xml
%{_datadir}/mime/packages/%{provider}.xml
%{_mandir}/man1/qpwgraph.1.gz

%changelog
* Thu Jan 12 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.3.9.1
- Update to 0.3.9

* Mon Nov 21 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.8.1
- Update to 0.3.8

* Thu Oct 27 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7.1
- Update to 0.3.7

* Mon Oct 17 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6.1
- Update to 0.3.6

* Wed Sep 21 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.5.1
- Update to 0.3.5

* Fri Jul 29 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.4.1
- Update to 0.3.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2.1
- Update to 0.3.2

* Sat Jun 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Fri May 06 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.6-1
- Update to 0.2.6
- Add BR qt6-qtsvg-devel

* Thu Apr 07 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Thu Mar 24 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Tue Mar 15 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Sun Mar 06 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.2-3
- Add RR shared-mime-info

* Fri Mar 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.2-2
- Use accurate dependency for qt6 packages

* Thu Mar 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Wed Mar 02 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.1-1
- Initial Build
