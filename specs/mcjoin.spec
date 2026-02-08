Name:           mcjoin
Version:        2.12
Release:        1%{?dist}
Summary:        Tiny multicast testing tool
# The project is shipped under ISC and most sources have this license.
# pev.c and pev.h are under Unlicensed https://github.com/troglobit/pev
# only queue.h has BSD-3-Clause.
License:        ISC AND BSD-3-Clause AND Unlicense
URL:            https://github.com/troglobit/mcjoin
Source0:        https://github.com/troglobit/mcjoin/releases/download/v%{version}/%{name}-%{version}.tar.gz

Patch0: configure.patch

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  git-core

%description
Mcjoin is a simple and easy-to-use tool for IPv4 and IPv6 multicast testing.
It can be run both as a multicast generator(server) and a sink(client).
Supports join/send messages to on or more groups and supports both
ASM(*,G) and SSM(S,G) multicasts.

%prep
%autosetup -S git

%build
autoreconf -ivf
%configure
%make_build

%install
%make_install
# remove the LICENSE file from docs and keep it in licenses
rm -f %{buildroot}/%{_datadir}/doc/mcjoin/LICENSE

%check
make check

%files
%doc README.md mcjoin-recv.jpg mcjoin-send.jpg
%license LICENSE
%{_mandir}/man1/mcjoin.1*
%{_bindir}/%{name}

%changelog
* Fri Jan 30 2026 Michal Ruprich <mruprich@redhat.com> - 2.12-1
- Initial commit
