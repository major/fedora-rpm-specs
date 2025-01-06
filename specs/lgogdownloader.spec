Name:		lgogdownloader
Version:	3.16
Release:	1%{?dist}
Summary:	GOG.com download client

License:	WTFPL
URL:		https://github.com/Sude-/lgogdownloader
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	help2man
BuildRequires:	binutils
BuildRequires:	pkgconfig(tidy)
BuildRequires:	pkgconfig(htmlcxx)
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(tinyxml2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	boost-devel
BuildRequires:	rhash-devel
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:	pkgconfig(Qt5WebEngine)
%endif

%description
LGOGDownloader is an unofficial GOG.com downloader for Linux users. It uses the
same API as the official GOG Galaxy.

%prep
%autosetup

%build
%ifarch %{qt5_qtwebengine_arches}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DUSE_QT_GUI=ON
%else
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DUSE_QT_GUI=OFF
%endif
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_bindir}/lgogdownloader
%{_mandir}/man1/lgogdownloader.1.*

%changelog
* Sat Jan 4 2025 Benjamin Lowry <ben@ben.gmbh> - 3.16-1
- lgogdownloader 3.16

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 3.15-2
- rebuild for tinyxml2

* Tue Oct 22 2024 Benjamin Lowry <ben@ben.gmbh> - 3.15-1
- lgogdownloader 3.15

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 23 2024 Orion Poplawski <orion@nwra.com> - 3.12-2
- Rebuild for rhash 1.4.4 soname bump

* Tue Mar 19 2024 Benjamin Lowry <ben@ben.gmbh> - 3.12-1
- lgogdownloader 3.12

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 3.11-3
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 2 2023 Benjamin Lowry <ben@ben.gmbh> - 3.11-1
- lgogdownloader 3.11

* Sat Mar 18 2023 Benjamin Lowry <ben@ben.gmh> - 3.10-1
- lgogdownloader 3.10

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 3.9-4
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Rich Mattes <richmattes@gmail.com> - 3.9-2
- Rebuild for tinyxml2-9.0.0

* Tue Sep 20 2022 Benjamin Lowry <ben@ben.gmbh> - 3.9-1
- lgogdownloader 3.9

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 3.8-4
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 3.8-2
- Rebuild (jsoncpp)

* Mon Sep 27 2021 Benjamin Lowry <ben@ben.gmbh> - 3.8-1
- lgogdownloader 3.8

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 3.7-9
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.7-6
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Benjamin Lowry <ben@ben.gmbh> - 3.7-5
- Update to new cmake macros, fix build error

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Benjamin Lowry <ben@ben.gmbh> 3.7-2
- Change source0 URL
- Replace /usr with _prefix macro
- Glob extension of manpage file
* Thu Jun 18 2020 Benjamin Lowry <ben@ben.gmbh> 3.7-1
- Initial Fedora package
