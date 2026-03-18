Name:     btrfs-dump
Version:  20260216
Release:  %autorelease
Summary:  Btrfs metadata dumper
License:  MIT AND BSD-2-Clause
URL:      https://github.com/maharmstone/btrfs-dump
Source:   %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Provides bundled base64 functionality from src/b64.cpp
Provides: bundled(base64)

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconfig(blkid)

%description
Prints btrfs metadata in a text format.

%prep
%autosetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%check
%{_vpath_builddir}/btrfs-dump --version

%files
%license LICENCE
%doc README.md
%{_bindir}/btrfs-dump

%changelog
%autochangelog
