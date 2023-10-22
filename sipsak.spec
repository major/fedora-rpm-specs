Summary:	SIP swiss army knife
Name:		sipsak
Version:	0.9.8.1
Release:	%autorelease
License:	GPL-2.0-or-later
URL:		https://github.com/nils-ohlmeier/sipsak
VCS:            scm:git:https://github.com/nils-ohlmeier/sipsak.git
Source0:	https://github.com/nils-ohlmeier/sipsak/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	c-ares-devel
BuildRequires:	gcc
#BuildRequires:	gnutls-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	openssl-devel

%description
sipsak is a small command line tool for developers and
administrators of Session Initiation Protocol (SIP) applications.
It can be used for some simple tests on SIP applications and
devices.

%prep
%autosetup -p1

%build
autoreconf -ivf
%configure --disable-gnutls
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
