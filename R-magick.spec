%global packname magick
%global packver  2.7.4
%global rlibdir  %{_libdir}/R/library

%bcond_with bootstrap
%global __suggests_exclude ^R\\((av|gifski)\\)

# Examples and vignettes require the network.
%bcond_with network

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Advanced Graphics and Image-Processing in R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.12.12, R-magrittr, R-curl
# Suggests:  R-av >= 0.3, R-spelling, R-jsonlite, R-methods, R-knitr, R-rmarkdown, R-rsvg, R-webp, R-pdftools, R-ggplot2, R-gapminder, R-IRdisplay, R-tesseract >= 2.0, R-gifski
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel >= 0.12.12
BuildRequires:    R-magrittr
BuildRequires:    R-curl
BuildRequires:    R-spelling
BuildRequires:    R-jsonlite
BuildRequires:    R-methods
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-rsvg
BuildRequires:    R-webp
BuildRequires:    R-ggplot2
BuildRequires:    R-gapminder
BuildRequires:    R-IRdisplay
%if %{without bootstrap}
BuildRequires:    R-pdftools
BuildRequires:    R-tesseract >= 2.0
%endif
BuildRequires:    pkgconfig(Magick++)

# Uses rust, so unlikely to package it soon.
# BuildRequires:    R-gifski
# Not in Fedora yet.
# BuildRequires:    R-av >= 0.3

%description
Bindings to 'ImageMagick': the most comprehensive open-source image
processing library available. Supports many common formats (png, jpeg,
tiff, pdf, etc) and manipulations (rotate, scale, crop, trim, flip, blur,
etc). All operations are vectorized via the Magick++ STL meaning they
operate either on a single frame or a series of frames for working with
layers, collages, or animation. In RStudio images are automatically
previewed when printed to the console, resulting in an interactive editing
environment. The latest version of the package includes a native graphics
device for creating in-memory graphics or drawing onto images using pixel
coordinates.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with network}
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples --no-vignettes
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/images


%changelog
%autochangelog
