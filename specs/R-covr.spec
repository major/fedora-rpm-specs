%global packname covr
%global packver  3.6.4
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          6%{?dist}
Summary:          Test Coverage for Packages

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-digest, R-stats, R-utils, R-jsonlite, R-rex, R-httr, R-crayon, R-withr >= 1.0.2, R-yaml
# Suggests:  R-R6, R-curl, R-knitr, R-rmarkdown, R-htmltools, R-DT >= 0.2, R-testthat, R-rlang, R-rstudioapi >= 0.2, R-xml2 >= 1.0.0, R-parallel, R-memoise, R-mockery
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-digest
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-jsonlite
BuildRequires:    R-rex
BuildRequires:    R-httr
BuildRequires:    R-crayon
BuildRequires:    R-withr >= 1.0.2
BuildRequires:    R-yaml
BuildRequires:    R-R6
BuildRequires:    R-curl
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-htmltools
BuildRequires:    R-DT >= 0.2
BuildRequires:    R-testthat
BuildRequires:    R-rlang
BuildRequires:    R-rstudioapi >= 0.2
BuildRequires:    R-xml2 >= 1.0.0
BuildRequires:    R-parallel
BuildRequires:    R-memoise
BuildRequires:    R-mockery

# MIT; inst/www/shared/bootstrap
Provides:         bundled(xstatic-bootstrap-common) = 3.3.5
# MIT; inst/www/shared/highlight.js
Provides:         bundled(js-highlight) = 6.2

%description
Track and report code coverage for your package and (optionally) upload the
results to a coverage service like 'Codecov' <https://codecov.io> or
'Coveralls' <https://coveralls.io>. Code coverage is a measure of the amount of
code being exercised by a set of tests. It is an indirect measure of test
quality and completeness. This package is compatible with any testing
methodology or framework and tracks coverage of both R code and compiled
C/C++/FORTRAN code.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
# It has itself as a Suggests. :P
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --ignore-vignettes %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/www


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 3.6.4-4
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Tom Callaway <spot@fedoraproject.org> - 3.6.4-1
- update to 3.6.4

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 3.6.1-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 3.6.1-1
- update to 3.6.1
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 3.5.1-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.5.1-1
- Update to latest version (#1879773)

* Mon Aug 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.5.0-1
- initial package for Fedora
