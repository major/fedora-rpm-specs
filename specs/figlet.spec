Name:       figlet
Summary:    A program for making large letters out of ordinary text
Version:    2.2.5
Release:    %autorelease
License:    BSD-3-Clause and MIT and ISC and WTFPL
URL:        http://www.figlet.org/

# Source repository at https://github.com/cmatsuoka/figlet
Source0:    https://github.com/cmatsuoka/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
FIGlet prints its input using large characters (called "FIGcharacters") made
up of ordinary screen characters (called "sub-characters"). FIGlet output is
generally reminiscent of the sort of "signatures" many people like to put at
the end of e-mail and UseNet messages. It is also reminiscent of the output of
some banner programs, although it is oriented normally, not sideways.

%prep
%autosetup

sed -i \
    -e 's|usr/local|usr|g' \
    -e 's|$(prefix)/man|$(prefix)/share/man|g' \
    Makefile

%build
%make_build

%check
make check

%install
%make_install

%files
%license LICENSE
%doc CHANGES README FAQ
%{_mandir}/man6/*
%{_bindir}/*
%{_datadir}/%{name}/

%changelog
%autochangelog
