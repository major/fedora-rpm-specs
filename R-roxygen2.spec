%global packname roxygen2
%global packver  7.2.3
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          In-Line Documentation for R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-brew, R-cli >= 3.3.0, R-commonmark, R-desc >= 1.2.0, R-knitr, R-methods, R-pkgload >= 1.0.2, R-purrr >= 0.3.3, R-R6 >= 2.1.2, R-rlang >= 1.0.6, R-stringi, R-stringr >= 1.0.0, R-utils, R-withr, R-xml2
# Suggests:  R-covr, R-rmarkdown >= 2.16, R-testthat >= 3.1.2, R-R.methodsS3, R-R.oo, R-yaml
# LinkingTo: cpp11
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-brew
BuildRequires:    R-cli >= 3.3.0
BuildRequires:    R-commonmark
BuildRequires:    R-desc >= 1.2.0
BuildRequires:    R-knitr
BuildRequires:    R-methods
BuildRequires:    R-pkgload >= 1.0.2
BuildRequires:    R-purrr >= 0.3.3
BuildRequires:    R-R6 >= 2.1.2
BuildRequires:    R-rlang >= 1.0.6
BuildRequires:    R-stringi
BuildRequires:    R-stringr >= 1.0.0
BuildRequires:    R-utils
BuildRequires:    R-withr
BuildRequires:    R-xml2
BuildRequires:    R-cpp11-devel
BuildRequires:    R-rmarkdown >= 2.16
BuildRequires:    R-testthat >= 3.1.2
BuildRequires:    R-R.methodsS3
BuildRequires:    R-R.oo
BuildRequires:    R-yaml

%description
Generate your Rd documentation, 'NAMESPACE' file, and collation field using
specially formatted comments. Writing documentation in-line with code makes it
easier to keep your documentation up-to-date as your requirements change.
'Roxygen2' is inspired by the 'Doxygen' system for C++.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/roxygen2-tags.yml

%changelog
%autochangelog
