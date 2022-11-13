%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global built_tag v2.1.5
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: conmon
Epoch: 2
Version: %{gen_version}
License: ASL 2.0
Release: %autorelease
Summary: OCI container runtime monitor
URL: https://github.com/containers/%{name}
# Tarball fetched from upstream
Source0: %{url}/archive/%{built_tag}.tar.gz
BuildRequires: go-md2man
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
%autochangelog
