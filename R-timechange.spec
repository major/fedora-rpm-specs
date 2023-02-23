%global packname timechange
%global packver	0.2.0
%global rlibdir %{_libdir}/R/library

Name:				R-%{packname}
Version:			%{packver}
Release:			%autorelease
Summary:			Efficient Updating of Date-Times

# Parts of the 'CCTZ' source code, released under the Apache 2.0 License
# while the rest is GPL-3.0-or-later
License:			GPL-3.0-or-later AND Apache-2.0
URL:				https://CRAN.R-project.org/package=%{packname}
Source0:			%{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:		R-devel
BuildRequires:		tex(latex)
BuildRequires:		R-cpp11-devel
BuildRequires:		R-knitr
BuildRequires:		R-testthat

%description	
Efficient routines for manipulation of date-time objects while accounting
for time-zones and daylight saving times. The package includes utilities
for updating of date-time components (year, month, day etc.), modification
of time-zones, rounding of date-times, period addition and subtraction etc.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
export _R_CHECK_FORCE_SUGGESTS_=0 LANG=C.UTF-8
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION	
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%changelog
%autochangelog
