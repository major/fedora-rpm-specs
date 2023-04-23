%bcond_with suggests

%global packname tibble
%global packver  3.2.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Simple Data Frames

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-fansi >= 0.4.0, R-lifecycle >= 1.0.0, R-magrittr, R-methods, R-pillar >= 1.8.1, R-pkgconfig, R-rlang >= 1.0.2, R-utils, R-vctrs >= 0.4.2
# Suggests:  R-bench, R-bit64, R-blob, R-brio, R-callr, R-cli, R-covr, R-crayon >= 1.3.4, R-DiagrammeR, R-dplyr, R-evaluate, R-formattable, R-ggplot2, R-here, R-hms, R-htmltools, R-knitr, R-lubridate, R-mockr, R-nycflights13, R-pkgbuild, R-pkgload, R-purrr, R-rmarkdown, R-stringi, R-testthat >= 3.0.2, R-tidyr, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-fansi >= 0.4.0
BuildRequires:    R-lifecycle >= 1.0.0
BuildRequires:    R-magrittr
BuildRequires:    R-methods
BuildRequires:    R-pillar >= 1.8.1
BuildRequires:    R-pkgconfig
BuildRequires:    R-rlang >= 1.0.2
BuildRequires:    R-utils
BuildRequires:    R-vctrs >= 0.4.2
%if %{with suggests}
BuildRequires:    R-bench
BuildRequires:    R-bit64
BuildRequires:    R-blob
BuildRequires:    R-brio
BuildRequires:    R-callr
BuildRequires:    R-cli
BuildRequires:    R-crayon >= 1.3.4
BuildRequires:    R-DiagrammeR
BuildRequires:    R-dplyr
BuildRequires:    R-evaluate
BuildRequires:    R-formattable
BuildRequires:    R-ggplot2
BuildRequires:    R-here
BuildRequires:    R-hms
BuildRequires:    R-htmltools
BuildRequires:    R-knitr
BuildRequires:    R-lubridate
BuildRequires:    R-mockr
BuildRequires:    R-nycflights13
BuildRequires:    R-pkgbuild
BuildRequires:    R-pkgload
BuildRequires:    R-purrr
BuildRequires:    R-rmarkdown
BuildRequires:    R-stringi
BuildRequires:    R-testthat >= 3.0.2
BuildRequires:    R-tidyr
BuildRequires:    R-withr
%endif

%description
Provides a 'tbl_df' class (the 'tibble') with stricter checking and better
formatting than the traditional data frame.


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
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples --no-vignettes --no-tests
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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
%autochangelog
