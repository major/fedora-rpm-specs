%bcond_with bootstrap
%bcond_with network

%global packname curl
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          7.0.0
Release:          %autorelease
Summary:          A Modern and Flexible Web Client for R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-spelling, R-testthat >= 1.0.0, R-knitr, R-jsonlite, R-rmarkdown, R-magrittr, R-httpuv >= 1.4.4, R-webutils
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pkgconfig(libcurl)
%if %{without bootstrap}
BuildRequires:    R-spelling
BuildRequires:    R-testthat >= 1.0.0
BuildRequires:    R-jsonlite
BuildRequires:    R-later
BuildRequires:    R-httpuv >= 1.4.4
BuildRequires:    R-knitr
BuildRequires:    glyphicons-halflings-fonts
BuildRequires:    R-rmarkdown
%if %{with network}
BuildRequires:    R-webutils
%endif
%endif

%description
The curl() and curl_download() functions provide highly configurable drop-in
replacements for base url() and download.file() with better performance,
support for encryption (https, ftps), gzip compression, authentication, and
other 'libcurl' goodies. The core of the package implements a framework for
performing fully customized requests where data can be processed either in
memory, on disk, or streaming via the callback or connection interfaces. Some
knowledge of 'libcurl' is recommended; for a more-user-friendly web client see
the 'httr' package which builds on this package with http specific tools and
logic.


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
export LANG=C.UTF-8
ARGS=
%if %{without network}
export _R_CHECK_FORCE_SUGGESTS_=0
ARGS="$ARGS --no-tests --no-examples --ignore-vignettes"
%endif
export _R_CHECK_FORCE_SUGGESTS_=0
ARGS="$ARGS --ignore-vignettes"
%{_bindir}/R CMD check %{packname} $ARGS
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
%autochangelog
