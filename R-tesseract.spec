# Examples and vignettes use the network.
%bcond_with network

# Need to bootstrap for magick
%bcond_with bootstrap

%global packname tesseract
%global packver  5.1.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Open Source OCR Engine

License:          ASL 2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Fix leptonica include
Patch0:           R-tesseract_include.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.12.12, R-pdftools >= 1.5, R-curl, R-rappdirs, R-digest
# Suggests:  R-magick >= 1.7, R-spelling, R-knitr, R-tibble, R-rmarkdown
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel >= 0.12.12
BuildRequires:    R-pdftools >= 1.5
BuildRequires:    R-curl
BuildRequires:    R-rappdirs
BuildRequires:    R-digest
%if %{without bootstrap}
BuildRequires:    R-magick >= 1.7
BuildRequires:    R-spelling
BuildRequires:    R-knitr
BuildRequires:    R-tibble
BuildRequires:    R-rmarkdown
%endif
BuildRequires:    pkgconfig(lept)
BuildRequires:    pkgconfig(tesseract)
%if %{with network}
# For rmarkdown, because docs get built.
BuildRequires:    glyphicons-halflings-fonts
%endif

%description
Bindings to 'Tesseract' <https://opensource.google/projects/tesseract>: a
powerful optical character recognition (OCR) engine that supports over 100
languages. The engine is highly configurable in order to tune the detection
algorithms and obtain the best possible results.


%prep
%autosetup -p1 -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%if %{with network}
%{_bindir}/R CMD check %{packname}
%else
%{_bindir}/R CMD check %{packname} --no-examples --no-vignettes
%endif
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/AUTHORS
%license %{rlibdir}/%{packname}/COPYRIGHT
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/WORDLIST


%changelog
%autochangelog
