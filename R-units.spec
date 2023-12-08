%global packname  units
%global packvers  0.8
%global packrel   5
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        %{packvers}.%{packrel}
Release:        %autorelease
Summary:        Measurement Units for R Vectors

License:        GPL-2.0-or-later
URL:            https://cran.r-project.org/package=%{packname}
Source0:        %{url}&version=%{packvers}-%{packrel}#/%{packname}_%{packvers}-%{packrel}.tar.gz

BuildRequires:  R-devel >= 3.0.0
BuildRequires:  udunits2-devel
BuildRequires:  R-Rcpp-devel >= 0.12.10
# BuildRequires:  R-NISTunits, R-measurements
# BuildRequires:  R-magrittr, R-pillar >= 1.3.0, R-dplyr >= 1.0.0, R-vctrs >= 0.3.1
# BuildRequires:  R-ggplot2 > 3.2.1, R-vdiffr
BuildRequires:  R-testthat >= 3.0.0
# BuildRequires:  R-knitr, R-rmarkdown
Recommends:     R-xml2
Obsoletes:      R-units-devel < 0.6.3

%description
Support for measurement units in R vectors, matrices and arrays: automatic
propagation, conversion, derivation and simplification of units; raising
errors in case of unit incompatibility. Compatible with the POSIXct, Date
and difftime classes. Uses the UNIDATA udunits library and unit database
for unit compatibility checking and conversion.
Documentation about 'units' is provided in the paper by Pebesma, Mailund
& Hiebert (2016, <doi:10.32614/RJ-2016-061>), included in this package as
a vignette; see 'citation("units")' for details.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
export LANG=C.UTF-8
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check --no-manual --ignore-vignettes %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/share

%changelog
%autochangelog
