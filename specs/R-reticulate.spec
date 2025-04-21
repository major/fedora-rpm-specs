%global packname reticulate
%global packver  1.20
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          R Interface to 'Python'

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:          Apache-2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Skip-network-tests.patch
Patch0002:        0002-rf-error.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Matrix, R-Rcpp >= 0.12.7, R-graphics, R-jsonlite, R-methods, R-png, R-rappdirs, R-utils, R-withr
# Suggests:  R-callr, R-knitr, R-rmarkdown, R-testthat
# LinkingTo:
# Enhances:

Requires:         python3
BuildRequires:    python3-devel
BuildRequires:    python3-docutils
BuildRequires:    python3-numpy
%ifnarch %{ix86}
# https://bugzilla.redhat.com/show_bug.cgi?id=2263999
BuildRequires:    python3-pandas
%endif
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Matrix
BuildRequires:    R-Rcpp-devel >= 0.12.7
BuildRequires:    R-graphics
BuildRequires:    R-jsonlite
BuildRequires:    R-methods
BuildRequires:    R-png
BuildRequires:    R-rappdirs
BuildRequires:    R-utils
BuildRequires:    R-withr
BuildRequires:    R-callr
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
# Test modules:
BuildRequires:   python3dist(docutils)
BuildRequires:   python3dist(matplotlib)
BuildRequires:   python3dist(numpy)
%ifnarch %{ix86}
BuildRequires:   python3dist(pandas)
%endif
BuildRequires:   python3dist(scipy)

%description
Interface to Python modules, classes, and functions. When calling into Python,
R data types are automatically converted to their equivalent Python types. When
values are returned from Python to R they are converted back to R types.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch -P0001 -p1
%patch -P0002 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%py_byte_compile %{python3} %{buildroot}%{rlibdir}/%{packname}/python/rpytools


%check
%{_bindir}/R CMD check --ignore-vignettes %{packname}


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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/config
%{rlibdir}/%{packname}/python


%changelog
%autochangelog
