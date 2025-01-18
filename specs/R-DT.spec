%global packname DT
%global packver  0.25
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          10%{?dist}
Summary:          R Wrapper of the JavaScript Library 'DataTables'

# Main: GPLv3; JavaScript files: MIT or ASL 2.0, see below
License:          GPL-3.0-only AND MIT AND Apache-2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-htmltools >= 0.3.6, R-htmlwidgets >= 1.3, R-jsonlite >= 0.9.16, R-magrittr, R-crosstalk, R-promises
# Suggests:  R-knitr >= 1.8, R-rmarkdown, R-shiny >= 1.2.0, R-testit
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-htmltools >= 0.3.6
BuildRequires:    R-htmlwidgets >= 1.3
BuildRequires:    R-jsonlite >= 0.9.16
BuildRequires:    R-magrittr
BuildRequires:    R-crosstalk
BuildRequires:    R-jquerylib
BuildRequires:    R-promises
BuildRequires:    R-knitr >= 1.8
BuildRequires:    R-rmarkdown
BuildRequires:    R-shiny >= 1.6
BuildRequires:    R-bslib
BuildRequires:    R-testit
BuildRequires:    R-future

# MIT; inst/htmlwidgets/lib/jquery
Provides:         bundled(js-jquery1) = 1.12.4
# MIT; inst/htmlwidgets/lib/datatables*, inst/htmlwidgets/css/datatables-crosstalk.css
Provides:         bundled(jquery.dataTables) = 1.10.20
# MIT; inst/htmlwidgets/lib/nouislider
Provides:         bundled(jquery.nouislider) = 7.0.10
# MIT; inst/htmlwidgets/lib/nouislider
Provides:         bundled(jquery.nouislider) = 7.0.10
# ASL 2.0; inst/lib/selectize
Provides:         bundled(js-brianreavis-selectize) = 0.12.1

%description
Data objects in R can be rendered as HTML tables using the JavaScript
library 'DataTables' (typically via R Markdown or Shiny). The 'DataTables'
library has been included in this R package. The package name 'DT' is an
abbreviation of 'DataTables'.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check --ignore-vignettes %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/htmlwidgets


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.25-8
- R-maint-sig mass rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 12 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.25-4
- Ignore vignettes

* Fri Apr 21 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.25-3
- R-maint-sig mass rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 17 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.25-1
- Update to 0.25 (RHBZ #2126248)

* Fri Sep  2 2022 Tom Callaway <spot@fedoraproject.org> - 0.24-1
- update to 0.24
- rebuild for R 4.2.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tom Callaway <spot@fedoraproject.org> - 0.17-3
- Rebuilt for R 4.1.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17-1
- Update to latest version (#1913446)

* Wed Oct 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16-1
- Update to latest version (#1888077)

* Sat Aug 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.15-1
- Update to latest version

* Mon Aug 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.14-1
- initial package for Fedora
