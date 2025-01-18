# FIXME: report to upstream
%define _lto_cflags %{nil}

%define utils_version 1.3

Name:           cbmc
Version:        6.4.1
Release:        2%{?dist}
Summary:        Bounded Model Checker for ANSI-C and C++ programs

License:        BSD-4-Clause
URL:            https://www.cprover.org/cbmc

Source0:        https://github.com/diffblue/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/aufover/%{name}-utils/archive/v%{utils_version}/%{name}-utils-%{utils_version}.tar.gz

# FIXME: Upstream these patches!
# Adapt to recent versions of glpk
Patch1:         %{name}-5.9-glpk.patch
# Implements https://github.com/diffblue/cbmc/issues/5965
Patch2:         %{name}-add-cmd-line-arg.patch
# Fix compilation on F40
Patch3:         %{name}-f41-fix-build.patch

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  glpk-devel
BuildRequires:  minisat2-devel
BuildRequires:  ninja-build
BuildRequires:  zlib-devel

%ifarch x86_64
# For the tests
BuildRequires:  cvc5
BuildRequires:  gdb
BuildRequires:  jq
BuildRequires:  perl
BuildRequires:  python3
BuildRequires:  z3

# For %%py3_shebang_fix
BuildRequires:  python3-devel
%endif

Requires:       gcc-c++

%description
CBMC generates traces that demonstrate how an assertion can be violated, or
proves that the assertion cannot be violated within a given number of loop
iterations.

%package doc
Summary:        Documentation for %{name}

%description doc
Documentation for %{name}.

%package utils
Summary:        Output conversion utilities for CBMC

%description utils
Output conversion utilities for CBMC (GCC like format).

%prep
%setup -T -q -b 1 -n %{name}-utils-%{utils_version}
%autosetup -p1 -b 0 -S git -n %{name}-%{name}-%{version}

sed -i 's/-Werror//g' CMakeLists.txt src/ansi-c/library_check.sh src/config.inc

%build
%cmake -GNinja -DWITH_JBMC:BOOL=OFF \
               -Dsat_impl:STRING=system-minisat2 \
%ifarch %{ix86} x86_64
               -DWITH_MEMORY_ANALYZER:BOOL=ON \
%endif
               -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%cmake_build --target doc

%install
%cmake_install

install -p -m 0755 "%{_builddir}/%{name}-utils-%{utils_version}/cbmc_utils/formatCBMCOutput.py" %{buildroot}%{_bindir}/%{name}-convert-output
install -p -m 0755 "%{_builddir}/%{name}-utils-%{utils_version}/cbmc_utils/csexec-cbmc.sh" %{buildroot}%{_bindir}/csexec-%{name}

# Remove Cprover API stuff because static libraries are not allowed!
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/libcprover.*.a

# FIXME: Report to upstream that the target directory for completions is wrong!
mkdir -p %{buildroot}%{bash_completions_dir}
mv %{buildroot}{/usr/etc/bash_completion.d/cbmc,%{bash_completions_dir}}

%ifarch x86_64
%check
# Fix unversioned shebang!
%py3_shebang_fix scripts/cpplint.py

# The tests were written with the assumption that they would be executed on
# an x86_64.  Other platforms suffer a large number of spurious test failures.
%ctest --label-regex CORE
%ctest --tests-regex unit-xfail
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/cbmc
%{_bindir}/cprover
%{_bindir}/crangler
%{_bindir}/goto-*
%{_bindir}/ls_parse.py
%{_bindir}/symtab2gb
%{bash_completions_dir}
%{_mandir}/man1/cbmc*.1.*
%{_mandir}/man1/crangler*.1.*
%{_mandir}/man1/goto-*.1.*
%ifarch %{ix86} x86_64
%{_mandir}/man1/memory-analyzer.1.*
%endif
%{_mandir}/man1/symtab2gb.1.*

%files doc
%doc %{__cmake_builddir}/doc/html README.md TOOLS_OVERVIEW.md
%license LICENSE

%files utils
%license ../%{name}-utils-%{utils_version}/LICENSE
%{_bindir}/%{name}-convert-output
%{_bindir}/csexec-%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 29 2024 Lukáš Zaoral <lzaoral@redhat.com> - 6.4.1-1
- rebase to latest upstream version (rhbz#2292926)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.95.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 09 2024 Lukáš Zaoral <lzaoral@redhat.com> - 5.95.1-4
- fix FTBFS on Rawhide (rhbz#2259235)

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.95.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.95.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Lukáš Zaoral <lzaoral@redhat.com> - 5.95.1-1
- Update to 5.95.1 (rhbz#2239079)

* Fri Jul 21 2023 Lukáš Zaoral <lzaoral@redhat.com> - 5.50.0-6
- Exclude installation of test dependencies on non-x86_64 architectures

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.50.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 Lukáš Zaoral <lzaoral@redhat.com> - 5.50.0-4
- Fix rawhide FTBFS
- Use SPDX license format
- Modernize the spec a bit

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 09 2022 Vincent Mihalkovic <vmihalko@redhat.com> - 5.50.0-1
- New upstream release of cbmc and also cbmc-utils
- Add "--add-cmd-line-arg" option for goto-instrument

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Vincent Mihalkovic <vmihalko@redhat.com> - 5.38.0-1
- New upstream release of cbmc and also cbmc-utils

* Mon Aug 23 2021 Pavel Simovec <psimovec@redhat.com> - 5.37.0-1
- New upstream release
- fix broken indentation in a patch

* Wed Aug  4 2021 Lukas Zaoral <lzaoral@redhat.com> - 5.35.0-1
- New upstream release
- Use plain doxygen to cut-down some build dependencies

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 12 2021 Vincent Mihalkovic <vmihalko@redhat.com> - 5.29.0-1
- New upstream release

* Wed Mar 10 2021 Vincent Mihalkovic <vmihalko@redhat.com> - 5.25.0-2
- Add Requires: clang

* Wed Mar 10 2021 Vincent Mihalkovic <vmihalko@redhat.com> - 5.25.0-1
- Add csexec-cbmc.sh script
- New upstream release

* Tue Feb 23 2021 Vincent Mihalkovic <vmihalko@redhat.com> - 5.24.0-1
- Add goto-clang for a hybrid binary translation
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.17.0-1
- New upstream release

* Thu Oct 08 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.15.0-1
- New upstream release

* Wed Sep 30 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.14.3-1
- New upstream release

* Tue Sep 29 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.13.1-1
- New upstream release
- Use CMake instead of plain Makefiles
- Add cbmc-utils subpackage

* Tue Sep 01 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.13.0-1
- New upstream release

* Wed Aug 12 2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.12.6-1
- Replace custom goto-cc.1 with symlinks to cbmc.1
- Enable full cbmc testsuite
- python to python3 fix in one test case

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 9  2020 Vincent Mihalkovic <vmihalko@redhat.com> - 5.12-1
- New upstream release. Skipping some of regression tests - temporary f33 build fix

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Jerry James <loganjerry@gmail.com> - 5.11-4
- Drop cudd support due to impending cudd retirement

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun  8 2019 Jerry James <loganjerry@gmail.com> - 5.11-2
- Fix man page links (bz 1718287)

* Thu Jan 31 2019 Jerry James <loganjerry@gmail.com> - 5.11-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 26 2018 Jerry James <loganjerry@gmail.com> - 5.10-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Jerry James <loganjerry@gmail.com> - 5.9-1
- New upstream release
- Drop upstreamed -float128 and -vec patches
- Musketeer and symex have been removed; do not try to build them

* Mon Jun 11 2018 Jerry James <loganjerry@gmail.com> - 5.8-4
- Fix out of bounds vector accesses

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 5.8-3
- Rebuild for glpk 4.65

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 12 2017 Jerry James <loganjerry@gmail.com> - 5.8-1
- New upstream release
- Drop upstreamed -musketeer patch
- Add -doc subpackage to hold doxygen-generated content

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr  6 2017 Jerry James <loganjerry@gmail.com> - 5.7-1
- New upstream release

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 5.6-3
- Rebuild for glpk 4.61

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 26 2016 Jerry James <loganjerry@gmail.com> - 5.6-1
- New upstream release

* Fri Sep 16 2016 Jerry James <loganjerry@gmail.com> - 5.5-2
- Fix two tests that fail on big endian architectures (bz 1371894)

* Sat Aug 27 2016 Jerry James <loganjerry@gmail.com> - 5.5-1
- New upstream release

* Thu Mar 17 2016 Jerry James <loganjerry@gmail.com> - 5.4-1
- New upstream release

* Sat Mar 12 2016 Jerry James <loganjerry@gmail.com> - 5.3-5
- Rebuild for glpk 4.59

* Fri Feb 19 2016 Jerry James <loganjerry@gmail.com> - 5.3-4
- Rebuild for glpk 4.58

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Jerry James <loganjerry@gmail.com> - 5.3-2
- Rebuild for cudd 3.0.0

* Tue Dec  1 2015 Jerry James <loganjerry@gmail.com> - 5.3-1
- New upstream release

* Wed Oct  7 2015 Jerry James <loganjerry@gmail.com> - 5.2-1
- New upstream release

* Fri Oct  2 2015 Jerry James <loganjerry@gmail.com> - 5.1-3
- Rebuild for cudd 2.5.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Jerry James <loganjerry@gmail.com> - 5.1-1
- New upstream release
- Drop upstreamed -messaget patch

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 5.0-1
- New upstream release
- Drop upstreamed ppc64le patch
- Add -messaget patch to fix a build failure

* Mon Sep 15 2014 Jerry James <loganjerry@gmail.com> - 4.9-1
- New upstream release
- Drop upstreamed patches

* Wed Sep  3 2014 Jerry James <loganjerry@gmail.com> - 4.7-3
- Add patch to fix the ppc64le build (bz 1133066)
- Add man page links for goto-cc and goto-instrument
- Fix license handling

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Jerry James <loganjerry@gmail.com> - 4.7-1
- New upstream release
- Build with CUDD support

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-2.20131201svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec  1 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.6-1.20131201svn
- Updated to upstream 4.6 release

* Tue Sep 10 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.3-7.20130515svn
- Fix build with unversioned docdir using _pkgdocdir (#992043)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-6.20130515svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Dan Horák <dan[at]danny.cz> - 4.3-5.20130515svn
- fix build on s390x

* Mon Jul  8 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.3-4.20130515svn
- Fixed changelog date

* Sun Jun 30 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.3-3.20130515svn
- Updated license
- Fixed doc and manual page directories

* Tue Jun 25 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.3-2.20130515svn
- Updated release

* Wed May 15 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 4.3-1.20130515svn
- First release
