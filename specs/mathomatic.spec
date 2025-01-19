Summary:       Small, portable symbolic math program
Name:          mathomatic
Version:       16.0.5
Release:       33%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2
URL:           http://www.mathomatic.org/math/
#Source0:      http://mathomatic.org/mathomatic-${version}.tar.bz2
Source0:       http://mathomatic.orgserve.de/mathomatic-%{version}.tar.bz2
Source1:       http://mathomatic.orgserve.de/math/png/mathomatic192x195.png
Patch0:        mathomatic-16.0.5-libedit.patch
Patch1:        mathomatic-16.0.5-py3.patch
Patch2:        mathomatic-16.0.5-shebang.patch
BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: libedit-devel
BuildRequires: ImageMagick
# for make test
BuildRequires: time
Requires:      m4
Requires:      rlwrap
%description
Mathomatic is a small, portable symbolic math program that can
automatically solve, simplify, differentiate, combine, and compare
algebraic equations, perform polynomial and complex arithmetic,
etc. It was written by George Gesslein II and has been under
development since 1986.

%package       tools
Summary:       Various small math tools from mathomatic
Requires:      %{name} = %{version}-%{release}
%description tools
This package contains small math tools from mathomatic to
 - calculate Pascal's triangle
 - compute any number of consecutive prime numbers
 - find the minimum number of positive integers that when squared 
   and added together, equal the given number

%prep
%autosetup -p1

%build
make %{?_smp_mflags} OPTFLAGS="%{optflags}" EDITLINE=1 prefix=%{_prefix} 
#make pdf
pushd primes
make %{?_smp_mflags} prefix=%{_prefix} CFLAGS="%{optflags}"

%install
make m4install-degrees DESTDIR=%{buildroot} prefix=%{_prefix}
ln -s %{name}.1.gz %{buildroot}/%{_mandir}/man1/rmath.1.gz
ln -s  %{name}.1.gz %{buildroot}/%{_mandir}/man1/matho.1.gz
rm -rf %{buildroot}%{_datadir}/doc/%{name}
desktop-file-install --delete-original \
    --dir %{buildroot}%{_datadir}/applications  \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
pushd primes
make install prefix=%{buildroot}%{_prefix} mandir=%{buildroot}%{_mandir}
convert %{SOURCE1} -resize 256x256 %{buildroot}%{_datadir}/pixmaps/%{name}.png
rm -f %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

%check
make test
pushd primes
make test

%files
%license COPYING
%doc AUTHORS README.txt changes.txt doc
%{_bindir}/%{name}
%{_bindir}/rmath
%{_bindir}/matho
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/rmath.1*
%{_mandir}/man1/matho.1*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%files tools
%license COPYING
%doc AUTHORS README.txt changes.txt doc
%{_bindir}/matho-sum
%{_bindir}/matho-mult
%{_bindir}/matho-pascal
%{_bindir}/matho-primes
%{_bindir}/matho-sumsq
%{_bindir}/primorial
%{_mandir}/man1/matho-sum.1*
%{_mandir}/man1/matho-mult.1*
%{_mandir}/man1/matho-pascal.1*
%{_mandir}/man1/matho-primes.1*
%{_mandir}/man1/matho-sumsq.1*
%{_mandir}/man1/primorial.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 16.0.5-32
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 04 2021 Terje Rosten <terje.rosten@ntnu.no> - 16.0.5-24
- Remove unused htmldoc

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Terje Rosten <terje.rosten@ntnu.no> - 16.0.5-18
- Convert scripts to Python 3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Terje Rosten <terje.rosten@ntnu.no> - 16.0.5-16
- Add C compiler

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Terje Rosten <terje.rosten@ntnu.no> - 16.0.5-8
- Fix icon (bz #1157556)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Terje Rosten <terje.rosten@ntnu.no> - 16.0.5-5
- Use mirror for source tarball
- Cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 26 2012 Terje Rosten <terje.rosten@ntnu.no> - 16.0.5-2
- Switch to libedit
- Disable pdf build (htmldoc crashes)

* Mon Nov 19 2012 Terje Rosten <terje.rosten@ntnu.no> - 16.0.5-1
- 16.0.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 21 2012 Terje Rosten <terje.rosten@ntnu.no> - 15.8.2-1
- 15.8.2

* Wed Feb 01 2012 Terje Rosten <terje.rosten@ntnu.no> - 15.7.3-1
- 15.7.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Terje Rosten <terje.rosten@ntnu.no> - 15.6.5-1
- 15.6.5

* Thu Jul 21 2011 Terje Rosten <terje.rosten@ntnu.no> - 15.6.2-1
- 15.6.2

* Sat Mar 05 2011 Terje Rosten <terje.rosten@ntnu.no> - 15.5.0-1
- 15.5.0
- Fix rmath support

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Terje Rosten <terje.rosten@ntnu.no> - 15.4.0-1
- 15.4.0
- Add rmath (#661410)

* Fri Nov  5 2010 Terje Rosten <terje.rosten@ntnu.no> - 15.3.2-1
- 15.3.2

* Sat Jul 31 2010 Terje Rosten <terje.rosten@ntnu.no> - 15.1.5-1
- 15.1.5

* Thu Jun 17 2010 Terje Rosten <terje.rosten@ntnu.no> - 15.1.3-1
- 15.1.3

* Thu Apr 29 2010 Terje Rosten <terje.rosten@ntnu.no> - 15.0.7-1
- 15.0.7

* Sat Dec  5 2009 Terje Rosten <terje.rosten@ntnu.no> - 15.0.0-1
- 15.0.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Terje Rosten <terje.rosten@ntnu.no> - 14.3.1-1
- 14.3.1

* Mon Jan  5 2009 Terje Rosten <terje.rosten@ntnu.no> - 14.2.8-1
- 14.2.8

* Fri Aug 22 2008 Terje Rosten <terje.rosten@ntnu.no> - 14.1.4-1
- 14.1.4
- add build patch (add optflags, dont strip)

* Wed Jun  4 2008 Terje Rosten <terje.rosten@ntnu.no> - 14.0.4-1
- 14.0.4

* Wed May 21 2008 Terje Rosten <terje.rosten@ntnu.no> - 14.0.3-1
- 14.0.3
- cleanup
- build with readline support
- add tools subpackage

* Mon Nov  5 2007 Dries Verachtert - 12.7.9-1
- Updated to release 12.7.9.

* Tue Apr 27 2004 Dries Verachtert - 11.0e-1
- Initial package.

