%bcond_with check

%global packname testthat
%global packver 3.2.0

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Unit Testing for R

License:          MIT
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.6.0, tetex-latex
BuildRequires:    R-brio >= 1.1.3
BuildRequires:    R-callr >= 3.7.3
BuildRequires:    R-cli >= 3.6.1
BuildRequires:    R-desc >= 1.4.2
BuildRequires:    R-digest >= 0.6.33
BuildRequires:    R-ellipsis >= 0.3.2
BuildRequires:    R-evaluate >= 0.21
BuildRequires:    R-jsonlite >= 1.8.7
BuildRequires:    R-lifecycle >= 1.0.3
BuildRequires:    R-magrittr >= 2.0.3
BuildRequires:    R-methods
BuildRequires:    R-pkgload >= 1.3.2.1
BuildRequires:    R-praise >= 1.0.0
BuildRequires:    R-processx >= 3.8.2
BuildRequires:    R-ps >= 1.7.5
BuildRequires:    R-R6 >= 2.5.1
BuildRequires:    R-rlang >= 1.1.1
BuildRequires:    R-utils
BuildRequires:    R-waldo >= 0.5.1
BuildRequires:    R-withr >= 2.5.0

BuildRequires:    R-curl >= 0.9.5
# for skip_if_offline()
Requires:         R-curl
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-rstudioapi
BuildRequires:    R-shiny
BuildRequires:    R-usethis
BuildRequires:    R-vctrs >= 0.1.0
BuildRequires:    R-xml2
# Not in Fedora as of 2023-11-01
# BuildRequires:    R-diffviewer >= 0.1.0

%description
A unit testing system designed to be fun, flexible, and easy to set up.

%prep
%setup -q -c -n %{packname}

# Don't need coverage
sed -i 's/covr, //g' %{packname}/DESCRIPTION

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check
export _R_CHECK_FORCE_SUGGESTS_=0 LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes --no-manual %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/CITATION
# Not the actual license text. Not too useful.
%doc %{_libdir}/R/library/%{packname}/LICENSE
%doc %{_libdir}/R/library/%{packname}/NEWS.md
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/examples/
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/resources/
%{_libdir}/R/library/%{packname}/include/

%changelog
%autochangelog
