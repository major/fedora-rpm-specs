%global		module		Bonmin
%global		with_asl	1
%global		with_mpi	0

Name:		coin-or-%{module}
Summary:	Basic Open-source Nonlinear Mixed INteger programming
Version:	1.8.9
Release:	4%{?dist}

# EPL-1.0: the project as a whole
# SMLNJ: Bonmin/src/Interfaces/Ampl/sos_kludge.cpp
License:	EPL-1.0 AND SMLNJ
URL:		https://projects.coin-or.org/%{module}
Source0:	https://github.com/coin-or/Bonmin/archive/releases/%{version}/%{module}-%{version}.tar.gz
BuildRequires:	coin-or-Cgl-doc
BuildRequires:	coin-or-Clp-doc
BuildRequires:	coin-or-Ipopt-common
%if %{with_mpi}
BuildRequires:	coin-or-Ipopt-openmpi-devel
%else
BuildRequires:	pkgconfig(ipopt)
%endif
BuildRequires:	doxygen-latex
BuildRequires:	gcc-c++
BuildRequires:	help2man
BuildRequires:	make
%if %{with_asl}
BuildRequires:	asl-devel
%endif
%if %{with_mpi}
BuildRequires:	pkgconfig(ompi)
BuildRequires:	scalapack-openmpi-devel
BuildRequires:	openssh-clients
%endif
BuildRequires:	pkgconfig(cbc)
BuildRequires:	tex(tex4ht.sty)
BuildRequires:	tex(threeparttable.sty)

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Fix mixed signed/unsigned operations
Patch1:		%{name}-sign.patch

# https://github.com/coin-or/Bonmin/issues/24
Patch2:         %{name}-bug24.patch

# Fix Modern C issues in the configure script
Patch3:         %{name}-configure-c99.patch

%global _docdir_fmt %{name}

%description
Bonmin (Basic Open-source Nonlinear Mixed INteger programming) is an
experimental open-source C++ code for solving general MINLP (Mixed Integer
NonLinear Programming) problems of the form:

   min     f(x)

s.t.	   g_L <= g(x) <= g_U
	   x_L <=  x   <= x_U
	   x_i in Z for all i in I and,
	   x_i in R for all i not in I.

where f(x): R^n --> R, g(x): R^n --> R^m are twice continuously differentiable
functions and I is a subset of {1,..,n}.

Bonmin features several algorithms

  * B-BB is a NLP-based branch-and-bound algorithm,
  * B-OA is an outer-approximation decomposition algorithm,
  * B-QG is an implementation of Quesada and Grossmann's branch-and-cut
    algorithm,
  * B-Hyb is a hybrid outer-approximation based branch-and-cut algorithm. 

The algorithms in Bonmin are exact when the functions f and g are convex;
in the case where f or g or both are non-convex they are heuristics.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Cbc-devel%{?_isa}
Requires:	coin-or-Cgl-devel%{?_isa}
%if %{with_mpi}
Requires:	coin-or-Ipopt-openmpi-devel%{?_isa}
%else
Requires:	coin-or-Ipopt-devel%{?_isa}
%endif
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Cgl-doc
Requires:	coin-or-Clp-doc
Requires:	coin-or-Ipopt-common
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n %{module}-releases-%{version}

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @BONMINLIB_PCLIBS@/\nLibs.private:&/' Bonmin/bonmin.pc.in

%build
%if %{with_mpi}
%_openmpi_load
%endif
%configure	\
%if %{with_asl}
	--with-asl-lib="-lasl -lipoptamplinterface" \
	--with-asl-incdir="%{_includedir}/asl"
%endif

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all
%make_build -C Bonmin doxydoc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_pkgdocdir}/LICENSE
cp -a Bonmin/{AUTHORS,README} Bonmin/doxydoc/{bonmin_doxy.tag,html} \
  %{buildroot}%{_pkgdocdir}
mkdir -p %{buildroot}%{_mandir}/man1
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N \
  Bonmin/src/Apps/.libs/bonmin > %{buildroot}%{_mandir}/man1/bonmin.1

%check
%if %{with_mpi}
%_openmpi_load
%endif
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH make test

%files
%license LICENSE
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/README
%{_bindir}/bonmin
%{_libdir}/libbonmin.so.4
%{_libdir}/libbonmin.so.4.*
%if %{with_asl}
%{_libdir}/libbonminampl.so.4
%{_libdir}/libbonminampl.so.4.*
%endif
%{_mandir}/man1/bonmin.1*

%files devel
%{_includedir}/coin/*
%{_libdir}/libbonmin.so
%{_libdir}/pkgconfig/bonmin.pc
%if %{with_asl}
%{_libdir}/libbonminampl.so
%{_libdir}/pkgconfig/bonminamplinterface.pc
%endif

%files doc
%{_pkgdocdir}/html/
%{_pkgdocdir}/bonmin_doxy.tag

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec  4 2024 Jerry James <loganjerry@gmail.com> - 1.8.9-3
- Rebuild for asl 20241111

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Jerry James <loganjerry@gmail.com> - 1.8.9-1
- Release 1.8.9
- Convert License to SPDX
- Drop upstreamed patches: -typo, -clear, -bool, -assertions, -fix_iFP_Ecp
- BR asl-devel instead of mp-devel
- Stop building for 32-bit x86

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.8.8-12
- Fix rhbz#2165475

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Florian Weimer <fweimer@redhat.com> - 1.8.8-10
- Port configure script to C99

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.8.8-7
- Patched for upstream bug #24

* Tue Sep 21 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.8.8-6
- Rebuild for Ipopt-3.14.4

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Jerry James <loganjerry@gmail.com> - 1.8.8-4
- Add upstream patches: -clear, -bool, and -assertions (bz 1956936)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 2020 Jerry James <loganjerry@gmail.com> - 1.8.8-1
- Release 1.8.8
- BR help2man and generate a man page for the binary
- Make the -doc subpackage be arch-specific to work around FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 1.8.7-2
- Correct license from CPL to EPL-1.0
- Eliminate unnecessary BRs and Rs
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Add doxygen documentation to the -doc subpackage
- Package doxygen tag file to enable cross-linking

* Tue Apr 09 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.8.7-1
- Release 1.8.7
- Avoid mixed use of %%doc and %%docdir

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.8.6-1
- Release 1.8.6

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.8.4-15
- Rebuild for Ipopt-3.12.10

* Fri Feb 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.8.4-14
- Rebuild for Ipopt-3.12.9
- Rebuild against openblas

* Wed Feb 21 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.8.4-13
- Add gcc gcc-c++ BR

* Thu Feb 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.8.4-12
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 29 2017 Antonio Trande <sagitterATfedoraproject.org> - 1.8.4-10
- Rebuild for MUMPS-5.1.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Antonio Trande <sagitterATfedoraproject.org> - 1.8.4-7
- Rebuild for MUMPS-5.1.1 (after a bug-fix)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Apr  5 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.4-5
- Rebuild for newer mumps

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.4-3
- rebuild (Power64)

* Tue Aug 02 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.4-2
- Rebuild for newer mumps

* Wed Mar 16 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.4-1
- Update to latest upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.1-7
- Correct docs listed in main package (#1239155).

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.1-6
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Feb 22 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8.1-1
- Update to latest upstream release.
- Add asl solver and openmpi build conditionals.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.7.4-2
- Add texlive as explicit build requires.

* Sat Apr 19 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.7.4-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.0-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.0-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.0-2
- Rename package to coin-or-Bonmin.
- Do not package Thirdy party data or data without clean license.

* Sat Sep 29 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.0-1
- Initial coinor-Bonmin spec.
