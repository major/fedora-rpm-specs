Name:           rabbitsign
Version:        2.1
Release:        %autorelease
Summary:        Digitally sign software for Texas Instruments calculators

# src/md5.c is GPLv2+, the rest is GPLv3+
License:        GPL-3.0-or-later AND GPL-2.0-or-later
URL:            https://www.ticalc.org/archives/files/fileinfo/383/38392.html
Source0:        https://www.ticalc.org/pub/unix/%{name}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gmp-devel

%description
RabbitSign is a free implementation of the algorithms used to digitally sign
software for the Texas Instruments TI-73, TI-83 Plus, TI-84 Plus, TI-89, TI-92
Plus, and Voyage 200 calculators.

RabbitSign can handle a variety of common input file formats, including
GraphLink files as well as "plain" hex and binary files. It is quite a lot
faster than the official application signing programs from TI, and unlike
those programs, does not have any arbitrary limitations on file names or
contents.  It also has the ability to re-sign applications that have been
signed previously.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%check
make check

%files
%license COPYING
%doc README
%{_bindir}/packxxk
%{_bindir}/rabbitsign
%{_bindir}/rskeygen
%{_mandir}/man1/packxxk.1*
%{_mandir}/man1/rabbitsign.1*
%{_mandir}/man1/rskeygen.1*

%changelog
%autochangelog
