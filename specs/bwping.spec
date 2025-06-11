%global forgeurl https://github.com/oleg-derevenetz/bwping
%global tag      RELEASE_2.6

Name:           bwping
Version:        2.6
Release:        %autorelease

Summary:        Measure bandwidth and response times using ICMP
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://bwping.sourceforge.net/

%forgemeta
Source0:        %{forgesource}

# bwping needs to be run with sudo, then these tests will fail
Patch0:         0001-remove-failing-tests.patch

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  autoconf

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
BWPing is a tool to measure bandwidth and response
times between two hosts using Internet Control Message
Protocol (ICMP) echo request/echo reply mechanism.
It does not require any special software on the remote host.
The only requirement is the ability to respond on ICMP echo
request messages.

%prep
%forgeautosetup

%build
autoreconf -i
%configure
%make_build

%install
%make_install

%check
make check

%files
%doc AUTHORS README
%license COPYING 
%{_sbindir}/bwping*
%{_mandir}/man8/bwping*

%changelog
%autochangelog
