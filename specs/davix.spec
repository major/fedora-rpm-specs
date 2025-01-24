%undefine __cmake_in_source_build

Name:         davix
Version:      0.8.8
Release:      2%{?dist}
Summary:      Toolkit for HTTP-based file management
License:      LGPL-2.1-or-later AND LGPL-2.0-or-later AND BSD-2-Clause AND MIT AND Apache-2.0 AND curl
URL:          https://dmc-docs.web.cern.ch/dmc-docs/davix.html
Source0:      https://github.com/cern-fts/davix/releases/download/R_0_8_8/davix-0.8.8.tar.gz

BuildRequires:      gcc-c++
BuildRequires:      python3
BuildRequires:      cmake
# main lib dependencies
%if 0%{?fedora} || 0%{?rhel} >= 9
# use bundled curl version on EPEL 8
BuildRequires:      curl-devel
%else
# build uses "git apply" to apply a patch to the bundled curl source
BuildRequires:      git-core
%endif
BuildRequires:      libxml2-devel
BuildRequires:      openssl-devel
BuildRequires:      zlib-devel
# davix-copy dependencies
BuildRequires:      gsoap-devel
BuildRequires:      libuuid-devel
# unit tests
BuildRequires:      gtest-devel
# documentation
BuildRequires:      doxygen
BuildRequires:      python3-sphinx
BuildRequires:      python3-sphinx_rtd_theme

Requires:     %{name}-libs%{?_isa} = %{version}-%{release}

%description
Davix is a toolkit designed for file operations
with HTTP based protocols (WebDav, Amazon S3, ...).
Davix provides an API and a set of command line tools.

%package libs
Summary:      Runtime libraries for %{name}
%if ! ( 0%{?fedora} || 0%{?rhel} >= 9)
Provides:     bundled(libcurl) = 7.69.0
%endif

%description libs
Libraries for %{name}. Davix is a toolkit designed for file operations
with HTTP based protocols (WebDav, Amazon S3, ...).

%package devel
Summary:      Development files for %{name}
Requires:     %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}. Davix is a toolkit designed for file operations
with HTTP based protocols (WebDav, Amazon S3, ...).

%package tests
Summary:      Test suite for %{name}
Requires:     %{name}-libs%{?_isa} = %{version}-%{release}

%description tests
Test suite for %{name}. Davix is a toolkit designed for file operations
with HTTP based protocols (WebDav, Amazon S3, ...).

%package doc
Summary:      Documentation for %{name}
BuildArch:    noarch

%description doc
Documentation and examples for %{name}. Davix is a toolkit designed
for file operations with HTTP based protocols (WebDav, Amazon S3, ...).

%clean
%cmake_build --target clean

%prep
%autosetup -p1

# Remove bundled stuff
%if 0%{?fedora} || 0%{?rhel} >= 9
# remove bundled curl version outside EPEL 8
rm -rf deps/curl
%endif
rm -rf test/pywebdav
rm -rf doc/sphinx/_themes/sphinx_rtd_theme

%build
%cmake \
%if 0%{?fedora} || 0%{?rhel} >= 9
  -DEMBEDDED_LIBCURL=FALSE \
%endif
  -DDOC_INSTALL_DIR=%{_pkgdocdir} \
  -DENABLE_THIRD_PARTY_COPY=TRUE \
  -DENABLE_HTML_DOCS=TRUE
%cmake_build
%cmake_build --target doc
( cd %{_vpath_builddir}/doc ; \
  sphinx-build -q -b html ../../doc/sphinx build/html ; \
  rm -f build/html/.buildinfo ; \
  rm -rf build/html/.doctrees )

%check
%{_vpath_builddir}/test/unit/davix-unit-tests

%install
%cmake_install
rm %{buildroot}%{_pkgdocdir}/LICENSE

%ldconfig_scriptlets libs

%files
%{_bindir}/davix-cp
%{_bindir}/davix-get
%{_bindir}/davix-http
%{_bindir}/davix-ls
%{_bindir}/davix-mkdir
%{_bindir}/davix-mv
%{_bindir}/davix-put
%{_bindir}/davix-rm
%doc %{_mandir}/man1/davix-get.1*
%doc %{_mandir}/man1/davix-http.1*
%doc %{_mandir}/man1/davix-ls.1*
%doc %{_mandir}/man1/davix-mkdir.1*
%doc %{_mandir}/man1/davix-mv.1*
%doc %{_mandir}/man1/davix-put.1*
%doc %{_mandir}/man1/davix-rm.1*

%files libs
%{_libdir}/libdavix.so.*
%{_libdir}/libdavix_copy.so.*
%doc %{_pkgdocdir}/RELEASE-NOTES.md
%license LICENSE

%files devel
%{_includedir}/davix
%{_libdir}/libdavix.so
%{_libdir}/libdavix_copy.so
%{_libdir}/pkgconfig/davix.pc
%{_libdir}/pkgconfig/davix_copy.pc
%doc %{_mandir}/man3/libdavix.3*

%files tests
%{_bindir}/davix-tester
%{_bindir}/davix-unit-tests

%files doc
%doc %{_pkgdocdir}/html
%license LICENSE

%changelog
* Wed Jan 22 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8.8-2
- Rebuilt for gtest 1.15.2

* Tue Jan 21 2025 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 0.8.8-1
- New upstream release 0.8.8
- Align specfile with upstream (including whitespace from tabs to spaces)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 31 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.8.7-4
- Rebuild for gsoap 2.8.135 (Fedora 42)
- Drop EPEL 7 specific instructions (EOL)
- Update License tag

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.7-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 0.8.7-1
- New upstream release 0.8.7

* Wed Apr 03 2024 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 0.8.6-1
- New upstream release 0.8.6

* Wed Jan 24 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.8.5-5
- Rebuild for gsoap 2.8.132 (Fedora 40)

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 0.8.5-3
- Rebuild for gtest 1.14.0 (bugzilla #2228663)

* Tue Oct 31 2023 Terje Rosten <terje.rosten@ntnu.no> - 0.8.5-2
- Rebuild for gtest 1.14.0 (bugzilla #2228663)

* Fri Oct 20 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 0.8.5-1
- New upstream release 0.8.5
- Fix CVE 2023-38545 in the bundled curl library (EPEL 7 and 8)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.8.4-1
- New upstream release 0.8.4
- Drop patches accepted upstream

* Tue Jan 24 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.8.3-4
- Rebuild for gtest 1.13.0
- Don't downgrade the C++ version

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.8.3-2
- Rebuild against gsoap-2.8.124 (bug #2155567)

* Thu Dec 15 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.8.3-1
- New upstream release 0.8.3
- Fix CVE 2022-32221 in the bundled curl library (EPEL 7 and 8)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-2
- Rebuild for new gtest

* Sat Jun 11 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.8.2-1
- New upstream release 0.8.2

* Tue Apr 05 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.8.1-1
- New upstream release 0.8.1
- Drop patches (all accepted upstream)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.8.0-2
- Fix some compilation warnings and errors

* Wed Oct 13 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.8.0-1
- New upstream release 0.8.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.7.6-8
- Rebuilt with OpenSSL 3.0.0

* Mon Aug 30 2021 Petr Pisar <ppisar@redhat.com> - 0.7.6-7
- Rebuild against gsoap-2.8.117 (bug #1996409)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 0.7.6-5
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 29 2020 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.6-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.5-1
- New upstream release

* Thu Aug 22 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.4-3
- Rebuilt for gsoap

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.4-1
- New upstream release

* Wed May 08 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.3-1
- New upstream release

* Wed Mar 20 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.2-2
- Drop build dependency on sphinx

* Fri Feb 15 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.2-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.1-2
- Rebuild for new gsoap

* Wed Oct 24 2018 Andrea Manzi <andrea.manzi at cern.ch> - 0.7.1-1
- New upstream release

* Tue Oct 02 2018 Andrea Manzi <andrea.manzi at cern.ch> - 0.6.9-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.6.8-1
- davix 0.68 release see RELEASE-NOTES for changes

* Mon Mar 26 2018 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.6.7-4
- Stop depending on unneeded gtest-devel and boost packages

* Mon Feb 12 2018 Andrea Manzi <andrea.manzi at cern.ch> - 0.6.7-3
- Rebuild for new gsoap

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Andrea Manzi <andrea.manzi at cern.ch> - 0.6.7-1
- New upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 0.6.6-5
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.6-3
- Rebuilt for Boost 1.64

* Wed Jun 28 2017 Andrea Manzi <andrea.manzi at cern.ch> - 0.6.6-2
- Rebuild for gsoap 2.8.48 (Fedora 27)

* Thu May 11 2017 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.6.6-1
- davix 0.6.6 release, see RELEASE-NOTES for changes

* Tue Feb 07 2017 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.6.5-1
- New upstream release

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 0.6.4-5
- Rebuilt for libgsoapssl++ soname bump

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.4-4
- Rebuilt for Boost 1.63

* Thu Jan 26 2017 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.6.4-3
- Remove trailing whitespaces on CMakeGeneratePkgConfig.cmake
- Patch for openssl 1.1.0

* Thu Aug 18 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.6.4-1
- davix 0.6.4 release, see RELEASE-NOTES for changes

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 0.6.3-3
- Rebuilt for linker errors in boost (#1331983)

* Fri Apr 22 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.6.3-2
- Rebuild for gsoap 2.8.30 (Fedora 25)

* Fri Apr 15 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.6.3-1
- davix 0.6.3 release, see RELEASE-NOTES for changes

* Wed Mar 02 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.6.0-1
- davix 0.6.0 release, see RELEASE-NOTES for changes

* Tue Feb 02 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.5.0-3
- Rebuilt for gsoap 2.8.28

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-2
- Rebuilt for Boost 1.60

* Mon Sep 14 2015 Adrien Devresse <adev@adev.name> - 0.5.0-1
- Update to davix 0.5.0, see release note for details

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.4.1-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.4.1-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Adrien Devresse <adevress at cern.ch> - 0.4.1-3 
- Update to version 0.4.1, see release-note for details

* Thu Apr 16 2015 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 0.4.0-5
- Recompile for another Rawhide C+++ ABI change

* Tue Mar 03 2015 Adrien Devresse <adevress at cern.ch> - 0.4.0-4
- Recompile for Rawhide C++ ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.4.0-3
- Rebuild for boost 1.57.0

* Mon Jan 26 2015 Adrien Devresse <adevress at cern.ch> - 0.4.0-2
- Rebuilt due to gSOAP update

* Fri Dec 05 2014 Adrien Devresse <adevress at cern.ch> - 0.4.0-1
- davix 0.4.0 release, see RELEASE-NOTES for changes

* Tue Aug 12 2014 Adrien Devresse <adevress at cern.ch> - 0.3.6-1
- davix 0.3.6 release, see RELEASE-NOTES for changes

* Tue Jul 22 2014 Adrien Devresse <adevress at cern.ch> - 0.3.4-1
- Update to release 0.3.4

* Wed Jun 04 2014 Adrien Devresse <adevress at cern.ch> - 0.3.1-1
- davix 0.3.1 release, see RELEASE-NOTES for changes

* Tue Jun 03 2014 Adrien Devresse <adevress at cern.ch> - 0.3.0-1
- davix 0.3.0 release, see RELEASE-NOTES for changes

* Tue Jan 28 2014 Adrien Devresse <adevress at cern.ch> - 0.2.10-1
- davix 0.2.10 release, see RELEASE-NOTES for details

* Mon Oct 28 2013 Adrien Devresse <adevress at cern.ch> - 0.2.7-3
- New update of davix, see RELEASE-NOTES for details

* Tue Sep 03 2013 Adrien Devresse <adevress at cern.ch> - 0.2.6-1
- Release 0.2.6 of davix, see RELEASE-NOTES for details

* Wed Jun 05 2013 Adrien Devresse <adevress at cern.ch> - 0.2.2-2
- Initial EPEL release
