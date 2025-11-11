%global debug_package %{nil}

Summary:	A filemanager similar to XTree
Name:		ytree
Version:	2.10
Release:	%autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://www.han.de/~werner/ytree.html
Source0:	https://www.han.de/~werner/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	ncurses-devel >= 5.4
BuildRequires:	readline-devel >= 4.3 

%description
A console based file manager in the tradition of Xtree.

%prep
%autosetup

%build
%make_build

%install
install -m644 -D -p ytree.1 $RPM_BUILD_ROOT/%{_mandir}/man1/ytree.1
install -m755 -D -p ytree $RPM_BUILD_ROOT/%{_bindir}/ytree

%files 
%doc CHANGES COPYING README THANKS ytree.conf
%doc %{_mandir}/man1/ytree.1.gz
%{_bindir}/ytree

%changelog
%autochangelog
