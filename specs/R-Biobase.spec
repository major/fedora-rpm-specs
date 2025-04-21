%define packname  Biobase
%define Rversion  3.4.0

Name:             R-%{packname}
Version:          2.68.0
Release:          %autorelease
Summary:          Base functions for Bioconductor
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/Biobase.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel >= %{Rversion} tex(latex) R-tkWidgets R-BiocGenerics >= 0.27.1 R-utils R-methods

%description
Base functions for Bioconductor (bioconductor.org). Biobase provides
functions that are needed by many other Bioconductor packages or which
replace R functions.

%description -l fr
Bibliothèque contenant des fonctions requises par d'autres bibliothèques
ou qui remplacent certaines fonctions dans R

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

%check
# This library ask for the library ALL which can not be compiled without
# R-Biobase
#%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/unitTests/
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/scripts
%{_libdir}/R/library/%{packname}/ExpressionSet
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/Code
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/testClass.R
%{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/doc
%{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html

%changelog
%autochangelog
