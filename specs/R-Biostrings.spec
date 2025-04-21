%global packname  Biostrings
%global Rvers     4.1.0
%global IRange    2.31.2

Name:             R-%{packname}
Version:          2.76.0
Release:          %autorelease
Summary:          String objects representing biological sequences
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/Biostrings.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel >= %{Rvers} tex(latex) R-methods R-utils R-IRanges-devel >= %{IRange}
BuildRequires:    R-XVector-devel >= 0.37.1, R-BiocGenerics >= 0.37.0, R-S4Vectors-devel >= 0.27.12
BuildRequires:    R-graphics, R-methods, R-stats, R-utils, R-grDevices, R-crayon, R-GenomeInfoDb

%description
Memory efficient string containers, string matching algorithms, and other
utilities, for fast manipulation of large biological sequences or set of
sequences.

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

# architecture dependent package
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

# Empty file
rm -f %{buildroot}%{_libdir}/R/library/%{packname}/doc/GenomeSearching.R

%check
# Requires for R-BSgenome which cannot build without R-Biostring
#%%{_bindir}/R CMD check %%{packname}

%files
#i386 arch
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc
%{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/unitTests/

%files devel
%{_libdir}/R/library/%{packname}/include

%changelog
%autochangelog
