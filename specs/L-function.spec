# FIXME: This package should be renamed to lcalc.

Name:		L-function
Version:	2.0.5
Release:	11%{?dist}
Summary:	C++ L-function class library and command line interface
License:	GPL-2.0-or-later
URL:		https://gitlab.com/sagemath/lcalc
VCS:		git:%{url}.git
Source0:	%{url}/-/archive/%{version}/lcalc-%{version}.tar.bz2
# Fix use of the wrong delete operator
# https://gitlab.com/sagemath/lcalc/-/merge_requests/5
Patch0:		%{name}-mismatched-delete.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:	gcc-c++
BuildRequires:	gengetopt
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	pari-devel

%description
C++ L-function class library and command line interface.

%package	devel
Summary:	Development libraries/headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Headers and libraries for development with %{name}.

%prep
%autosetup -p1 -n lcalc-%{version}

autoreconf -fi .

%build
%configure --with-pari

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libLfunction.la

# We select the files we want in doc
rm -fr %{buildroot}%{_docdir}/lcalc

%check
make check

%files
%doc doc/{ChangeLog,CONTRIBUTORS,README.md}
%license doc/COPYING
%{_bindir}/lcalc
%{_libdir}/libLfunction.so.1*
%{_mandir}/man1/lcalc.1*

%files devel
%doc doc/examples
%{_includedir}/lcalc/
%{_libdir}/libLfunction.so
%{_libdir}/pkgconfig/lcalc.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct  5 2024 Jerry James <loganjerry@gmail.com> - 2.0.5-10
- Rebuild for pari 2.17.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 2.0.5-5
- Stop building for 32-bit x86

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 26 2022 Jerry James <loganjerry@gmail.com> - 2.0.5-3
- Rebuild for pari 2.15.0
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 17 2022 Jerry James <loganjerry@gmail.com> - 2.0.5-1
- Version 2.0.5
- New URLs
- Drop all patches
- New patch to fix mismatched delete operators
- Add %%check script

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 1.23-33
- Replace value_via_Riemann_sum.patch with sagemath's Lvalue.h.patch

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Jerry James <loganjerry@gmail.com> - 1.23-31
- Add gcc11 patch to fix build failure

* Mon Nov  9 2020 Jerry James <loganjerry@gmail.com> - 1.23-30
- Rebuild for pari 2.13.0
- Build with OpenMP support
- Add value_via_Riemann_sum and unlink patches

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Jerry James <loganjerry@gmail.com> - 1.23-25
- Discard our patches in favor of sagemath's patches for ease of maintenance
- Add -stringstream patch to avoid deprecated APIs

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.23-24
- Rebuild for pari 2.11.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.23-22
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov  9 2016 Paul Howarth <paul@city-fan.org> - 1.23-17
- Add patch to build with pari 2.9

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.23-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Feb  8 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.23-13
- Correct problems with sagemath build with gcc 5.0.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.23-10
- Add Debian patch to rebuild with pari 2.7.
- Add patch to build with gcc 4.9.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.23-6
- Build with $RPM_OPT_FLAGS and %%{_smp_mflags} (regression in -5).
- Build with $RPM_LD_FLAGS.

* Sun Jul 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.23-5
- Merge with duplicate review request #821195 that had changelog
  + Correct license tag.
  + Install example source code.
  + Add %%post sections for library.
  + Build lcalc with openmp support.
  + Rename to L to match upstream tarball.
  + Add proper documentation to main package.
  + Remove the "see also" section of lcalc.1 as there is no info page.
  + Initial lcalc spec.
- Do not provide %%{name}-static as no such library is/was installed.
- Install CONTRIBUTORS as documentation.
- Remove %%defattr usage.

* Sat Apr 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.23-4
- Fix build failure (since F-11!) 

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Conrad Meyer <konrad@tylerc.org> - 1.23-1
- Bump to latest upstream.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Conrad Meyer <konrad@tylerc.org> - 1.2-3
- Add missing BR on pari-devel.

* Sat Mar 14 2009 Conrad Meyer <konrad@tylerc.org> - 1.2-2
- Include headers in -devel subpackage.
- Include PARI support.

* Sat Nov 8 2008 Conrad Meyer <konrad@tylerc.org> - 1.2-1
- Initial package.
