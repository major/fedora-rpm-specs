%global packname ragg
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3.3
Release:          %autorelease
Summary:          Graphic Devices Based on AGG

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source:           https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-systemfonts >= 1.0.3, R-textshaping >= 0.3.0
# Suggests:  R-covr, R-graphics, R-grid, R-testthat >= 3.0.0
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-systemfonts-devel >= 1.0.3
BuildRequires:    R-textshaping-devel >= 0.3.0
BuildRequires:    R-graphics
BuildRequires:    R-grid
BuildRequires:    R-testthat >= 3.0.0

BuildRequires:    gcc-c++
BuildRequires:    pkgconfig(freetype2)
BuildRequires:    pkgconfig(libpng)
BuildRequires:    pkgconfig(libtiff-4)
BuildRequires:    libjpeg-devel

%description
Anti-Grain Geometry (AGG) is a high-quality and high-performance 2D drawing
library. The 'ragg' package provides a set of graphic devices based on AGG
to use as alternative to the raster devices provided through the
'grDevices' package.


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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
%autochangelog
