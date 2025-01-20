Name:       rtmidi
Version:    5.0.0
Release:    6%{?dist}
Summary:    Library for realtime MIDI input/output (ALSA support)
License:    MIT
URL:        https://www.music.mcgill.ca/~gary/rtmidi/index.html
Source0:    https://www.music.mcgill.ca/~gary/rtmidi/release/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  alsa-lib-devel, pkgconfig(jack)
BuildRequires:  autoconf, automake, libtool, /usr/bin/dos2unix
BuildRequires:  doxygen
BuildRequires:  gcc-c++
Obsoletes:  %{name}-jack < 2.0.0

%description
RtMidi is a set of C++ classes (RtMidiIn and RtMidiOut) that provides a common 
API (Application Programming Interface) for realtime MIDI input/output across 
Linux (ALSA & Jack), Macintosh OS X, Windows (Multimedia Library), and SGI 
operating systems. RtMidi significantly simplifies the process of interacting 
with computer MIDI hardware and software. It was designed with the following 
goals:
* object oriented C++ design
* simple, common API across all supported platforms
* only two header files and one source file for easy inclusion in programming 
  projects
* MIDI device enumeration

%package devel
Summary:    Development headers and libraries for rtmidi
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   alsa-lib-devel, pkgconfig(jack)

%description devel
Development headers and libraries for rtmidi.

%prep
%setup -q

sed -i.orig -e 's/\/lib/\/%{_lib}/' Makefile.in rtmidi.pc.in
# fix end of line
dos2unix doc/release.txt doc/doxygen/tutorial.txt

%build
%configure --docdir=%{_docdir}/%{name}-devel --with-jack --with-alsa
make %{?_smp_mflags} AM_DEFAULT_VERBOSITY=1

# Get rid of the -L/usr/lib in the output of this convenience script
sed -i -E 's/-L[^ "]+//' %{name}-config

%install
make DESTDIR=%{buildroot} install

install --verbose -D -t %{buildroot}%{_bindir} %{name}-config

rm %{buildroot}%{_libdir}/lib%{name}.{a,la}

%ldconfig_scriptlets

%files
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/html
%{_bindir}/%{name}-config
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 04 2023 Joonas Sarajärvi <muep@iki.fi> - 5.0.0-1
- New version
- C++11 syntax used in headers

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Joonas Sarajärvi <muep@iki.fi> - 4.0.0-1
- Update to RtMidi 4.0.0
- new C API wrapper
- new APIs

* Mon Sep 27 2021 Joonas Sarajärvi <muep@iki.fi> - 3.0.0-12
- Require pkgconfig(jack)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Than Ngo <than@redhat.com> - 3.0.0-9
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Joonas Sarajärvi <muep@iki.fi> - 3.0.0-1
- New upstream release, version 3.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Joonas Sarajärvi <muep@iki.fi> 2.1.0-6
- Rebuild to make the package available after unretirement

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Robin Lee <cheeselee@fedoraproject.org> - 2.1.0-3
- Obsoletes rtmidi-jack

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Oct 23 2014 Robin Lee <cheeselee@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug  7 2013 Robin Lee <cheeselee@fedoraproject.org> - 1.0.15-7
- Use unversioned docdir (BZ#993937)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Karsten Hopp <karsten@redhat.com> 1.0.15-2.1
- use config.sub, config.guess from rpm, i.e. ppc64 was missing in the included files

* Sun Oct  9 2011 Robin Lee <cheeselee@fedoraproject.org> - 1.0.15-2
- Include an enhanced patch
- Don't include the test apps
- Include the documents in the devel package
- Untabified

* Thu Sep 1 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.15-1
- initial package
