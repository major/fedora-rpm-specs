%global packname  maps
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((mapdata|maptools|rnaturalearth)\\)

# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%{?_with_bootstrap: %global bootstrap 1}
# Disable things for review.
%global bootstrap 1

Name:             R-%{packname}
Version:          3.4.2.1
Release:          %autorelease
Summary:          Draw Geographical Maps

License:          GPL-2.0-only
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-graphics, R-utils
# Suggests:  R-mapproj >= 1.2-0, R-mapdata >= 2.3.0, R-sp, R-rnaturalearth
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-graphics
BuildRequires:    R-utils
BuildRequires:    R-sp
%if ! 0%{?bootstrap}
BuildRequires:    R-mapproj >= 1.2.0
BuildRequires:    R-mapdata >= 2.3.0
BuildRequires:    R-rnaturalearth
%endif

%description
Display of maps.  Projection code and larger maps are in separate packages
('mapproj' and 'mapdata').


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if ! 0%{?bootstrap}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/mapdata


%changelog
%autochangelog
