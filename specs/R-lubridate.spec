%global packname lubridate
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.9.4
Release:          %autorelease
Summary:          Make dealing with dates a little easier
License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source:           https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-generics, R-timechange >= 0.1.1
# Suggests:  R-covr, R-knitr, R-rmarkdown, R-testthat >= 2.1.0, R-vctrs >= 0.5.0
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-generics
BuildRequires:    R-timechange >= 0.3.0
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-vctrs >= 0.6.5

%description
Functions to work with date-times and time-spans: fast and user friendly
parsing of date-time data, extraction and updating of components of a date-time
(years, months, days, hours, minutes, and seconds), algebraic manipulation on
date-time and time-span objects. The 'lubridate' package has a consistent and
memorable syntax that makes working with dates easy and fun.


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

# Used to update sources; don't need to package it.
rm %{buildroot}%{rlibdir}/%{packname}/cctz.sh


%check
%{_bindir}/R CMD check --ignore-vignettes %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/pkgdown
%{rlibdir}/%{packname}/WORDLIST


%changelog
%autochangelog
