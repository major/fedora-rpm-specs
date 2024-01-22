%define       mver 2.0

Name:         guile-reader
Version:      0.6.3
Release:      2%{?dist}
Summary:      A simple framework for building readers for GNU Guile

License:      GPL-3.0-or-later
URL:          https://www.nongnu.org/guile-reader/%{name}
Source0:      https://git.savannah.nongnu.org/cgit/%{name}.git/snapshot/%{name}-%{version}.tar.gz 

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gperf
BuildRequires:  guile
BuildRequires:  guile-devel
BuildRequires:  libtool
# Error in configuring lightning, but optional
#BuildRequires:  lightning-devel
BuildRequires:  make
BuildRequires:  texinfo
Requires:       info

%package devel
Summary: Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}


%description
The idea is to make it easy to build procedures that extend
Guile’s read procedure. Readers supporting various syntax
variants can easily be written, possibly by re-using existing
“token readers” of a standard Scheme readers.

%description devel
Files to allow guile-reader to be used from other applications.

%prep
%autosetup
# Generate internationalization options
sed -i '/AC_CONFIG_AUX_DIR(build-aux)/a AM_GNU_GETTEXT_VERSION(0.18.2)' configure.ac

%build
autoupdate
autopoint
libtoolize
autoreconf -fi
%configure --with-guilemoduledir=%{_datadir}/guile/site/%{mver}
%make_build

%install
%make_install

#packaged by info package, updated by post-installation script, do not package here
#https://src.fedoraproject.org/rpms/gnuplot/blob/rawhide/f/gnuplot.spec
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

 
%check  
make check


%files
%license COPYING
%doc README
%doc NEWS
%doc ChangeLog
%doc THANKS
%{_libdir}/libguile-reader.so.1*

%files devel
%dir %{_datadir}/guile
%dir %{_datadir}/guile/site
%dir %{_datadir}/guile/site/%{mver}/
%dir %{_datadir}/guile/site/%{mver}/system
%{_datadir}/guile/site/%{mver}/system/*.scm
%{_datadir}/guile/site/%{mver}/system/*.go
%dir %{_datadir}/guile/site/%{mver}/system/documentation
%{_datadir}/guile/site/%{mver}/system/documentation/*.scm
%{_datadir}/guile/site/%{mver}/system/documentation/*.go
%dir %{_datadir}/guile/site/%{mver}/system/reader
%{_datadir}/guile/site/%{mver}/system/reader/*.scm
%{_datadir}/guile/site/%{mver}/system/reader/*.go
%{_infodir}/guile-reader.info*
%dir %{_includedir}/guile-reader
%{_includedir}/guile-reader/*.h
%{_libdir}/libguile-reader.so

%changelog
* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jun 28 2023 Benson Muite <benson_muite@emailplus.org> - 0.6.3-1
- Initial packaging
