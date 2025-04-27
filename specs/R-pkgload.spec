%bcond_with check

%global packname pkgload
%global packver  1.4.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Simulate Package Installation and Attach

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:          GPL-3.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli, R-crayon, R-desc, R-methods, R-rlang, R-rprojroot, R-rstudioapi, R-utils, R-withr
# Suggests:  R-bitops, R-covr, R-pkgbuild, R-Rcpp, R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli >= 3.3.0
BuildRequires:    R-desc
BuildRequires:    R-fs
BuildRequires:    R-glue
BuildRequires:    R-lifecycle
BuildRequires:    R-methods
BuildRequires:    R-pkgbuild
BuildRequires:    R-processx
BuildRequires:    R-rlang >= 1.1.1
BuildRequires:    R-rprojroot
BuildRequires:    R-utils
BuildRequires:    R-withr >= 2.4.3
%if %{with check}
BuildRequires:    R-bitops
BuildRequires:    R-jsonlite
BuildRequires:    R-mathjaxr
BuildRequires:    R-pak
BuildRequires:    R-Rcpp-devel
BuildRequires:    R-remotes
BuildRequires:    R-rstudioapi
BuildRequires:    R-testthat >= 3.2.1.1
BuildRequires:    R-usethis
%endif

%description
Simulates the process of installing a package and then attaching it. This
is a key part of the 'devtools' package as it allows you to rapidly iterate
while developing a package.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/, covr//g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with check}
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/print-var.mk


%changelog
%autochangelog
