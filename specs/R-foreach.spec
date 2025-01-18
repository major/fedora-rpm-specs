%bcond_with bootstrap

%global packname foreach
%global packver  1.5.2
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          11%{?dist}
Summary:          Provides Foreach Looping Construct

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:          Apache-2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-codetools, R-utils, R-iterators
# Suggests:  R-randomForest, R-doMC, R-doParallel, R-testthat, R-knitr, R-rmarkdown
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-codetools
BuildRequires:    R-utils
BuildRequires:    R-iterators
%if %{without bootstrap}
BuildRequires:    R-randomForest
BuildRequires:    R-doMC
BuildRequires:    R-doParallel
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
%endif

%description
Support for the foreach looping construct.  Foreach is an idiom that allows for
iterating over elements in a collection, without the use of an explicit loop
counter.  This package in particular is intended to be used for its return
value, rather than for its side effects.  In that sense, it is similar to the
standard lapply function, but doesn't require the evaluation of a function.
Using foreach without side effects also facilitates executing the loop in
parallel.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes --no-tests
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/examples


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul  24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.2-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 1.5.2-8
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 28 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.5.2-4
- Ignore vignettes

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 1.5.2-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 1.5.2-1
- update to 1.5.2
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Tom Callaway <spot@fedoraproject.org> - 1.5.1-4
- bootstrap off

* Tue Jun 15 2021 Tom Callaway <spot@fedoraproject.org> - 1.5.1-3
- bootstrap
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.1-1
- Update to latest version (#1888528)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun  6 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.0-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.8-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.7-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-1
- initial package for Fedora
