Name:           libzrtpcpp
Version:        4.6.6
Release:        20%{?dist}
Summary:        ZRTP support library for the GNU ccRTP stack

License:        GPL-3.0-or-later
URL:            https://github.com/wernerd/ZRTPCPP
Source0:        https://github.com/wernerd/ZRTPCPP/archive/V%{version}/%{name}-%{version}.tar.gz
# Look. Don't put #warning statements in header files that every application
# needs to include. Most modern things treat warnings as errors, causing every
# dependent build to fail, even if its not even calling zrtp_getSasType
Patch0:         libzrtpcpp-4.4.0-no-warning.patch
# Fix build with gcc15
Patch1:         libzrtpcpp-gcc15.patch


BuildRequires:  ccrtp-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  openssl-devel

%description
This package provides a library that adds ZRTP support to the GNU
ccRTP stack. Phil Zimmermann developed ZRTP to allow ad-hoc, easy to
use key negotiation to setup Secure RTP (SRTP) sessions. GNU ZRTP
together with GNU ccRTP (1.5.0 or later) provides a ZRTP
implementation that can be directly embedded into client and server
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n ZRTPCPP-%{version}
# Make the NEWS.md file non executable
chmod 644 NEWS.md


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%doc README.md AUTHORS NEWS.md
%license COPYING
%{_libdir}/libzrtpcpp.so.4*

%files devel
%{_includedir}/libzrtpcpp/
%{_libdir}/libzrtpcpp.so
%{_libdir}/pkgconfig/libzrtpcpp.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 4.6.6-5
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Sandro Mani <manisandro@gmail.com> - 4.6.6-1
- Update to 4.6.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Sandro Mani <manisandro@gmail.com> - 4.6.5-1
- Update to 4.6.5

* Fri Nov 11 2016 Sandro Mani <manisandro@gmail.com> - 4.6.4-1
- Update to 4.6.4

* Thu Mar 17 2016 Sandro Mani <manisandro@gmail.com> - 4.6.3-1
- Update to 4.6.3

* Thu Feb 04 2016 Sandro Mani <manisandro@gmail.com> - 4.6.2-1
- Update to 4.6.2

* Tue Feb 02 2016 Sandro Mani <manisandro@gmail.com> - 4.6.0-1
- Update to 4.6.0

* Mon Jan 04 2016 Sandro Mani <manisandro@gmail.com> - 4.5.0-1
- Update to 4.5.0

* Sat Dec 26 2015 Sandro Mani <manisandro@gmail.com> - 4.4.0-2
- Rebuild (ucommon)

* Wed Aug 05 2015 Sandro Mani <manisandro@gmail.com> - 4.4.0-1
- Update to 4.4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/GCC5
- Include upstream patch to add -I/usr/include/libzrtpcpp to pkgconfig file

* Thu Feb 26 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/GCC5

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org> - 4.2.4-1
- update to 4.2.4

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 18 2013 Alexey Kurov <nucleo@fedoraproject.org> - 2.3.4-3
- re-enable ec encryption

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Kevin Fenzi <kevin@scrye.com> 2.3.4-1
- Update to 2.3.4
- Fixes CVE-2013-2221 CVE-2013-2222 CVE-2013-2223

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Kevin Fenzi <kevin@scrye.com> 2.3.2-1
- Update to 2.3.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for c++ ABI breakage

* Fri Feb 24 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2
- drop upstreamed 64-bit patch
- visibility issue fixed in upstream

* Thu Feb 23 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.1.1-2
- Workaround for -fvisibility=hidden from commoncpp.pc

* Wed Feb 22 2012 Alexey Kurov <nucleo@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1
- Updated URL

* Tue Feb 21 2012 Dan Horák <dan[at]danny.cz> - 2.0.0-2
- fix build on 64-bit arches

* Sun Jan 22 2012 Kevin Fenzi <kevin@scrye.com> - 2.0.0-1
- Update to 2.0.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 07 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.3-1
- Update to 1.4.3 and rebuild against new ccrtp

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 30 2008 Kevin Fenzi <kevin@tummy.com> - 1.3.0-2
- Fix unused-direct-shlib-dependency and other minor issues. 

* Wed Jun 25 2008 Kevin Fenzi <kevin@tummy.com> - 1.3.0-1
- Initial version for Fedora

