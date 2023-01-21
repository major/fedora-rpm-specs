Name:		hidviz
Version:	0.1.5
Release:	20%{?dist}
Summary:	A tool for in-depth analysis of USB HID devices communication
License:	GPLv3+
URL:		https://github.com/ondrejbudai/hidviz
Source0:	https://hidviz.org/releases/%{name}-%{version}.tar.gz
Source1:	hidviz.desktop
Requires:	hicolor-icon-theme
BuildRequires:	gcc-c++, cmake, qt5-qtbase-devel, protobuf-devel, libusbx-devel
BuildRequires:	asio-devel, desktop-file-utils, ImageMagick
# https://github.com/ondrejbudai/hidviz/issues/27
Patch0:		hidviz-0.1.5-build-fix.patch
Patch1:         hidviz-gcc11.patch

%description
Hidviz is a GUI application for in-depth analysis of USB HID class devices.

%prep
%setup -q
%patch0 -p1 -b .build-fix
%patch1 -p1 -b .gcc11

%build
%cmake
%cmake_build

%install
%cmake_install

# icon not yet available, temporal hack to make and install one :)
convert hidviz/images/usb.png -resize 128x128 -background transparent \
  -compose copy -gravity center -extent 128x128 hidviz.png
install -Dpm 0644 hidviz.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/hidviz.png

# desktop file
mkdir -p  %{buildroot}%{_datadir}/applications
desktop-file-install --add-category="Utility" \
  --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}/libhid*.so*
%{_libexecdir}/libhidx_server_daemon
%{_datadir}/icons/hicolor/128x128/apps/hidviz.png
%{_datadir}/applications/hidviz.desktop

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 0.1.5-17
- Rebuilt for protobuf 3.19.0

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 0.1.5-16
- Rebuilt for protobuf 3.18.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 0.1.5-14
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 08:46:21 CET 2021 Adrian Reber <adrian@lisas.de> - 0.1.5-12
- Rebuilt for protobuf 3.14

* Fri Dec 04 2020 Jeff Law <law@redhat.com> - 0.1.5-11
- Fix missing #include for gcc-11

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 0.1.5-10
- Rebuilt for protobuf 3.13

* Wed Aug  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.5-9
- New version
  Resolves: rhbz#1863849

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Adrian Reber <adrian@lisas.de> - 0.1.5-6
- Rebuilt for protobuf 3.12

* Mon Jun 22 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.5-5
- Fixed FTBFS in f33

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 0.1.5-4
- Rebuilt for protobuf 3.12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 0.1.5-2
- Rebuild for protobuf 3.11

* Mon Dec  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.5-1
- New version
- Switched to HTTPS
- Dropped system-asio, gcc-7-compile-fix, qt-5.11-compile-fix,
  gcc-10-compile-fix patches (all upstreamed)

* Wed Sep 25 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-17
- Fixed compilation with gcc-10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-14
- Rebuild for protobuf 3.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-12
- Fixed build with qt-5.11

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-10
- Remove obsolete scriptlets

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1.4-9
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-8
- Rebuild for protobuf 3.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-5
- Rebuilt for new protobuf

* Wed Jun 14 2017 Orion Poplawski <orion@cora.nwra.com> - 0.1.4-4
- Rebuild for protobuf 3.3.1

* Fri May 19 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-3
- Added explicit requirement on hicolor-icon-theme
  Related: rhbz#1448557

* Wed May 17 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-2
- Minor tweaks according to review
  Related: rhbz#1448557

* Mon May 15 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.4-1
- New version

* Fri May  5 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.3-1
- New version
- Used system asio library

* Fri May  5 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.2-1
- New version

* Fri May  5 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-1
- New version

* Thu May  4 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1-1
- Initial release
