%global git0 https://github.com/containers/%{name}

%global built_tag_strip 1.9

%{!?_modulesloaddir:%global _modulesloaddir %{_usr}/lib/modules-load.d}

Name: fuse-overlayfs
Version: 1.9
%if "%{_vendor}" == "debbuild"
Packager: Podman Debbuild Maintainers <https://github.com/orgs/containers/teams/podman-debbuild-maintainers>
License: GPL-3.0+
Release: 0%{?dist}
%else
Release: %autorelease
License: GPLv3+
%endif
Summary: FUSE overlay+shiftfs implementation for rootless containers
URL: https://github.com/containers/%{name}
Source0: %{url}/archive/v%{built_tag_strip}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
Requires: fuse3
Requires: kmod
%if "%{_vendor}" == "debbuild"
BuildRequires: autoconf-archive
BuildRequires: git
BuildRequires: libfuse3-dev
BuildRequires: m4
BuildRequires: pkg-config
%else
BuildRequires: fuse3-devel
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: make
BuildRequires: systemd-rpm-macros
Provides: bundled(gnulib) = cb634d40c7b9bbf33fa5198d2e27fdab4c0bf143
%endif

%description
%{summary}.

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%autosetup -Sgit %{name}-%{built_tag_strip}

%build
./autogen.sh
./configure --prefix=%{_prefix} --libdir=%{_libdir}
%{__make}

%install
%make_install
install -d %{buildroot}%{_modulesloaddir}
echo fuse > %{buildroot}%{_modulesloaddir}/fuse-overlayfs.conf

%post
modprobe fuse > /dev/null 2>&1 || :

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_modulesloaddir}/fuse-overlayfs.conf

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
