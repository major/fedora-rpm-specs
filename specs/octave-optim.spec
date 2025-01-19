%global octpkg optim

Name:           octave-%{octpkg}
Version:        1.6.2
Release:        12%{?dist}
Summary:        A non-linear optimization tool kit for Octave
# C++ and .m are GPLv3+, documentation is GFDL
# Automatically converted from old format: GPLv3+ and GFDL - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
URL:            https://octave.sourceforge.io/optim/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel
BuildRequires:  octave-struct >= 1.0.12
BuildRequires:  octave-statistics >= 1.4.0 
BuildRequires:  tex(latex)
BuildRequires:  tex(dsfont.sty)
BuildRequires:  ghostscript

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
Requires:       octave-struct >= 1.0.10


%description
This package contains a non-linear optimization tool kit for Octave, containing
functions for curve fitting and the following minimization algorithms:
* Nead-Miller simplex
* Conjugate Gradients
* Memory limited BFGS
* Simulated Annealing

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install
rm -rf %{buildroot}/%{octpkgdir}/doc/.svnignore
chmod a-x %{buildroot}/%{octpkgdir}/*.m
rm -rf  %{buildroot}/%{octpkgdir}/doc

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%{octpkglibdir}
%{octpkgdir}/PKG_ADD
%{octpkgdir}/private/optim_problems_p_r_y.data
%{octpkgdir}/private/*.m
%{octpkgdir}/+__optim_checks__/*.m
%{_metainfodir}/octave-%{octpkg}.metainfo.xml
%doc doc/development/interfaces.txt

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 Orion Poplawski <orion@nwra.com> - 1.6.2-11
- Rebuild for octave 9.2

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.2-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 1.6.2-5
- Rebuild with octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 1.6.2-2
- Rebuild for octave 7.1

* Thu Apr 14 2022 Thomas Sailer <fedora@tsailer.ch> - 1.6.2-1
- update to 1.6.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 1.6.1-3
- Rebuild for octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 17 2021 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.6.1-1
- update to 1.6.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 1.6.0-4
- Rebuild with octave 64bit indexes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 1.6.0-2
- Rebuild for octave 5.1

* Tue Apr 16 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.6.0-1
- update to 1.6.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 1.5.3-2
- Rebuild for octave 4.4

* Mon Aug 06 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.5.3-1
- update to 1.5.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Orion Poplawski <orion@cora.nwra.com> - 1.5.2-6
- Rebuild to ship metainfo.xml so this package will appear in Software

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Orion Poplawski <orion@cora.nwra.com> - 1.5.2-2
- Rebuild for octave 4.2

* Mon Oct 03 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.5.2-1
- update to 1.5.2

* Thu Feb 25 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.5.0-1
- update to 1.5.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.4.1-1
- Update to 1.4.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.4.0-1
- update to 1.4.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.3.0-1
- update to 1.3.0

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-5
- Rebuild for octave 3.8.0

* Thu Sep 26 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.2-4
- rebuild for blas and atlas

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov  6 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.2-1
- update to 1.2.2

* Sun Sep 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.1-1
- update to 1.2.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.0-1
- update to 1.2.0

* Tue Jun  5 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.0-1
- update to 1.1.0

* Mon Jan 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.17-3
- rebuild for octave 3.6.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.17-1
- update to 1.0.17

* Fri Aug 26 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.16-3
- compile tex docs into a pdf file instead of shipping tex sources

* Wed Aug 24 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.16-2
- review input

* Fri Jun 03 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> 1.0.16-1
- initial package for Fedora
