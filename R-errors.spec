%bcond_without check

%global packname errors
%global rlibdir %{_datadir}/R/library

Name:           R-%{packname}
Version:        0.4.1
Release:        %autorelease
Summary:        Uncertainty Propagation for R Vectors

License:        MIT
URL:            https://cran.r-project.org/package=%{packname}
Source0:        %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:  R-devel >= 3.0.0
%if %{with check}
# BuildRequires:  R-dplyr >= 1.0.0, R-vctrs >= 0.5.0, R-pillar
# BuildRequires:  R-ggplot2 > 3.2.1, R-vdiffr
BuildRequires:  R-testthat
BuildRequires:  R-knitr, R-rmarkdown
%endif
BuildArch:      noarch

%description
Support for measurement errors in R vectors, matrices and arrays:
automatic uncertainty propagation and reporting.
Documentation about 'errors' is provided in the paper by Ucar,
Pebesma & Azcorra (2018, <doi:10.32614/RJ-2018-075>), included in
this package as a vignette; see 'citation("errors")' for details.

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
export _R_CHECK_FORCE_SUGGESTS_=0
rm -rf %{packname}/tests/testthat/{_snaps,test-tidyverse.R}
%{_bindir}/R CMD check --no-manual --ignore-vignettes %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data

%changelog
%autochangelog
