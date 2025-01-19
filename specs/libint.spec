# Please void making new releases of the package, because all depending
# packages will be needing rebuilds.

# RPM macro directory
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# Commit hash
%global commit 29a6a6df4cd1242c54b5651fc0ac6dd563edf7c0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Version of flags used in configure. Increment always when changing the flags, since it will break the API and ABI.
%global apiversion 0

# LTO fails on Fedora 36 i686 (out of memory)
%if 0%{?fedora} == 36
%ifarch %{ix86}
%global _lto_cflags %nil
%endif
%endif

Name:           libint
Version:        1.2.1
Release:        23%{?dist}
Summary:        A library for computing electron repulsion integrals efficiently
# Libint is two things: a code generator, and a generated
# library. This package builds and runs the compiler (GPLv3), and
# builds and ships the generated library (LGPLv3). The license tag
# refers to the binaries, i.e. here the generated library.
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            http://sourceforge.net/p/libint
Source0:        https://github.com/evaleev/libint/archive/%{commit}/libint-%{commit}.tar.gz

# Increase maxnode
Patch1:         libint-1.2.1-maxnode.patch
# Use old-style soname
Patch2:         libint-1.2.1-soname.patch

# Capabilities provided by library
Provides:       libint(api)%{?_isa} = %{apiversion}

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%if 0%{?rhel} == 6
# Required to build documentation
BuildRequires:  /usr/bin/bibtex
BuildRequires:  /usr/bin/pdflatex
%endif

%if 0%{?fedora} > 17 || 0%{?rhel} > 6
# Required to build documentation
BuildRequires:  texlive-collection-latexrecommended
BuildRequires:  texlive-bibtex
%endif

%description
LIBINT computes the Coulomb and exchange integrals, which in electronic
structure theory are called electron repulsion integrals (ERIs). This is by
far the most common type of integrals in molecular structure theory.

LIBINT uses recursive schemes that originate in seminal Obara-Saika method and
Head-Gordon and Pople’s variation thereof. The idea of LIBINT is to optimize
computer implementation of such methods by implementing an optimizing compiler
to generate automatically highly-specialized code that runs well on
super-scalar architectures.

%package devel
Summary:  Development headers and libraries for libint
Requires: libint%{?_isa} = %{version}-%{release}
Requires: libderiv%{?_isa} = %{version}-%{release}
Requires: libr12%{?_isa} = %{version}-%{release}

%description devel
This package contains development headers and libraries for libint.
It also contains a programmer's manual.

%package -n libr12
Summary:  A library for computing integrals that arise in Kutzelnigg’s linear R12 theories

%description -n libr12
libr12 computes types integrals that appear in Kutzelnigg’s linear R12 theories
for electronic structure. All linear R12 methods, such as MP2-R12, contain
terms in the wave function that are linear in the inter-electronic distances
r_{ij} (hence the name). Appearance of several types of two-body integrals is
due to the use of the approximate resolution of the identity to reduce three-
and four-body integrals to products of simpler integrals.

%package -n libderiv
Summary:  A library for computing derivatives of electron repulsion integrals
Requires: libint%{?_isa} = %{version}-%{release}

%description -n libderiv
libderiv computes first and second derivatives of ERIs with respect to the
coordinates of the basis function origin. This type of integrals are also very
common in electronic structure theory, where they appear in analytic gradient
expressions. The derivatives are typically used in the calculation of forces.


%prep
%setup -q -n %{name}-%{commit}
%patch -P1 -p1 -b .maxnode
%patch -P2 -p1 -b .soname
libtoolize --copy --force
aclocal -I lib/autoconf
autoconf

%build
# Disable stack size limit due to static allocation of arrays
ulimit -s unlimited
%configure --enable-shared --disable-static \
 --with-libint-max-am=10 --with-libint-opt-am=6 \
 --with-libderiv-max-am1=6 --with-libderiv-max-am2=5 \
 --with-libr12-max-am=5 --with-libr12-opt-am=4

# The generated library is already highly optimized for performance,
# so it's safe to use a lower level of compiler optimization here.
oflags=`echo %{optflags} | sed "s|-O2|-O1|g"`
make CFLAGS="${oflags}" CXXFLAGS="${oflags}" %{?_smp_mflags}

# Build documentation
cd doc/progman
pdflatex progman
bibtex progman
pdflatex progman
pdflatex progman


%install
rm -rf %{buildroot} 
make install DESTDIR=%{buildroot}
find %{buildroot} -name *.la -delete
find %{buildroot} -name *.so.*.* -exec chmod 755 {} \;

# Create macro file
mkdir -p %{buildroot}%{macrosdir}
cat > %{buildroot}%{macrosdir}/macros.libint << EOF
# Current version of libint is
%_libint_apiversion %{apiversion}
EOF

%ldconfig_scriptlets

%ldconfig_scriptlets -n libderiv

%ldconfig_scriptlets -n libr12

%files
%doc LICENSE COPYING COPYING.LESSER
%{_libdir}/libint*.so.*

%files -n libderiv
%doc LICENSE COPYING COPYING.LESSER
%{_libdir}/libderiv*.so.*

%files -n libr12
%doc LICENSE COPYING COPYING.LESSER
%{_libdir}/libr12*.so.*

%files devel
%doc doc/progman/progman.pdf
%{macrosdir}/macros.libint
%{_includedir}/libint/
%{_includedir}/libderiv/
%{_includedir}/libr12/
%{_libdir}/*.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.1-6
- Added gcc and gcc-c++ buildrequires.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.1-2
- Patch to make sonames same as before (no functional changes in 1.2 series).

* Wed May 17 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1, changing the license from GPL to LGPL.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 08 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.6-9
- Modify progman build dependencies.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 13 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.6-7
- Rebuild (aarch64)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.6-5
- Fix FTBFS caused by libtool version mismatch.

* Tue Sep 09 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.6-4
- Provide %%_libint_apiversion instead of %%_libint_version.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 09 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6.

* Mon Feb 03 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.5-4
- Use proper macro for rpm macro dir.

* Sun Dec 22 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.5-3
- Increase maximum angular momentum (BZ #1045781), but limit optimized one.
- Use -O1 level of optimization on all architectures.
- Patch for -Werror=format-security (BZ #1037165).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 15 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5, bringing aarch64 support.

* Tue Feb 19 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.4-11
- Fix FTBFS in rawhide.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.4-9
- Increased libint-max-am from 6 to 7 and libr12-max-am from 5 to 6.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 28 2012 Dan Horák <dan[at]danny.cz> - 1.1.4-7
- drop the s390 workaround, gcc 4.7 seems to work correctly

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Dan Horák <dan[at]danny.cz> - 1.1.4-4
- workaround memory exhaustion on s390

* Tue Nov 30 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.4-3
- Increase maximum angular momentum values by 2, making it possible to
  use basis sets that use up to I-type functions, such as Dunning's cc-pVXZ
  basis sets.
- Split libderiv and libr12 into their own packages, as e.g. PyQuante currently
  only needs the libint library.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.4-1
- First release.
