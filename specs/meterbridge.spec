Name:          meterbridge
Summary:       Meter Bridge for JACK
Version:       0.9.2
Release:       36%{?dist}
URL:           http://plugin.org.uk/meterbridge/
Source0:       http://plugin.org.uk/%{name}/%{name}-%{version}.tar.gz
# Patch sent upstream via email (there is no bugtracker)
Patch0:        meterbridge-gcc10.patch
License:       GPL-1.0-or-later

BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: SDL_image-devel

%description
%{name} is a software meter bridge for the UNIX based JACK audio system.
It supports a number of different types of meter, rendered using the SDL
library and user-editable pixmaps.

%prep
%setup -q
%patch -P0 -p1 -b .gcc10

%build
# FIXME: The Makefile.ams don't honor CFLAGS correctly
# Resort to overriding CPPFLAGS.
# FIXME: Package suffers from c11/inline issues
# Workaround by appending -std=gnu89 to CPPFLAGS
# Proper fix would be to fix the source-code
export CPPFLAGS="%{optflags} -std=gnu89"
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.2-34
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 08 2020 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.2-24
- gcc 10 fixes

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.2-21
- run autoreconf before build

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 18 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.9.2-13
- Append -std=gnu89 to CPPFLAGS (Fix F23FTBFS, RHBZ#1239678).
- Modernise spec.
- Add %%license.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May  6 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.2-3
- prepare package for Fedora submission (SPEC file from PlanetCCRMA)

* Tue Feb  5 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- rebuilt on CentOS 5

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.2-2
- spec file tweaks, build for fc6

* Sat May 13 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- same fix needed for fc5, should make a patch instead

* Wed Jul 13 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- fix build on fc4/gcc4

* Thu Dec 30 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- spec file cleanup

* Mon May 10 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added buildrequires

* Sat Nov  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.2-1
- added release tags, clean up spec file

* Tue Jun 10 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.2-1
- updated to version 0.9.2

* Sun Dec 15 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.9.0-1
- 0.9.0, add patch to compile with jack 0.41

* Sat Oct 26 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.6-1
- 0.0.6, added docs

* Fri Oct 11 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- Initial build.
