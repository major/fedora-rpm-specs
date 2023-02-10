%bcond_with bootstrap

%global packname pdftools
%global packver  3.3.3
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          %autorelease
Summary:          Text Extraction, Rendering and Converting of PDF Documents

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.12.12, R-qpdf
# Suggests:  R-png, R-webp, R-tesseract, R-testthat
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel >= 0.12.12
BuildRequires:    R-qpdf
%if %{without bootstrap}
BuildRequires:    R-png
BuildRequires:    R-webp
BuildRequires:    R-tesseract
BuildRequires:    R-testthat
%endif
BuildRequires:    poppler-cpp-devel
BuildRequires:    poppler-data

%description
Utilities based on 'libpoppler' for extracting text, fonts, attachments and
metadata from a PDF file. Also supports high quality rendering of PDF documents
into PNG, JPEG, TIFF format, or into raw bitmap vectors for further processing
in R.


%prep
%setup -q -c -n %{packname}
cd %{packname}
%autopatch -p1


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
%autochangelog
