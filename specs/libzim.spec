Name: libzim
Version: 8.2.0
Release: 8%{?dist}

License: GPL-2.0-only AND Apache-2.0 AND BSD-3-Clause
Summary: Reference implementation of the ZIM specification

URL: https://github.com/openzim/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gtest-devel
BuildRequires: libicu-devel
BuildRequires: libzstd-devel
BuildRequires: xapian-core-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: ninja-build

Provides: zimlib = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: zimlib < %{?epoch:%{epoch}:}%{version}-%{release}

%description
The ZIM library is the reference implementation for the ZIM file
format. It's a solution to read and write ZIM files on many systems
and architectures.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%meson -Dcpp_std=c++14 -Dwerror=false
%meson_build

%install
%meson_install

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_libdir}/%{name}.so.8*

%files devel
%{_includedir}/zim
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 8.2.0-6
- Rebuild for ICU 74

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 8.2.0-2
- Rebuilt for ICU 73.2

* Sat Apr 29 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 8.2.0-1
- Updated to version 8.2.0.

* Sat Apr 01 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 8.1.1-1
- Renamed package to libzim.
- Updated to version 8.1.1.

* Mon Jan 30 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 8.1.0-4
- Build with C++14 instead of C++11 for gtest-1.13.0.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 8.1.0-2
- Rebuild for ICU 72

* Thu Dec 01 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 8.1.0-1
- Updated to version 8.1.0.

* Thu Sep 08 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 8.0.0-1
- Updated to version 8.0.0.

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 7.2.2-3
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 7.2.2-1
- Updated to version 7.2.2.

* Mon Jan 24 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 7.2.0-1
- Updated to version 7.2.0.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 6.3.0-5
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 6.3.0-4
- Rebuild for ICU 69

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 6.3.0-3
- Rebuilt for removed libstdc++ symbol (#1937698)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 6.3.0-1
- Updated to version 6.3.0.

* Thu Oct 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 6.2.2-1
- Updated to version 6.2.2.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 6.1.8-1
- Updated to version 6.1.8.

* Wed Jul 01 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 6.1.7-1
- Updated to version 6.1.7.

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 6.1.1-2
- Rebuild for ICU 67

* Sun May 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 6.1.1-1
- Updated to version 6.1.1.

* Thu Apr 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 6.1.0-1
- Updated to version 6.1.0.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 6.0.2-2
- Rebuild for ICU 65

* Sun Oct 13 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 6.0.2-1
- Updated to version 6.0.2.

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.1-1
- Updated to version 5.0.1.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.0-1
- Updated to version 5.0.0.

* Tue Apr 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.7-1
- Updated to version 4.0.7.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.6-3
- Removed Werror build flag.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.6-2
- Removed rpath.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.6-1
- Updated to version 4.0.6.

* Tue Mar 19 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.5-1
- Updated to version 4.0.5.
- Major SPEC cleanup.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Micah Roth <micah.roth_ucla.edu> 1.0-5
- forced INSTALL to preserve timestamps for non-compiled files

* Thu Apr 25 2013 Micah Roth <micah.roth_ucla.edu> 1.0-4
- --formal review volter--
- removed INSTALL, NEWS, README files from %%docs
- added COPYING file to %%docs
- removed unnecessary commented lines and empty sections
- improved %%files devel section with asterisk removal and more specificity
- added spaces in the %%changelog area between updates

* Tue Apr 23 2013 Micah Roth <micah.roth_ucla.edu> 1.0-3
- --informal review volter--
- updated descriptions to match %%files lists
- added --disable-static to %%configure

* Sat Apr 20 2013 Micah Roth <micah.roth_ucla.edu> 1.0-2
- added %%doc files
- removed commented lines
- removed --disable-static because it doesn't apply (right?)
- ---volter's informal review---
- moved binaries to base package %%files list
- commented libtool BR
- uncommented removal of *la file(s)
- added macros into Source0
- commented *a %%files list entry

* Sat Apr 20 2013 Micah Roth <micah.roth_ucla.edu> 1.0-1
- created spec file
- commented automake and autotools BRs as recommended by rdieter 
