Name:		uncrustify
Version:	0.76.0
Release:	%autorelease
Summary:	Reformat Source

License:	GPLv2
URL:		https://uncrustify.sourceforge.net/
Source0:	https://prdownloads.sourceforge.net/uncrustify/uncrustify-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Source Code Beautifier for C, C++, C#, D, Java, and Pawn

%prep
%autosetup

%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc NEWS
%doc documentation
%{_bindir}/uncrustify
%{_datadir}/doc/uncrustify/*
%{_mandir}/man1/uncrustify.1*


%autochangelog
