%global with_debug 1
%global with_check 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global built_tag_strip 2.1.4

Name: conmon
Epoch: 2
Version: 2.1.4
%if "%{_vendor}" == "debbuild"
Packager: Podman Debbuild Maintainers <https://github.com/orgs/containers/teams/podman-debbuild-maintainers>
License: ASL-2.0+
Release: 0%{?dist}
%else
License: ASL 2.0
Release: %autorelease
%endif
Summary: OCI container runtime monitor
URL: https://github.com/containers/%{name}
Source0: %{url}/archive/v%{built_tag_strip}.tar.gz
BuildRequires: go-md2man
%if "%{_vendor}" == "debbuild"
BuildRequires: git
BuildRequires: libglib2.0-dev
BuildRequires: libseccomp-dev
BuildRequires: libsystemd-dev
Requires: libglib2.0-0
Requires: libseccomp2
%else
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: glib2-devel
BuildRequires: libseccomp-devel
BuildRequires: systemd-devel
BuildRequires: systemd-libs
BuildRequires: make
Requires: glib2
Requires: systemd-libs
Requires: libseccomp
%endif

%description
%{summary}.

%prep
%autosetup -Sgit %{name}-%{built_tag_strip}
sed -i 's/install.bin: bin\/conmon/install.bin:/' Makefile
sed -i 's/install.crio: bin\/conmon/install.crio:/' Makefile

%build
%{__make} DEBUGFLAG="-g" bin/conmon
%{__make} GOMD2MAN=go-md2man -C docs

%install
%{__make} PREFIX=%{buildroot}%{_prefix} install.bin install.crio
%{__make} PREFIX=%{buildroot}%{_prefix} -C docs install

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/crio/%{name}
%dir %{_libexecdir}/crio
%{_mandir}/man8/%{name}.8.gz

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
