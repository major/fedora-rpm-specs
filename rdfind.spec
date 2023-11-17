Name:		rdfind
Version:	1.6.0
Release:	%autorelease
Summary:	Program that finds duplicate files

License:	GPL-2.0-or-later
URL:		https://rdfind.pauldreik.se/
Source0:	%{url}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	nettle-devel

%description
Rdfind is a program that finds duplicate files. It is useful for compressing
backup directories or just finding duplicate files. It compares files based on
their content, NOT on their file names.


%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install


%check
make check


%files
%doc AUTHORS ChangeLog
%license COPYING LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
