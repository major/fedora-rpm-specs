%global packname jsonlite
%global packver  2.0.0
%global rlibdir  %{_libdir}/R/library

# Several hard-require this package or are not yet available.
%bcond_with suggests

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          A Simple and Robust JSON Parser and Generator for R

# Bundled yajl is ISC.
License:          MIT and ISC
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:
# Suggests:  R-httr, R-vctrs, R-testthat, R-knitr, R-rmarkdown, R-R.rsp, R-sf
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
%if %{with suggests}
BuildRequires:    R-httr
BuildRequires:    R-vctrs
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-R.rsp
BuildRequires:    R-sf
%endif
# https://github.com/jeroen/jsonlite/issues/201
Provides: bundled(yajl) = 2.1.1

%description
A reasonably fast JSON parser and generator, optimized for statistical data and
the web. Offers simple, flexible tools for working with JSON in R, and is
particularly powerful for building pipelines and interacting with a web API.
The implementation is based on the mapping described in the vignette (Ooms,
2014). In addition to converting JSON data from/to R objects, 'jsonlite'
contains functions to stream, validate, and prettify JSON data.  The unit tests
included with the package verify that all edge cases are encoded and decoded
consistently for use with dynamic data in systems and applications.


%prep
%setup -q -c -n %{packname}

%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes --no-examples --no-tests
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
%autochangelog
