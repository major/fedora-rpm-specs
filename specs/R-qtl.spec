%global packname qtl

%global __suggests_exclude ^R\\(testthat\\)

Name:		R-%{packname}
Version:	1.70
Release:	2%{?dist}
Source0:	https://rqtl.org/download/%{packname}_%{version}.tar.gz
License:	GPL-3.0-only
URL:		https://rqtl.org/
Summary:	Tools for analyzing QTL experiments
#		R versions before 3.1.1 have a bug that causes the checks
#		to fail on 64 bit big endian architectures (ppc64, s390x)
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	R-core-devel >= 3.1.1
BuildRequires:	tex(latex)
BuildRequires:	tex(fancyhdr.sty)
BuildRequires:	tex(fullpage.sty)
%if %{?fedora}%{!?fedora:0} >= 38
BuildRequires:	tex(inconsolata.sty)
%endif
BuildRequires:	R-parallel, R-graphics, R-stats, R-utils, R-grDevices
%if %{?fedora}%{!?fedora:0}
#		R-testthat is not available in EPEL
BuildRequires:	R-testthat
%endif
BuildRequires:	R-rpm-macros

%description
R-qtl is an extensible, interactive environment for mapping
quantitative trait loci (QTLs) in experimental crosses. Our goal is to
make complex QTL mapping methods widely accessible and allow users to
focus on modeling rather than computing.

A key component of computational methods for QTL mapping is the hidden
Markov model (HMM) technology for dealing with missing genotype
data. We have implemented the main HMM algorithms, with allowance for
the presence of genotyping errors, for backcrosses, intercrosses, and
phase-known four-way crosses.

The current version of R-qtl includes facilities for estimating
genetic maps, identifying genotyping errors, and performing single-QTL
genome scans and two-QTL, two-dimensional genome scans, by interval
mapping (with the EM algorithm), Haley-Knott regression, and multiple
imputation. All of this may be done in the presence of covariates
(such as sex, age or treatment). One may also fit higher-order QTL
models by multiple imputation and Haley-Knott regression.

%prep
%setup -q -c
%if ! %{?fedora}%{!?fedora:0}
# R-testthat is not available in EPEL
rm qtl/tests/testthat.R
%endif

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css
rm -rf %{buildroot}%{_libdir}/R/library/%{packname}/contrib

%check
_R_CHECK_FORCE_SUGGESTS_=0 R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/BUGS.txt
%doc %{_libdir}/R/library/%{packname}/INSTALL_ME.txt
%doc %{_libdir}/R/library/%{packname}/MQM-TODO.txt
%doc %{_libdir}/R/library/%{packname}/NEWS.md
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/sampledata

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 23 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.70-1
- Update to 1.70

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.66-4
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 05 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.66-1
- Update to 1.66

* Sun Nov 26 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.62-1
- Update to 1.62

* Sun Jul 23 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.60-3
- Fix build requires

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 16 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.60-1
- Update to 1.60
- Drop workaround for broken openblas on aarch64 in RHEL 8 and 9
  Fixed in RHEL 8.8 and 9.2 respectively

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.58-2
- R-maint-sig mass rebuild

* Wed Jan 25 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.58-1
- Update to 1.58
- Workaround broken openblas on aarch64 in RHEL 8 and 9

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  1 2022 Tom Callaway <spot@fedoraprojet.org> - 1.52-3
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.52-1
- Update to 1.52

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.50-1
- Update to 1.50

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Tom Callaway <spot@fedoraproject.org> - 1.48.1-2
- Rebuilt for R 4.1.0

* Sun Mar 28 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.48.1-1
- Update to 1.48-1

* Wed Jan 27 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.47.9-1
- Update to 1.47-9

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.46.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Tom Callaway <spot@fedoraproject.org> - 1.46.2-5
- rebuild for FlexiBLAS R

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.46.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.46.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Tom Callaway <spot@fedoraproject.org> - 1.46.2-2
- rebuild for R 4

* Sat Mar 21 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.46.2-1
- Update to 1.46-2

* Tue Feb 18 2020 Tom Callaway <spot@fedoraproject.org> - 1.44.9-7
- rebuild against R without libRlapack.so

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.44.9-5
- Unify specfile

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.44.9-4
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.44.9-1
- Update to 1.44-9

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 1.42.8-1.1
- actually rebuild against R 3.5.0

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.42.8-1
- update to 1.42-8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.41.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.41.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.41.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.41.6-1
- Update to 1.41.6
- Add BuildRequires on R-testthat for Fedora (not available in EPEL)
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove license macro definition
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.40.8-3
- rebuild for R 3.4.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.40.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.40.8-1
- Update to 1.40.8

* Fri Apr 15 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.39.5-1
- Update to 1.39.5

* Tue Feb 09 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.38.4-1
- Update to 1.38.4
- Use license tag in files section

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 08 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.37.11-1
- Update to 1.37.11

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.36.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 06 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.36.6-1
- Update to 1.36.6

* Sun Jan 04 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.35.3-1
- Update to 1.35.3

* Mon Oct 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.33.7-1
- Update to 1.33.7

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.32.10-4
- Remove stack limit workaround (bug fixed in R 3.1.1)

* Tue Jul 01 2014 Jakub Čajka <jcajka@redhat.com> - 1.32.10-3
- Changed stack limit on ppc64 and s390x to allow checks to pass

* Sat Jun 28 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.32.10-2
- Disable checks on ppc64

* Wed Jun 25 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.32.10-1
- Update to 1.32.10
- Use R-core-devel instead of R-devel as BR
- Re-enable checks

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.31.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Tom Callaway <spot@fedoraproject.org> - 1.31.9-1
- Update to 1.31.9

* Sat Dec 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.29.2-1
- Update to 1.29.2
- Add BR for blas-devel and lapack-devel

* Tue Oct 15 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.28.19-1
- Update to 1.28.19

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 17 2013 Tom Callaway <spot@fedoraproject.org> - 1.27.10-2
- rebuild for R3

* Thu Apr 11 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.27.10-1
- Update to 1.27.10

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 1.26.14-3
- rebuild for R3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.26.14-1
- New upstream release

* Tue Nov 13 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.25.15-1
- New upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.23.16-1
- New upstream release

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 02 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.22.21-1
- New upstream release

* Tue Nov 08 2011 Tom Callaway <spot@fedoraproject.org> - 1.21.2-2
- rebuild for R 2.14.0

* Wed Jun 29 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.21.2-1
- New upstream release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.19.20-1
- New upstream release

* Thu Sep 02 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.18.7-1
- New upstream release

* Fri Jun 11 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.16.6-1
- New upstream release

* Sun Nov 22 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.14.2-2
- Modify build for R 2.10 and higher - remove scriptlets

* Wed Oct 07 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.14.2-1
- New upstream release
- Disable the check since it trips on a missing suggested package
- Change license tag to GPLv3 to reflect an upstream license change

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.11-1
- New upstream release

* Wed Mar 18 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.10-2
- Update package summary and description
- Change defines to globals

* Sat Feb 28 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.10-1
- Updated to new upstream version - contains consistent licensing information
- Reverted License tag from GPLv2 to GPLv2+ to reflect the new information

* Tue Dec 02 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.09-2
- Corrected License tag from GPLv2+ to GPLv2

* Wed Nov 05 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.09-1
- Initial package creation
