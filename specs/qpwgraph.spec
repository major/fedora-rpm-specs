%global provider org.rncbc.qpwgraph

Name:           qpwgraph
Version:        0.8.1
Release:        2%{?dist}
Summary:        PipeWire Graph Qt GUI Interface
# Main license is GPL-2.0-or-later in sources,
License:        GPL-2.0-or-later
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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 29 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Fri Nov 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Tue Oct 29 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.7.9-1
- Update to 0.7.9

* Wed Sep 25 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.7.8-1
- Update to 0.7.8

* Fri Aug 23 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.7.7-1
- Update to 0.7.7

* Fri Jul 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.7.5-1
- Update to 0.7.5

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.4-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4

* Sun Jun 23 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3

* Wed May 22 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Thu May 02 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Mon Apr 22 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Sat Feb 17 2024 Jan Grulich <jgrulich@redhat.com> - 0.6.2-2
- Rebuild (qt6)

* Fri Feb 02 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.2.1
- Update to 0.6.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 28 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1.1
- Update to 0.6.1

* Mon Sep 25 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.5.3.1
- Update to 0.5.3

* Tue Aug 22 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.5.2.1
- Update to 0.5.2

* Wed Jul 26 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.5.1.1
- Update to 0.5.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 06 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1.1
- Update to 0.4.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
