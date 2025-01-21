Summary:       Convolution engine library
Name:          zita-convolver
Version:       4.0.3
Release:       16%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: fftw-devel
BuildRequires: gcc-c++

%description
%{name} is a fast, partitioned convolution engine library.

%package  devel
Summary:       Fast, partitioned convolution engine library
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      fftw-devel

%description devel
%{name} is a fast, partitioned convolution engine library. This package
contains libraries and header files for developing applications that use
%{name}.

%prep
%setup -q

# Preserve timestamps
sed -i 's|install |install -p |' source/Makefile

# No need to call ldconfig during packaging
sed -i '\|ldconfig|d' source/Makefile

sed -i '\|^CXXFLAGS += -march=native|d' source/Makefile

%build
%set_build_flags
%make_build -C source PREFIX=%{_prefix}

%install
%make_install -C source PREFIX=%{_prefix} LIBDIR=%{_libdir}

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/lib%{name}.so.4*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0.3-15
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 27 2021 Guido Aulisi <guido.aulisi@gmail.com> - 4.0.3-7
- Add dependency on fftw-devel to devel package (#1953349)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Guido Aulisi <guido.aulisi@gmail.com> - 4.0.3-2
- Use the correct libdir

* Mon Jun 10 2019 Guido Aulisi <guido.aulisi@gmail.com> - 4.0.3-1
- Update to 4.0.3
- Some spec cleanup

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 3.1.0-15
- Use Fedora link flags
- Add BR: gcc-c++
- Some cleanup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Brendan Jones <brendan.jones.it@gmail.com> - 3.1.0-1
- updated to 3.1.0
- updated URL

* Mon Oct 31 2011 Brendan Jones <brendan.jones.it@gmail.com> - 3.0.3-2
- Relicensed to GPLv3+

* Wed Oct 26 2011 Brendan Jones <brendan.jones.it@gmail.com> - 3.0.3-1
- updated to 3.0.3

* Wed Oct 19 2011 Brendan Jones <brendan.jones.it@gmail.com> - 3.0.2-1
- updated to 3.0.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 17 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.0.0-2
- Fix compilation flags on i686, causing us SELinux denials. RHBZ#615650

* Wed Dec 16 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.0.0-1
- updated to 2.0.0

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.0-2
- prepare package for Fedora submission (SPEC file from PlanetCCRMA)

* Sat Mar 21 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0-1
- updated to 1.0.0

* Wed Oct 29 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.0-1
- initial release
