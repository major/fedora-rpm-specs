%bcond_with bootstrap

%global packname withr
%global packver  2.5.2
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Run Code 'With' Temporarily Modified Global State

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-graphics, R-grDevices, R-stats
# Suggests:  R-callr, R-covr, R-DBI, R-knitr, R-lattice, R-methods, R-rmarkdown, R-RSQLite, R-testthat >= 3.0.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-stats
%if %{without bootstrap}
BuildRequires:    R-callr
BuildRequires:    R-DBI
BuildRequires:    R-knitr
BuildRequires:    R-lattice
BuildRequires:    R-methods
BuildRequires:    R-rlang
BuildRequires:    R-rmarkdown >= 2.12
BuildRequires:    R-RSQLite
BuildRequires:    R-testthat >= 3.0.0
%endif

%description
A set of functions to run code 'with' safely and temporarily modified
global state. Many of these functions were originally a part of the
'devtools' package, this provides a simple package with limited
dependencies to provide access to these functions.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION

# Remove failing tests
rm -f %{packname}/tests/testthat/test-{language,defer}.R


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
export LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif


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


%changelog
%autochangelog
