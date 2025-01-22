Name: libmodbus
Version: 3.1.11
Release: 3%{?dist}
Summary: A Modbus library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: http://www.libmodbus.org/

Source0: https://github.com/stephane/libmodbus/releases/download/v%{version}/libmodbus-%{version}.tar.gz
Patch 0: libmodbus-revert-CFLAGS-changes.patch

BuildRequires: gcc
BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: make

%description
libmodbus is a C library designed to provide a fast and robust implementation of
the Modbus protocol. It runs on Linux, Mac OS X, FreeBSD, QNX and Windows.

This package contains the libmodbus shared library.

%package devel
Summary: Development files for libmodbus
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
libmodbus is a C library designed to provide a fast and robust implementation of
the Modbus protocol. It runs on Linux, Mac OS X, FreeBSD, QNX and Windows.

This package contains libraries, header files and developer documentation needed
for developing software which uses the libmodbus library.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING*
%doc AUTHORS NEWS README.md
%{_libdir}/libmodbus.so.*

%files devel
%{_includedir}/modbus/

%{_libdir}/pkgconfig/libmodbus.pc
%{_libdir}/libmodbus.so

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 24 2024 Eric Sandeen <sandeen@redhat.com> - 3.1.11-1
- New upstream version
- manpages are sadly removed from upstream

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.7-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 25 2023 Eric Sandeen <sandeen@sandeen.net> - 3.1.7-1
- New upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 Eric Sandeen <sandeen@sandeen.net> - 3.1.6-3
- Fix CVE-2022-0367

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Eric Sandeen <sandeen@sandeen.net> - 3.1.6-1
- Move to upstream "development release" as the web page now states that
  the "stable release" is old and should not be used for new projects.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Eric Sandeen <sandeen@sandeen.net> - 3.0.8-1
- New upstream release
- Addresses CVE-2019-14462 and CVE-2019-14463

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct  3 2017 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.6-5
- Cleanup and modernise spec
- Use %%license

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 26 2016 Eric Sandeen <sandeen@sandeen.net> - 3.0.6-1
- New upstream release
- Fix remote buffer overflow vulnerability on write requests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 28 2013 John Morris <john@zultron.com> - 3.0.5-2
- Fix 'bogus date in %%changelog' warnings
- Run aclocal and automake to fix fc21 autoconf problems

* Thu Dec 19 2013 John Morris <john@zultron.com> - 3.0.5-1
- new upstream release
- new Fedora EPEL6 branch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.3-1
- new upstream release

* Mon Jan 16 2012 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.2-1
- new upstream release

* Sat Jul 23 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.1-2
- package reviewed by Peter Lemenkov <lemenkov@gmail.com> and Veeti Paananen
  <veeti.paananen@rojekti.fi> of Fedora Quality Assurance team

* Mon Jul 18 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.1-1
- new upstream release

* Mon Jul 11 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.0-1
- revert the license to LGPLv2.1+
- new spec file generated by autoconf
- add documentation, devel package and various changes

* Sun Jun 5 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.9.4-1
- new upstream release

* Mon Jan 10 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.9.3-1
- new upstream release

* Tue Oct 5 2010 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.9.2-1
- new upstream release

* Wed Jul 2 2008 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.0.1-1
- new upstream release

* Fri May 2 2008 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.0.0-1
- integrate extern_for_cpp in upstream.
- update the license to version LGPL v3.

* Wed Apr 30 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.9.0-2
- get the license corrected in the spec file.
- add a URL for where to find libmodbus.
- tweak the summary and description.

* Tue Apr 29 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.9.0-1
- upgrade to latest upstream (pre-release)
- port extern_for_cpp patch to 1.9.0

* Tue Apr 29 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.2.4-2_tad
- add a patch to allow compiling with c++ code.

* Mon Apr 28 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.2.4-1_tad
- build spec file.
- include patch for controling error-treat.
