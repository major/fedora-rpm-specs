# Per upstream recommendations.
# https://www.cryptopp.com/wiki/Link_Time_Optimization
%define _lto_cflags %{nil}

# Switch toolchain to clang to workaround gcc-12 issue
# See also https://github.com/weidai11/cryptopp/issues/1141
%global toolchain clang

Name:           cryptopp
Version:        8.8.0
Release:        2%{?dist}
Summary:        C++ class library of cryptographic schemes
License:        Boost
URL:            http://www.cryptopp.com/
Source0:        http://www.cryptopp.com/cryptopp880.zip
Source1:        cryptopp.pc
#Patch0:         https://github.com/weidai11/cryptopp/commit/94aba0105efa.patch

BuildRequires:  doxygen
BuildRequires:  clang
BuildRequires: make

# Obsoletes pycryptopp to avoid breaking upgrades
Obsoletes:  pycryptopp < 0.7
Provides:   pycryptopp = 0.7


%description
Crypto++ Library is a free C++ class library of cryptographic schemes.
See http://www.cryptopp.com/ for a list of supported algorithms.

One purpose of Crypto++ is to act as a repository of public domain
(not copyrighted) source code. Although the library is copyrighted as a
compilation, the individual files in it are in the public domain.

%package devel
Summary:        Header files and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Crypto++ Library is a free C++ class library of cryptographic schemes.

This package contains the header files and development documentation
for %{name}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Crypto++ Library is a free C++ class library of cryptographic schemes.

This package contains documentation for %{name}.

%package progs
Summary:        Programs for manipulating %{name} routines
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description progs
Crypto++ Library is a free C++ class library of cryptographic schemes.

This package contains programs for manipulating %{name} routines.

%prep
%autosetup -c -p1
perl -pi -e 's/\r$//g' License.txt Readme.txt


%build
%{set_build_flags}
%make_build -f GNUmakefile \
  ZOPT='' \
  shared cryptest.exe

doxygen

%install
%make_install INSTALL="install -p -c " PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

# Install the pkg-config file
install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/pkgconfig/cryptopp.pc
# Fill in the variables
sed -i "s|@PREFIX@|%{_prefix}|g" $RPM_BUILD_ROOT%{_libdir}/pkgconfig/cryptopp.pc
sed -i "s|@LIBDIR@|%{_libdir}|g" $RPM_BUILD_ROOT%{_libdir}/pkgconfig/cryptopp.pc
sed -i "s|@VERSION@|%{version}}|g" $RPM_BUILD_ROOT%{_libdir}/pkgconfig/cryptopp.pc

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/TestVectors
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/TestData
install -m644 TestVectors/* $RPM_BUILD_ROOT%{_datadir}/%{name}/TestVectors
install -m644 TestData/* $RPM_BUILD_ROOT%{_datadir}/%{name}/TestData

# Rename cryptest
mv $RPM_BUILD_ROOT%{_bindir}/cryptest.exe \
   $RPM_BUILD_ROOT%{_bindir}/cryptest

# Remove static lib
rm  %{buildroot}%{_libdir}/libcryptopp.a

%check
./cryptest.exe v

%ldconfig_scriptlets

%files
%{_libdir}/libcryptopp.so.8*
%doc Readme.txt
%license License.txt

%files devel
%{_includedir}/cryptopp
%{_libdir}/libcryptopp.so
%{_libdir}/pkgconfig/cryptopp.pc

%files doc
%license License.txt
%doc html-docs/*

%files progs
%{_bindir}/cryptest
%{_datadir}/%{name}

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Vasiliy N. Glazov <vascom2@gmail.com> 8.8.0-1
- Update to 8.8.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Nicolas Chauvet <kwizart@gmail.com> - 8.7.0-1
- Update to 8.7.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 26 2021 Vasiliy N. Glazov <vascom2@gmail.com> 8.6.0-1
- Update to 8.6.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Vasiliy N. Glazov <vascom2@gmail.com> 8.4.0-1
- Update to 8.4.0

* Wed Dec 30 2020 Vasiliy N. Glazov <vascom2@gmail.com> 8.3.0-1
- Update to 8.3.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Vasiliy N. Glazov <vascom2@gmail.com> 8.2.0-1
- Update to 8.2.0

* Thu Feb 28 2019 Nicolas Chauvet <kwizart@gmail.com> - 8.1.0-2
- Improve how to set our flags
- Remove ppc fixup
- Backport patch to fix build

* Tue Feb 26 2019 Nicolas Chauvet <kwizart@gmail.com> - 8.1.0-1
- Update to 8.1.0

* Thu Feb 14 2019 Nicolas Chauvet <kwizart@gmail.com> - 8.0.0-1
- Update to 8.0.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 7.0.0-2
- Obsoletes pycryptopp

* Sun Aug 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 7.0.0-1
- Update to 7.0.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 6.1.0-2
- Disable ppc64le war - fixed upstream

* Thu Feb 22 2018 Nicolas Chauvet <kwizart@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Mon Feb 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 6.0.0-1
- Update to 6.0.0

* Mon Feb 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 5.6.5-1
- Update to 5.6.5 (vanilla)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 01 2017 Petr Šabata <contyk@redhat.com> - 5.6.3-8
- Hitting rhbz#1404466 again; increasing the number of retries to 1024
- There appears to be a better long-term fix available at GH
  weidai11/cryptopp but that approach hasn't been merged upstream yet

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Merlin Mathesius <mmathesi@redhat.com> - 5.6.3-6
- Include upstream RDSEED patch to correct FTBFS (BZ#1404466).

* Tue Jul 26 2016 Morten Stevens <mstevens@fedoraproject.org> - 5.6.3-5
- Rebuilt f25/f26 dist tag

* Tue Jul 26 2016 Morten Stevens <mstevens@fedoraproject.org> - 5.6.3-4
- Rebuilt for c++ ABI breakage (#1360441)

* Mon Apr 11 2016 Morten Stevens <mstevens@fedoraproject.org> - 5.6.3-3
- CVE-2016-3995

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Morten Stevens <mstevens@fedoraproject.org> - 5.6.3-1
- Update to 5.6.3

* Sun Nov 08 2015 Morten Stevens <mstevens@fedoraproject.org> - 5.6.2-10
- Remove libdir from pkg-config file #1161960

* Mon Jun 29 2015 Morten Stevens <mstevens@fedoraproject.org> - 5.6.2-9
- CVE-2015-2141

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Morten Stevens  <mstevens@fedoraproject.org> - 5.6.2-7
- Rebuilt for yet another C++ ABI break

* Thu Feb 19 2015 Morten Stevens <mstevens@fedoraproject.org> - 5.6.2-6
- GCC 5 rebuilt

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr  4 2013 Alexey Kurov <nucleo@fedoraproject.org> - 5.6.2-2
- cryptopp.pc cleanup

* Wed Apr  3 2013 Alexey Kurov <nucleo@fedoraproject.org> - 5.6.2-1
- Crypto++ 5.6.2
- License: Boost

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.1-7
- Rebuilt for c++ ABI breakage

* Thu Jan  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 5.6.1-6
- fix build with gcc-4.7.0

* Mon Oct 17 2011 Alexey Kurov <nucleo@fedoraproject.org> - 5.6.1-5
- remove includedir in cryptopp.pc (rhbz#732208)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Alexey Kurov <nucleo@fedoraproject.org> - 5.6.1-3
- patch config.h for enable SSE2 only on x86_64

* Thu Oct 21 2010 Alexey Kurov <nucleo@fedoraproject.org> - 5.6.1-2
- add -DCRYPTOPP_DISABLE_SSE2 to CXXFLAGS instead of config.h for non-x86_64 (rhbz#645169)
- install TestVectors and TestData in cryptopp-progs
- patch cryptest for using data files in /usr/share/cryptopp
- build cryptestcwd for build time test only
- fix check section

* Wed Sep  1 2010 Alexey Kurov <nucleo@fedoraproject.org> - 5.6.1-1
- Crypto++ 5.6.1
- fixed pkgconfig file installation
- build cryptopp-doc as noarch subpkg

* Thu Nov 26 2009 Alexey Kurov <nucleo@fedoraproject.org> - 5.6.1-0.1.svn479
- svn r479. MARS placed in the public domain by Wei Dai
- Fixes rhbz#539227

* Fri Oct 30 2009 Rahul Sundaram <sundaram@fedoraproject.org> 5.6.0-5
- Fix source

* Wed Oct 28 2009 Rahul Sundaram <sundaram@fedoraproject.org> 5.6.0-4
- Add pkgconfig file. Fixes rhbz#512761

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun  9 2009 Dan Horak <dan[at]dannu.cz> 5.6.0-2
- add support for s390/s390x

* Sun Mar 15 2009 Aurelien Bompard <abompard@fedoraproject.org> 5.6.0-1
- version 5.6.0
- rediff patches

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 30 2008 Aurelien Bompard <abompard@fedoraproject.org> 5.5.2-3
- purge source archive from patented code
- use SSE2 on x86_64
- preserve timestamps on install

* Mon Sep 22 2008 Aurelien Bompard <abompard@fedoraproject.org> 5.5.2-2
- rediff gcc 4.3 patch

* Wed Aug 27 2008 Aurelien Bompard <abompard@fedoraproject.org> 5.5.2-1
- adapt to fedora, from Mandriva
