Summary:       Fast, high-quality sample rate conversion library
Name:          zita-resampler
Version:       1.11.2
Release:       2%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://kokkinizita.linuxaudio.org/linuxaudio/zita-resampler/resampler.html
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/zita-resampler-%{version}.tar.xz
BuildRequires: gcc-c++
BuildRequires: libsndfile-devel
BuildRequires: make

%description
zita-resampler is a C++ library for resampling audio signals. It is
designed to be used within a real-time processing context, to be fast,
and to provide high-quality sample rate conversion.

The library operates on signals represented in single-precision
floating point format. For multichannel operation both the input and
output signals are assumed to be stored as interleaved samples.

The API allows a trade-off between quality and CPU load. For the
latter a range of approximately 1:6 is available. Even at the highest
quality setting zita-resampler will be faster than most similar
libraries, e.g. libsamplerate.

%package  devel
Summary:       Development libraries and headers for %{name}
Requires:      %{name} = %{version}-%{release}

%description devel
This package contains the headers and development libraries for %{name}.

%prep
%setup -q

# To make sure to have the correct Fedora specific flags:
sed -i -e 's|-O[23]||' -e 's|ldconfig||' -e 's|-march=native||' -e '/^CPPFLAGS += -DENABLE_SSE2/d' source/Makefile
sed -i -e 's|-O[23]||' -e 's|-march=native||' apps/Makefile

%build
%set_build_flags

# Enable SSE2 on x86_64
%ifarch x86_64
CPPFLAGS+=" -DENABLE_SSE2"
export CPPFLAGS
%endif

%make_build -C source
# In order to build apps, we need to create the symlink
# Note that this is originally done at "make install" stage
ln -sf libzita-resampler.so.%{version} source/libzita-resampler.so

CXXFLAGS+=" -I../source"
LDFLAGS+=" -L../source"
%make_build -C apps

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} -C source install
%make_install MANDIR=%{_mandir}/man1 PREFIX=%{_prefix} LIBDIR=%{_libdir} -C apps install
chmod 755 %{buildroot}/%{_libdir}/lib%{name}.so.%{version}


%files
%doc AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.1*
%{_bindir}/zresample
%{_bindir}/zretune
%{_mandir}/man1/zresample.1.*
%{_mandir}/man1/zretune.1.*

%files devel
%doc docs/*
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 10 2024 Guido Aulisi <guido.aulisi@inps.it> - 1.11.2-1
- Version 1.11.2

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.0-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.8.0-1
- Version 1.8.0
- Some spec cleanup

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 08 2018 Nils Philippsen <nils@tiptoe.de> - 1.6.2-1
- version 1.6.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.3.0-13
- Use Fedora link flags
- Add BR: gcc-c++
- Some cleanup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 27 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.3.0-1
- New upstream release

* Fri Oct 26 2012 Dan Horák <dan[at]danny.cz> - 1.1.0-3
- can't use -march=native in build system

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.1.0-1
- Update to 1.1.0
- Update URL, bring SPEC file up to date to current version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 04 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.1.1-3
- Fix header includes

* Sat Apr 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.1.1-2
- Fix libdir on non-*x86* systems

* Sat Apr 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.1.1-1
- Update to 0.1.1
- Prepare package for Fedora (specfile from PlanetCCRMA)

* Wed Oct 29 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.0-1
- initial release
