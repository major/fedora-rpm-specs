Name:           DSDP
Version:        5.8
Release:        37%{?dist}
Summary:        Software for semidefinite programming

# The content is DSDP.  The remaining licenses cover the various fonts embedded
# in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
License:        DSDP AND OFL-1.1-RFN AND Knuth-CTAN
URL:            https://www.mcs.anl.gov/hs/software/DSDP/
Source0:        https://www.mcs.anl.gov/hs/software/DSDP/%{name}%{version}.tar.gz
# Man pages written by Jerry James using text from the sources.
# Therefore, the man pages have the same copyright and license as the source.
Source1:        DSDP-man.tar.xz
# A substitute makefile to fix the brokenness of the distributed Makefiles
Source2:        DSDP.Makefile
# Fix a buffer overflow in one of the examples.
Patch:          %{name}-overflow.patch
# Fix -Wint-in-bool-context warnings.
Patch:          %{name}-int-in-bool-context.patch
# Fix big endian problems (patch courtesy of Debian)
Patch:          %{name}-type-mismatch.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  doxygen-latex
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)

%description
DSDP is a free open source implementation of an interior-point method
for semidefinite programming.  It provides primal and dual solutions,
exploits low-rank structure and sparsity in the data, and has relatively
low memory requirements for an interior-point method.  It allows
feasible and infeasible starting points and provides approximate
certificates of infeasibility when no feasible solution exists.  The
dual-scaling algorithm implemented in this package has a convergence
proof and worst-case polynomial complexity under mild assumptions on the
data.  The software can be used as a set of subroutines, through Matlab,
or by reading and writing to data files.  Furthermore, the solver offers
scalable parallel performance for large problems and a well documented
interface.  Some of the most popular applications of semidefinite
programming and linear matrix inequalities (LMI) are model control,
truss topology design, and semidefinite relaxations of combinatorial and
global optimization problems. 

%package devel
# The content is DSDP.  The remaining licenses cover the various fonts embedded
# in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
License:        DSDP AND OFL-1.1-RFN AND Knuth-CTAN
Summary:        Headers and libraries for developing with DSDP
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       bundled(js-jquery)

%description devel
Headers and libraries for developing with DSDP.

%package examples
License:        DSDP
Summary:        Example programs that use DSDP
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description examples
Examples programs that use the DSDP library.

%prep
%autosetup -p0 -n %{name}%{version} -a 1

%conf
sed -e 's|@RPM_OPT_FLAGS@|%{build_cflags}|' \
    -e 's|@RPM_LD_FLAGS@|%{build_ldflags}|' \
    -e 's|@libdir@|%{_libdir}|' \
    -e 's|@version@|%{version}|' \
    %{SOURCE2} > Makefile

%build
%make_build
cd docs
unzip DSDP5-api-html.zip
cd dox
rm -fr html images
doxygen

%install
# Install the library
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -p -m 0755 src/libdsdp.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -s libdsdp.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libdsdp.so.5
ln -s libdsdp.so.5 $RPM_BUILD_ROOT%{_libdir}/libdsdp.so

# Install the header files
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a include $RPM_BUILD_ROOT%{_includedir}/DSDP

# Install the example programs with a dsdp- prefix, except for dsdp5
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for f in maxcut theta stable color; do
  install -p -m 0755 examples/$f $RPM_BUILD_ROOT%{_bindir}/dsdp-$f
done
install -p -m 0755 examples/dsdp5 $RPM_BUILD_ROOT%{_bindir}

# Install the man pages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cd man
for f in *.1; do
  sed "s/@VERSION@/%{version}/" $f > $RPM_BUILD_ROOT%{_mandir}/man1/$f
done

%files
%doc docs/DSDP5-Exe-UserGuide.pdf docs/DSDP5-P1289-0905.pdf
%license dsdp-license
%{_libdir}/libdsdp.so.5*

%files devel
%doc docs/DSDP5-API-UserGuide.pdf docs/dox
%{_libdir}/libdsdp.so
%{_includedir}/DSDP

%files examples
%doc examples/Contents
%{_bindir}/dsdp*
%{_mandir}/man1/dsdp*

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Jerry James <loganjerry@gmail.com> - 5.8-31
- Add SPDX License identifiers for PDF documentation
- Minor spec file cleanups

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun  3 2021 Jerry James <loganjerry@gmail.com> - 5.8-28
- Change ghostscript-core BR to ghostscript

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 5.8-26
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Jerry James <loganjerry@gmail.com> - 5.8-23
- Add -type-mismatch patch from Debian to fix big endian issues

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct  2 2018 Jerry James <loganjerry@gmail.com> - 5.8-20
- Build with openblas instead of atlas (bz 1618936)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 12 2015 Jerry James <loganjerry@gmail.com>
- Use license macro
- Note bundled jquery

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct  8 2013 Jerry James <loganjerry@gmail.com> - 5.8-9
- Change project URL according to upstream's wishes
- Remove file URL and note project's orphan status upstream

* Sat Sep 21 2013 Jerry James <loganjerry@gmail.com> - 5.8-8
- Rebuild for atlas 3.10.1

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Jerry James <loganjerry@gmail.com> - 5.8-6
- Some of the examples now need to be linked with -lm
- Use RPM_LD_FLAGS when linking the library and examples
- Add ghostscript BR due to TeXLive 2012 changes

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 5.8-3
- Rebuild for GCC 4.7

* Tue Jun  7 2011 Jerry James <loganjerry@gmail.com> - 5.8-2
- Ensure the libraries are installed with the execute bit on
- Name the license according to the response from Fedora-Legal

* Wed May 25 2011 Jerry James <loganjerry@gmail.com> - 5.8-1
- Initial RPM
