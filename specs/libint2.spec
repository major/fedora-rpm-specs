# We run out of memory on the ARM builders with LTO
%ifarch %{arm}
%define _lto_cflags %{nil}
%endif
# We run out of memory on many builders since the source files are big, drop down to four threads
%define _smp_mflags -j4
# Disable x86 architectures since builders run out of memory
ExcludeArch: %{ix86}

# RPM macro directory
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# The source code the libint compiler generates is already very highly
# optimized.  Further optimization done by the compiler does not
# increase performance, but it just takes a *lot* longer to compile.
# We use -O2 for the compiler and -O1 for the library (these are given
# in configure). The common flags are
%global commonflags %(echo %{optflags} | sed "s|-O2||g")
%global optflags %commonflags -O1 -fno-var-tracking-assignments

# API version provided. Increment this whenever you change the configure time flags.
%global apiversion 1

Name:		libint2
Version:	2.9.0
Release:	5%{?dist}
Summary:	A library for efficient evaluation of electron repulsion integrals
# Generator itself is GPLv2+, generated library packaged in Fedora is LGPLv3
License:	LGPL-3.0-only
URL:		https://github.com/evaleev/libint

# Compiler sources
Source0:	https://github.com/evaleev/libint/archive/v%{version}.tar.gz
# The library sources, which are generated by the compiler. The
# compiler needs a rather recent C++11 compiler to build. Regardless
# of the C++ compiler used, the generated sources are
# identical. However, EPEL doesn't have a recent enough C++ compiler
# to be able to generate the sources. Also, if the sources are
# generated on the same run, debuginfo will turn up missing from the
# RPM (BZ #9619635). For this reason pregenerated sources are used. To
# generate the sources, run the generate-sources.sh script.
Source1:	libint-%{version}.tar.xz
# The programmers' manual is compiled from the LaTeX source by generate-sources.sh
Source2:	progman-%{version}.pdf

# The source tarball generator does not introduce all info in the CMake config for now, this patches in the missing info
Patch0:         libint-2.8.2-fedoraver.patch
# Fix location of data directory in generated CMake config
Patch1:         libint-2.9.0-datadir.patch

Provides:	libint2(api)%{?_isa} = %{apiversion}

BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  boost-devel
BuildRequires:  mpfr-devel
BuildRequires:  python3-devel
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  pybind11-devel

%description
LIBINT computes the Coulomb and exchange integrals, which in electronic
structure theory are called electron repulsion integrals (ERIs). This is by
far the most common type of integrals in molecular structure theory.

LIBINT uses recursive schemes that originate in seminal Obara-Saika method and
Head-Gordon and Pople’s variation thereof. The idea of LIBINT is to optimize
computer implementation of such methods by implementing an optimizing compiler
to generate automatically highly-specialized code that runs well on
super-scalar architectures.

%package data
Summary:	Shared data for libint2
Requires:	libint2 = %{version}-%{release}
BuildArch:      noarch

%description data
This package contains shared data for libint2.

%package doc
Summary:	Documentation for libint2
Requires:	libint2 = %{version}-%{release}
BuildArch:      noarch

%description doc
This package contains a programmer's manual and doxygen documentation
for the classes.

%package devel
Summary:	Development headers and libraries for libint2
Requires:	libint2%{?_isa} = %{version}-%{release}
# For dir ownership
Requires:       cmake
# Dependencies for compiling code
Requires:       boost-devel
Requires:       eigen3-devel
Requires:       gmp-devel
Requires:       mpfr-devel

%description devel
This package contains development headers and libraries for libint2.

%prep
%setup -q -T -b 1 -n libint-%{version}
%patch 0 -p1 -b .fedora
# Copy programmers manual
cp -p %{SOURCE2} doc/progman.pdf

%build
export CXX=g++
%cmake -DENABLE_FORTRAN=ON -DENABLE_MPFR=ON -DLIBINT2_PYTHON=ON -DLIBINT2_INSTALL_LIBDIR=%{_libdir} -DLIBINT2_INSTALL_DATADIR=%{_datadir}/%{name} -DLIBINT2_INSTALL_CMAKEDIR=%{_libdir}/cmake/%{name}
%cmake_build

%install
%cmake_install
find %{buildroot} -name *.la -delete
# Make sure libraries are executable (otherwise they are not stripped)
find %{buildroot} -name *.so* -exec chmod 755 {} \;

# Create macro file
mkdir -p %{buildroot}%{macrosdir}
cat > %{buildroot}%{macrosdir}/macros.libint2 << EOF
# Current version of libint2 is
%_libint2_apiversion %{apiversion}
EOF

# Move module file to the correct location
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/libint_f.mod %{buildroot}%{_fmoddir}/

%ldconfig_scriptlets

%files
%doc LICENSE COPYING
%{_libdir}/libint2.so.2
%{_libdir}/libint2.so.%{version}

%files data
%{_datadir}/libint2/

%files doc
%doc doc/progman.pdf

%files devel
%{macrosdir}/macros.libint2
%{_libdir}/cmake/libint2/
%{_includedir}/libint2/
%{_includedir}/libint2.h
%{_includedir}/libint2.hpp
%{_libdir}/pkgconfig/libint2.pc
%{_fmoddir}/libint_f.mod
%{_libdir}/libint2.so

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Susi Lehtola <jussilehtola@fedoraproject.org>  2.9.0-3
- Fix location of data directory in generated CMake config.

* Tue Sep 03 2024 Susi Lehtola <jussilehtola@fedoraproject.org>  2.9.0-2
- Devel package now pulls in boost, eigen3, gmp, and mpfr development
  packages that are needed to build against libint2.

* Sun Aug 18 2024 Susi Lehtola <jussilehtola@fedoraproject.org>  2.9.0-1
- Disable build on i386 architecture where the build runs out of memory.
- Update license tag to LGPL-3.0-only (generated library).
- Update to 2.9.0.

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.8.2-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 21 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.8.2-1
- Update to 2.8.2.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 21 2021 Jeff Law <law@redhat.com> - 2.6.0-10
- Disable LTO on arm

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 20 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-8
- Add BR: python3-devel.

* Tue Sep 29 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-7
- Disable buggy Eigen3 support until 2.7.0 is released.

* Sun Aug 16 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-6
- Enable Eigen3 support in build.

* Fri Aug 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-5
- Enable Fortran bindings.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.1.0-2
- Rebuilt for Boost 1.63

* Sun Jul 10 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0.

* Fri Jul 08 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.3-17.644hg
- Use pregenerated programmer's manual when not bootstrapping.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-16.644hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.0.3-15.644hg
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.0.3-14.644hg
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-13.644hg
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.0.3-12.644hg
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-11.644hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.3-10.644hg
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.0.3-9.644hg
- Rebuild for boost 1.57.0

* Tue Sep 09 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.3-8.644hg
- Provide libint2(api) and rpm macro.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-7.644hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6.644hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.0.3-5.644hg
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-4.644hg
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.0.3-3.644hg
- Rebuild for boost 1.54.0

* Thu Jul 11 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.3-1.644hg
- Use xz to compress tarballs (BZ #979817).
- Update to revision 644.

* Tue May 21 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.3-2.641hg
- Reduce maximum angular momentum for derivative ERIs, since 2nd derivatives of
  (kk|kk) takes more than 2 GB of RAM.
- Enabled g12 and g12dkh integrals.

* Thu May 16 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.3-1.641hg
- Use pregenerated tarballs only on EPEL.

* Sun May 12 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.2-2.618hg
- Switch to using a pregenerated tarball of library sources instead of
  rerunning compiler for each build, solving BZ #961963.

* Thu May 09 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.2-1.615hg
- Update to hg snapshot 615 (version 2.0.2), fixing FTBFS on rawhide.
- Added possibility to run tests, but not by default since running them
  takes *eons*.

* Mon May 06 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.0-3.607hg
- Explicitly arched requires in -devel package.

* Mon Feb 18 2013 Dominik Mierzejewski <rpm@greysector.net> - 2.0.0-2.607hg
- Add missing tex build dependencies
- Fix devel subpackage dependencies

* Wed Jan 23 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.0-1.607hg
- First release.
