%global packname hms
%global packver  1.1.2
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Pretty Time of Day

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-ellipsis >= 0.3.2, R-lifecycle, R-methods, R-pkgconfig, R-rlang, R-vctrs >= 0.3.8
# Suggests:  R-crayon, R-lubridate, R-pillar >= 1.1.0, R-testthat >= 3.0.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-ellipsis >= 0.3.2
BuildRequires:    R-lifecycle
BuildRequires:    R-methods
BuildRequires:    R-pkgconfig
BuildRequires:    R-rlang
BuildRequires:    R-vctrs >= 0.3.8
BuildRequires:    R-crayon
BuildRequires:    R-lubridate
BuildRequires:    R-pillar >= 1.1.0
BuildRequires:    R-testthat >= 3.0.0

%description
Implements an S3 class for storing and formatting time-of-day values, based
on the 'difftime' class.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


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


%changelog
%autochangelog
