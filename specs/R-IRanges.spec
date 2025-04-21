%global packname  IRanges
%global Rvers     4.0.0
%global suggests  0

Name:             R-%{packname}
Version:          2.42.0
Release:          %autorelease
Summary:          Low-level containers for storing sets of integer ranges
# Automatically converted from old format: Artistic 2.0 and Copyright only - review is highly recommended.
License:          Artistic-2.0 AND LicenseRef-Callaway-Copyright-only
# See https://www.redhat.com/archives/fedora-r-devel-list/2009-April/msg00001.html
URL:              http://bioconductor.org/packages/release/bioc/html/IRanges.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel >= %{Rvers} tex(latex)
BuildRequires:    R-methods R-stats R-RUnit R-utils R-stats4 R-BiocGenerics >= 0.53.2
BuildRequires:    R-S4Vectors-devel >= 0.45.4
%if %{suggests}
BuildRequires:    R-GenomicRanges
BuildRequires:    R-BSgenome.Celegans.UCSC.ce2
BuildRequires:    R-XVector
BuildRequires:    R-Rsamtools
BuildRequires:    R-GenomicAlignments
BuildRequires:    R-GenomicFeatures
BuildRequires:    R-pasillaBamSubset
BuildRequires:    R-RUnit
BuildRequires:    R-BiocStyle
%endif

%description
The IRanges class and its extensions are low-level containers
for storing sets of integer ranges. A typical use of these containers
in biology is for representing a set of chromosome regions.
More specific extensions of the IRanges class will typically
allow the storage of additional information attached to each
chromosome region as well as a hierarchical relationship between
these regions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}


# x86/x86_64 -> Architecture dependent package
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

%check
%if %{suggests}
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/unitTests

%files devel
%{_libdir}/R/library/%{packname}/include

%changelog
%autochangelog
