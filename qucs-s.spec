%global name_u qucs_s

Summary: Qucs circuit simulator which works with SPICE
Name:    qucs-s
Version: 2.1.0
Release: 2%{?dist}
License: GPLv2+
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
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtsvg-devel
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
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license COPYING
%doc AUTHORS NEWS.md README.md THANKS TODO
%exclude %{_datadir}/%{name}/examples
%exclude %{_datadir}/%{name}/library
%exclude %{_datadir}/%{name}/xspice_cmlib
%{_bindir}/qucs*
%{_bindir}/vcd2qucsdat
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_datadir}/icons/hicolor/*


%files library
%{_datadir}/%{name}/library

%files devel
%{_datadir}/%{name}/xspice_cmlib


%files examples
%{_datadir}/%{name}/examples


%changelog
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
