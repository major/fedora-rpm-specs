%global upstreamver 2-5-4

Name:           cxsc
Version:        %(tr - . <<< %{upstreamver})
Release:        28%{?dist}
Summary:        C++ library for Extended Scientific Computing

%global majver  %(cut -d. -f1 <<< %{version})

License:        LGPL-2.0-or-later
URL:            https://www2.math.uni-wuppertal.de/wrswt/xsc/cxsc_new.html
Source:         https://www2.math.uni-wuppertal.de/wrswt/xsc/%{name}/%{name}-%{upstreamver}.tar.gz
# Sent upstream 22 Jun 2016.  Fix an operator error.
Patch:          %{name}-operator.patch
# Sent upstream 22 Jun 2016.  Fix build problem on ppc64.
Patch:          %{name}-ppc64.patch
# Fix endianness detection
Patch:          %{name}-endian.patch
# Fix a sequence point error
Patch:          %{name}-seq.patch
# Fix a mistaken euro symbol which leads to LaTeX errors
Patch:          %{name}-euro.patch
# Fix access to an uninitialized variable
Patch:          %{name}-uninit.patch
# Do not allocate arrays with negative size
Patch:          %{name}-neg-alloc.patch
# Remove template IDs from constructors
Patch:          %{name}-template-id.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)

%description
C-XSC is the C language variant of the XSC (eXtensions for Scientific
Computing) project.  It provides routines that guarantee accuracy and
reliability of results.  Problem-solving routines with automatic result
verification have been developed for many standard problems of numerical
analysis, such as linear or nonlinear systems of equations, differential
and integral equations, etc. as well as for a large number of
applications in engineering and the natural sciences.  Some of the
features of C-XSC are:
- Operator concept (user-defined operators)
- Overloading concept
- Module concept
- Dynamic arrays
- Controlled rounding
- Predefined arithmetic data types real, extended real, complex,
  interval, complex interval, and corresponding vector and matrix types
- Predefined arithmetic operators and elementary functions of the highest
  accuracy for the arithmetic data types
- Data type dotprecision for the exact representation of dot products
- Library of mathematical problem-solving routines with automatic result
  verification and high accuracy

%package devel
Summary:        Header files for developing applications that use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and library links for developing applications that use %{name}.

%package doc
# The project as a whole is LGPL-2.0-or-later.
# Doxygen adds files with other licenses.
# GPL-1.0-or-later: bc_s.png, bc_sd.png, bdwn.png, closed.png, doc.png,
#   docd.png, doxygen.css, doxygen.svg, folderclosed.png, folderopen.png,
#   nav_f.png, nav_fd.png, nav_g.png, nav_h.png, nav_hd.png, navtree.css,
#   open.png, splitbar.png, splitbard.png, sync_off.png, sync_on.png, tab_a.png,
#   tab_ad.png, tab_b.png, tab_bd.png, tab_h.png, tab_hd.png, tab_s.png,
#   tab_sd.png, tabs.css
# MIT: dynsections.js, jquery.js, menu.js, menudata.js, navtree.js, resize.js
License:        LGPL-2.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        API documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       bundled(js-jquery)

%description doc
API documentation for %{name}.

%prep
%autosetup -p0 -n %{name}-%{upstreamver}

%conf
# Don't set rpath
sed -i 's/\(RPATH[[:blank:]]*=\).*/\1/;' Makefile.in CToolbox/Makefile
sed -i '/LINKERPATH=-Wl,-R/d' install_cxsc

# Don't build with SSE2 support on platforms the script doesn't recognize
%ifnarch %{ix86} x86_64
sed -i 's/ -mfpmath=sse -msse2//' install_cxsc.in
%endif

# Link with the BLAS and OpenMP libraries
sed -i 's/\$(RARI)/& -lflexiblas -lgomp/' src/Makefile
sed -i 's/(LIBS)/& -lflexiblas/' CToolbox/Makefile

# Install in the right place on 64-bit systems
if [ %{_libdir} != "%{_prefix}/lib" ]; then
  sed -e 's|\$(PREFIX)/lib$|$(PREFIX)/%{_lib}|' \
      -e 's|\$(PREFIX)/lib;|$(PREFIX)/%{_lib};|' \
      -i src/Makefile
fi

# Use an efficient representation for a_btyp on 64-bit systems
if [ "%{__isa_bits}" = "64" ]; then
  sed -ri 's/(#define SHORTABTYP) .*/\1 1/' src/rts/o_spec.h
  sed -i 's/#if DEC_ALPHA_C+GNU_X86_64+CXSC_PPC64/#if 1/' src/rts/p88rts.h
else
  sed -ri 's/(#define SHORTABTYP) .*/\1 0/' src/rts/o_spec.h
  sed -i 's/#if DEC_ALPHA_C+GNU_X86_64+CXSC_PPC64/#if 0/' src/rts/p88rts.h
fi

# Remove spurious executable bits
chmod a-x src/fi_lib/*.{cpp,hpp}

# Remove throw() specifications for C++17 compatibility
for fil in $(find src -type f); do
  sed -e 's/\([[:blank:]]\)throw[[:blank:]]*([[:blank:]]*)/\1noexcept/g' \
      -e 's/^throw[[:blank:]]*([[:blank:]]*)/noexcept/g' \
      -e 's/[[:blank:]]throw[[:blank:]]*([^)]*)//g' \
      -e 's/^throw[[:blank:]]*([^)]*)//g' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build
# FIXME: tests fail without -fno-inline.  Why?
if [ "%{__isa_bits}" = "64" ]; then
  use64=-DIS_64_BIT
else
  use64=
fi
printf "yes\n\
gnu\n\
no\n\
yes\n\
%ifarch x86_64
%{build_cxxflags} -DCXSC_USE_BLAS -DCXSC_USE_LAPACK -DCXSC_USE_OPENMP -DCXSC_USE_FMA -DIS_64_BIT -fopenmp %{build_ldflags}\n\
64\n\
asm\n\
%elifarch %{power64}
%{build_cxxflags} -DCXSC_USE_BLAS -DCXSC_USE_LAPACK -DCXSC_USE_OPENMP -DCXSC_USE_FMA -DIS_64_BIT -fopenmp %{build_ldflags}\n\
asm\n\
%else
%{build_cxxflags} -DCXSC_USE_BLAS -DCXSC_USE_LAPACK -DCXSC_USE_OPENMP -DCXSC_USE_FMA $use64 -fopenmp -frounding-math -fno-inline %{build_ldflags}\n\
hard\n\
safe\n\
%endif
%{buildroot}%{_prefix}\n\
dynamic\n\
no\n" | ./install_cxsc

# The individual targets can be built in parallel, but specifying more than one
# to the same make invocation leads to build failures.
%make_build cxsc
%make_build libcxsc.so
mkdir usr
ln -s ../src usr/lib
ln -s lib%{name}.so.%{version} src/lib%{name}.so.%{majver}
ln -s lib%{name}.so.%{majver} src/lib%{name}.so
export LD_LIBRARY_PATH=$PWD/usr/lib
%make_build toolbox_dyn CXSCDIR=$PWD/usr

# Make the documentation
cd src
doxygen src-doxyfile

%install
make install_dyn PREFIX=%{buildroot}%{_prefix}

# Fix permissions on the library
chmod 0755 %{buildroot}%{_libdir}/lib%{name}.so.%{version}

# There are a lot of header files, so hide them in a private directory
mkdir %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.{h,hpp,inl} %{buildroot}%{_includedir}/%{name}

# Don't package the example binaries
rm -fr %{buildroot}/%{_prefix}/examples

%check
sed -i 's/ASM$/ASM LD_LIBRARY_PATH/' Makefile
sed -i 's/export RPATH/export LD_LIBRARY_PATH/' CToolbox/Makefile
if [ %{_libdir} != "%{_prefix}/lib" ]; then
  sed -i 's|/lib|/%{_lib}|' CToolbox/Makefile
fi
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make toolboxtest_dyn

%files
%doc changelog README
%license docu/COPYING
%{_libdir}/lib%{name}.so.2*

%files devel
%doc examples
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files doc
%doc docu/apidoc

%changelog
* Wed Sep 11 2024 Jerry James <loganjerry@gmail.com> - 2.5.4-28
- Add patch to remove template-ids on constructors

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 2.5.4-23
- Stop building for 32-bit x86

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 31 2022 Jerry James <loganjerry@gmail.com> - 2.5.4-21
- Update ppc64 patch due to "uname -p" breakage

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 2.5.4-20
- Convert License tags to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Jerry James <loganjerry@gmail.com> - 2.5.4-16
- Update the code for C++17, fixes gap-pkg-float build
- Add -uninit and -neg-alloc patches

* Mon Aug 10 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2.5.4-15
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Jeff Law <lwa@redhat.com> - 2.5.4-14
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Jerry James <loganjerry@gmail.com> - 2.5.4-9
- Build with openblas instead of atlas (bz1618943)
- Do not build both SSE2/non-SSE2 for 32-bit x86 any more; default is now SSE2
- Add -euro patch to fix documentation build failure

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Jerry James <loganjerry@gmail.com> - 2.5.4-2
- Fix endianness detection
- Make the ppc64le build use the same asm as ppc64

* Wed Jun 22 2016 Jerry James <loganjerry@gmail.com> - 2.5.4-1
- Initial RPM
