Summary:	A file manager similar to XTree
Name:		ytree
Version:	2.13
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
install -D -p -m 0755 ytree %{buildroot}%{_bindir}/ytree
install -D -p -m 0644 ytree.1 %{buildroot}%{_mandir}/man1/ytree.1

%files
%license COPYING
%doc CHANGES README THANKS ytree.conf
%{_bindir}/ytree
%{_mandir}/man1/ytree.1*

%check
%{buildroot}%{_bindir}/ytree -v 2>&1 | grep -q Usage

%changelog
%autochangelog
