Name:           fftw2
Version:        2.1.5
Release:        52%{?dist}
Summary:        Fast Fourier Transform library (version 2)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.fftw.org
Source0:        https://www.fftw.org/fftw-%{version}.tar.gz
Patch1:         fftw2-configure.patch
Patch2:         fftw2-texi.patch
BuildRequires:  gcc-gfortran
BuildRequires:  make
%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size. We believe that FFTW, which is free
software, should become the FFT library of choice for most
applications. Our benchmarks, performed on on a variety of platforms,
show that FFTW's performance is typically superior to that of other
publicly available FFT software.

%package        devel
Summary:        Headers, libraries and docs for the FFTW library (version 2)
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains header files and development libraries needed to
develop programs using the FFTW fast Fourier transform library version
2.

%package        static
Summary:        Static version of the FFTW library (version 2)
Requires:       %{name} = %{version}-%{release}

%description    static
This package contains the static linked libraries of the FFTW fast
Fourier transform library (version 2).

%prep
%autosetup -N -c -n fftw-%{version}
%autopatch -p0
mv fftw-%{version} double
cp -a double single

%build
pushd double
%configure \
    --enable-shared \
%ifarch i386
    --enable-i386-hacks \
%endif
    --enable-threads
%make_build
popd

pushd single
%configure \
    --enable-shared \
    --enable-type-prefix \
    --enable-threads \
    --enable-float
%make_build
popd

%install
pushd double
%make_install
popd

pushd single
%make_install

find %{buildroot} -type f -name "*.la" -delete
rm %{buildroot}%{_infodir}/dir
cp -a doc COPYING AUTHORS COPYRIGHT ChangeLog NEWS README* TODO ..
popd
rm doc/{Makefile*,mdate-sh,stamp-vti,texi2html,texinfo.tex,*.texi,fftw.info*}

%files
%license COPYING
%doc AUTHORS COPYRIGHT ChangeLog NEWS README* TODO
%{_libdir}/libfftw.so.2*
%{_libdir}/libfftw_threads.so.2*
%{_libdir}/librfftw.so.2*
%{_libdir}/librfftw_threads.so.2*
%{_libdir}/libsfftw.so.2*
%{_libdir}/libsfftw_threads.so.2*
%{_libdir}/libsrfftw.so.2*
%{_libdir}/libsrfftw_threads.so.2*

%files devel
%license COPYING
%doc doc/
%{_includedir}/fftw.h
%{_includedir}/fftw_threads.h
%{_includedir}/rfftw.h
%{_includedir}/rfftw_threads.h
%{_includedir}/sfftw.h
%{_includedir}/sfftw_threads.h
%{_includedir}/srfftw.h
%{_includedir}/srfftw_threads.h
%{_libdir}/libfftw.so
%{_libdir}/libfftw_threads.so
%{_libdir}/librfftw.so
%{_libdir}/librfftw_threads.so
%{_libdir}/libsfftw.so
%{_libdir}/libsfftw_threads.so
%{_libdir}/libsrfftw.so
%{_libdir}/libsrfftw_threads.so
%{_infodir}/fftw.info*

%files static
%license COPYING
%{_libdir}/libfftw.a
%{_libdir}/libfftw_threads.a
%{_libdir}/librfftw.a
%{_libdir}/librfftw_threads.a
%{_libdir}/libsfftw.a
%{_libdir}/libsfftw_threads.a
%{_libdir}/libsrfftw.a
%{_libdir}/libsrfftw_threads.a

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.5-51
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb  5 2024 Terje Rosten <terje.rosten@ntnu.no> - 2.1.5-49
- Use modern macros and explicit file listing
- Add patch to fix info build

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Florian Weimer <fweimer@redhat.com> - 2.1.5-44
- Avoid implicit function declaration during configure (#2143573)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 22 2010 José Matos <jamatos@fc.up.pt> - 2.1.5-21
- Move static libraries to a static subpackage (bz556047)
- Add remarks that this is version 2 of fftw to description and summaries

* Fri May 21 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.5-20
- drop static libs (bz556047)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Robert Scheck <robert@fedoraproject.org> - 2.1.5-18
- Removed the shipping and owning of %%{_infodir}/dir file

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 José Matos <jamatos[AT]fc.up.pt> - 2.1.5-16
- Rebuild for gcc 4.3

* Tue Aug 28 2007 José Matos <jamatos[AT]fc.up.pt> - 2.1.5-15
- License fix, rebuild for devel (F8).

* Sat Apr 21 2007 José Matos <jamatos[AT]fc.up.pt> - 2.1.5-14
- Rebuild for F7.

* Tue Aug 29 2006 José Matos <jamatos[AT]fc.up.pt> - 2.1.5-13
- Rebuild for FE6

* Sat Feb 18 2006 José Matos <jamatos[AT]fc.up.pt> - 2.1.5-12
- Rebuild for FC-5.

* Wed Feb  1 2006 José Matos <jamatos[AT]fc.up.pt> - 2.1.5-11
- Fix incomplete substitution

* Wed Feb  1 2006 José Matos <jamatos[AT]fc.up.pt> - 2.1.5-10
- Add disttag to release.

* Wed Feb  1 2006 José Matos <jamatos[AT]fc.up.pt> - 2.1.5-9
- Rename package to fftw2.

* Mon May 23 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.1.5-8
- BuildReq gcc-gfortran (#156490).

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.1.5-7
- rebuild on all arches
- buildrequire compat-gcc-32-g77

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 2.1.5-5
- Bump release to provide Extras upgrade path.

* Tue Apr 06 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.5-0.fdr.4
- BuildReq gcc-g77.

* Mon Sep 22 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.5-0.fdr.3
- Dropped post/preun scripts for info.

* Wed Sep 17 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.5-0.fdr.2
- Remove aesthetic comments.
- buildroot -> RPM_BUILD_ROOT.
- post/preun for info files.

* Mon Apr 07 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.5-0.fdr.1
- Updated to 2.1.5.

* Tue Apr 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:2.1.4-0.fdr.2
- Added Epoch:0.
- Added ldconfig to post and postun.

* Sun Mar 22 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 2.1.4-0.fdr.1
- Updated to 2.1.4.

* Fri Mar 14 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 2.1.3-0.fdr.1
- Fedorafied.

* Mon Oct 21 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.
