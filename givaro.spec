Name:           givaro
Version:        4.2.0
%global so_version 9
Release:        1%{?dist}
Summary:        C++ library for arithmetic and algebraic computations

# The entire source is CECILL-B except for src/kernel/recint/reclonglong.h,
# which is LGPL-3.0-or-later, and various Autotools build-system files, which
# do not contribute to the licenses of the binary RPMs.
License:        CECILL-B AND LGPL-3.0-or-later
URL:            https://casys.gricad-pages.univ-grenoble-alpes.fr/givaro/
Source0:        https://github.com/linbox-team/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Add missing #include <cstdint> for (u)int64_t
# Fixes failure to compile on GCC 13.
# https://github.com/linbox-team/givaro/pull/218
Patch:          https://github.com/linbox-team/%{name}/pull/218.patch

BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  tex(stmaryrd.sty)

%description
Givaro is a C++ library for arithmetic and algebraic computations.
Its main features are implementations of the basic arithmetic of many
mathematical entities: Prime fields, Extension Fields, Finite Fields,
Finite Rings, Polynomials, Algebraic numbers, Arbitrary precision
integers and rationals (C++ wrappers over gmp).  It also provides
data-structures and templated classes for the manipulation of basic
algebraic objects, such as vectors, matrices (dense, sparse, structured),
and univariate polynomials (and therefore recursive multivariate).


%package        devel
Summary:        Files useful for %{name} development
Requires:       %{name}%{?_isa} = %{version}-%{release}

Obsoletes:      %{name}-devel-doc < 4.1.1-15

%description    devel
The libraries and header files for using %{name} for development.


# The static library is required by Macaulay2. See its spec file for a full
# explanation; the essential justification is excerpted below:
#
#   We have to use the static version of the libfplll and givaro library. They
#   have global objects whose constructors run before GC is initialized. If we
#   allow the shared libraries to be unloaded, which happens as a normal part
#   of Macaulay2's functioning, then GC tries to free objects it did not
#   allocate, which leads to a segfault.
%package        static
Summary:        Static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}


%description    static
A static library for %{name}.


%prep
%autosetup -p1


%build
%ifarch %{ix86}
# Excess precision leads to test failures
%global optflags %optflags -ffloat-store
%endif
%ifarch s390x
%global optflags %optflags -ffp-contract=off
%endif

%configure --without-archnative

# Get rid of undesirable hardcoded rpaths, and workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build


%install
%make_install

# We don't want libtool archives
rm -f %{buildroot}%{_libdir}/lib%{name}.la


%check
export LD_LIBRARY_PATH=$PWD/src/.libs
%make_build check


%files
%doc AUTHORS ChangeLog README.md
%license COPYING COPYRIGHT Licence_CeCILL-B_V1-en.txt Licence_CeCILL-B_V1-fr.txt
%{_libdir}/lib%{name}.so.%{so_version}{,.*}


%files devel
%{_bindir}/%{name}-config
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}-makefile
%{_includedir}/%{name}/
%{_includedir}/gmp++/
%{_includedir}/recint/
%{_includedir}/%{name}-config.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%files static
%{_libdir}/lib%{name}.a


%changelog
* Tue Oct 17 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.2.0-1
- Update to 4.2.0 (fix RHBZ#2032674)

* Tue Jul 25 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.1.1-15
- Drop and Obsolete the -devel-doc subpackage (fix RHBZ#2225830)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 25 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.1.1-13
- Re-enable documentation on F37

* Mon Jan 23 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.1.1-12
- Revert workaround for missing dependency on texlive-wasy

* Thu Jan 19 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.1.1-11
- Update License to SPDX
- Work around missing dependency on texlive-wasy
- Fix missing include for GCC 13; stop numbering patches

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 4.1.1-9
- Build docs as PDF instead of HTML due to guidelines issues
- Move large documentation to a new -devel-doc subpackage
- Temporarily disable doxygen docs on F37 due to a doxygen bug
- Correct License from CeCILL-B to (CeCILL-B and LGPLv3+)
- Do not glob over the .so version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov  1 2019 Jerry James <loganjerry@gmail.com> - 4.1.1-1
- New upstream release
- Drop upstreamed -iszero and -vec patches
- Add -mem-leak and -26932_recintvsflint_longlong patches

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 4.0.4-2
- Add -vec patch to fix out-of-bounds vector accesses

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 4.0.4-1
- New upstream release
- Work around FTBFS (bz 1582892)
- Update URL

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Mar 10 2017 Jerry James <loganjerry@gmail.com> - 4.0.2-5
- Add a -static subpackage for use in Macaulay2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 4.0.2-3
- Fix breakage due to new iszero macro in glibc

* Tue Aug 23 2016 Dan Horák <dan[at]danny.cz> - 4.0.2-2
- Fix test-ringarith failure on s390x

* Fri Aug 12 2016 Jerry James <loganjerry@gmail.com> - 4.0.2-1
- New upstream release

* Fri Feb 26 2016 Jerry James <loganjerry@gmail.com> - 4.0.1-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.8.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 16 2015 Jerry James <loganjerry@gmail.com> - 3.8.0-2
- Note bundled jquery

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 3.8.0-1
- New upstream release
- Fix license handling

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb  8 2013 Jerry James <loganjerry@gmail.com> - 3.7.2-1
- New upstream release
- Add BRs for TeXLive 2012
- Make sure the library doesn't have an rpath
- Link with --as-needed
- Add AUTHORS and COPYING to doc

* Wed Sep 26 2012 Jerry James <loganjerry@gmail.com> - 3.7.1-1
- New upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 3 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.0-1
- Update to latest upstream release.
- Remove gcc 4.7 patch already applied to upstream tarball.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-3
- Rebuilt for c++ ABI breakage

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 3.5.0-2
- Rebuild for GCC 4.7

* Tue Nov  1 2011 Jerry James <loganjerry@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.4.2-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 3.4.2-1.1
- rebuild with new gmp

* Tue Jul  5 2011 Jerry James <loganjerry@gmail.com> - 3.4.2-1
- Update to 3.4.2
- Add doxygen documentation and examples to docs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 02 2010 D Haley <mycae(a!t)yahoo.com> - 3.3.1-1
- Update to 3.3.1

* Fri Oct 09 2009 D Haley <mycae(a!t)yahoo.com> - 3.3.0-1
- Update to 3.3.0
- Relicence per CeCILL-B

* Sat Sep 12 2009 D Haley <mycae(a!t)yahoo.com> - 3.2.15-0.2.rc1
- Change to GPL+ from GPL2 per bugzilla comment

* Sun Aug 23 2009 D Haley <mycae(a!t)yahoo.com> - 3.2.15-0.1.rc1
- Upgrade to 3.2.15rc1
- Modify givaro-config.in to allow multiple flags simultaneously

* Sat Dec 6 2008 Conrad Meyer <konrad@tylerc.org> - 3.2.13-2
- Fix endian header to be non-endian.

* Sat Dec 6 2008 Conrad Meyer <konrad@tylerc.org> - 3.2.13-1
- Initial package.
