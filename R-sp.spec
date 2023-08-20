%global packname sp
%global packver  2.0-0
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((gstat|maptools)\\)

# Limit loops and extra dependencies.
%global with_suggests 0

Name:             R-%{packname}
Version:          2.0.0
Release:          %autorelease
Summary:          Classes and Methods for Spatial Data

License:          GPL-2.0-or-later
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-utils, R-stats, R-graphics, R-grDevices, R-lattice, R-grid
# Suggests:  R-RColorBrewer, R-rgdal >= 1.2-3, R-rgeos >= 0.3-13, R-gstat, R-maptools, R-deldir, R-knitr, R-rmarkdown, R-sf, R-terra, R-raster
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
BuildRequires:    R-stats
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-lattice
BuildRequires:    R-grid
%if 0%{with_suggests}
BuildRequires:    R-RColorBrewer
BuildRequires:    R-gstat
BuildRequires:    R-deldir
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-sf
BuildRequires:    R-terra
BuildRequires:    R-raster
%endif

%description
Classes and methods for spatial data; the classes document where the spatial
location information resides, for 2D or 3D data. Utility functions are
provided, e.g. for plotting data as maps, spatial selection, as well as methods
for retrieving coordinates, for subsetting, print, summary, etc.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%if %{with_loop}
%{_bindir}/R CMD check %{packname}
%else
rm %{packname}/tests/agg.R* %{packname}/tests/over2.R*  # whole file requires rgeos
%{_bindir}/R CMD check %{packname} --no-examples --no-vignettes
%endif
%else
rm %{packname}/tests/agg.R* %{packname}/tests/over2.R*  # whole file requires rgeos
_R_CHECK_FORCE_SUGGESTS_=0 \
    %{_bindir}/R CMD check %{packname} --no-examples --no-vignettes
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
%autochangelog
