%global		module		SYMPHONY
%global		giturl		https://github.com/coin-or/%{module}

Name:		coin-or-%{module}
Summary:	Solver for mixed-integer linear programs
Version:	5.7.2
Release:	2%{?dist}

# The project as a whole is licensed EPL-2.0.  However, many source files still
# claim to be licensed EPL-1.0.  This is probably an upstream oversight.
License:	EPL-2.0 AND EPL-1.0
URL:		%{giturl}/wiki
VCS:		git:%{giturl}.git
Source0:	%{giturl}/archive/releases/%{version}/%{module}-%{version}.tar.gz
# The PDF manual cannot be built from source, missing BibTeX file (as of 5.6.17)
Source1:	https://coin-or.github.io/%{module}/doc/%{module}-%{version}-Manual.pdf
BuildRequires:	coin-or-Cgl-devel
BuildRequires:	coin-or-Data-miplib3
BuildRequires:	coin-or-Data-Netlib
BuildRequires:	coin-or-DyLP-devel
BuildRequires:	coin-or-Vol-devel
BuildRequires:	gcc-c++
BuildRequires:	glpk-devel
BuildRequires:	make
BuildRequires:	readline-devel

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Fix GCC warnings about aliased arguments to restrict-qualified parameters
Patch1:		%{name}-restrict.patch

Patch2:		coin-or-SYMPHONY-configure-c99.patch

%description
SYMPHONY is an open-source solver for mixed-integer linear programs (MILPs)
written in C. It can be used in three different main modes:

  * As a callable library through either the native C interface or through
    the Osi.
  * As an interactive solver using a command-line interface.
  * As a framework to build customized solvers for specific problem classes. 

SYMPHONY can be executed in either parallel (distributed or shared memory)
or sequential modes and has a number of advanced features that make it unique,
including the ability to

  * solve biobjective MILPs,
  * warm start the solution procedure, and
  * perform basic sensitivity analyses. 

SYMPHONY links to a number of other COIN projects for additional
functionality, including:

   * Clp (the default solver for LP relaxations)
   * Osi (an interface to alternative solvers for solving LP relaxations)
   * Cgl (for cut generation)
   * CoinUtils (for reading in MPS files and various utilities)

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Osi-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{module}-releases-%{version}

%build
%configure \
  --enable-draw-graph \
  --enable-sensitivity-analysis \
  --with-glpk_incdir=%{_includedir} \
  --with-glpk-lib=-lglpk \
  --with-gmpl

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,sym_addlibs.txt}
cp -p %{SOURCE1} %{buildroot}%{_docdir}/%{name}

# We do not build the application library, so do not ship its pkgconfig file
rm -f %{buildroot}%{_libdir}/pkgconfig/symphony-app.pc

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ -lglpk//' %{buildroot}%{_libdir}/pkgconfig/symphony.pc

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%ldconfig_scriptlets

%files
%license LICENSE
%{_docdir}/%{name}
%{_bindir}/symphony
%{_libdir}/libOsiSym.so.3
%{_libdir}/libOsiSym.so.3.*
%{_libdir}/libSym.so.3
%{_libdir}/libSym.so.3.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libOsiSym.so
%{_libdir}/libSym.so
%{_libdir}/pkgconfig/osi-sym.pc
%{_libdir}/pkgconfig/symphony.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Jerry James <loganjerry@gmail.com> - 5.7.2-1
- Version 5.7.2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Jerry James <loganjerry@gmail.com> - 5.7.1-1
- Version 5.7.1
- Get source tarball from github
- Convert License to SPDX
- Stop building for 32-bit x86

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Florian Weimer <fweimer@redhat.com> - 5.6.17-9
- Port configure script to C99

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 5.6.17-1
- Update to latest upstream release
- Update project URL
- Change License from EPL to EPL-1.0
- Eliminate unnecessary BRs and Rs
- Package the manual
- Eliminate rpath from the library
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Filter out unnecessary Libs values from pkgconfig files

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 5.6.14-8
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 5.6.14-3
- Rebuild for glpk 4.61

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 17 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.6.14-1
- Update to latest upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.6.8-4
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.6.8-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Feb 22 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.6.8-1
- Update to latest upstream release.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.5.7-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.6-1
- Update to latest upstream release.

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.5-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.5-2
- Rename package to coin-or-SYMPHONY.
- Do not package Thirdy party data or data without clean license.

* Thu Sep 27 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.4.5-1
- Initial coinor-SYMPHONY spec.
