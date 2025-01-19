Name:           libwbxml
Version:        0.11.10
Release:        3%{?dist}
Summary:        Library and tools to parse, encode and handle WBXML documents
## Used and installed:
# COPYING:                          LGPL-2.1-or-later
# GNU-LGPL:                         LGPL-2.1 text
# Other files:                      LGPL-2.1-or-later
## Not installed:
# cmake/modules/AddDocumentation.cmake:             "see the accompanying COPYING-CMAKE-SCRIPTS"
# cmake/modules/COPYING-CMAKE-SCRIPTS:              BSD-3-Clause text
# cmake/modules/MacroEnsureOutOfSourceBuild.cmake:  "see the accompanying COPYING-CMAKE-SCRIPTS"
# cmake/modules/ShowStatus.cmake:                   "see the accompanying COPYING-CMAKE-SCRIPTS"
## Not used:
# win32/leaktrack/COPYING.txt:      BSD-4-Clause
# win32/leaktrack/leaktrack.h:      GPL-2.0-or-later
# win32/leaktrack/lt_log.h:         GPL-2.0-or-later
# win32/expat/COPYING.txt:          MIT
# win32/expat/expat.h:              "See the file COPYING"
# win32/expat/README.txt:           "see COPYING, same as MIT/X Consortium license"
License:        LGPL-2.1-or-later
SourceLicense:  GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-4-Clause AND BSD-3-Clause AND MIT
URL:            https://github.com/%{name}/%{name}
Source:         %{url}/archive/%{name}-%{version}.tar.gz
# Fix installing CMake configuration files, in upstream after 0.11.10,
# <https://github.com/libwbxml/libwbxml/pull/95>.
Patch0:         libwbxml-0.11.10-Fix-installing-CMake-configuration-files.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  coreutils
BuildRequires:  expat-devel
BuildRequires:  gcc
# cmake executes make, but does not declare the dependency
BuildRequires:  make
BuildRequires:  pkgconfig(check)
# Tests:
BuildRequires:  bash
BuildRequires:  perl-interpreter
BuildRequires:  perl(English)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Obsoletes:      wbxml2 <= 0.9.3

%description
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce
bandwidth in mobile communications.

%package devel
Summary:       Development files of %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig
# ??? FIXME Deps for libwbxml2-config.cmake file
# <https://github.com/libwbxml/libwbxml/issues/96>
Provides:      wbxml2-devel = %{version}-%{release}
Obsoletes:     wbxml2-devel <= 0.9.3

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
# Upstream does not support in-source-directory building
%{cmake} \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DBUILD_STATIC_LIBS:BOOL=OFF \
    -DENABLE_INSTALL_DOC:BOOL=OFF \
    -DENABLE_UNIT_TEST:BOOL=ON \
    -DWBXML_ENCODER_USE_STRTBL:BOOL=ON \
    -DWBXML_INSTALL_FULL_HEADERS:BOOL=OFF \
    -DWBXML_LIB_VERBOSE:BOOL=OFF \
    -DWBXML_SUPPORT_AIRSYNC:BOOL=ON \
    -DWBXML_SUPPORT_CO:BOOL=ON \
    -DWBXML_SUPPORT_CONML=ON \
    -DWBXML_SUPPORT_DRMREL:BOOL=ON \
    -DWBXML_SUPPORT_EMN:BOOL=ON \
    -DWBXML_SUPPORT_OTA_SETTINGS:BOOL=ON \
    -DWBXML_SUPPORT_PROV:BOOL=ON \
    -DWBXML_SUPPORT_SI:BOOL=ON \
    -DWBXML_SUPPORT_SL:BOOL=ON \
    -DWBXML_SUPPORT_SYNCML:BOOL=ON \
    -DWBXML_SUPPORT_WML:BOOL=ON \
    -DWBXML_SUPPORT_WTA:BOOL=ON \
    -DWBXML_SUPPORT_WV:BOOL=ON
%{cmake_build}

%install
%{cmake_install}

%check
%{ctest}

%files
%license COPYING GNU-LGPL
%doc BUGS ChangeLog README References THANKS TODO
%{_bindir}/wbxml2xml
%{_bindir}/xml2wbxml
%{_libdir}/libwbxml2.so.*

%files devel
%{_includedir}/libwbxml-1.1
%{_libdir}/cmake/libwbxml2
%{_libdir}/libwbxml2.so
%{_libdir}/pkgconfig/libwbxml2.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Petr Pisar <ppisar@redhat.com> - 0.11.10-1
- 0.11.10 bump

* Mon Jun 17 2024 Petr Pisar <ppisar@redhat.com> - 0.11.9-1
- 0.11.9 bump

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Petr Pisar <ppisar@redhat.com> - 0.11.8-3
- Convert a License tag to an SPDX format

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 01 2022 Petr Pisar <ppisar@redhat.com> - 0.11.8-1
- 0.11.8 bump

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jul 30 2020 Petr Pisar <ppisar@redhat.com> - 0.11.7-3
- Adjust packaging to new CMake

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Petr Pisar <ppisar@redhat.com> - 0.11.7-1
- 0.11.7 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Petr Pisar <ppisar@redhat.com> - 0.11.6-3
- Modernize a spec file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 16 2017 Petr Pisar <ppisar@redhat.com> - 0.11.6-1
- 0.11.6 bump

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Petr Pisar <ppisar@redhat.com> - 0.11.5-1
- 0.11.5 bump

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Petr Pisar <ppisar@redhat.com> - 0.11.3-3
- Require gcc instead of glibc-headers (bug #1230475)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Petr Pisar <ppisar@redhat.com> - 0.11.3-1
- 0.11.3 bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 Petr Pisar <ppisar@redhat.com> - 0.11.2-1
- 0.11.2 bump

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Petr Pisar <ppisar@redhat.com> - 0.11.1-1
- 0.11.1 bump
- The license is LGPLv2+ only for all the code

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 23 2011 Petr Pisar <ppisar@redhat.com> - 0.11.0-1
- 0.11.0 bump: This version breaks API
- Add GPLv2+ to license tag because of xml2wbxml_tool
- Remove explicit defattr spec code

* Thu Feb 10 2011 Petr Pisar <ppisar@redhat.com> - 0.10.9-3
- Correct devel dependency typo

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Petr Pisar <ppisar@redhat.com> - 0.10.9-1
- 0.10.9 bump
- Remove BuildRoot stuff
- Make devel subpackage ISA specific

* Tue Aug 10 2010 Petr Pisar <ppisar@redhat.com> - 0.10.8-1
- 0.10.8 import
- based on and obsoletes wbxml2-0.9.2-16
