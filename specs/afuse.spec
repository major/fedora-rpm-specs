Name:		afuse
Summary:	An automounter implemented with FUSE
Version:	0.5.0
Release:	%autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Source0:	https://github.com/pcarrier/afuse/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		afuse-0.5.0-strcpy-buffer-overflow-fix.patch
URL:		https://github.com/pcarrier/afuse/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fuse-devel
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	pkgconfig

%description
Afuse is an automounting file system implemented in user-space using FUSE.
Afuse currently implements the most basic functionality that can be expected
by an automounter; that is it manages a directory of virtual directories. If
one of these virtual directories is accessed and is not already automounted,
afuse will attempt to mount a filesystem onto that directory. If the mount
succeeds the requested access proceeds as normal, otherwise it will fail
with an error.

%prep
%autosetup -p1

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install

%check
# No upstream tests exist

%files
%license COPYING COPYING.LIB
%doc AUTHORS README
%{_bindir}/afuse
%{_bindir}/afuse-avahissh

%changelog
%autochangelog
