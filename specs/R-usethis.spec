%global packname usethis
%global packver  3.1.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Automate Package and Project Setup

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli, R-clipr >= 0.3.0, R-crayon, R-curl >= 2.7, R-desc, R-fs >= 1.3.0, R-gert >= 1.0.2, R-gh >= 1.2.0, R-glue >= 1.3.0, R-jsonlite, R-lifecycle, R-purrr, R-rappdirs, R-rlang >= 0.4.10, R-rprojroot >= 1.2, R-rstudioapi, R-stats, R-utils, R-whisker, R-withr >= 2.3.0, R-yaml
# Suggests:  R-covr, R-knitr, R-magick, R-mockr, R-rmarkdown, R-roxygen2, R-spelling >= 1.2, R-styler >= 1.2.0, R-testthat >= 3.0.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli >= 3.0.1
BuildRequires:    R-clipr >= 0.3.0
BuildRequires:    R-crayon
BuildRequires:    R-curl >= 2.7
BuildRequires:    R-desc >= 1.4.2
BuildRequires:    R-fs >= 1.3.0
BuildRequires:    R-gert >= 1.4.1
BuildRequires:    R-gh >= 1.2.1
BuildRequires:    R-glue >= 1.3.0
BuildRequires:    R-jsonlite
BuildRequires:    R-lifecycle >= 1.0.0
BuildRequires:    R-purrr
BuildRequires:    R-rappdirs
BuildRequires:    R-rlang >= 1.1.0
BuildRequires:    R-rprojroot >= 1.2
BuildRequires:    R-rstudioapi
BuildRequires:    R-stats
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-whisker
BuildRequires:    R-withr >= 2.3.0
BuildRequires:    R-yaml
BuildRequires:    R-knitr
BuildRequires:    R-magick
BuildRequires:    R-pkgload >= 1.3.2.1
BuildRequires:    R-rmarkdown
BuildRequires:    R-roxygen2 >= 7.1.2
BuildRequires:    R-spelling >= 1.2
BuildRequires:    R-styler >= 1.2.0
BuildRequires:    R-testthat >= 3.1.8

%description
Automate package and project setup tasks that are otherwise performed manually.
This includes setting up unit testing, test coverage, continuous integration,
Git, GitHub, licenses, Rcpp, RStudio projects, and more.


%prep
%setup -q -c -n %{packname}
rm %{packname}/tests/testthat/test-release.R # requires Internet

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check --no-manual --ignore-vignettes %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/templates


%changelog
%autochangelog
