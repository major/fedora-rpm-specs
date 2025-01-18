%global		module		OS
%global		giturl		https://github.com/coin-or/OS

%global		with_asl	1
%global		with_mpi	0

Name:		coin-or-%{module}
Summary:	Optimization Services
Version:	2.10.3
Release:	17%{?dist}
License:	EPL-1.0
URL:		http://projects.coin-or.org/%{module}
VCS:		git:%{giturl}.git
Source0:	%{giturl}/archive/releases/%{version}/%{module}-releases-%{version}.tar.gz
BuildRequires:	bison
BuildRequires:	coin-or-Bcp-doc
BuildRequires:	coin-or-Couenne-doc
BuildRequires:	csdp-devel
BuildRequires:	doxygen
BuildRequires:	dos2unix
BuildRequires:	flex
BuildRequires:	gcc-c++
BuildRequires:	libsoplex-devel
BuildRequires:	make
BuildRequires:	pkgconfig(bcp)
BuildRequires:	pkgconfig(couenne)
BuildRequires:	pkgconfig(cppad)
BuildRequires:	pkgconfig(symphony)
%if %{with_asl}
BuildRequires:	asl-devel
%endif
%if %{with_mpi}
BuildRequires:	openmpi-devel
BuildRequires:	scalapack-openmpi-devel
BuildRequires:	openssh-clients
%endif

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Bad #define generated if svnversion is available
Patch1:		%{name}-svnversion.patch

# Correct build when regenerating parsers
Patch2:		%{name}-flex-bison.patch

# Fix bad code in the parser
Patch4:		%{name}-parser.patch

# Delete a bad vector initializer; explicit initialization is not needed
# Fix comparison of OSMatrix objects
Patch5:		%{name}-OSMatrix.patch

# Fix use of incorrect variables in a unit test
Patch6:		%{name}-test.patch

# Do not catch polymorphic exceptions by value
Patch7:		%{name}-except.patch

# Prevent access to uninitialized values
Patch8:		%{name}-uninitialized.patch

# Fix some mixed signed/unsigned operations
Patch9:		%{name}-signed.patch

# Fix use of implicitly declared functions in the configure script
Patch10:	%{name}-configure-c99.patch

%description
The objective of Optimization Services (OS) is to provide a set of standards
for representing optimization instances, results, solver options, and
communication between clients and solvers in a distributed environment using
Web Services. This COIN-OR project provides source code for libraries and
executable programs that implement OS standards. See the Home Site
http://www.optimizationservices.org/ for more information.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Couenne-devel%{?_isa}
Requires:	cppad-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Bcp-doc
Requires:	coin-or-Couenne-doc
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains the documentation for %{name}.

%prep
%autosetup -N -n %{module}-releases-%{version}
dos2unix OS/src/OSParsers/OSParseosil.l
%autopatch -p1

# Fix a small typo
sed -i 's/CyLP/DyLP/' configure

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @OSLIB_PCLIBS@/\nLibs.private:&/' OS/os.pc.in

%build
# --with-flex-bison is to force parser regeneration; and ensure the
# package is fully rebuildable from sources.
%configure --enable-openmp --with-flex-bison \
%if %{with_asl}
	--with-asl-lib="-lasl -lipoptamplinterface -lbonminampl -lmpfr -lgmp -lz-ng" \
	--with-asl-incdir=%{_includedir}/asl \
%endif
	--with-csdp-lib="-lsdp" \
	--with-csdp-incdir=%{_includedir}/csdp --with-gnu-ld \
	ADD_CXXFLAGS=" -I%{_includedir}/asl -std=gnu++14"

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# GCC normally assumes that, in a method, this != NULL.  However, the code
# requires that, in some situations, this == NULL.  Tell GCC not to optimize
# those checks away.  The code should really be fixed to not need this.
export CFLAGS="%{build_cflags} -fno-delete-null-pointer-checks"
export CXXFLAGS="%{build_cxxflags} -std=gnu++14 -I%{_includedir}/asl"
make -j1 all doxydoc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

# Remove unused directory
rm -rf %{buildroot}%{_datadir}/coin

# The pkgconfig file lists cppad as a dependency multiple times
sed -i 's/\([[:alpha:]]\) cppad/\1/g' %{buildroot}%{_libdir}/pkgconfig/os.pc

%check
%if %{with_mpi}
%_openmpi_load
%endif
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%files
%license LICENSE
%doc AUTHORS README
%{_bindir}/OSAmplClient
%{_bindir}/OSSolverService
%{_libdir}/libOS.so.6
%{_libdir}/libOS.so.6.10.3

%files devel
%{_includedir}/coin/*
%{_libdir}/libOS.so
%{_libdir}/pkgconfig/os.pc

%files doc
%doc doxydoc/* OS/doc/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec  4 2024 Jerry James <loganjerry@gmail.com> - 2.10.3-16
- Rebuild for asl 20241111

* Mon Sep 23 2024 Jerry James <loganjerry@gmail.com> - 2.10.3-15
- Rebuild for soplex 7.1.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Jerry James <loganjerry@gmail.com> - 2.10.3-13
- Rebuild for soplex 7.1.0

* Wed Jun 19 2024 Jerry James <loganjerry@gmail.com> - 2.10.3-12
- Rebuild for soplex 7.0.1

* Wed Mar 13 2024 Jerry James <loganjerry@gmail.com> - 2.10.3-11
- Rebuild for soplex 7.0.0

* Wed Jan 31 2024 Jerry James <loganjerry@gmail.com> - 2.10.3-10
- Build with soplex support
- Verify that License is valid SPDX
- BR asl-devel instead of mp-devel
- Stop building for 32-bit x86
- Avoid deprecated %%patchN usage
- Fix damaged changelog entries

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Antonio Trande <sagitter@fedoraproject.org> - 2.10.3-7
- Rebuild for cppad-20240000.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Florian Weimer <fweimer@redhat.com> - 2.10.3-5
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.10.3-1
- Rebuilt for Ipopt-3.14.4
- Release 2.10.3

* Thu Sep 16 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.10.2-9
- Rebuilt for Ipopt-3.14.3

* Thu Jul 29 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
- Explicitate the flag of ALS's include directory

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 2.10.2-6
- Force C++14 as the code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 2020 Jerry James <loganjerry@gmail.com> - 2.10.2-4
- Make the -doc subpackage be arch-specific to work around FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 2.10.2-2
- Eliminate unnecessary BRs and Rs
- Add -csdp, -parser, -OSMatrix, and -test patches
- Add -fno-delete-null-pointer-checks to build flags to prevent crashes due to
  invalid optimizations
- Build with csdp support
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Filter out unnecessary Libs values from pkgconfig files
- Package doxygen tag file to enable cross-linking

* Tue Apr 09 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.10.2-1
- Release 2.10.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.10.1-18
- Remove Group tags

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.10.1-16
- Rebuild for Ipopt-3.12.10

* Fri Feb 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.10.1-15
- Rebuild for Ipopt-3.12.9
- Rebuild against openblas

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.10.1-14
- Add gcc gcc-c++ BR

* Fri Feb 16 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.10.1-13
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 02 2017 Antonio Trande <sagitterATfedoraproject.org> - 2.10.1-11
- Rebuild for MUMPS-5.1.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Antonio Trande <sagitterATfedoraproject.org> - 2.10.1-8
- Define %%check on fedora < 26
- Downgrade make job to 1

* Thu Jun 29 2017 Antonio Trande <sagitterATfedoraproject.org> - 2.10.1-7
- Rebuild for MUMPS-5.1.1 (after a bug-fix)
- Exclude test on armv7hl

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Apr  5 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.10.1-5
- Rebuild for newer mumps

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.10.1-3
- Rebuild (Power64)

* Tue Aug 02 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.10.1-2
- Rebuild for newer mumps

* Thu Mar 17 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.10.1-1
- Update to latest upstream release
- Correct FTBFS in rawhide (#1307390)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.3-5
- Correct docs listed in main package (#1239155).

* Sun Jun 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.3-4
- Full rebuild of coin-or stack.
- Correct file listing when asl is disabled.

* Fri Jun 19 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.3-3
- Remove non functional attempt to prevent overlink.

* Mon Jun 15 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.3-2
- Build documentation (#894609#c11)
- Do not overlink generated library (#894609#c11)
- Update file list when asl is disabled

* Sun Jun 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.3-1
- Update to latest upstream release
- Regenerate parsers (#894609#c7)

* Mon Apr 13 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.2-2
- Add missing bzip2, mp and zlib devel build requires
- Remove non needed doxygen build requires

* Sat Apr 11 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.2-1
- Update to latest upstream release

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.6.0-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.6.0-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.6.0-2
- Rename package to coin-or-OS.
- Do not package Thirdy party data or data without clean license.

* Sat Sep 29 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.6.0-1
- Initial coinor-OS spec.
