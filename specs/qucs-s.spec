%global name_u qucs_s

Summary: Qucs circuit simulator which works with SPICE
Name:    qucs-s
Version: 24.4.1
Release: 2%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://ra3xdh.github.io/

Source0: https://github.com/ra3xdh/qucs_s/archive/%{version}/%{name_u}-%{version}.tar.gz

# Desktop file categories must terminate with a semicolon, bug #1424234
Patch0:  qucs-s-0.0.19-fix-desktop-file.patch

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: bison
BuildRequires: desktop-file-utils
# for "appstream-util validate-relax"
BuildRequires: libappstream-glib
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtcharts-devel
Requires: ngspice
Recommends: %{name}-library

%description
Qucs-S is a spin-off of the Qucs cross-platform circuit simulator. "S" letter
indicates SPICE. The purpose of the Qucs-S subproject is to use free SPICE
circuit simulation kernels with the Qucs GUI. It merges the power of SPICE
and the simplicity of the Qucs GUI.


%package library
Summary: Qucs-S library
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description library
Qucs-S library.


%package devel
Summary: Qucs-S development files
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
Qucs-S development files.


%package examples
Summary: Qucs-S examples
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description examples
Qucs-S examples.


%prep
%autosetup -n %{name_u}-%{version} -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.ra3xdh.qucs_s.metainfo.xml


%files
%license COPYING
%doc AUTHORS NEWS.md README.md THANKS TODO
%exclude %{_datadir}/%{name}/examples
%exclude %{_datadir}/%{name}/library
%exclude %{_datadir}/%{name}/xspice_cmlib
%{_bindir}/qucs*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_datadir}/icons/hicolor/*
%{_metainfodir}/io.github.ra3xdh.qucs_s.metainfo.xml


%files library
%{_datadir}/%{name}/library

%files devel
%{_datadir}/%{name}/xspice_cmlib


%files examples
%{_datadir}/%{name}/examples


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 16 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 24.4.1-1
- New version
  Resolves: rhbz#2326331

* Tue Nov  5 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 24.4.0-1
- New version
  Resolves: rhbz#2323122

* Wed Sep 25 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 24.3.2-1
- New version
  Resolves: rhbz#2310704

* Fri Jul 26 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 24.3.0-1
- New version
  Resolves: rhbz#2299767

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 24.2.1-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr  4 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 24.2.1-1
- New version
  Resolves: rhbz#2272334

* Thu Mar 28 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 24.2.0-1
- New version
  Resolves: rhbz#2271697

* Mon Feb 19 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 24.1.0-1
- New version
  Resolves: rhbz#2264647

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 31 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.0-1
- New version
  Resolves: rhbz#2246531

* Fri Aug 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.0-1
- New version
  Resolves: rhbz#2232874

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-1
- New version
  Resolves: rhbz#2213381

* Wed Apr 26 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.2-1
- New version
  Resolves: rhbz#2189343

* Thu Feb  9 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.1-1
- New version
  Resolves: rhbz#2167132

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov  1 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.0-1
- New version
  Resolves: rhbz#2138647

* Thu Jul 21 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.24-4
- Fixed according to the review
  Related: rhbz#2106445

* Tue Jul 19 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.24-3
- Fixed according to the review
  Related: rhbz#2106445

* Thu Jul 14 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.24-2
- Fixed according to the review

* Tue Jul 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.24-1
- New version

* Tue Aug 18 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.22-1
- Initial release
