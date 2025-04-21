%define packname  affyio
%define Rversion  3.4.0

Name:             R-%{packname}
Version:          1.78.0
Release:          %autorelease
Summary:          Tools for parsing Affymetrix data files
Summary(fr):      Outils d'analyse de fichier de données de puces affymetrix
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:          LicenseRef-Callaway-LGPLv2+
URL:              http://bioconductor.org/packages/release/bioc/html/affyio.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel >= %{Rversion} tex(latex) zlib-devel R-methods

%description
Routines for parsing Affymetrix data files based upon file format 
information. Primary focus is on accessing the CEL and CDF file formats.

%description -l fr
Scripts pour analyser les fichiers de données issuent de puces affymetrix
basé sur les informations fournis pas les extensions. Un des premier 
objectifs est de convertir les données dans des fichiers au format
CEL ou CDF.

%prep
%setup -q -c -n %{packname}
sed -i '/Imports: zlibbioc/d' %{packname}/DESCRIPTION
sed -i '/import(zlibbioc)/d' %{packname}/NAMESPACE

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir}/R/library 
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css


%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs

%changelog
%autochangelog
