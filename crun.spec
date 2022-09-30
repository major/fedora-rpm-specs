%global krun_opts %{nil}

%if 0%{?fedora} >= 37
%ifarch aarch64 || x86_64
%global krun_support enabled
%global krun_opts --with-libkrun
%endif
%endif

%global built_tag_strip 1.6

Summary: OCI runtime written in C
Name: crun
Version: 1.6
URL: https://github.com/containers/%{name}
Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
%if "%{_vendor}" == "debbuild"
Packager: Podman Debbuild Maintainers <https://github.com/orgs/containers/teams/podman-debbuild-maintainers>
License: GPL-2.0+
Release: 0%{?dist}
%else
License: GPLv2+
Release: %autorelease
%endif
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: go-md2man
BuildRequires: libtool
%if "%{_vendor}" == "debbuild"
BuildRequires: git
BuildRequires: libcap-dev
BuildRequires: libseccomp-dev
BuildRequires: libsystemd-dev
BuildRequires: libyajl-dev
BuildRequires: pkg-config
Requires: criu
%else
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: python3
BuildRequires: libcap-devel
BuildRequires: systemd-devel
BuildRequires: yajl-devel
%if "%{krun_support}" == "enabled"
BuildRequires: libkrun-devel
%endif
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: python3-libmount
BuildRequires: make
BuildRequires: glibc-static
BuildRequires: protobuf-c-devel
%ifnarch %ix86
BuildRequires: criu-devel >= 3.17.1-2
%endif
Requires: criu >= 3.17.1
%endif
Provides: oci-runtime

%description
%{name} is a runtime for running OCI containers

%prep
%autosetup -Sgit %{name}-%{built_tag_strip}

%build
./autogen.sh
%configure --disable-silent-rules %{krun_opts}
%make_build

%install
%make_install
rm -rf %{buildroot}%{_prefix}/lib*
%if "%{krun_support}" == "enabled"
ln -s ../bin/%{name} %{buildroot}%{_bindir}/krun
%endif

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/*

%if "%{krun_support}" == "enabled"
%package krun
Summary: OCI Runtime providing Virtualization-based process isolation capabilities.
Provides: krun
Requires: libkrun

%description krun
%{name}-krun OCI Runtime providing Virtualization-based process isolation capabilities.

%files krun
%{_bindir}/krun

%endif

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
