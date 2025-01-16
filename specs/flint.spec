Name:           flint
Version:        3.1.2
Release:        3%{?dist}
Summary:        Fast Library for Number Theory

# LGPL-3.0-or-later: the project as a whole
# LGPL-2.1-or-later: src/longlong.h, src/fmpz/is_perfect_power.c,
#   src/generic_files/clz_tab.c, src/mpn_extras/get_d.c
# GPL-2.0-or-later: src/dirichlet/char_index.c, src/dirichlet/index_char.c
# LGPL-3.0-or-later OR GPL-2.0-or-later: src/mpn_extras/asm-defs.m4,
#   src/mpn_extras/broadwell/x86_64-defs.m4
# BSD-2-Clause: src/bernoulli/mod_p_harvey.c
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND (LGPL-3.0-or-later OR GPL-2.0-or-later) AND BSD-2-Clause
URL:            https://www.flintlib.org/
VCS:            git:https://github.com/flintlib/flint.git
Source:         https://www.flintlib.org/%{name}-%{version}.tar.gz
# Fix noreturn attribute in C23 mode
Patch:          https://github.com/flintlib/flint/pull/2116.patch

BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  ntl-devel
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  tex(latex)

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# This can be removed when F43 reaches EOL
Obsoletes:      antic < 3.0.0
Obsoletes:      arb < 3.0.0
Obsoletes:      arb-doc < 3.0.0
Obsoletes:      flint-static < 3.0.0
Provides:       antic = %{version}-%{release}
Provides:       arb = %{version}-%{release}
Provides:       arb-doc = %{version}-%{release}
Provides:       flint-static = %{version}-%{release}

%description
FLINT is a C library for doing number theory, written by William Hart
and David Harvey.


%package        devel
Summary:        Development files for FLINT
Requires:       %{name}%{?_isa} = %{version}-%{release}

# This can be removed when F43 reaches EOL
Obsoletes:      antic-devel < 3.0.0
Provides:       antic-devel = %{version}-%{release}
Obsoletes:      arb-devel < 3.0.0
Provides:       arb-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# sanitize header files
ln -sf $PWD flint
# sanitize references to external headers
for fil in $(find src -name \*.c -o -name \*.h -o -name \*.in); do
  sed -ri.orig 's/"((cblas|gc|gmp|math|mpfr|string)\.h)"/<\1>/' $fil
  fixtimestamp $fil
done
# sanitize references to project headers
for fil in $(find src -name \*.c -o -name \*.h); do
  sed -ri.orig 's@"(\.\./)?([^"]+\.h])"@<flint/\2>@' $fil
  fixtimestamp $fil
done
# "

# Use the classic sphinx theme
sed -i "s/'default'/'classic'/" doc/source/conf.py

# Look for flexiblas
sed -i 's/openblas/flexiblas/' configure


%build
%configure \
  --disable-arch \
  --disable-static \
  --with-blas-include=%{_includedir}/flexiblas \
  --with-ntl-include=%{_includedir}/NTL
%make_build

# Build the documentation
make -C doc html


%install
%make_install


%check
make check


%files
%doc AUTHORS
%doc README.md
%license COPYING COPYING.LESSER
%{_libdir}/libflint.so.19*


%files devel
%doc doc/build/html
%{_includedir}/flint/
%{_libdir}/libflint.so
%{_libdir}/pkgconfig/flint.pc


%changelog
* Tue Jan 14 2025 Jerry James <loganjerry@gmail.com> - 3.1.2-3
- Add patch to fix GCC 15 build

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 19 2024 Jerry James <loganjerry@gmail.com> - 3.1.2-1
- Version 3.1.2
- Switch back to autotools at upstream request
- Drop unneeded popcount patch

* Wed Mar 13 2024 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- Version 3.1.0
- License: add LGPL-3.0-or-later
- License: add (LGPL-3.0-or-later OR GPL-2.0-or-later)
- Drop the static subpackage, unused in Fedora
- Drop the C++ interface, now a separate project
- Build with cmake
- Stop building the GC-enabled library, not supported by the cmake build
- FLINT now includes the formerly separate arb and antic packages

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 10 2023 Jerry James <loganjerry@gmail.com> - 2.9.0-5
- Use a more reliable way of detecting CPU features

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2.9.0-2
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 2.9.0-1
- Version 2.9.0
- Add -test patch to work around broken tests

* Tue Apr 26 2022 Jerry James <loganjerry@gmail.com> - 2.8.5-1
- Version 2.8.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 17 2021 Jerry James <loganjerry@gmail.com> - 2.8.4-1
- Version 2.8.4
- Drop upstreamed -sphinx3.5 patch

* Sat Oct  2 2021 Jerry James <loganjerry@gmail.com> - 2.8.1-1
- Version 2.8.1

* Tue Aug 24 2021 Jerry James <loganjerry@gmail.com> - 2.8.0-1
- Version 2.8.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Jerry James <loganjerry@gmail.com> - 2.7.1-1
- Version 2.7.1

* Tue Jun 29 2021 Jerry James <loganjerry@gmail.com> - 2.6.3-4
- Rebuild for ntl 11.5.1

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 2.6.3-3
- Add -sphinx3.5 patch to fix FTBFS with Sphinx 3.5 (bz 1930919)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Jerry James <loganjerry@gmail.com> - 2.6.3-1
- Version 2.6.3

* Fri Jul 31 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-1
- Version 2.6.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jerry James <loganjerry@gmail.com> - 2.6.1-1
- Version 2.6.1
- Drop patches added in 2.6.0-1
- Drop no longer needed -latex patch

* Wed Jul 22 2020 Tom Stellard <tstellar@redhat.com> - 2.6.0-2
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- Version 2.6.0
- Add upstream patches to fix bugs discovered after release:
  -fmpq-poly-add-fmpq.patch, -nmod-mpolyn-interp-crt-lg-poly.patch,
  -fmpz-mpoly-div-monagan-pearce.patch, -fmpz-poly-factor.patch,
  -fmpz-mod-poly-gcdiv-euclidean.patch
- Disable tests on 32-bit arches until upstream can diagnose a failure

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 2.5.2-30
- Rebuild for ntl 11.4.3

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 2.5.2-29
- Rebuild for mpfr 4

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 2.5.2-28
- Rebuild for ntl 11.3.4
- Add -pie-hardening-conflict patch from sagemath

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 Jerry James <loganjerry@gmail.com> - 2.5.2-26
- Drop the workaround for bz 1555151, now fixed

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 2.5.2-24
- Rebuild for ntl 11.3.0
- Build with openblas instead of atlas

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 2.5.2-23
- Rebuild for ntl 11.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 2.5.2-21
- Rebuild for ntl 11.1.0

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 2.5.2-20
- Rebuild for ntl 11.0.0
- Add i686 to the architectures with slow compilers due to FTBFS (bz 1555753)
- Work around apparent compiler bug on 32-bit arm (bz 1555151)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 2.5.2-18
- Rebuild for ntl 10.5.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 2.5.2-15
- Rebuild for ntl 10.3.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-13
- Rebuild for ntl 10.1.0

* Wed Aug 31 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-12
- Rebuild for ntl 9.11.0

* Thu Aug 11 2016 Michal Toman <mtoman@fedoraproject.org> - 2.5.2-11
- HAVE_FAST_COMPILER=0 on 32-bit MIPS (bz 1366672)

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-10
- Rebuild for ntl 9.10.0

* Thu Jun  2 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-9
- Rebuild for ntl 9.9.1

* Fri Apr 29 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-8
- Rebuild for ntl 9.8.0

* Fri Mar 18 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-7
- Rebuild for ntl 9.7.0

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-6
- Rebuild for ntl 9.6.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 2.5.2-4
- Rebuild for ntl 9.6.2

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 2.5.2-3
- Rebuild for ntl 9.4.0

* Sat Oct 10 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.5.2-2
- Correct detection of gcc 5 as a fast compiler (#1270271)

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 2.5.2-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 2.4.5-4
- Rebuild for ntl 9.1.1

* Sat May  9 2015 Jerry James <loganjerry@gmail.com> - 2.4.5-3
- Rebuild for ntl 9.1.0

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.5-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 20 2015 Jerry James <loganjerry@gmail.com> - 2.4.5-1
- New upstream release

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 2.4.4-6
- Rebuild for ntl 8.1.2

* Mon Jan 12 2015 Jerry James <loganjerry@gmail.com> - 2.4.4-5
- Rebuild for ntl 8.1.0

* Mon Sep 22 2014 Jerry James <loganjerry@gmail.com> - 2.4.4-4
- Rebuild for ntl 6.2.1
- Fix license handling

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Jakub Čajka <jcajka@redhat.com> - 2.4.4-2
- Disable tests that exhaust memory on s390 (bz 1123757)

* Mon Jul 21 2014 Jerry James <loganjerry@gmail.com> - 2.4.4-1
- New upstream release

* Wed Jul 16 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.4.2-4
- Fix FTBFS with GMP 6.0 (#1107245)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 2.4.2-2
- Rebuild for ntl 6.1.0
- The -devel subpackage requires ntl-devel

* Mon Mar 17 2014 Jerry James <loganjerry@gmail.com> - 2.4.2-1
- New upstream release

* Mon Feb 10 2014 Jerry James <loganjerry@gmail.com> - 2.4.1-1
- New upstream release
- Enable C++ interface
- Tests now work on 32-bit systems
- Minimize the set of LaTeX BRs
- Enable verbose build
- Link with Fedora LDFLAGS
- On ARM arches, disable tests that exhaust virtual memory while compiling
- Add -fno-strict-aliasing to the test program builds, due to violations of
  the strict aliasing rules in some of the C++ tests

* Mon Aug  5 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.3-1.20130801git4b383e2
- Update to pre 2.4 snapshot that supports gmp, required by sagemath 5.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 1.6-7
- Rebuild for ntl 6.0.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-4
- Build with ntl support to have all symbols resolved.
- Force -fPIC in CFLAGS to avoid ntl link failures.

* Mon May  7 2012 Jerry James <loganjerry@gmail.com> - 1.6-3
- Update warning patch to fix bz 819333

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 1.6-2
- Rebuild for GCC 4.7

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.6-1.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 1.6-1.1
- rebuild with new gmp

* Mon Jul 18 2011 Jerry James <loganjerry@gmail.com> - 1.6-1
- New upstream release
- Build against the system zn_poly instead of the included sources
- Make sure there is no PIC code in the static archive
- Link mpQS against the shared library instead of including the library
- Fix build errors and scary warnings with gcc 4.6
- Remove unnecessary spec file elements (BuildRoot, etc.)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 26 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.5.2-1
- update to new version
- renew both patches

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Conrad Meyer <konrad@tylerc.org> - 1.2.0-1
- Bump to 1.2.0.

* Fri Mar 6 2009 Conrad Meyer <konrad@tylerc.org> - 1.0.21-1
- Bump to 1.0.21.
- Build static subpackage.

* Sat Dec 6 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.18-1
- Bump to 1.0.18.
- Patches apply with --fuzz=0.

* Sat Nov 29 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.17-1
- Initial package.
