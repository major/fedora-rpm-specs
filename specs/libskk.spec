Name:		libskk
Version:	1.1.1
Release:	%{?autorelease}%{!?autorelease:1%{?dist}}
Summary:	Library to deal with Japanese kana-to-kanji conversion method

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/ueno/libskk
Source0:	https://github.com/ueno/libskk/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:	vala
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	json-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gettext-devel
BuildRequires:	libxkbcommon-devel

%description
The libskk project aims to provide GObject-based interface of Japanese
input methods.  Currently it supports SKK (Simple Kana Kanji) with
various typing rules including romaji-to-kana, AZIK, ACT, TUT-Code,
T-Code, and NICOLA.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:	Tools for %{name}
BuildRequires:	libfep-devel
BuildRequires: make
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	tools
The %{name}-tools package contains tools for developing applications
that use %{name}.


%prep
%autosetup -p1
find -name '*.vala' -exec touch {} \;

%build
%configure --disable-static --enable-fep
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}


%ldconfig_scriptlets


%files -f %{name}.lang
%doc README rules/README.rules COPYING
%{_libdir}/*.so.*
%{_datadir}/libskk
%{_libdir}/girepository-1.0/Skk*.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Skk*.gir
%{_datadir}/vala/vapi/*

%files tools
%{_bindir}/skk*
%{_libexecdir}/skk*
%{_mandir}/man1/skk*


%changelog
%autochangelog
