%global packname rgeos
%global packver  0.6
%global packrev  4
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((maptools)\\)

# Suggests loops with maps and maptools.
%bcond_with suggests

Name:             R-%{packname}
Version:          %{packver}.%{packrev}
Release:          %autorelease
Summary:          Interface to Geometry Engine - Open Source ('GEOS')

License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrev}.tar.gz
# Not yet sure why this is necessary.
Patch0001:        %{packname}-Be-explicit-about-sp.patch

# Here's the R view of the dependencies world:
# Depends:   R-methods, R-sp >= 1.1-0
# Imports:   R-utils, R-stats, R-graphics
# Suggests:  R-maptools >= 0.8-5, R-testthat, R-XML, R-maps, R-rgdal
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    geos-devel >= 3.2.0
BuildRequires:    R-methods
BuildRequires:    R-sp-devel >= 1.1.0
BuildRequires:    R-utils
BuildRequires:    R-stats
BuildRequires:    R-graphics
BuildRequires:    R-testthat
BuildRequires:    R-XML
BuildRequires:    R-rgdal
%if %{with suggests}
BuildRequires:    R-maptools >= 0.8.5
BuildRequires:    R-maps
%endif

%description
Interface to Geometry Engine - Open Source ('GEOS') using the C 'API' for
topology operations on geometries.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch -P0001 -p1
popd

# Not important.
rm %{packname}/inst/SVN_VERSION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with suggests}
%{_bindir}/R CMD check --no-manual %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check --no-manual %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/poly-ex-gpc
%{rlibdir}/%{packname}/test_cases
%{rlibdir}/%{packname}/wkts


%changelog
%autochangelog
