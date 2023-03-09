%bcond_with check

%global packname bookdown
%global packver  0.33
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Authoring Books and Technical Documents with R Markdown

License:          GPL-3.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-htmltools >= 0.3.6, R-knitr >= 1.38, R-rmarkdown >= 2.14, R-jquerylib, R-xfun >= 0.29, R-tinytex >= 0.12, R-yaml >= 2.1.19
# Suggests:  R-bslib >= 0.2.4, R-downlit >= 0.4.0, R-htmlwidgets, R-jsonlite, R-rstudioapi, R-miniUI, R-rsconnect >= 0.4.3, R-servr >= 0.13, R-shiny, R-tibble, R-testit >= 0.9, R-tufte, R-xml2, R-webshot, R-testthat >= 3.1.0, R-withr >= 2.3.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-htmltools >= 0.3.6
BuildRequires:    R-knitr >= 1.38
BuildRequires:    R-rmarkdown >= 2.14
BuildRequires:    R-jquerylib
BuildRequires:    R-xfun >= 0.29
BuildRequires:    R-tinytex >= 0.12
BuildRequires:    R-yaml >= 2.1.19
# not sure if/when we can turn this on due to missing deps
%if %{with check}
BuildRequires:    R-bslib >= 0.2.4
BuildRequires:    R-downlit >= 0.4.0
BuildRequires:    R-htmlwidgets
BuildRequires:    R-jsonlite
BuildRequires:    R-rstudioapi
BuildRequires:    R-miniUI
BuildRequires:    R-rsconnect >= 0.4.3
BuildRequires:    R-servr >= 0.13
BuildRequires:    R-shiny
BuildRequires:    R-tibble
BuildRequires:    R-testit >= 0.9
BuildRequires:    R-tufte
BuildRequires:    R-xml2
BuildRequires:    R-webshot
BuildRequires:    R-testthat >= 3.1.0
BuildRequires:    R-withr >= 2.3.0
%endif

%description
Output formats and utilities for authoring books and technical documents with R
Markdown.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with check}
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/resources
%{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/templates


%changelog
%autochangelog
