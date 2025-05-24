%bcond_with suggests

%global packname rlang
%global packver  1.1.6
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Functions for Base Types and Core R and 'Tidyverse' Features

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

Patch0001:        0001-Unbundle-libxxhash.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-utils
# Suggests:  R-cli >= 3.1.0, R-covr, R-crayon, R-fs, R-glue, R-knitr, R-magrittr, R-methods, R-pillar, R-rmarkdown, R-stats, R-testthat >= 3.0.0, R-tibble, R-usethis, R-vctrs >= 0.2.3, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    pkgconfig(libxxhash)
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
BuildRequires:    R-testthat >= 3.0.0
%if %{with suggests}
BuildRequires:    R-cli >= 3.1.0
BuildRequires:    R-crayon
BuildRequires:    R-desc
BuildRequires:    R-fs
BuildRequires:    R-glue
BuildRequires:    R-knitr
BuildRequires:    R-magrittr
BuildRequires:    R-methods
BuildRequires:    R-pillar
BuildRequires:    R-pkgload
BuildRequires:    R-rmarkdown
BuildRequires:    R-stats
BuildRequires:    R-tibble
BuildRequires:    R-usethis
BuildRequires:    R-vctrs >= 0.2.3
BuildRequires:    R-withr
%endif

%description
A toolbox for working with base types, core R features like the condition
system, and core 'Tidyverse' features like tidy evaluation.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch -P0001 -p1

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION

%if %{without suggests}
rm -f tests/testthat/test-deparse.R # pillar stuff
%endif
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes --no-manual
%endif


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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/backtrace-ver


%changelog
%autochangelog
