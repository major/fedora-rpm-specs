%global srcnm Qalculate
%global libversion 23
%global libsymlink 3.2

Summary:	Multi-purpose calculator library
Name:		libqalculate
Version:	5.5.0
Release:	%autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later

URL:		https://qalculate.github.io/
Source0:	https://github.com/%{srcnm}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	glib2-devel
BuildRequires:	cln-devel
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	curl-devel
BuildRequires:	libicu-devel
BuildRequires:	mpfr-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	gettext
BuildRequires:	perl(Getopt::Long)
BuildRequires: make

%description
This library underpins the Qalculate! multi-purpose desktop calculator for
GNU/Linux

%package	devel
Summary:	Development tools for the Qalculate calculator library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	glib2-devel
Requires:	libxml2-devel
Requires:	cln-devel
Requires:	mpfr-devel

%description	devel
The libqalculate-devel package contains the header files needed for development
with libqalculate.

%package -n	qalculate
Summary:	Multi-purpose calculator, text mode interface
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

Provides:	qalc

%description -n	qalculate
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides the text-mode interface for Qalculate! The GTK and QT
frontends are provided by qalculate-gtk and qalculate-kde packages resp.

%prep
%setup -q

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

%find_lang %{name}
rm -f %{buildroot}/%{_libdir}/*.la

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_libdir}/libqalculate.so.%{libversion}
%{_libdir}/libqalculate.so.%{libversion}.%{libsymlink}
%{_datadir}/qalculate/

%files devel
%{_libdir}/libqalculate.so
%{_libdir}/pkgconfig/libqalculate.pc
%{_includedir}/libqalculate/

%files -n qalculate
%{_bindir}/qalc
%{_mandir}/man1/qalc.1*

%changelog
%autochangelog
