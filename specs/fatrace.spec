Name:		fatrace
Version:	0.18.0
Release:	%autorelease
Summary:	Reports file access events from all running processes

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/martinpitt/fatrace
Source0:        https://github.com/martinpitt/fatrace/archive/refs/tags/%{version}.tar.gz
Patch:          fatrace-0.18.0-sbin-to-bin.patch
BuildRequires:  gcc
BuildRequires: make

%description
fatrace reports file access events from all running processes.

Its main purpose is to find processes which keep waking up the disk
unnecessarily and thus prevent some power saving.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
export PREFIX=%{_prefix}
make install DESTDIR=%{buildroot}

%files
%doc COPYING NEWS
%{_bindir}/fatrace
%{_bindir}/power-usage-report
%{_mandir}/man*/*

%changelog
%autochangelog
