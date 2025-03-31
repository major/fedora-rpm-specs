Name:           fpart
Version:        1.7.0
Release:        %autorelease
Summary:        Helps you sort file trees and pack them into bags
# main source is BSD-2-Clause
# src/fts.c and src/fts.h are BSD-3-Clause
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://fpart.org
Source:         https://github.com/martymac/fpart/archive/fpart-%{version}.tar.gz

BuildRequires:  gcc autoconf automake
BuildRequires:  make

%description
Fpart is a Filesystem partitioner.  It helps you sort file trees and pack them
into bags (called "partitions").  It is developed in C and available under the
BSD license.


%prep
%autosetup -n fpart-fpart-%{version}


%build
autoreconf --install
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc docs/www.fpart.org/docs/changelog.md README.md
%{_mandir}/man1/fpart.1*
%{_mandir}/man1/fpsync.1*
%{_bindir}/fpart
%{_bindir}/fpsync


%changelog
%autochangelog
