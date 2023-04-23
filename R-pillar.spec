%bcond_with check

%global packname pillar
%global packver  1.9.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Coloured Formatting for Columns

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli >= 2.3.0, R-fansi, R-glue, R-lifecycle, R-rlang >= 1.0.2, R-utf8 >= 1.1.0, R-utils, R-vctrs >= 0.3.8
# Suggests:  R-bit64, R-debugme, R-DiagrammeR, R-dplyr, R-formattable, R-ggplot2, R-knitr, R-lubridate, R-nanotime, R-nycflights13, R-palmerpenguins, R-rmarkdown, R-scales, R-stringi, R-survival, R-testthat >= 3.1.1, R-tibble, R-units >= 0.7.2, R-vdiffr, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli >= 2.3.0
BuildRequires:    R-fansi
BuildRequires:    R-glue
BuildRequires:    R-lifecycle
BuildRequires:    R-rlang >= 1.0.2
BuildRequires:    R-utf8 >= 1.1.0
BuildRequires:    R-utils
BuildRequires:    R-vctrs >= 0.5.0
%if %{with check}
BuildRequires:    R-bit64
BuildRequires:    R-debugme
BuildRequires:    R-DiagrammeR
BuildRequires:    R-dplyr
BuildRequires:    R-formattable
BuildRequires:    R-ggplot2
BuildRequires:    R-knitr
BuildRequires:    R-lubridate
BuildRequires:    R-nanotime
BuildRequires:    R-nycflights13
BuildRequires:    R-palmerpenguins
BuildRequires:    R-rmarkdown
BuildRequires:    R-scales
BuildRequires:    R-stringi
BuildRequires:    R-survival
BuildRequires:    R-testthat >= 3.1.1
BuildRequires:    R-tibble
BuildRequires:    R-units >= 0.7.2
BuildRequires:    R-vdiffr
BuildRequires:    R-withr
%endif

%description
Provides 'pillar' and 'colonnade' generics designed for formatting columns
of data using the full range of colours provided by modern terminals.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with check}
export LANG=C.UTF-8
%{_bindir}/R CMD check %{packname}
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
%{rlibdir}/%{packname}/WORDLIST


%changelog
%autochangelog
