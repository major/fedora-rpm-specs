%global with_debug 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider github
%global provider_tld com
%global project opencontainers
%global repo runc
# https://github.com/opencontainers/runc
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path %{provider_prefix}
%global git0 https://github.com/opencontainers/runc

Name: %{repo}
Epoch: 2
Version: 1.1.12
Release: %autorelease
Summary: CLI for running Open Containers
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT
URL: %{git0}
Source0: %{git0}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{golang_arches_future}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: pkgconfig(libseccomp)
BuildRequires: go-md2man
BuildRequires: make
Provides: oci-runtime
# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/checkpoint_restore/go_criu/v5)) = v5.3.0
Provides: bundled(golang(github.com/cilium/ebpf)) = v0.7.0
Provides: bundled(golang(github.com/containerd/console)) = v1.0.3
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.3.2
Provides: bundled(golang(github.com/cpuguy83/go_md2man/v2)) = v2.0.0_20190314233015_f79a8a8ca69d
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.2.3
Provides: bundled(golang(github.com/docker/go_units)) = v0.4.0
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.0.6
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.5.0
Provides: bundled(golang(github.com/mrunalp/fileutils)) = v0.5.0
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20210326190908_1c3f411f0417
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.10.0
Provides: bundled(golang(github.com/russross/blackfriday/v2)) = v2.0.1
Provides: bundled(golang(github.com/seccomp/libseccomp_golang)) = v0.9.2_0.20220502022130_f33da4d89646
Provides: bundled(golang(github.com/shurcooL/sanitized_anchor_name)) = v1.0.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/urfave/cli)) = v1.22.1
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.1.0
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.0_20191106174202_0a2b9b5464df
Recommends: container-selinux >= 2:2.85-1

%ifnarch s390x
Recommends: criu
%endif

%description
The runc command can be used to start containers which are packaged
in accordance with the Open Container Initiative's specifications,
and to manage containers running under runc.

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i 's/ -trimpath//g' Makefile

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

mkdir -p GOPATH
pushd GOPATH
    mkdir -p src/%{provider}.%{provider_tld}/%{project}
    ln -s $(dirs +1 -l) src/%{import_path}
popd

pushd GOPATH/src/%{import_path}
export GOPATH=$(pwd)/GOPATH

make BUILDTAGS="seccomp selinux" all

sed -i '/\#\!\/bin\/bash/d' contrib/completions/bash/%{name}

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}

# generate man pages
man/md2man-all.sh

# install man pages
install -d -p %{buildroot}%{_mandir}/man8
install -p -m 0644 man/man8/*.8 %{buildroot}%{_mandir}/man8/.
# install bash completion
install -d -p %{buildroot}%{_datadir}/bash-completion/completions
install -p -m 0644 contrib/completions/bash/%{name} %{buildroot}%{_datadir}/bash-completion/completions

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc MAINTAINERS_GUIDE.md PRINCIPLES.md README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}*
%{_datadir}/bash-completion/completions/%{name}

%changelog
%autochangelog
