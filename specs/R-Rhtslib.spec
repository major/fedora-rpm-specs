%global packname Rhtslib
%global rlibdir %{_libdir}/R/library

Name:		R-%{packname}
Version:	3.4.0
Release:	%autorelease
Summary:	HTSlib high-throughput sequencing library as an R package
License:	LGPL-2.0-or-later
URL:		http://www.bioconductor.org/packages/release/bioc/html/Rhtslib.html
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Patch1:		R-Rhtslib-buildroot-fix.patch
BuildRequires:	R-devel >= 3.0.0 bzip2-devel zlib-devel xz-devel libcurl-devel

# Do not check for Provides in internal shared libraries
%global __provides_exclude_from ^%{rlibdir}/%{packname}/usrlib/.*\\.so.*$

%description
This package provides version 1.15.1 of the 'HTSlib' C library for
high-throughput sequence analysis. The package is primarily useful to
developers of other R packages who wish to make use of HTSlib. Motivation and
instructions for use of this package are in the vignette,
vignette(package="Rhtslib", "Rhtslib").

%package devel
Summary:	Development files for R-Rhtslib
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}

%description devel
Development files for R-Rhtslib.

%prep
%setup -q -c -n %{packname}
pushd %{packname}
%patch -P1 -p1
popd

%build

%install
mkdir -p %{buildroot}%{rlibdir}
R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
# Missing R-BiocStyle
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{rlibdir}/%{packname}/
%doc %{rlibdir}/%{packname}/doc/
%doc %{rlibdir}/%{packname}/html/
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/testdata/
%{rlibdir}/%{packname}/libs/
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/usrlib/
%{rlibdir}/%{packname}/usrlib/*.so*

%files devel
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/usrlib/*.a

%changelog
%autochangelog
