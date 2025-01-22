Name:           mpqc
Summary:        Ab-inito chemistry program
Version:        2.3.1
Release:        63%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.mpqc.org/
Source0:        http://downloads.sourceforge.net/mpqc/%{name}-%{version}.tar.bz2
Source1:        bash-script-noarch
Patch0:         mpqc-2.3.1-mdv-fix-wfn-lib.patch
Patch1:         mpqc-2.3.1-format-security.patch
# C++11 build fix
Patch2:         mpqc-2.3.1-cpp11-constexpr.patch
# C23 strict function prototype fix
Patch3:         mpqc-2.3.1-c23-function-prototype.patch
# C++17 build fix: remove deprecated exception specification
Patch4:         mpqc-2.3.1-cpp17-exception-specification.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libtool flex bison
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-gfortran perl-generators tk doxygen
BuildRequires:  libint-devel
BuildRequires:  flexiblas-devel

%description
MPQC is the Massively Parallel Quantum Chemistry Program. It computes
properties of atoms and molecules from first principles using the time
independent Schrödinger equation. It runs on a wide range of
architectures ranging from individual workstations to symmetric
multiprocessors to massively parallel computers. Its design is object
oriented, using the C++ programming language.

%package data
Summary:    Atom info and basis sets from MPQC
#Requires:   %{name}-doc = %{version}-%{release}
BuildArch:  noarch

%description data
Atom info and basis sets from MPQC.

%package doc
Summary:    HTML documentation for MPQC
BuildArch:  noarch

%description doc
This package contains the full documentation for MPQC that can be viewed
with a graphical browser like Mozilla.

%package libs
Summary:    Main libraries for %{name}
Requires:   %{name}-data = %{version}-%{release}
# Libint can have API breakage between releases
Requires:   libint(api)%{?_isa} = %{_libint_apiversion}

%description libs
This package contains the shared libraries needed to run programs
dynamically linked with %{name}, the scientific computing toolkit,
based on mpqc computational chemistry package from Sandia Labs.

%package devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and static libraries needed to
build programs linked with %{name}, the scientific computing toolkit,
based on mpqc computational chemistry package from Sandia Labs.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1 -b .cpp11
%patch -P3 -p1 -b .c23
%patch -P4 -p1 -b .cpp17

sed -i -e 's,molrender.in,%{_datadir}/molrender/molrender.in,g' src/bin/molrender/tkmolrender.in
sed -i -e 's,prefix/lib,prefix/%{_lib},g' configure.in
# fixup for modern autoreconf
mv configure.in configure.ac
sed -i -r -e 's/AC_DEFINE\(([^)]*)\)/AC_DEFINE([\1],1,[\1])/g' configure.ac
sed -i -r -e 's/AC_DEFINE_UNQUOTED\(([^,]*),([^)]*)\)/AC_DEFINE_UNQUOTED([\1],\2,[\1])/g' configure.ac
sed -i -r -e 's/AC_DEFINE_DIR\(([^,]*),([^)]*)\)/AC_DEFINE_DIR([\1],\2,[\1])/g' configure.ac
sed -i -r -e 's/AC_CANONICAL_SYSTEM/AC_CANONICAL_SYSTEM\nAC_DEFINE([SHMTYPE], [void *], [data type for shmat])/g' configure.ac
sed -i -r -e 's/AC_DEFINE\(\[CXX_RESTRICT\],1,\[CXX_RESTRICT\]\)/AC_DEFINE([restrictxx],[restrict],[have restrict keyword]),AC_DEFINE([restrictxx],[],[do not have restrict keyword])/g' configure.ac
# Make configure.ac c99 conformant, -Werror=implicit-int -Werror=implicit-function-declaration
sed -i -e '\@main.*FF@s|main|extern void FF(void); int main|' configure.ac
rm -f lib/autoconf/libtool.m4
# end autoreconf fixup
cat >molrender.desktop << EOF
[Desktop Entry]
Name=Molrender
Comment=Graphically render 3D molecules
Exec=%{_bindir}/tkmolrender
Icon=applications-science
Terminal=false
Type=Application
Categories=Education;Science;Chemistry;Physics;
Version=1.0
EOF

%build
export F77=gfortran
autoreconf -v -f -i -I lib/autoconf

%configure --enable-shared --disable-static \
    --enable-threads --disable-parallel \
    --includedir="%{_includedir}/mpqc"  \
    --with-cxx-optflags="$CXXFLAGS"     \
    --with-cc-optflags="$CFLAGS" \
    --with-libs="-lflexiblas"
sed -i 's|.rpath .libdir||g' bin/sc-config
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
cd doc
make
make man1
make man3

%install
make installroot="%{buildroot}" INSTALL="install -p" install
make installroot="%{buildroot}" INSTALL="install -p" install_devel
# rename some man pages with sc_ prefix
find doc/man/man3 -type f | grep -v '/sc' | while read a; do
    m=$(basename $a)
    d=$(dirname $a)
    mv "$a" "$d/sc_$m"
done
# install the man pages
mkdir %{buildroot}%{_mandir}
cp -r -p doc/man/* %{buildroot}%{_mandir}
install -D -p -m 644  src/bin/molrender/molrender.in %{buildroot}%{_datadir}/molrender/molrender.in
install -D -p -m 644  molrender.desktop %{buildroot}%{_datadir}/applications/molrender.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/molrender.desktop
find %{buildroot}%{_libdir} -name *.la -exec rm -rf {} \;
find %{buildroot}%{_libdir} -name *.so.* -exec chmod 755 {} \;
sed -i -e "1,1s,^.*$,#!/usr/bin/perl," %{buildroot}%{_bindir}/sc-mkf77sym
sed -i -e "1,1s,^.*$,#!/usr/bin/perl -I%{_datadir}/mpqc/${_version}/perl," %{buildroot}%{_bindir}/chkmpqcout
chmod 755 %{buildroot}%{_bindir}/chkmpqcout

# Fix up sc-config all_libs
sed -i %{buildroot}%{_bindir}/sc-config \
	-e 's|^LIBSUF=la$|LIBSUF=so|' \
	-e '\@all_sclibs@s|\(lib[^ \t][^ \t]*\)\.la|\1.so|g' \
	-e 's|-L[^ \t]*gcc[^ \t]*||g' \
	%{nil}

# And rename arch-dependent script to arch-dependent name
for f in \
	sc-config \
	sc-libtool \
	%{nil}
do
	mv %{buildroot}%{_bindir}/${f}{,-$(arch)}
	cat %{SOURCE1} | sed -e "s|@BINARY@|$f|" > %{buildroot}%{_bindir}/${f}
	chmod 0755 %{buildroot}%{_bindir}/${f}
done

%ldconfig_scriptlets libs

%files
%doc CHANGES CITATION README
%{_bindir}/mpqc
%{_bindir}/chkmpqcout
%{_bindir}/scls
%{_bindir}/scpr
%{_bindir}/*run
%{_mandir}/man1/mpqc*
%{_mandir}/man1/scls*
%{_mandir}/man1/scpr*
%{_bindir}/molrender
%{_bindir}/tkmolrender
%{_datadir}/molrender
%{_datadir}/applications/molrender.desktop
%{_mandir}/man1/molrender*

%files data
%{_datadir}/mpqc
%license LICENSE COPYING COPYING.LIB

%files doc
%doc doc/html
%license LICENSE COPYING COPYING.LIB

%files libs
%{_libdir}/lib*.so.*

%files devel
%{_bindir}/sc-*
%{_libdir}/lib*.so
%{_includedir}/mpqc
%{_mandir}/man1/sc-*
%{_mandir}/man3/sc*


%changelog
* Mon Jan 20 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.1-63
- Support C++17, remove deprecated exception specification

* Sun Jan 19 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.1-62
- Support C23 strict function prototype

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.1-60
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 31 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.1-58
- Update %%patch usage for recent rpm

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.1-53
- Make configure (wrt Fortran symbol detection) c99 conformant
  for -Werror=implicit-int -Werror=implicit-function-declaration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2.3.1-48
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 2.3.1-46
- Use C++14 as this code is not C++17 ready

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.1-40
- F-28: rebuild against gfortran 8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.1-35
- F-26: rebuild against gfortran 7

* Fri May  6 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.1-34
- Fix up sc-config all_sclibs
- Rename arch-dependent scripts into arch-dependent names
- Kill -doc dependency from -data

* Sun Apr 24 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.1-33
- C++11 build fix by using constexpr

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.1-30
- Rebuilt for GCC 5 C++11 ABI change

* Thu Sep 11 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.1-29
- Libint require needs to be in -libs, not main package.

* Thu Sep 11 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.1-28.1
- Forgot to do buildroot override.

* Tue Sep 09 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.1-28
- Requires: libint(api).

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.3.1-26
- Fix FTBFS with -Werror=format-security (#1106244)
- Update to recent packaging guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 23 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.1-24
- Fix build against new atlas.
- Rebuild against libint.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.3.1-22
- Perl 5.18 rebuild

* Fri Mar 29 2013 Carl Byington <carl@five-ten-sg.com> 2.3.1-21
- add autoreconf for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.3.1-19
- Rebuild due to changed libint.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-17
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Carl Byington <carl@five-ten-sg.com> 2.3.1-14
- rebuild for libint changes

* Wed Jul 07 2010 Carl Byington <carl@five-ten-sg.com> 2.3.1-13
- Subpackage Licensing, main package requires -libs to get
  license files. -data requires -doc with another copy of the
  license files.

* Fri Jan 08 2010 Carl Byington <carl@five-ten-sg.com> 2.3.1-12
- cp -p to preserve time stamps.
- remove assumption that mandir = datadir/man

* Wed Jan 06 2010 Carl Byington <carl@five-ten-sg.com> 2.3.1-11
- rename some man pages with sc_ prefix

* Wed Jan 06 2010 Carl Byington <carl@five-ten-sg.com> 2.3.1-10
- remove rpath from sc-config script
- move include files down one level into mpqc directory

* Tue Jan 05 2010 Carl Byington <carl@five-ten-sg.com> 2.3.1-9
- remove rpath from binaries
- remove patch backups
- use rpm build compiler flags

* Mon Jan 04 2010 Carl Byington <carl@five-ten-sg.com> 2.3.1-8
- use blas and lapack from atlas.

* Sat Jan 02 2010 Carl Byington <carl@five-ten-sg.com> 2.3.1-7
- add libint-devel to speed up computations.
- drop mpich2-devel for now.
- add atlas-devel

* Wed Dec 09 2009 Carl Byington <carl@five-ten-sg.com> 2.3.1-6
- install -p to preserve timestamps
- trim changelog

* Wed Dec 09 2009 Carl Byington <carl@five-ten-sg.com> 2.3.1-5
- reset release to -5, renumber older releases to compensate
  for typo in release numbers, started at -11 rather than -1.

* Sat Dec 05 2009 Carl Byington <carl@five-ten-sg.com> 2.3.1-4
- disable parallel, did not help with ghemical anyway, and
  conflicts with current mpich.

* Thu Dec 03 2009 Carl Byington <carl@five-ten-sg.com> 2.3.1-3
- re-enable parallel to try to use multiple cpus.

* Wed Dec 02 2009 Carl Byington <carl@five-ten-sg.com> 2.3.1-2
- merge molrender subpackage into main package
- remove static libraries
- fix permissions on installed shared libraries
- trim changelog
- move license file to -libs package so it is always installed

* Sun Nov 29 2009 Carl Byington <carl@five-ten-sg.com> 2.3.1-1
- convert to fedora compatible spec file
- convert spec file to utf8 coding
- use applications-science for molrender icon
- install sample molrender.in file
- patch tkmolrender to reference the installed molrender.in
- add buildrequires desktop-file-utils
- changes for fedora review

* Wed Oct 14 2009 Guillaume Bedot <littletux@mandriva.org> 2.3.1-8mdv2010.0
- Revision: 457268
- Fix linkage and sc-config
