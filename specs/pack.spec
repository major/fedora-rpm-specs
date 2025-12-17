%global with_debug 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global gomodulesmode GO111MODULE=on

%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}

Name: pack
Version: 0.39.1
Release: %autorelease
Summary: Convert code into runnable images
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and MIT
URL: https://github.com/buildpacks/%{name}
## On the upstream repo, run:
# git checkout v%%{version} && go mod vendor && git add vendor/* && \
# git commit -asm 'add vendor' && \
# git archive --prefix=%%{name}-%%{version}/ -o v%%{version}-vendor.tar.gz HEAD
Source0: v%{version}-vendor.tar.gz
BuildRequires: golang
BuildRequires: go-rpm-macros
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: glibc-static
BuildRequires: make
Provides: %{name}cli = %{version}-%{release}
Provides: %{name}-cli = %{version}-%{release}

%description
%{name} is a CLI implementation of the Platform Interface Specification
for Cloud Native Buildpacks.

%prep
%autosetup -Sgit -n %{name}-%{version}

%build
%set_build_flags
export CGO_CFLAGS=$CFLAGS
# These extra flags present in $CFLAGS have been skipped for now as they break the build
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')
export LDFLAGS=''

%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif

%if 0%{?rhel} <= 8
# handled automatically in %%gobuild for fedora and epel9
export GO111MODULE=off
%endif

%gobuild -o out/%{name} .

%install
export GOPATH=$(pwd)/_build:$(pwd)
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
