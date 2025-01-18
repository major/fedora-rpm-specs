Name:       eureka
Version:    2.0.2
Release:    2%{?dist}
Summary:    A cross-platform map editor for the classic DOOM games

License:    GPL-2.0-or-later
URL:        http://eureka-editor.sourceforge.net
Source0:    https://github.com/ioan-chera/eureka-editor/archive/refs/tags/%{name}-%{version}/%{name}-%{version}.tar.gz

# Eureka's CMakeLists separate the code into a few static libraries,
# with some of them getting additional compiler flags. For whatever reason
# this causes those libraries to get their CFLAGS quoted, resulting in
# build failures because "-O2 -whatever" is not a valid compiler flag.
Patch0:     0000-quoted-cflags.patch

# Remove bits of code covered under the CC0 license.
Patch1:     0001-no-cc0-code.patch

BuildRequires:  gcc-c++
BuildRequires:  fltk-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libGL-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-fluid
BuildRequires:  make
BuildRequires:  ImageMagick
BuildRequires:  xdg-utils

%description
Eureka is a cross-platform map editor for the classic DOOM games.

It started when the ported the Yadex editor to a proper GUI toolkit, namely
FLTK, and implemented a system for multi-level Undo / Redo. These and other
features have required rewriting large potions of the existing code, and adding
lots of new code too. Eureka is now an independent program with its own
work-flow and its own quirks.


%prep
%autosetup -p1 -n eureka-editor-%{name}-%{version}

# Remove CC0-licensed code
rm -rf src/tl/


%build
# The test suite expects to download gtest sources from the internet,
# and simply disabling that results in linking failures.
%cmake -DENABLE_UNIT_TESTS=OFF
%cmake_build


%install
%cmake_install

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
magick convert misc/eureka.ico %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/eureka.png

install -m 755 -d %{buildroot}/%{_mandir}/man6/
install -m 644 -p misc/eureka.6 %{buildroot}%{_mandir}/man6/%{name}.6

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p misc/eureka.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license GPL.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/128x128/apps/eureka.png
%{_datadir}/applications/*.desktop
%{_mandir}/man6/%{name}.6*
%doc AUTHORS.md README.txt TODO.txt
%doc changelogs/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 22 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.2-1
- Update to v2.0.2

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.27b-7
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.27b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.27b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.27b-1
- Update to v1.27b
- Include man page in the package
- Clean up the spec file

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.27-1
- 1.27

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.24-1
- 1.24

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.21-1
- Bump to latest version (1.21)
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Rex Dieter <rdieter@fedoraproject.org> 1.00-5
- rebuild (fltk)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.00-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Sep 8 2013 Jay Greguske <brolem@gmail.com> 1.00-3
- add changes from Ralf Corsepius during review

* Thu Sep 5 2013 Jay Greguske <brolem@gmail.com> 1.00-2
- incorporate a few suggestions from Christopher Meng

* Mon Aug 26 2013 Jay Greguske <brolem@gmail.com> 1.00-1
- Initial import from upstream 1.00 release
