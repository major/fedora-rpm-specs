%global         with_allprogs 0

Name:           eclib
Version:        20221012
Release:        4%{?dist}
Summary:        Library for Computations on Elliptic Curves
License:        GPL-2.0-or-later
URL:            https://homepages.warwick.ac.uk/~masgaj/mwrank/
Source0:        https://github.com/JohnCremona/eclib/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  boost-devel
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  ntl-devel
BuildRequires:  pari-devel


%description
John Cremona's programs for enumerating and computing with elliptic
curves defined over the rational numbers.


%package        devel
Summary:        Development Files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       ntl-devel%{?_isa}


%description    devel
Development libraries and headers for %{name}.


%prep
%autosetup


%build
# FLINT_LEVEL 2 assumes that the C int type == half the width of a limb_t.
# This is only true on 64 bit platforms.
if [ %{__isa_bits} = "64" ]; then
  export FLINT_LEVEL=2
fi

export CPPFLAGS="-I %{_includedir}/flint"
%ifarch %{ix86}
# Excess precision leads to test failures
export CFLAGS="%{build_cflags} -ffloat-store"
export CXXFLAGS="$CFLAGS"
%endif
%configure \
        --disable-static \
        --enable-shared \
        --with-flint \
        --with-boost \
%if %{with_allprogs}
        --enable-allprogs
%else
        --disable-allprogs
%endif

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
 sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
     -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
     -i libtool

%make_build


%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%if !%{with_allprogs}
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/{g0n,howto,progs}.txt
%endif


%check
make check LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}


%files
%doc AUTHORS NEWS README doc/mwrank
%license COPYING
%if %{with_allprogs}
%{_bindir}/*
%else
%{_bindir}/mwrank
%endif
%{_libdir}/libec.so.10*
%{_mandir}/man1/mwrank.1*


%files devel
%doc doc/g0n.txt
%{_includedir}/%{name}
%{_libdir}/libec.so
%{_libdir}/pkgconfig/eclib.pc


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20221012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Jerry James <loganjerry@gmail.com> - 20221012-3
- Version 20221012

* Mon Sep 26 2022 Jerry James <loganjerry@gmail.com> - 20220621-3
- Rebuild for pari 2.15.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 20220621-2
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220621-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 20220621-1
- Version 20220621

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 20210625-6
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210625-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Jerry James <loganjerry@gmail.com> - 20210625-4
- Rebuild for flint 2.8.0

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 20210625-3
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210625-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Jerry James <loganjerry@gmail.com> - 20210625-1
- Version 20210625

* Tue Jun 29 2021 Jerry James <loganjerry@gmail.com> - 20190909-11
- Rebuild for ntl 11.5.1
- Reenable tests on 32-bit architectures

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 20190909-10
- Rebuild for multithreaded pari

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190909-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 20190909-8
- Rebuilt for Boost 1.75

* Mon Nov  9 2020 Jerry James <loganjerry@gmail.com> - 20190909-7
- Rebuild for pari 2.13.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190909-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 20190909-5
- Rebuild for flint 2.6.0

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 20190909-4
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190909-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 20190909-2
- Rebuild for ntl 11.4.3

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 20190909-1
- New upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190226-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Jerry James <loganjerry@gmail.com> - 20190226-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180815-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 20180815-2
- Rebuilt for Boost 1.69

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 20180815-1
- New upstream release

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 20180710-1
- New upstream release
- Drop all patches; all upstreamed

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171219-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 20171219-2
- Fix out of bounds vector accesses
- Reenable use of boost

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 20171219-1
- New upstream release
- Work around FTBFS (bz 1582888)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170815-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jerry James <loganjerry@gmail.com> - 20170815-1
- New upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170330-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 20170330-5
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170330-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 20170330-3
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20170330-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Mar 30 2017 Jerry James <loganjerry@gmail.com> - 20170330-1
- New upstream release

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 20160720-5
- Rebuilt for Boost 1.63

* Wed Nov  9 2016 Paul Howarth <paul@city-fan.org> - 20160720-4
- Rebuild for pari 2.9.0

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 20160720-3
- Rebuild for NTL 10.1.0
- Add -iszero patch to fix breakage with newer glibc versions

* Mon Sep  5 2016 Jerry James <loganjerry@gmail.com> - 20160720-2
- Rebuild for NTL 9.11.0

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> - 20160720-1
- New upstream release

* Thu Jun  2 2016 Jerry James <loganjerry@gmail.com> - 20160215-4
- Rebuild for NTL 9.9.1

* Fri Apr 29 2016 Jerry James <loganjerry@gmail.com> - 20160215-3
- Rebuild for NTL 9.8.0

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 20160215-2
- Rebuild for NTL 9.7.0

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 20160215-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20160101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Jerry James <loganjerry@gmail.com> - 20160101-2
- Rebuild for boost 1.60.0

* Sat Jan  9 2016 Jerry James <loganjerry@gmail.com> - 20160101-1
- New upstream release

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 20150827-3
- Rebuild for NTL 9.6.2

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 20150827-2
- Rebuild for NTL 9.4.0

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 20150827-1
- New upstream release (bz 1257389)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120830-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 20120830-13
- Rebuild for NTL 9.1.1

* Sat May  9 2015 Jerry James <loganjerry@gmail.com> - 20120830-12
- Rebuild for NTL 9.1.0

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 20120830-11
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 20120830-10
- Rebuild for NTL 8.1.2

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 20120830-9
- Rebuild for NTL 8.1.0

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 20120830-8
- Rebuild for NTL 6.2.1
- Fix license handling

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120830-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120830-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 20120830-5
- Rebuild for NTL 6.1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120830-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 20120830-3
- Rebuild for NTL 6.0.0
- autoreconf already calls libtoolize; don't need to call the latter
- drop now unneeded -ntl-underlink patch

* Wed Mar 27 2013 Jerry James <loganjerry@gmail.com> - 20120830-2
- Add -fi to libtoolize and autoreconf invocations to get updates (bz 925294)
- Modify libtool to get rid of unused direct library dependencies and rpaths

* Sat Jan 26 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 20120830-1
- Update to latest upstream release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120428-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 20120428-1
- Update to latest upstream release.
- Rework package build that now uses autotools instead of hand made Makefiles.

* Thu Jul 5 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 20100711-5
- Install mwrank binary as it is required by sagemath.
- Install mwrank documentation.

* Wed Jul 4 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 20100711-4
- Rebuild with newer pari.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100711-3
- Rebuilt for c++ ABI breakage

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 20100711-2
- Rebuild for GCC 4.7

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 20100711-1.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 20100711-1.1
- rebuild with new gmp

* Mon May 23 2011 Jerry James <loganjerry@gmail.com> - 20100711-1
- New upstream version
- Drop unnecessary elements of the spec file (BuildRoot, clean script, etc.)
- Convert previous patches into sed expressions
- Add compiler warning elimination patch
- Eliminate unused direct shared library dependencies
- Fix the FSF's address to make rpmlint shut up
- Add documentation to -devel

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080310-10.p10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Thomas Spura <tomspur@fedoraproject.org> - 20080310-9.p10
- update to patched version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080310-9.p7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Conrad Meyer <konrad@tylerc.org> - 20080310-8.p7
- Make only shared libs.

* Fri May 8 2009 Conrad Meyer <konrad@tylerc.org> - 20080310-7.p7
- Kill parallel make to fix the build (thanks Mamoru Tasaka).

* Sun Mar 22 2009 Conrad Meyer <konrad@tylerc.org> - 20080310-6.p7
- Incorporate Michael Schwendt's patch to fix the build process
  (thanks again :)).

* Fri Mar 20 2009 Conrad Meyer <konrad@tylerc.org> - 20080310-5.p7
- Changed BR on ntl-devel to ntl-static.

* Fri Mar 20 2009 Conrad Meyer <konrad@tylerc.org> - 20080310-4.p7
- Fixed path in %%check section.

* Thu Mar 19 2009 Conrad Meyer <konrad@tylerc.org> - 20080310-3.p7
- Move libraries back to _libdir proper and add main package.
- Added check section (thanks Michael Schwendt) commented out because
  it doesn't pass right now.
- Add a versioned SONAME.

* Wed Mar 18 2009 Conrad Meyer <konrad@tylerc.org> - 20080310-2.p7
- Fix soname mess.
- Use install -p.

* Sat Dec 13 2008 Conrad Meyer <konrad@tylerc.org> - 20080310-1.p7
- Initial package.
