%global octpkg odepkg
%global hg_rev 611

Name:           octave-%{octpkg}
Version:        0.9.1
Release:        0.25.20210827hg%{hg_rev}%{?dist}
Summary:        A package for solving ordinary differential equations and more

# Most source files are GPLv2+
# A few source files are BSD in src/daskr
License:        GPLv2+ and BSD
URL:            http://octave.sourceforge.net/odepkg/

# hg clone http://hg.code.sf.net/p/octave/odepkg
# cd odepkg
# hg archive -t tgz ../odepkg-0.9.1-609.tar.gz
Source0:        %{octpkg}-%{version}-%{hg_rev}.tar.gz
# Includes fixes for new Octave from this Merge request: https://sourceforge.net/p/octave/odepkg/merge-requests/1/
# hg clone http://hg.code.sf.net/u/hroderick/odepkg-octave hroderick-odepkg-octave
# cd hroderick-odepkg-octave
# hg archive -t tgz ../odepkg-0.9.1-611.tar.gz

BuildRequires:  octave-devel

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
A package for solving ordinary differential equations and more

%prep
%setup -q -n %{octpkg}-%{version}-%{hg_rev}
rm -f */.svnignore

# correct wrong end of line encoding errors
iconv -f iso8859-1 -t utf-8 doc/odepkg.texi > doc/odepkg.texi.conv && mv -f doc/odepkg.texi.conv doc/odepkg.texi


%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/packinfo
%{octpkgdir}/inexact_solvers/
%{octpkgdir}/integrate_functions/
%{octpkgdir}/steppers/
%{octpkgdir}/string_compare/
%{octpkgdir}/utilities/

%doc %{octpkgdir}/doc-cache
%doc %{octpkgdir}/doc
%license COPYING

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.25.20210827hg611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.24.20210827hg611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.23.20210827hg611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 0.9.1-0.22.20210827hg611
- Rebuild with octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.21.20210827hg611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.20.20210827hg611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 0.9.1-0.19.20210827hg611
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.18.20210827hg611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 27 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-0.17.20210827hg611
- Update to snapshot to fix for Octave 6

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 0.9.1-0.16.20170102hg609
- Rebuild for octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.15.20170102hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.14.20170102hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.9.1-0.13.20170102hg609
- Rebuilt for https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.12.20170102hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.11.20170102hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 0.9.1-0.10.20170102hg609
- Rebuild with octave 64bit indexes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.9.20170102hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 0.9.1-0.8.20170102hg609
- Rebuild for octave 5.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.7.20170102hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.6.20170102hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Orion Poplawski <orion@nwra.com> - 0.9.1-0.5.20170102hg609
- Explicitly BR octave-devel >= 4.2

* Tue Feb 06 2018 Ankur Sinha <sanjay.ankur@gmail.com> - 0.9.1-0.4.20170102hg609
- rebuilt for libgfortran bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.3.20170102hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-0.2.20170102hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 8 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-0.1.20170102hg609
- Update to 0.9.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 0.8.5-1
- Update to 0.8.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.4-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.8.4-1
- Update to latest upstream release

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 0.8.2-7
- Rebuild for octave 3.8.0

* Sun Sep 22 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.8.2-6
- Rebuild for atlas rebase

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.8.2-3
- specbump to attempt another build

* Wed Oct 24 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.8.2-2
- Added comment for the two licenses
- Correct permissions

* Thu Oct 18 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.8.2-1
- inital rpm build

