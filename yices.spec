Name:           yices
Version:        2.6.4
Release:        5%{?dist}
Summary:        SMT solver

# The yices code is GPL-3.0-or-later.  The cudd code is BSD-3-Clause.
License:        GPL-3.0-or-later and BSD-3-Clause
URL:            http://yices.csl.sri.com/
Source0:        https://github.com/SRI-CSL/yices2/archive/Yices-%{version}.tar.gz
# The CUDD web site disappeared in 2018.  The Fedora package was retired in 2019
# when there were no more Fedora users.  Instead of resurrecting the package for
# the sole use of yices, we bundle a snapshot of the last released version.
Source1:        https://github.com/ivmai/cudd/archive/cudd-3.0.0.tar.gz
# Adapt to newer versions of cryptominisat
Patch0:         %{name}-cryptominisat.patch
# Get rid of an implicit-int function declaration in a configure check.
Patch1:         implicit-int.patch

BuildRequires:  cadical-devel
BuildRequires:  cryptominisat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gperf
BuildRequires:  kissat-devel
BuildRequires:  latexmk
BuildRequires:  libpoly-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  tex(latex)

# See Source1 comment
Provides:       bundled(cudd) = 3.0.0

%description
Yices 2 is an efficient SMT solver that decides the satisfiability of
formulas containing uninterpreted function symbols with equality, linear
real and integer arithmetic, bitvectors, scalar types, and tuples.

Yices 2 can process input written in the SMT-LIB notation (both versions
2.0 and 1.2 are supported).

Alternatively, you can write specifications using the Yices 2
specification language, which includes tuples and scalar types.

Yices 2 can also be used as a library in other software.

%package devel
Summary:        Development files for yices
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
This package contains the header files necessary for developing programs
which use yices.

%package tools
Summary:        Command line tools that use the yices library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Command line tools that use the yices library.

%package doc
Summary:        Documentation for yices
BuildArch:      noarch

%description doc
This package contains yices documentation.

%prep
%autosetup -n yices2-Yices-%{version} -a 1 -p1

# Do not try to avoid -fstack-protector
sed -i 's/@NO_STACK_PROTECTOR@//' make.include.in

# Do not override our build flags
sed -i 's/ -O3//;s/ -fomit-frame-pointer//' src/Makefile tests/unit/Makefile

# Generate the configure scripts
autoreconf -fi
cd cudd-cudd-3.0.0
autoreconf -fi
cd -

# Fix end of line encodings
sed -i 's/\r//' examples/{jinpeng,problem_with_input}.ys

# Fix permissions
sed -i 's/cp/install -m 0644/' utils/make_source_version

%build
# Build cudd
cd cudd-cudd-3.0.0
%configure CFLAGS="%{build_cflags} -fPIC" CXXFLAGS="%{build_cxxflags} -fPIC"
%make_build
cd -

#bv64_interval_abstraction depends on wrapping for signed overflow
export CFLAGS='%{build_cflags} -fwrapv'
export CXXFLAGS='%{build_cxxflags} -fwrapv'
export CPPFLAGS="-I$PWD/cudd-cudd-3.0.0/cudd -DHAVE_CADICAL -DHAVE_CRYPTOMINISAT -DHAVE_KISSAT"
export LDFLAGS="%{build_ldflags} -L$PWD/cudd-cudd-3.0.0/cudd/.libs"
export LIBS='-lcadical -lcryptominisat5 -lkissat'
%configure --enable-mcsat

guess=$(./config.guess)
if [ "%{_host}" != "$guess" ]; then
  mv configs/make.include.%{_host} configs/make.include.${guess}
fi
%make_build MODE=debug

# Build the manual
make doc

# Build the interface documentation
make -C doc/sphinx html
rm doc/sphinx/build/html/.buildinfo

%install
make install prefix=%{buildroot}%{_prefix} exec_prefix=%{buildroot}%{_prefix} \
     bindir=%{buildroot}%{_bindir} libdir=%{buildroot}%{_libdir} \
     includedir=%{buildroot}%{_includedir}/%{name} MODE=debug
rm -f %{buildroot}%{_libdir}/libyices.a
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/*.1 %{buildroot}%{_mandir}/man1

%check
make check MODE=debug

%files
%doc doc/SMT-LIB-LANGUAGE doc/YICES-LANGUAGE
%license copyright.txt LICENSE.txt
%{_libdir}/libyices.so.2*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libyices.so

%files tools
%{_bindir}/yices
%{_bindir}/yices-sat
%{_bindir}/yices-smt
%{_bindir}/yices-smt2
%{_mandir}/man1/yices.1*
%{_mandir}/man1/yices-sat.1*
%{_mandir}/man1/yices-smt.1*
%{_mandir}/man1/yices-smt2.1*

%files doc
%doc doc/manual/manual.pdf doc/sphinx/build/html examples
%license copyright.txt LICENSE.txt

%changelog
* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 2.6.4-5
- Regenerate the cudd configure script to fix FTBFS
- Convert License tag to SPDX

* Mon Nov 28 2022 Timm Bäder <tbaeder@redhat.com> - 2.6.4-5
- Get rid of an implicit int function declaration in a configure check

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Jerry James <loganjerry@gmail.com> - 2.6.4-2
- Build with kissat support

* Mon Oct 25 2021 Jerry James <loganjerry@gmail.com> - 2.6.4-1
- Version 2.6.4
- Drop upstreamed -big-endian and -sphinx3 patches
- Enable tests on 32-bit platforms

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-6
- Rebuild for cryptominisat 5.8.0

* Mon Aug  3 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-5
- Rebuild for cadical 1.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 25 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-3
- Rebuild for cryptominisat 5.7.0
- Switch to upstream's solution for sphinx 3 support

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-2
- Use native sphinx 3 support for enum instead of cenum extension (bz 1823515)

* Thu Mar 26 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-1
- Version 2.6.2
- Drop upstreamed -missing-typedef patch
- Add -big-endian patch to fix s390x build
- Add -cryptominisat5 patch to fix build with recent cryptominisat releases
- Skip tests on 32-bit platforms; some tests fail due to the limited size of a
  C integer

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Jerry James <loganjerry@gmail.com> - 2.6.1-5
- Add -missing-typedef patch to fix FTBFS with gcc 10
- Set -doc subpackage to noarch

* Fri Nov 22 2019 Jerry James <loganjerry@gmail.com> - 2.6.1-4
- Add -fwrapv to build flags; thanks to Jeff Law for the diagnosis

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 2.6.1-1
- New upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul  4 2018 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Jerry James <loganjerry@gmail.com> - 2.5.4-2
- Add a -doc subpackage
- Fix end of line encodings
- Fix permissions on yices_debug_version.c

* Mon Jan  1 2018 Jerry James <loganjerry@gmail.com> - 2.5.4-1
- Initial RPM
