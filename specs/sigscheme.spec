Name:		sigscheme
Version:	0.9.6
Release:	%autorelease
License:	BSD-3-Clause
URL:		https://github.com/uim/sigscheme
BuildRequires: make
BuildRequires:	libgcroots-devel
BuildRequires:	gcc

Source0:	https://github.com/uim/sigscheme/releases/download/%{version}/%{name}-%{version}.tar.bz2
#Patch1:		%%{name}-vararg-func.patch


Summary:	R5RS Scheme interpreter for embedded use

%description
sigscheme is a R5RS Scheme interpreter that features small footprint,
low memory consumption, multibytes characters handling and more.

%package devel
Summary:	Development files for sigscheme
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
sigscheme is a R5RS Scheme interpreter that features small footprint,
low memory consumption, multibytes characters handling and more.

This package contains header files and development library.

%prep
%autosetup -p1

%build
%configure --disable-static --with-libgcroots=installed
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

# Remove unnecessary files
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}/sigscheme

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS QALog README RELNOTE TODO
%doc doc/*.html doc/*.txt
%{_bindir}/sscm
%{_libdir}/libsscm.so.3*
%{_datadir}/sigscheme

%files devel
%license COPYING
%doc AUTHORS NEWS QALog README RELNOTE TODO
%{_includedir}/sigscheme
%{_libdir}/libsscm.so
%{_libdir}/pkgconfig/sigscheme.pc

%changelog
%autochangelog
