Name:           libopkele
Version:        2.0.4
Release:        41%{?dist}
Summary:        C++ implementation of the OpenID decentralized identity system
License:        MIT
URL:            http://kin.klever.net/libopkele/
Source0:        http://kin.klever.net/dist/%{name}-%{version}.tar.bz2
# Patch from debian bug http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=667253
Patch0:         fix-ftbfs-gcc4.7.diff
# Patch from upstream already applied to git.
Patch1:         libopkele-2.0.4-remove-iterator.patch
Patch2:		0001-Fix-DH-parameter-access-for-OpenSSL-1.1.0.patch

BuildRequires:  boost-devel, openssl-devel, libxslt, libcurl-devel, expat-devel
BuildRequires:  tidy-devel, sqlite-devel, libuuid-devel, gcc-c++
BuildRequires: make

%description
libopkele is a C++ implementation of the OpenID decentralized identity
system. It provides OpenID protocol handling, leaving authentication
and user interaction to the implementor.

%package devel
Summary:        Header files and libraries for %{name} development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libcurl-devel

%description devel
The %{name}-devel package contains the header files and libraries needed
to develop programs that use the %{name} OpenID library.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/*.{a,la}

%check
./test/test

%files
%doc AUTHORS COPYING NEWS
%{_libdir}/libopkele.so.*

%files devel
%{_includedir}/opkele
%{_libdir}/libopkele.so
%{_libdir}/pkgconfig/libopkele.pc

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.0.4-33
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Kevin Fenzi <kevin@scrye.com> - 2.0.4-26
- Fix FTBFS by adding BuildRequires: gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.0.4-21
- Rebuilt for Boost 1.64

* Sun Feb 19 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.4-20
- Add patch for OpenSSL 1.1.0 support

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.0.4-17
- Rebuilt for Boost 1.60

* Thu Nov 19 2015 Kevin Fenzi <kevin@scrye.com> - 2.0.4-16
- Rebuild for new libtidy

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.0.4-15
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.0.4-13
- rebuild for Boost 1.58

* Sun Jul 05 2015 Kevin Fenzi <kevin@scrye.com> 2.0.4-12
- Add patch for gcc issues to fix FTBFS. Fixes bug 1239647

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.0.4-10
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.0.4-7
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.0.4-5
- Rebuild for boost 1.54.0

* Mon May 20 2013 Kevin Fenzi <kevin@scrye.com> 2.0.4-4
- Just own %%{_includedir}/opkele

* Sun Jun 03 2012 Kevin Fenzi <kevin@scrye.com> - 2.0.4-3
- Fixed devel subpackage requires. 
- Dropped leading A from summary. 
- Added BuildRequires: libuuid-devel
- Added tests in %%check 

* Fri May 25 2012 Kevin Fenzi <kevin@scrye.com> - 2.0.4-2
- Add AUTHORS file as a doc, per review at bug 691597
- Add patch for gcc 4.7 issues. 

* Mon Mar 28 2011 Bryan O'Sullivan <bos@serpentine.com> - 2.0.4-1
- Initial packaging for Fedora
