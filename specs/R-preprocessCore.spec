%global packname  preprocessCore
%global Rvers     3.4.0

Name:             R-%{packname}
Version:          1.70.0
Release:          %autorelease
Summary:          A collection of pre-processing functions
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:          LicenseRef-Callaway-LGPLv2+
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Source1:          preprocessCore_license
BuildRequires:    R-devel >= %{Rvers} tex(latex) R-stats
BuildRequires:    autoconf, automake, libtool

%package           devel
Summary:           Development files for %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description
A library of core preprocessing routines

%description    devel
The %{name}-devel  package contains Header and libraries files for
developing applications that use %{name}

%prep
%setup -q -c -n %{packname}
pushd %{packname}
autoreconf -ifv .
popd

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

## Keep the headers of place for the -devel
## see: https://www.redhat.com/archives/fedora-r-devel-list/2009-March/msg00001.html

install -m 664 -p %{SOURCE1}  %{buildroot}%{_libdir}/R/library/%{packname}

%check
%if 0
# 2020-09-10: sh: line 1: 1879370 Segmentation fault      (core dumped) LANGUAGE=en _R_CHECK_INTERNALS2_=1 '/usr/lib64/R/bin/R' --vanilla > 'preprocessCore-Ex.Rout' 2>&1 <
%ifnarch s390x
%{_bindir}/R CMD check %{packname}
%endif
%endif

%files
#i386 arch
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/preprocessCore_license
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/help

%files          devel
%{_libdir}/R/library/%{packname}/include/

%changelog
%autochangelog
