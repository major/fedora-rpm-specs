# We need to rebuild this package every time the clang major version
# changes, since clang releases are not ABI compatible between major
# versions. See also https://bugzilla.redhat.com/1544964.

Version:       4.05c
%global forgeurl https://github.com/AFLplusplus/AFLplusplus/
%forgemeta

Name:          american-fuzzy-lop
Summary:       Practical, instrumentation-driven fuzzer for binary formats
License:       ASL 2.0

Release:       1%{?dist}
URL:           %{forgeurl}
Source0:       %{forgesource}

# For running the tests:
Source1:       hello.c

# Only specific architectures are supported by upstream.
# On non-x86 only afl-clang-fast* are built.
ExclusiveArch: %{ix86} x86_64 s390x

BuildRequires: clang
BuildRequires: llvm-devel
BuildRequires: make
%ifarch %{ix86} x86_64
BuildRequires: lld
%endif

Requires:      gcc

%global afl_helper_path %{_libdir}/afl


%description
American fuzzy lop uses a novel type of compile-time instrumentation
and genetic algorithms to automatically discover clean, interesting
test cases that trigger new internal states in the targeted
binary. This substantially improves the functional coverage for the
fuzzed code. The compact synthesized corpuses produced by the tool are
also useful for seeding other, more labor- or resource-intensive
testing regimes down the road.

Compared to other instrumented fuzzers, afl-fuzz is designed to be
practical: it has a modest performance overhead, uses a variety of
highly effective fuzzing strategies, requires essentially no
configuration, and seamlessly handles complex, real-world use cases -
say, common image parsing or file compression libraries.

%global clang_major %(command -v clang >/dev/null && clang --version | sed -n -r 's/clang version ([0-9]+).*/\\1/p')

%package clang
Summary:       Clang and clang++ support for %{name}
Requires:      %{name} = %{version}-%{release}

%if "%{clang_major}" != ""
Requires:      clang(major) = %{clang_major}
%endif
%ifarch %{ix86} x86_64
Requires:      lld
%endif

%description clang
This subpackage contains clang and clang++ support for
%{name}.


%prep
%forgesetup


%build
# This package appears to be failing because links to the LLVM plugins
# are not installed which results in the tools not being able to
# interpret the .o/.a files.  Disable LTO for now
%define _lto_cflags %{nil}

%ifnarch %{ix86} x86_64
AFL_NO_X86=1 \
%endif
CFLAGS="%{optflags}" \
%{__make} %{?_smp_mflags} \
  PREFIX="%{_prefix}" \
  HELPER_PATH="%{afl_helper_path}" \
  DOC_PATH="%{_pkgdocdir}" \
  MAN_PATH="%{_mandir}/man8" \
  MISC_PATH="%{_pkgdocdir}" \
  source-only


%install
%ifnarch %{ix86} x86_64
AFL_NO_X86=1 \
%endif
%{make_install} \
  PREFIX="%{_prefix}" \
  HELPER_PATH="%{afl_helper_path}" \
  DOC_PATH="%{_pkgdocdir}" \
  MAN_PATH="%{_mandir}/man8" \
  MISC_PATH="%{_pkgdocdir}"

%ifnarch %{ix86} x86_64
# On non-x86 these files are built and installed but they don't
# function, so delete them.  Only afl-clang-fast* works.
# afl-clang-fast* is a symlink to afl-cc / afl-c++ so we cannot delete
# those binaries.
rm $RPM_BUILD_ROOT%{_bindir}/afl-clang
rm $RPM_BUILD_ROOT%{_bindir}/afl-clang++
rm $RPM_BUILD_ROOT%{_bindir}/afl-gcc
rm $RPM_BUILD_ROOT%{_bindir}/afl-g++
rm $RPM_BUILD_ROOT%{_mandir}/man8/afl-cc.8*
rm $RPM_BUILD_ROOT%{_mandir}/man8/afl-c++.8*
%endif

# Otherwise we see:
# ERROR: No build ID note found in <.o file>
chmod -x $RPM_BUILD_ROOT%{afl_helper_path}/*.o

# This file is created when I build locally, but not when I build in
# Koji.  Remove it so I can build locally.
%if 0%{?__isa_bits} == 64
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-compiler-rt-32.o
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-llvm-rt-32.o
rm -f $RPM_BUILD_ROOT%{afl_helper_path}/afl-llvm-rt-lto-32.o
%endif

# Remove docs since we will package them using %%doc.
mv $RPM_BUILD_ROOT%{_pkgdocdir} pkg-docs


%check
# This just checks that simple programs can be compiled using
# the compiler wrappers.
ln -s %{SOURCE1} hello.cpp
%ifarch %{ix86} x86_64
./afl-gcc %{SOURCE1} -o hello
./hello
./afl-g++ hello.cpp -o hello
./hello
./afl-clang %{SOURCE1} -o hello
./hello
./afl-clang++ hello.cpp -o hello
./hello
%endif
./afl-clang-fast %{SOURCE1} -o hello
./hello
./afl-clang-fast++ hello.cpp -o hello
./hello

# Also check that we got the %%clang_major macro
test -n '%{clang_major}'

%files
%license docs/COPYING
%doc pkg-docs/*
%ifarch %{ix86} x86_64
%{_bindir}/afl-g++
%{_bindir}/afl-gcc
%endif
%{_bindir}/afl-analyze
%{_bindir}/afl-cc
%{_bindir}/afl-c++
%{_bindir}/afl-cmin
%{_bindir}/afl-cmin.bash
%{_bindir}/afl-fuzz
%{_bindir}/afl-gotcpu
%{_bindir}/afl-persistent-config
%{_bindir}/afl-plot
%{_bindir}/afl-showmap
%{_bindir}/afl-system-config
%{_bindir}/afl-tmin
%{_bindir}/afl-whatsup
%dir %{afl_helper_path}
%{afl_helper_path}/afl-as
%{afl_helper_path}/as
%if 0%{?__isa_bits} == 32
%{afl_helper_path}/afl-compiler-rt-32.o
%else
%{afl_helper_path}/afl-compiler-rt-64.o
%endif
%{afl_helper_path}/afl-compiler-rt.o
%ifarch %{ix86} x86_64
%{_mandir}/man8/afl-c++.8*
%{_mandir}/man8/afl-cc.8*
%endif
%{_mandir}/man8/afl-analyze.8*
%{_mandir}/man8/afl-as.8*
%{_mandir}/man8/afl-cmin.8*
%{_mandir}/man8/afl-cmin.bash.8*
%{_mandir}/man8/afl-fuzz.8*
%{_mandir}/man8/afl-gotcpu.8*
%{_mandir}/man8/afl-plot.8*
%{_mandir}/man8/afl-persistent-config.8*
%{_mandir}/man8/afl-showmap.8*
%{_mandir}/man8/afl-system-config.8*
%{_mandir}/man8/afl-tmin.8*
%{_mandir}/man8/afl-whatsup.8*


%files clang
%license docs/COPYING

%ifarch %{ix86} x86_64
%{_bindir}/afl-clang
%{_bindir}/afl-clang++
%endif
%{_bindir}/afl-clang-fast
%{_bindir}/afl-clang-fast++
%ifarch %{ix86} x86_64
%{_bindir}/afl-clang-lto
%{_bindir}/afl-clang-lto++
%{_bindir}/afl-ld-lto
%{_bindir}/afl-lto
%{_bindir}/afl-lto++
%endif

%{afl_helper_path}/afl-llvm-dict2file.so
%ifarch %{ix86} x86_64
%{afl_helper_path}/afl-llvm-lto-instrumentlist.so
%endif
%{afl_helper_path}/afl-llvm-pass.so

%ifarch %{ix86} x86_64
%if 0%{?__isa_bits} == 32
%{afl_helper_path}/afl-llvm-rt-lto-32.o
%else
%{afl_helper_path}/afl-llvm-rt-lto-64.o
%endif
%{afl_helper_path}/afl-llvm-rt-lto.o
%endif

%{afl_helper_path}/cmplog-instructions-pass.so
%{afl_helper_path}/cmplog-routines-pass.so
%{afl_helper_path}/cmplog-switches-pass.so
%{afl_helper_path}/compare-transform-pass.so
%{afl_helper_path}/dynamic_list.txt
%{afl_helper_path}/libAFLDriver.a*
%{afl_helper_path}/libAFLQemuDriver.a
%{afl_helper_path}/libdislocator.so
%{afl_helper_path}/libtokencap.so
%ifarch %{ix86} x86_64
%{afl_helper_path}/SanitizerCoverageLTO.so
%endif
%{afl_helper_path}/SanitizerCoveragePCGUARD.so
%{afl_helper_path}/split-compares-pass.so
%{afl_helper_path}/split-switches-pass.so

%{_mandir}/man8/afl-clang-fast.8*
%{_mandir}/man8/afl-clang-fast++.8*
%ifarch %{ix86} x86_64
%{_mandir}/man8/afl-clang-lto.8.gz
%{_mandir}/man8/afl-clang-lto++.8.gz
%{_mandir}/man8/afl-lto.8.gz
%{_mandir}/man8/afl-lto++.8.gz
%endif


%changelog
* Fri Jan 06 2023 Richard W.M. Jones <rjones@redhat.com> - 4.05c-1
- New upstream release 4.05c (RHBZ#2158888)

* Tue Oct 11 2022 Richard W.M. Jones <rjones@redhat.com> - 4.04c-1
- New upstream version 4.04c (RHBZ#2133825)

* Tue Sep 20 2022 Richard W.M. Jones <rjones@redhat.com> - 4.03c-1
- New upstream version 4.03c (RHBZ#2128509)
- Remove patch which is now upstream.

* Thu Sep 15 2022 Nikita Popov <npopov@redhat.com> - 4.02c-3
- Restore previous clang_major macro

* Wed Sep 14 2022 Nikita Popov <npopov@redhat.com> - 4.02c-2
- Rebuild against LLVM 15

* Tue Aug 09 2022 Richard W.M. Jones <rjones@redhat.com> - 4.02c-1
- New upstream version 4.02c (RHBZ#2116584)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.01c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Richard W.M. Jones <rjones@redhat.com> - 4.01c-1
- New upstream version 4.01c (RHBZ#2101976)

* Thu Mar 31 2022 Richard W.M. Jones <rjones@redhat.com> - 4.00c-3
- Rebuild for clang 14
- Add upstream patches to commit 285a5cb3.

* Fri Mar 18 2022 Richard W.M. Jones <rjones@redhat.com> - 4.00c-2
- Enable clang-LTO support.

* Wed Jan 26 2022 Richard W.M. Jones <rjones@redhat.com> - 4.00c-1
- New upstream version 4.00c (RHBZ#2046452)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14c-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Tom Stellard <tstellar@redhat.com> - 3.14c-6
- Rebuild for llvm-13.0.0

* Fri Sep 03 2021 Richard W.M. Jones <rjones@redhat.com> - 3.14c-5
- Add support for s390x (RHBZ#2000116)

* Wed Aug 18 2021 Richard W.M. Jones <rjones@redhat.com> - 3.14c-3
- Rebuild for clang 13.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Richard W.M. Jones <rjones@redhat.com> - 3.14c-1
- New upstream version 3.14c (RHBZ#1983648).
- Remove a few rogue "/usr/bin" in %%files section.
- Add new file to afl_helper_path.

* Tue Jun 01 2021 Richard W.M. Jones <rjones@redhat.com> - 3.13c-1
- New upstream version 3.13c (RHBZ#1966720).

* Sat May 15 2021 Richard W.M. Jones <rjones@redhat.com> - 3.12c-3
- Rebuild for previous commit.

* Mon May 10 2021 Jonathan Wakely <jwakely@redhat.com> - 3.12c-2
- Rebuilt for removed libstdc++ symbols (#1937698)

* Wed Mar 24 2021 Richard W.M. Jones <rjones@redhat.com> - 3.12c-1
- New upstream version 3.12c (RHBZ#1942625).
- Add afl-clang-fast(8) and afl-clang-fast++(8) man pages.

* Tue Mar 16 2021 Richard W.M. Jones <rjones@redhat.com> - 3.11c-1
- New upstream version 3.11c (RHBZ#1939443).

* Mon Mar 15 2021 Richard W.M. Jones <rjones@redhat.com> - 3.10c-1
- Switch to fork AFL++, see discussion on Fedora devel list.
- New upstream version 3.10c (RHBZ#1938600).

* Tue Feb 23 2021 Richard W.M. Jones <rjones@redhat.com> - 2.57b-1
- New upstream version 2.57b.
- Clang 12 in Fedora 34+ (RHBZ#1932050).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.56b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.56b-5
- Clang 11 in Fedora 33+ (RHBZ#1870933).

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.56b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jeff Law <law@redhat.com> - 2.56b-3
- Disable LTO

* Sat Mar 14 2020 Richard W.M. Jones <rjones@redhat.com> - 2.56b-2
- Clang 10 in Fedora 32+ (RHBZ#1813541).

* Tue Jan 28 2020 Richard W.M. Jones <rjones@redhat.com> - 2.56b-1
- New upstream version 2.56b.
- New clang version 9 in Fedora >= 31.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.53b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 2.53b-1
- New upstream release 2.53b.
- Change Source URL for new hosting location.
- Compile against clang 8.
- Filter out -fstack-clash-protection from clang.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.52b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.52b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Richard W.M. Jones <rjones@redhat.com> - 2.52b-6
- Rebuild against new clang 7.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.52b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Richard W.M. Jones <rjones@redhat.com> - 2.52b-4
- Depend on clang(major) exact version (see RHBZ#1547444 RHBZ#1544964).
- Fix C++ flags passed to clang++ to remove GCC-isms.

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.52b-3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.52b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Richard W.M. Jones <rjones@redhat.com> - 2.52b-1
- New upstream version 2.52b (RHBZ#1509729).

* Tue Sep 12 2017 Richard W.M. Jones <rjones@redhat.com> - 2.51b-1
- New upstream version 2.51b (RHBZ#1487190).

* Tue Aug 22 2017 Richard W.M. Jones <rjones@redhat.com> - 2.50b-1
- New upstream version 2.50b (RHBZ#1483318).

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.49b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.49b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Richard W.M. Jones <rjones@redhat.com> - 2.49b-1
- New upstream version 2.49b (RHBZ#1472016).

* Fri Jul 14 2017 Richard W.M. Jones <rjones@redhat.com> - 2.47b-1
- New upstream version 2.47b (RHBZ#1470893).

* Tue Jul 11 2017 Richard W.M. Jones <rjones@redhat.com> - 2.46b-1
- New upstream version 2.46b (RHBZ#1467746).

* Thu Jun 29 2017 Richard W.M. Jones <rjones@redhat.com> - 2.44b-1
- New upstream version 2.44b (RHBZ#1458261).

* Thu Apr 13 2017 Richard W.M. Jones <rjones@redhat.com> - 2.41b-4
- New upstream version 2.41b (RHBZ#1441654).
- Fix Source URL.
- Compile afl-clang-fast (in a new subpackage).
- Add a simple check section.

* Tue Apr  4 2017 Richard W.M. Jones <rjones@redhat.com> - 2.40b-1
- New upstream version 2.40b (RHBZ#1418875).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.38b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Richard W.M. Jones <rjones@redhat.com> - 2.38b-1
- New upstream version 2.38b (RHBZ#1376789).

* Sat Aug 27 2016 Richard W.M. Jones <rjones@redhat.com> - 2.33b-3
- New upstream version 2.33b (RHBZ#1350795).
- Remove patch.

* Fri Jun 24 2016 Richard W.M. Jones <rjones@redhat.com> - 2.16b-1
- New upstream version 2.16b (RHBZ#1336154).

* Wed May 04 2016 Richard W.M. Jones <rjones@redhat.com> - 2.12b-1
- New upstream version 2.12b (RHBZ#1331192).

* Thu Mar 31 2016 Richard W.M. Jones <rjones@redhat.com> - 2.10b-1
- New upstream version 2.10b (RHBZ#1317205).

* Tue Mar 08 2016 Richard W.M. Jones <rjones@redhat.com> - 2.07b-1
- New upstream version 2.07b (RHBZ#1311776).

* Mon Feb 22 2016 Richard W.M. Jones <rjones@redhat.com> - 2.04b-1
- New upstream version 2.04b (RHBZ#1310407).

* Thu Feb 18 2016 Richard W.M. Jones <rjones@redhat.com> - 2.02b-1
- New upstream version 2.02b (RHBZ#1309139).
- Remove afl-as, packaged in error.

* Mon Feb 15 2016 Richard W.M. Jones <rjones@redhat.com> - 2.00b-1
- New upstream version 2.00b (RHBZ#1306060).
- Rebase CFLAGS override patch.
- New programs afl-analyze, afl-as.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.96b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Richard W.M. Jones <rjones@redhat.com> - 1.96b-1
- New upstream version 1.96b (RHBZ#1292637).

* Tue Nov 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.95b-1
- New upstream version 1.95b (RHBZ#1262537).

* Wed Sep  9 2015 Richard W.M. Jones <rjones@redhat.com> - 1.93b-1
- New upstream version 1.93b (RHBZ#1259960).

* Thu Sep  3 2015 Richard W.M. Jones <rjones@redhat.com> - 1.90b-1
- New upstream version 1.90b.

* Mon Aug 31 2015 Pádraig Brady <pbrady@redhat.com> - 1.88b-1
- Latest upstream

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Richard W.M. Jones <rjones@redhat.com> - 1.71b-1
- New upstream version 1.71b.

* Tue Feb 10 2015 Richard W.M. Jones <rjones@redhat.com> - 1.42b-1
- New upstream version 1.42b.
- Remove trademarked image from source (RHBZ#1191184).
- Use wildcard in .gitignore file.

* Sat Feb  7 2015 Richard W.M. Jones <rjones@redhat.com> - 1.40b-1
- New upstream version 1.40b (RHBZ#1188782).

* Tue Feb 03 2015 Pádraig Brady <pbrady@redhat.com> - 1.38b-1
- Latest upstream

* Mon Jan 26 2015 Pádraig Brady <pbrady@redhat.com> - 1.28b-1
- Latest upstream

* Thu Jan 22 2015 Pádraig Brady <pbrady@redhat.com> - 1.19b-1
- Latest upstream

* Mon Jan 19 2015 Richard W.M. Jones <rjones@redhat.com> - 1.15b-1
- New upstream version 1.15b (RHBZ#1177434).

* Tue Dec 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.98b-1
- New upstream version 0.98b (RHBZ#1172581).
- Rename afl-plot.sh script to afl-plot.

* Mon Dec  8 2014 Richard W.M. Jones <rjones@redhat.com> - 0.88b-1
- New upstream version 0.88b (RHBZ#1170943).
- Add afl-plot.sh script.  This requires gnuplot, but it gives a
  suitable error message if gnuplot is not installed, so don't
  add a dependency.

* Sun Nov 30 2014 Pádraig Brady <pbrady@redhat.com> - 0.78b-1
- Latest upstream

* Mon Nov 17 2014 Richard W.M. Jones <rjones@redhat.com> - 0.50b-2
- Don't use epoch in requires.

* Sun Nov 16 2014 Richard W.M. Jones <rjones@redhat.com> - 0.50b-1
- New upstream version 0.50b.
- Remove 'sed' dependency as it is no longer used.
- Rebase CFLAGS patch.
- Add clang wrapper as a subpackage.

* Sat Nov 15 2014 Richard W.M. Jones <rjones@redhat.com> - 0.48b-1
- New upstream version 0.48b.
- Fix: https://code.google.com/p/american-fuzzy-lop/issues/detail?id=13

* Sat Nov 15 2014 Richard W.M. Jones <rjones@redhat.com> - 0.47b-1
- New upstream version 0.47b.
- Use stable Source URL.
- Remove parallel fix which is now upstream.

* Fri Nov 14 2014 Richard W.M. Jones <rjones@redhat.com> - 0.46b-1
- New upstream version 0.46b.
- Ditch USE_64BIT/CONF_64BIT.
- Package now owns afl_helper_path.
- Parallel builds now work, and make uses _smp_mflags.
- Uses CFLAGS optflags.
- Include (some) experimental scripts.

* Thu Nov 13 2014 Richard W.M. Jones <rjones@redhat.com> - 0.45b-1
- Initial packaging of afl.
