%if "%{_vendor}" == "debbuild"
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -tags=" ${BUILDTAGS:-}" -a -v -x %{?**};
%endif

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
%global repo buildah
# https://github.com/containers/buildah
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}

%global built_tag_strip 1.27.1

Name: %{repo}
Version: 1.27.1
%if "%{_vendor}" == "debbuild"
Packager: Podman Debbuild Maintainers <https://github.com/orgs/containers/teams/podman-debbuild-maintainers>
License: ASL-2.0+
Release: 0%{?dist}
%else
License: ASL 2.0 and BSD and MIT and MPLv2.0
Release: %autorelease
%endif
Summary: A command line tool used for creating OCI Images
URL: https://%{name}.io
Source: %{git0}/archive/v%{built_tag_strip}.tar.gz
BuildRequires: go-md2man
%if "%{_vendor}" == "debbuild"
BuildRequires: git
BuildRequires: golang
BuildRequires: libassuan-dev
BuildRequires: libbtrfs-dev
BuildRequires: libdevmapper-dev
BuildRequires: libglib2.0-dev
BuildRequires: libgpg-error-dev
BuildRequires: libgpgme-dev
BuildRequires: libseccomp-dev
BuildRequires: libsystemd-dev
BuildRequires: pkg-config
Requires: containers-common >= 4:1
%else
BuildRequires: device-mapper-devel
BuildRequires: git-core
BuildRequires: golang >= 1.16.6
BuildRequires: glib2-devel
BuildRequires: glibc-static
BuildRequires: go-rpm-macros
BuildRequires: gpgme-devel
BuildRequires: libassuan-devel
BuildRequires: make
BuildRequires: ostree-devel
BuildRequires: btrfs-progs-devel
BuildRequires: shadow-utils-subid-devel
Requires: containers-common >= 4:1-46
Suggests: containernetworking-plugins >= 0.9.1-1
Requires: netavark
Requires: iptables
Requires: nftables
BuildRequires: libseccomp-static
Requires: libseccomp >= 2.4.1-0
Suggests: cpp
Suggests: qemu-user-static
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/containerd/containerd)) = v1.5.9
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.0.1
Provides: bundled(golang(github.com/containers/common)) = v0.47.4
Provides: bundled(golang(github.com/containers/image/v5)) = v5.19.1
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.2
Provides: bundled(golang(github.com/containers/storage)) = v1.38.2
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.0+incompatible
Provides: bundled(golang(github.com/docker/docker)) = v20.10.12+incompatible
Provides: bundled(golang(github.com/docker/go_units)) = v0.4.0
Provides: bundled(golang(github.com/docker/libnetwork)) = v0.8.0_dev.2.0.20190625141545_5a177b73e316
Provides: bundled(golang(github.com/fsouza/go_dockerclient)) = v1.7.8
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/ishidawataru/sctp)) = v0.0.0_20210226210310_f2269e66cdee
Provides: bundled(golang(github.com/konsorten/go_windows_terminal_sequences)) = v1.0.3
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/onsi/ginkgo)) = v1.16.5
Provides: bundled(golang(github.com/onsi/gomega)) = v1.18.1
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.0.3_0.20211202193544_a5463b7f9c84
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.1.0
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20210326190908_1c3f411f0417
Provides: bundled(golang(github.com/opencontainers/runtime_tools)) = v0.9.0
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.10.0
Provides: bundled(golang(github.com/openshift/imagebuilder)) = v1.2.2
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/seccomp/libseccomp_golang)) = v0.9.2_0.20210429002308_3879420cc921
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/spf13/cobra)) = v1.3.0
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stretchr/testify)) = v1.7.0
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
%endif

%description
The %{name} package provides a command line tool which can be used to
* create a working container from scratch
or
* create a working container from an image as a starting point
* mount/umount a working container's root file system for manipulation
* save container's root file system layer to create a new image
* delete a working container or an image

%package tests
Summary: Tests for %{name}

Requires: %{name} = %{version}-%{release}
Requires: bats
Requires: bzip2
Requires: podman
Requires: golang
Requires: jq
Requires: httpd-tools
Requires: openssl
Requires: nmap-ncat
Requires: git-daemon

%description tests
%{summary}

This package contains system tests for %{name}

%prep
%autosetup -Sgit

%build
%if "%{_vendor}" != "debbuild"
%set_build_flags
# These extra flags present in $CFLAGS have been skipped for now as they break the build
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')

%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif
%endif

export GOPATH=$(pwd)/_build:$(pwd)
export CGO_CFLAGS=$CFLAGS

mkdir _build
cd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path}
cd ..

mv vendor src

export CNI_VERSION=`grep '^# github.com/containernetworking/cni ' src/modules.txt | sed 's,.* ,,'`
export LDFLAGS="-X main.buildInfo=`date +%s` -X main.cniVersion=${CNI_VERSION}"

export BUILDTAGS='seccomp exclude_graphdriver_devicemapper'
%if "%{_vendor}" != "debbuild"
export BUILDTAGS+=' libsubid selinux'
%endif
%gobuild -o bin/%{name} %{import_path}/cmd/%{name}
%gobuild -o bin/imgtype %{import_path}/tests/imgtype
%gobuild -o bin/copy %{import_path}/tests/copy
%gobuild -o bin/tutorial %{import_path}/tests/tutorial
GOMD2MAN=go-md2man %{__make} -C docs

%install
export GOPATH=$(pwd)/_build:$(pwd)
%if "%{_vendor}" != "debbuild"
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install install.completions
make DESTDIR=%{buildroot} PREFIX=%{_prefix} -C docs install
%else
install -D -m0755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -m 644 -D contrib/completions/bash/%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -d %{buildroot}/%{_mandir}/man1
install -m 0644 docs/%{name}*.1 %{buildroot}%{_mandir}/man1
install -m 0644 docs/links/%{name}*.1 %{buildroot}%{_mandir}/man1
%endif

install -d -p %{buildroot}/%{_datadir}/%{name}/test/system
cp -pav tests/. %{buildroot}/%{_datadir}/%{name}/test/system
cp bin/imgtype %{buildroot}/%{_bindir}/%{name}-imgtype
cp bin/copy    %{buildroot}/%{_bindir}/%{name}-copy
cp bin/tutorial %{buildroot}/%{_bindir}/%{name}-tutorial

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%files tests
%license LICENSE
%{_bindir}/%{name}-imgtype
%{_bindir}/%{name}-copy
%{_bindir}/%{name}-tutorial
%{_datadir}/%{name}/test

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
