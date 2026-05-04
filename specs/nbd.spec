Name:           nbd
Version:        3.27.1
Release:        %autorelease
Summary:        Network Block Device user-space tools (TCP version)
# SPDX migration
License:        GPL-2.0-only
URL:            https://github.com/NetworkBlockDevice/nbd
Source0:        https://github.com/NetworkBlockDevice/nbd/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        nbd-server.service
Source2:        nbd-server.sysconfig
# Backport parsing fixes from main branch
Patch1:         89ba7b5379548d6ebbfa36db15f2b8e3787a09ea.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  glib2-devel >= 2.26
BuildRequires:  gnutls-devel
BuildRequires:  zlib-devel
BuildRequires:  libnl3-devel
BuildRequires:  bison
BuildRequires:  docbook-utils
BuildRequires:  systemd
# We need to run autogen.sh now
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  flex
%{?systemd_requires}

Excludearch: %{ix86}

%description
Tools for the Linux Kernel's network block device, allowing you to use
remote block devices over a TCP/IP network.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}
# tarball doesn't include git history, force the version it returns
# from the release tag
echo "echo %{version}" > support/genver.sh

# wait longer for nbd-server to fully start,
# five seconds may not be enough on Fedora building infra
sed -i 's/tv_sec = 5/tv_sec = 30/' tests/run/nbd-tester-client.c

%build
./autogen.sh
%configure --enable-syslog --enable-lfs --enable-manpages
%make_build

%install
%make_install
install -pDm644 systemd/nbd@.service %{buildroot}%{_unitdir}/nbd@.service
mkdir -p %{buildroot}%{_unitdir}/nbd@.service.d
cat > %{buildroot}%{_unitdir}/nbd@.service.d/modprobe.conf <<EOF
[Service]
ExecStartPre=/sbin/modprobe nbd
EOF
install -pDm644 %{S:1} %{buildroot}%{_unitdir}/nbd-server.service
install -pDm644 %{S:2} %{buildroot}%{_sysconfdir}/sysconfig/nbd-server

%check
# wait longer for nbd-server to fully start,
# one second may not be enough on Fedora building infra
DELAY=10 make check

%post
%systemd_post nbd-server.service

%preun
%systemd_preun nbd-server.service

%postun
%systemd_postun nbd-server.service

%files
%doc README.md doc/*.md doc/todo.txt
%license COPYING
%{_bindir}/nbd-server
%{_bindir}/nbd-trdump
%{_bindir}/nbd-trplay
%{_mandir}/man*/nbd*
%{_sbindir}/nbd-client
%{_sbindir}/min-nbd-client
%config(noreplace) %{_sysconfdir}/sysconfig/nbd-server
%{_unitdir}/nbd-server.service
%{_unitdir}/nbd@.service
%{_unitdir}/nbd@.service.d

%changelog
%autochangelog
