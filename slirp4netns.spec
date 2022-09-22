%global built_tag_strip 1.2.0

Name: slirp4netns
Version: 1.2.0
%if "%{_vendor}" == "debbuild"
Packager: Podman Debbuild Maintainers <https://github.com/orgs/containers/teams/podman-debbuild-maintainers>
License: GPL-2.0+
Release: 0%{?dist}
%else
Release: %autorelease
License: GPLv2
%endif
Summary: slirp for network namespaces
URL: https://github.com/rootless-containers/%{name}
Source0: %{url}/archive/v%{built_tag_strip}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: go-md2man
%if "%{_vendor}" == "debbuild"
BuildRequires: git
BuildRequires: libglib2.0-dev
BuildRequires: libcap-dev
BuildRequires: libseccomp-dev
BuildRequires: libslirp-dev
%else
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: git-core
BuildRequires: libcap-devel
BuildRequires: libseccomp-devel
BuildRequires: libslirp-devel
BuildRequires: make
%endif

%description
slirp for network namespaces, without copying buffers across the namespaces.

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
./configure --prefix=%{_usr} --libdir=%{_libdir}
%{__make} generate-man

%install
make DESTDIR=%{buildroot} install install-man

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
