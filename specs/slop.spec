Name:       slop
Version:    7.6
Release:    16%{?dist}
Summary:    Command line tool to perform region SeLect OPeration with mouse
URL:        https://github.com/naelstrof/slop

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:    GPL-3.0-only
Source0:    https://github.com/naelstrof/slop/archive/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 7
BuildRequires: libXext-devel
%endif
BuildRequires: gcc-c++ >= 4.9
BuildRequires: cmake
BuildRequires: glew-devel
BuildRequires: glm-devel
BuildRequires: libicu-devel
BuildRequires: libXrender-devel
BuildRequires: mesa-libEGL-devel

%description
slop (Select Operation) is an application that queries for a selection
from the user and prints the region to stdout.

%package -n libslopy
Summary: Library to perform region SeLect OPeration with mouse
%description -n libslopy
slop (Select Operation) is an application that queries for a selection
from the user and prints the region to stdout.

This sub-package contains libslopy library.

%package -n libslopy-devel
Summary: Library to perform region SeLect OPeration with mouse
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n libslopy-devel
slop (Select Operation) is an application that queries for a selection
from the user and prints the region to stdout.

This sub-package contains development files for libslopy library.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libslopy

%check
%ctest

%files
%doc README.md
%license COPYING license.txt
%{_bindir}/slop
%{_mandir}/man1/slop.1.*

%files -n libslopy
%{_libdir}/libslopy.so.%{version}

%files -n libslopy-devel
%{_libdir}/libslopy.so
%{_includedir}/slop.hpp

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 7.6-15
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 7.6-13
- Rebuild for ICU 74

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 7.6-10
- Rebuilt for ICU 73.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 7.6-8
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 7.6-7
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 12 2022 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 7.6-5
- Enable libXext dependency for RHEL/CentOS

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 7.6-4
- Rebuild for glew 2.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Alois Mahdal <amahdal@redhat.com> - 7.6-2
- Bumping to allow rebuild with maim.src.rpm

* Mon Sep 13 2021 Alois Mahdal <amahdal@redhat.com> - 7.6-1
- Updated upstream to 7.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 7.5-4
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 7.5-3
- Rebuild for ICU 69

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Alois Mahdal <amahdal@redhat.com> - 7.5-1
- Updated upstream to 7.5

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 7.4-10
- Rebuild for ICU 67

* Mon Mar 16 2020 Alois Mahdal <n9042e84@vornet.cz> - 7.4-9
- Fixed BZ#1800099; missing libXext build dependency

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 7.4-5
- Rebuild for ICU 63

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 7.4-4
- Rebuilt for glew 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 7.4-2
- Rebuild for ICU 62

* Thu Jun 28 2018 Alois Mahdal <n9042e84@vornet.cz> 7.4-1
- Initial packaging.
