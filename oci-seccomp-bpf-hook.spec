%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider github
%global provider_tld com
%global project containers
%global repo oci-seccomp-bpf-hook
# https://github.com/containers/oci-seccomp-bpf-hook
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}

%global built_tag v1.2.10
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

# use the same arch definitions as present in the bcc package
ExclusiveArch:  x86_64 %{power64} aarch64 s390x armv7hl

Name: %{repo}
Version: %{gen_version}
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and MIT
Release: %autorelease
ExclusiveArch: %{golang_arches_future}
Summary: OCI Hook to generate seccomp json files based on EBF syscalls used by container
URL: %{git0}
# Tarball fetched from upstream
Source0: %{url}/archive/%{built_tag}.tar.gz
BuildRequires: golang
BuildRequires: go-md2man
BuildRequires: go-rpm-macros
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: bcc-devel
BuildRequires: git
BuildRequires: gpgme-devel
BuildRequires: libseccomp-devel
BuildRequires: make
Requires: bcc
Enhances: podman
Enhances: cri-o
# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/iovisor/gobpf)) = v0.2.0
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20200728170252_4d89ac9fbff6
Provides: bundled(golang(github.com/seccomp/containers_golang)) = v0.6.0
Provides: bundled(golang(github.com/seccomp/libseccomp_golang)) = v0.9.1
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/stretchr/testify)) = v1.4.0

%description
%{summary}
%{name} provides a library for applications looking to use
the Container Pod concept popularized by Kubernetes.

%package tests
Summary: Tests for %{name}

Requires: %{name} = %{version}-%{release}
Requires: bats
Requires: podman

%description tests
%{summary}

This package contains system tests for %{name}

%prep
%autosetup -Sgit -n %{name}-%{built_tag_strip}
sed -i 's;HOOK_BIN_DIR;%{_libexecdir}/oci/hooks.d;' %{name}.json
sed -i '/$(HOOK_DIR)\/%{name}.json/d' Makefile

%build
%set_build_flags
export CGO_CFLAGS=$CFLAGS
# These extra flags present in $CFLAGS have been skipped for now as they break the build
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')

%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif

export GO111MODULE=off
export GOPATH=$(pwd):$(pwd)/_build

mkdir _build
cd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path}
cd ..
ln -s vendor src

export GOPATH=$(pwd)/_build:$(pwd)
export LDFLAGS="-X main.version=%{version}"
%gobuild -o bin/%{name} %{import_path}

cd docs
go-md2man -in %{name}.md -out %{name}.1
cd ..

%install
%{__make} DESTDIR=%{buildroot} PREFIX=%{_prefix} install-nobuild
%{__make} DESTDIR=%{buildroot} PREFIX=%{_prefix} GOMD2MAN=go-md2man -C docs install-nobuild

install -d -p %{buildroot}/%{_datadir}/%{name}/test/system
cp -pav test/. %{buildroot}/%{_datadir}/%{name}/test/system

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
# Since we aren't packaging up the vendor directory we need to link
# back to it somehow. Hack it up so that we can add the vendor
# directory from BUILD dir as a gopath to be searched when executing
# tests from the BUILDROOT dir.
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor

export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/src/%{name}
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%dir %{_libexecdir}/oci/hooks.d
%{_libexecdir}/oci/hooks.d/%{name}
%{_datadir}/containers/oci/hooks.d/%{name}.json
%{_mandir}/man1/%{name}.1*

%files tests
%license LICENSE
%{_datadir}/%{name}/test

%changelog
%autochangelog
