Summary:       Real-time Convolution Engine
Name:          jconvolver
Version:       1.0.3
Release:       15%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://kokkinizita.linuxaudio.org/linuxaudio/index.html
Source0:       https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Demo reverbs
# Don't bundle until license is cleared up
#Source1:      https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-reverbs.tar.bz2

Obsoletes:     jace <= 0.2.0
Provides:      jace = %{version}-%{release}
Obsoletes:     jconv <= 0.8.1
Provides:      jconv = %{version}-%{release}

BuildRequires: clthreads-devel >= 2.4.0
BuildRequires: fftw-devel
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
BuildRequires: zita-convolver-devel >= 4.0.0
BuildRequires: make

Requires: zita-convolver >= 4.0.0

%description
Jconvolver is a real-time convolution engine. It can execute up to a 64 by 64
convolution matrix (i.e. 4096 simultaneous convolutions) as long as your CPU(s)
can handle the load. It is designed to be efficient also for sparse (e.g.
diagonal) matrices. Unused matrix elements do not take any CPY time.

%prep
#setup -q -a 1
%setup -q

# fix paths of configuration files
find config-files/ -name \*.conf \
  -exec sed -i -e "s|/audio/reverbs|%{_datadir}/%{name}/reverbs|g" {} \; \
  -exec sed -i -e "s|^#/cd |/cd |g" {} \;

# Force Fedora's flags
sed -i -e '/^CXXFLAGS += -march=native/d' source/Makefile

# Preserve timestamps
sed -i 's|install |install -p |' source/Makefile

%build
%set_build_flags
%make_build PREFIX=%{_prefix} -C source

%install
%make_install PREFIX=%{_prefix} -C source

# install configuration files and demo reverbs
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a config-files/* %{buildroot}%{_datadir}/%{name}
#cp -a reverbs/ %%{buildroot}%%{_datadir}/%%{name}/

%files
%doc AUTHORS README*
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.3-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Guido Aulisi <guido.aulisi@gmail.com> - 1.0.3-1
- Update to 1.0.3
- Some spec cleanup

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.2-15
- Use Fedora link flags
- Add BR: gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.2-8
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 19 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.1-1
- Updated to version 0.9.2

* Wed Oct 19 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.9.1-1
- Updated to version 0.9.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 02 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.8.7-1
- New version (2 more attempts & still no response from upstream about the reverbs)

* Fri Mar 12 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.8.6-1
- New version (still no response from upstream about the reverbs)

* Tue Dec 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.8.4-2
- Don't bundle the reverbs until we hear from the author about the license

* Wed Dec 16 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.8.4-1
- update version to 0.8.4
- software name changed from jconv to jconvolver
- drop libsndfile patch. not needed anymore

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.8.1-1
- update version to 0.8.1
- prepare package for Fedora submission (SPEC file from PlanetCCRMA)

* Sat Mar 21 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.0-2
- fix typo in uhjenc.conf

* Sat Mar 21 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.8.0-1
- updated to 0.8.0, include new extended demo reverb files
- move configuration and examples to /usr/share/jconv/

* Wed Oct 29 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.0-1
- package renamed to jconv from jace, now uses the zita-convolver library
- upgrade to jconv 0.2.0

* Wed Sep  5 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.0-1
- update to 0.2.0
- add springreverb.wav

* Thu Apr 19 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.0-1
- update to 0.1.0

* Sun Apr  1 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.4-2
- update to 0.0.4
- include lucia.wav example impulse response
- tweak demo configuration files to point to the doc directory

* Tue Dec 12 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.3-2
- build on fc6

* Sat May 13 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.8-1
- initial build
