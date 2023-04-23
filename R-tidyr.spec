%global packname tidyr
%global packver  1.3.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Tidy Messy Data

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli >= 3.4.1, R-dplyr >= 1.0.10, R-glue, R-lifecycle >= 1.0.3, R-magrittr, R-purrr >= 1.0.1, R-rlang >= 1.0.4, R-stringr >= 1.5.0, R-tibble >= 2.1.1, R-tidyselect >= 1.2.0, R-utils, R-vctrs >= 0.5.2
# Suggests:  R-covr, R-data.table, R-knitr, R-readr, R-repurrrsive >= 1.1.0, R-rmarkdown, R-testthat >= 3.0.0
# LinkingTo: R-cpp11 >= 0.4.0
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli >= 3.4.1
BuildRequires:    R-dplyr >= 1.0.10
BuildRequires:    R-glue
BuildRequires:    R-lifecycle >= 1.0.3
BuildRequires:    R-magrittr
BuildRequires:    R-purrr >= 1.0.1
BuildRequires:    R-rlang >= 1.0.4
BuildRequires:    R-stringr >= 1.5.0
BuildRequires:    R-tibble >= 2.1.1
BuildRequires:    R-tidyselect >= 1.2.0
BuildRequires:    R-utils
BuildRequires:    R-vctrs >= 0.5.2
BuildRequires:    R-cpp11-devel >= 0.4.0
BuildRequires:    R-data.table
BuildRequires:    R-knitr
BuildRequires:    R-readr
BuildRequires:    R-repurrrsive >= 1.1.0
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 3.0.0

%description
Tools to help to create tidy data, where each column is a variable, each
row is an observation, and each cell contains a single value.  'tidyr'
contains tools for changing the shape (pivoting) and hierarchy (nesting and
'unnesting') of a dataset, turning deeply nested lists into rectangular
data frames ('rectangling'), and extracting values out of string columns.
It also includes tools for working with missing values (both implicit and
explicit).


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
%{_bindir}/R CMD check --ignore-vignettes %{packname}


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
%{rlibdir}/%{packname}/data


%changelog
%autochangelog
