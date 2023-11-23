%bcond_with bootstrap

%global packname stringr
%global packver  1.5.1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Simple, Consistent Wrappers for Common String Operations

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli, R-glue >= 1.6.1, R-lifecycle >= 1.0.3, R-magrittr, R-rlang >= 1.0.0, R-stringi >= 1.5.3, R-vctrs >= 0.4.0
# Suggests:  R-covr, R-dplyr, R-gt, R-htmltools, R-htmlwidgets, R-knitr, R-rmarkdown, R-testthat >= 3.0.0, R-tibble
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli
BuildRequires:    R-glue >= 1.6.1
BuildRequires:    R-lifecycle >= 1.0.3
BuildRequires:    R-magrittr
BuildRequires:    R-rlang >= 1.0.0
BuildRequires:    R-stringi >= 1.5.3
BuildRequires:    R-vctrs >= 0.4.0
%if %{without bootstrap}
BuildRequires:    R-dplyr
# BuildRequires:    R-gt
BuildRequires:    R-htmltools
BuildRequires:    R-htmlwidgets
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-tibble
%endif

%description
A consistent, simple and easy to use set of wrappers around the fantastic
'stringi' package. All function and argument names (and positions) are
consistent, all functions deal with "NA"'s and zero length vectors in the
same way, and the output from one function is easy to feed into the input
of another.


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
%if %{without bootstrap}
export LANG=C.UTF-8
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/htmlwidgets


%changelog
%autochangelog
