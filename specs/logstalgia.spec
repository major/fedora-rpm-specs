Summary:       Web server access log visualizer
Name:          logstalgia
Version:       1.1.4
Release:       9%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://code.google.com/p/logstalgia/
Source0:       https://github.com/acaudwell/Logstalgia/releases/download/logstalgia-%{version}/logstalgia-%{version}.tar.gz
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: boost-devel
BuildRequires: ftgl-devel
BuildRequires: gcc-c++
BuildRequires: glew-devel
BuildRequires: glm-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: make
BuildRequires: pcre2-devel
Requires:      gnu-free-mono-fonts
Requires:      gnu-free-serif-fonts

%description
Logstalgia (aka ApachePong) replays or streams a standard website
access log (eg access.log) as a retro arcade game-like simulation.

%prep
%autosetup -p1

%build
%configure \
%ifarch ppc64le
  --with-boost-filesystem=boost_filesystem \
%endif
  --enable-ttf-font-dir=%{_datadir}/fonts/gnu-free/
%make_build

%install
%make_install

%files
%license COPYING
%doc README THANKS
%{_bindir}/logstalgia
%{_datadir}/logstalgia/
%{_mandir}/man1/logstalgia.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.4-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-4
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-2
- Rebuilt for Boost 1.81

* Thu Jan 26 2023 Terje Rosten <terje.rosten@ntnu.no> - 1.1.4-1
- 1.1.4
- C99 patch is now upstream

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Florian Weimer <fweimer@redhat.com> - 1.1.3-4
- Port configure script to C99

* Mon Oct 24 2022 Terje Rosten <terje.rosten@ntnu.no> - 1.1.3-3
- Switch to pcre2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 21 2022 Terje Rosten <terje.rosten@ntnu.no> - 1.1.3-1
- 1.1.3
- boost-filesystem detection don't work on ppc64le

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 1.1.2-11
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.1.2-3
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.1.2-1
- 1.1.2

* Tue Feb 13 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.1.1-1
- 1.1.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.1.0-1
- 1.1.0

* Sun Oct 01 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.0.8-1
- 1.0.8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.0.7-5
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.0.7-3
- Rebuilt for Boost 1.63

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.0.7-2
- Rebuild for glew 2.0.0

* Sun Oct 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.0.7-1
- 1.0.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.6-10
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1.0.6-9
- Rebuild for glew 1.13

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.0.6-8
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.0.6-6
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.6-4
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.0.6-3
- Rebuild for boost 1.57.0

* Sat Oct 18 2014 Terje Røsten <terje.rosten@ntnu.no> - 1.0.6-2
- Fix changelog

* Fri Oct 17 2014 Terje Røsten <terje.rosten@ntnu.no> - 1.0.6-1
- 1.0.6

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.0.5-3
- Rebuild for boost 1.55.0

* Sun Apr 06 2014 Terje Røsten <terje.rosten@ntnu.no> - 1.0.5-2
- Fix upgrade path

* Tue Apr 01 2014 Christopher Meng <rpm@cicku.me> - 1.0.5-1
- Update to 1.0.5, switch to SDL2.
- Unbundle GNU Free Fonts to save package size by using fonts from gnu-free-fonts.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Christopher Meng <rpm@cicku.me> - 1.0.3-7
- Cleanup the spec.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.0.3-5
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.0.3-4
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.0.3-2
- Rebuild against PCRE 8.30

* Wed Feb 01 2012 Terje Røsten <terje.rosten@ntnu.no> - 1.0.3-1
- 1.0.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Terje Røsten <terje.rosten@ntnu.no> - 1.0.2-3
- Rebuilt for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Terje Røsten <terje.rosten@ntnu.no> - 1.0.2-1
- 1.0.2

* Sun Jun 20 2010 Terje Røsten <terje.rosten@ntnu.no> - 1.0.0-1
- 1.0.0

* Wed Feb 10 2010 Terje Røsten <terje.rosten@ntnu.no> - 0.9.8-1
- 0.9.8

* Sat Dec 05 2009 Terje Røsten <terje.rosten@ntnu.no> - 0.9.2-1
- 0.9.2
- All patches now upstream

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 18 2008 Terje Røsten <terje.rosten@ntnu.no> - 0.9.1-2
- Upstream patch refs
- Fix license

* Sun Oct  5 2008 Terje Røsten <terje.rosten@ntnu.no> - 0.9.1-1
- initial build
