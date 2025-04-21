%global packname  S4Vectors
%global rlibdir %{_libdir}/R/library

%global __suggests_exclude ^R\\((BiocStyle|ShortRead|graph)\\)

Name:             R-%{packname}
Version:          0.46.0
Release:          %autorelease
Summary:          S4 implementation of vectors and lists
License:          Artistic-2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/S4Vectors.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel >= 4.0.0 tex(latex) R-methods R-utils R-stats R-stats4
BuildRequires:    R-BiocGenerics >= 0.53.2

%description
The S4Vectors package defines the Vector and List virtual classes and a set of
generic functions that extend the semantic of ordinary vectors and lists in R.
Package developers can easily implement vector-like or list-like objects as
concrete subclasses of Vector or List. In addition, a few low-level concrete
subclasses of general interest (e.g. DataFrame, Rle, and Hits) are implemented
in the S4Vectors package itself (many more are implemented in the IRanges
package and in other Bioconductor infrastructure packages).

%package devel
Summary:          Development files for R-S4Vectors
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for R-S4Vectors.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
# Testing tests optional deps we don't package
# _R_CHECK_FORCE_SUGGESTS_=false %%{_bindir}/R CMD check %%{packname}

%files
%dir %{rlibdir}/%{packname}/
%doc %{rlibdir}/%{packname}/html/
%doc %{rlibdir}/%{packname}/doc/
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/help/
%{rlibdir}/%{packname}/unitTests/
%{rlibdir}/%{packname}/libs/

%files devel
%{rlibdir}/%{packname}/include/

%changelog
%autochangelog
