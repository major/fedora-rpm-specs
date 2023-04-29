%bcond_without check

%global packname quantities
%global rlibdir %{_libdir}/R/library

Name:           R-%{packname}
Version:        0.2.1
Release:        %autorelease
Summary:        Quantity Calculus for R Vectors

License:        MIT
URL:            https://cran.r-project.org/package=%{packname}
Source0:        https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

BuildRequires:  R-devel >= 3.1.0, R-Rcpp-devel >= 0.12.10
BuildRequires:  R-units >= 0.8.0, R-errors >= 0.4.0
%if %{with check}
# BuildRequires:  R-dplyr >= 1.0.0, R-vctrs >= 0.5.0, R-tidyr, R-pillar
# BuildRequires:  R-ggplot2 > 3.2.1, R-vdiffr
BuildRequires:  R-testthat
BuildRequires:  R-knitr, R-markdown
%endif

%description
Integration of the 'units' and 'errors' packages for a complete quantity
calculus system for R vectors, matrices and arrays, with automatic
propagation, conversion, derivation and simplification of magnitudes and
uncertainties.
Documentation about 'units' and 'errors' is provided in the papers by Pebesma,
Mailund & Hiebert (2016, <doi:10.32614/RJ-2016-061>) and by Ucar, Pebesma &
Azcorra (2018, <doi:10.32614/RJ-2018-075>), included in those packages as
ignettes; see 'citation("quantities")' for details.

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
%{_bindir}/R CMD check --no-manual --ignore-vignettes %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

%changelog
%autochangelog
