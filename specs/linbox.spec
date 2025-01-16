%global giturl  https://github.com/linbox-team/linbox

Name:           linbox
Version:        1.7.0
%global so_version 0
Release:        9%{?dist}
Summary:        C++ Library for High-Performance Exact Linear Algebra

License:        LGPL-2.1-or-later
URL:            https://linalg.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

# Fix the size formula for an allocation
# https://github.com/linbox-team/linbox/pull/307
#
# Fixes:
#
# crashes in test-{smith-form-valence,regression} compiling with
# -D_FORTIFY_SOURCE=3
# https://github.com/linbox-team/linbox/issues/304
Patch:          https://github.com/linbox-team/%{name}/pull/307.patch

# Fixes an attempt to return a void value in the OpenCL code
Patch:          https://github.com/linbox-team/%{name}/pull/308.patch

# const_cast missing; faster empty init
# https://github.com/linbox-team/linbox/commit/b8f2d4ccdc0af4418d14f72caf6c4d01969092a3
# Fixes FTBFS with GCC 14. Cherry-picked to v1.7.0.
Patch:          0001-const_cast-missing.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# The sole dependent package, sagemath, is already not built on i686.
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  expat-devel
BuildRequires:  fflas-ffpack-devel
BuildRequires:  flexiblas-devel
BuildRequires:  flint-devel
BuildRequires:  givaro-devel
BuildRequires:  iml-devel
BuildRequires:  libfplll-devel
BuildRequires:  mpfr-devel
BuildRequires:  ntl-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  saclib-devel
BuildRequires:  tinyxml2-devel

Obsoletes:      linbox-doc < 1.7.0-1

%description
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.


%package        devel
Summary:        Development libraries/headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fflas-ffpack-devel%{?_isa}
Requires:       iml-devel%{?_isa}
Requires:       libfplll-devel%{?_isa}
Requires:       ntl-devel%{?_isa}
Requires:       ocl-icd-devel%{?_isa}


%description    devel
Headers and libraries for development with %{name}.


%package        doc
Summary:        Documentation for %{name}

BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%autosetup -p1


%conf
# Adapt to the way saclib is packaged in Fedora
sed -e 's,include/saclib,&/saclib,' \
    -e '/saclib\.h/,+1s/__GNU_MP_VERSION < 3/SACMAJVERS < 2/' \
    -i macros/saclib-check.m4

# Remove spurious executable bits
find -O3 . \( -name \*.h -o -name \*.inl \) -perm /0111 -exec chmod a-x {} +


%build
# Regenerate configure after monkeying with m4 macros
autoreconf -fi

export CPPFLAGS='-I%{_includedir}/saclib'
%configure --disable-silent-rules \
  --disable-static \
  --with-ocl=yes \
  --with-saclib=yes \
  --without-archnative
chmod -v a+x linbox-config

# Remove hardcoded rpaths; workaround libtool reordering -Wl,--as-needed after
# all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# Don't try to optimize the tests; the build takes gargantuan amounts of memory
sed -i 's|-O2|-Og|g' tests/Makefile

%make_build


%install
%make_install

# We don't want libtool archives
rm -f %{buildroot}%{_libdir}/*.la

# Documentation is installed in the wrong place
rm -vrf '%{buildroot}%{_prefix}/doc'


%check
# Do not test in parallel, leads to duplicated work
LD_LIBRARY_PATH=$PWD/linbox/.libs %make_build check -j1


%files
%doc AUTHORS ChangeLog README.md
%license COPYING COPYING.LESSER
%{_libdir}/lib%{name}.so.%{so_version}
%{_libdir}/lib%{name}.so.%{so_version}.*


%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/%{name}-config
%{_mandir}/man1/%{name}-config.1*


%changelog
* Sun Jan  5 2025 Jerry James <loganjerry@gmail.com> - 1.7.0-9
- Remove unused m4ri and m4rie deps

* Fri Nov 22 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.7.0-8
- Rebuild for libfplll 5.5.0

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.7.0-7
- rebuild for tinyxml2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.7.0-5
- Backport a commit to fix building with GCC 14 (fix RHBZ#2260378)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Jerry James <loganjerry@gmail.com> - 1.7.0-2
- Fix accidentally-introduced -Og; restore normal optimizations
- Fix OpenCL support

* Tue Oct 17 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.7.0-1
- Update to 1.7.0 (close RHBZ#2032716)
- Stop building Doxygen documentation; drop and Obsolete the -doc subpackage
- Fix an undersized allocation (upstream issue #304, PR #307)

* Tue Aug 15 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 1.6.3-17
- Drop workarounds for 32-bit ARM
  (https://fedoraproject.org/wiki/Changes/RetireARMv7)
- Drop i686 (https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval)
- Drop the patch for 32-bit since we no longer build for 32-bit architectures

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.6.3-14
- Rebuild for libfplll 5.4.4
- Convert License tag to SPDX

* Sun Sep 25 2022 Rich Mattes <richmattes@gmail.com> - 1.6.3-13
- Rebuild for tinyxml2-9.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Jerry James <loganjerry@gmail.com> - 1.6.3-10
- Rebuild for flint 2.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.3-7
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 1.6.3-4
- Rebuild for flint 2.6.0 and libfplll 5.3.3

* Sat Feb  1 2020 Jerry James <loganjerry@gmail.com> - 1.6.3-3
- Add -32bit patch to fix FTBFS on 32-bit platforms
- Make docs arch-specific for now due to differences across platforms

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 1.6.3-1
- Rebuild for ntl 11.4.3

* Fri Nov  1 2019 Jerry James <loganjerry@gmail.com> - 1.6.3-1
- New upstream version
- Drop upstreamed -gcc8, -vec, and -charpoly-fullCRA patches

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 1.5.2-8
- Rebuild for ntl 11.3.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 1.5.2-5
- Build with openblas instead of atlas (bz 1619043)
- BR ocl-icd-devel for OpenCL support
- Add -charpoly-fullCRA patch

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.5.2-4
- Rebuild for ntl 11.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 1.5.2-2
- Fix out-of-bounds vector accesses

* Thu Apr 12 2018 Jerry James <loganjerry@gmail.com> - 1.5.2-1
- New upstream version (bz 1514773)
- Work around FTBFS (bz 1582910)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jerry James <loganjerry@gmail.com> - 1.4.2-11
- Rebuild for ntl 10.5.0 and libfplll 5.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 1.4.2-7
- Rebuild for ntl 10.3.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan  6 2017 Jerry James <loganjerry@gmail.com> - 1.4.2-5
- Rebuild with fflas-ffpack fixed for big endian architectures

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 1.4.2-4
- Rebuild for ntl 10.1.0

* Thu Sep 29 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.4.2-3
- Enable -O optimization in tests CFLAGS to fix build on aarch64 (#1380101)

* Mon Sep  5 2016 Jerry James <loganjerry@gmail.com> - 1.4.2-2
- Rebuild for ntl 9.11.0

* Fri Aug 12 2016 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- New upstream version (bz 1361824)

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> - 1.4.1-4
- Rebuild for ntl 9.10.0

* Thu Jun  2 2016 Jerry James <loganjerry@gmail.com> - 1.4.1-3
- Rebuild for ntl 9.9.1

* Fri Apr 29 2016 Jerry James <loganjerry@gmail.com> - 1.4.1-2
- Rebuild for ntl 9.8.0

* Wed Apr 13 2016 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- New upstream version (bz 1325572)

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 1.4.0-2
- Rebuild for ntl 9.7.0

* Fri Feb 26 2016 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- New upstream version (bz 1312150)

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 1.3.2-28
- Rebuild for ntl 9.6.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 1.3.2-26
- Rebuild for ntl 9.6.2

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 1.3.2-25
- Rebuild for ntl 9.4.0

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 1.3.2-24
- Rebuild for ntl 9.3.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 1.3.2-22
- Rebuild for ntl 9.1.1

* Sat May  9 2015 Jerry James <loganjerry@gmail.com> - 1.3.2-21
- Rebuild for ntl 9.1.0

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.2-20
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 28 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.2-19
- Rebuild for new c++ string and list abi

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 1.3.2-18
- Rebuild for ntl 8.1.2

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 1.3.2-17
- Rebuild for ntl 8.1.0
- Note bundled jquery in the documentation

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 1.3.2-16
- Rebuild for givaro 3.8.0, m4ri(e) 20140914, and ntl 6.2.1
- Prepare for future saclib support
- Fix license handling

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 1.3.2-13
- Rebuild for ntl 6.1.0
- Add missing Requires to -devel
- Fix overlinking

* Mon Sep 23 2013 Jerry James <loganjerry@gmail.com> - 1.3.2-12
- Rebuild for atlas 3.10.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 1.3.2-10
- Rebuild for libfplll 4.0.3, m4ri and m4rie 20130416, and ntl 6.0.0

* Fri Feb  8 2013 Jerry James <loganjerry@gmail.com> - 1.3.2-9
- Rebuild for givaro 3.7.2

* Wed Jan  2 2013 Dan Horák <dan[at]danny.cz> - 1.3.2-8
- Only s390 needs the size_t fix

* Tue Jan  1 2013 Dan Horák <dan[at]danny.cz> - 1.3.2-7
- Fix build when size_t is unsigned long (eg. on s390)

* Mon Dec 31 2012 Jerry James <loganjerry@gmail.com> - 1.3.2-6
- Rebuild for m4ri 20121224

* Mon Dec 10 2012 Jerry James <loganjerry@gmail.com> - 1.3.2-5
- Enable FPLLL support
- Adjust BRs for texlive 2012

* Tue Oct  2 2012 Jerry James <loganjerry@gmail.com> - 1.3.2-4
- Rebuild for givaro 3.7.1
- Fix all linkage problems in the same patch
- Fix driver compile

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 3 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.2-2
- Force linkage to mpfr and iml to avoid unresolved symbols.

* Tue Jul 3 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.2-1
- Update to latest upstream release.
- Rediff linbox-destructor patch.
- Rediff gcc 4.7 patch as it is partially applied to upstream tarball.
- Correct 64 bit build.
- Add m4rie-devel to build requires and set CPPFLAGS to detect it.
- Disable --enable-driver as it no longer compiles.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for c++ ABI breakage

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 1.2.2-3
- Rebuild for GCC 4.7

* Wed Nov  9 2011 Jerry James <loganjerry@gmail.com> - 1.2.2-2
- New -destructor patch that doesn't cause memory leaks

* Tue Nov  1 2011 Jerry James <loganjerry@gmail.com> - 1.2.2-1
- Update to new upstream release
- Reenable the tests

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.2.1-1.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 1.2.1-1.1
- rebuild with new gmp

* Mon Aug 29 2011 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- Final 1.2.1 release

* Tue Jul  5 2011 Jerry James <loganjerry@gmail.com> - 1.2.1-0.1.svn3901
- Update to snapshot with fixes for Fedora
- Drop all patches, now upstream
- Remove unnecessary spec file elements (%%defattr, etc.)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-0.3.svn3214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.1.7-0.2.svn3212
- add ugly sed to configure to look for *.so and not for *.a anymore
  (atlas maintainer removed them)
  (fixes FTBFS #564837)

* Sat Nov 21 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.1.7-0.1.svn3214
- fetch new version from svn
  (fixes FTBFS bug #539006)
- change summary to *exact* linear algebra as requested by upstream
- change building a bit

* Mon Oct 19 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.1.6-6
- installing docs breaks naming guidelines -> install them different

* Sun Oct 18 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.1.6-5
- properly install docs and don't mv them around
- add other files to %%doc

* Sun Oct 18 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.1.6-4
- %%check
- patch for --cflags and --lflags in config

* Sat Oct 17 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.1.6-3
- patches are send upstream
- correct BuildRequires
- INSTALL is not in %%doc

* Sat Oct 17 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.1.6-2
- disable static library
- patch for double named header files
- extra doc package

* Fri Dec 12 2008 Conrad Meyer <konrad@tylerc.org> - 1.1.6-1
- Initial package.
