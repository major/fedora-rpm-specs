Name:           ncrack
Version:        0.7
Release:        %autorelease
Summary:        A high-speed network auth cracking tool

# Automatically converted from old format: GPLv2 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            http://nmap.org/ncrack/
Source0:        http://nmap.org/ncrack/dist/%{name}-%{version}.tar.gz
# Properly parse IPv6 services in the cli
Patch0:         https://github.com/nmap/ncrack/commit/bdcd5d6a0c9ed0b21de33d7bfe34c0f43ced8edd.patch
# Fix segfault in the ssh plugin
Patch1:         https://github.com/nmap/ncrack/commit/9232958b35a6f5118049f252814a26bbe21783d6.patch
# SSH module is not iterating on the credential list properly
Patch2:         https://github.com/nmap/ncrack/pull/99.patch
# Fedora C99 Fixes
Patch3:         ncrack-0.7-fedora-c99.patch
# Fix build with openssl4 - https://github.com/nmap/ncrack/issues/146
Patch4:         ncrack-0.7-fedora-openssl.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
Ncrack is a high-speed network authentication cracking tool. It was
built to help companies secure their networks by proactively testing
all their hosts and networking devices for poor passwords. Security
professionals also rely on Ncrack when auditing their clients. Ncrack
was designed using a modular approach, a command-line syntax similar to
Nmap and a dynamic engine that can adapt its behaviour based on network
feedback. It allows for rapid, yet reliable large-scale auditing of
multiple hosts.

%prep
%autosetup -p1

%build
autoreconf -ivf
export CFLAGS="%{build_cflags} -fcommon"
%configure
%make_build

%install
%make_install STRIP=true

%check
# Upstream does not provide a test suite

%files
%doc CHANGELOG README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/

%changelog
%autochangelog
