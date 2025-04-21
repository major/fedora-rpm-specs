%global packname   BufferedMatrix
%global Rvers      3.4.0

Name:              R-%{packname}
Version:           1.72.0
Release:           %autorelease
Summary:           A matrix data storage object method from bioconductor
Summary(fr):       Stockage des données d'un matrice dans un fichier temporaire
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:           LicenseRef-Callaway-LGPLv2+
URL:               http://bioconductor.org/packages/release/bioc/html/BufferedMatrix.html
Source0:           http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:     R-devel >= %{Rvers} tex(latex) R-methods

%package           devel
Summary:           Development files for %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description
A tabular style data object where most data is stored outside main memory.
A buffer is used to speed up access to data.

This library is part of the bioconductor (bioconductor.org) project.

%description -l fr
Une table de données dans laquelle la plus part des données sont stocké,
en dehors de la mémoire principale. Une mémoire tampon est utilisé pour
accélérer l'accès aux données.

%description    devel
The %{name}-devel  package contains Header and libraries files for
developing applications that use %{name}

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf %{buildroot}i
sed -i -e 's/\r$//' %{packname}/inst/doc/BufferedMatrix.Rnw

mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

## Change the header of place for the -devel --> Removed
## see: https://www.redhat.com/archives/fedora-r-devel-list/2009-March/msg00001.html

#mkdir -p  $RPM_BUILD_ROOT%{_datadir}/R/library/%{packname}/include/
#install -D %{packname}/inst/include/*  $RPM_BUILD_ROOT%{_datadir}/R/library/%{packname}/include/
#chmod -x $RPM_BUILD_ROOT%{_datadir}/R/library/%{packname}/include/*
#rm -rf %{buildroot}%{_libdir}/R/library/%{packname}/include/

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/NAMESPACE
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html

%files		devel
%{_libdir}/R/library/%{packname}/include/


%changelog
%autochangelog
