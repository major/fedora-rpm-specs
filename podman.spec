%if "%{_vendor}" == "debbuild"
%global _unitdir %{_usr}/lib/systemd/system
%global _userunitdir %{_usr}/lib/systemd/user
%global _tmpfilesdir %{_usr}/lib/tmpfiles.d
# Older distros don't work yet
%if (0%{?debian} && 0%{?debian} <= 11) || (0%{?ubuntu} && 0%{?ubuntu} < 2204)
%define gobuild(o:) GO111MODULE=off %{_prefix}/lib/go-1.16/bin/go build -buildmode pie -tags=" ${BUILDTAGS:-}" -a -v -x %{?**};
%else
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -tags=" ${BUILDTAGS:-}" -a -v -x %{?**};
%endif
%endif

%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global provider github
%global provider_tld com
%global project containers
%global repo %{name}
# https://github.com/containers/%%{name}
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}

# dnsname
%global repo_plugins dnsname
# https://github.com/containers/dnsname
%global import_path_plugins %{provider}.%{provider_tld}/%{project}/%{repo_plugins}
%global git_plugins https://%{import_path_plugins}
%global commit_plugins 18822f9a4fb35d1349eb256f4cd2bfd372474d84

# gvproxy
%global repo_gvproxy gvisor-tap-vsock
# https://github.com/containers/gvisor-tap-vsock
%global import_path_gvproxy %%{provider}.%{provider_tld}/%{project}/%{repo_gvproxy}
%global git_gvproxy https://%{import_path_gvproxy}
%global commit_gvproxy fdc231ae7b8fe1aec4cf0b8777274fa21b70d789

%global built_tag_strip 4.3.0-rc1

Name: podman
Epoch: 4
Version: 4.3.0~rc1
%if "%{_vendor}" == "debbuild"
Packager: Podman Debbuild Maintainers <https://github.com/orgs/containers/teams/podman-debbuild-maintainers>
License: ASL-2.0+ and BSD and ISC and MIT and MPLv2.0
Release: 0%{?dist}
%else
License: ASL 2.0 and BSD and ISC and MIT and MPLv2.0
Release: %autorelease
ExclusiveArch: %{golang_arches}
%endif
Summary: Manage Pods, Containers and Container Images
URL: https://%{name}.io/
Source0: %{git0}/archive/v%{built_tag_strip}.tar.gz
Source1: %{git_plugins}/archive/%{commit_plugins}/%{repo_plugins}-%{commit_plugins}.tar.gz
Source2: %{git_gvproxy}/archive/%{commit_gvproxy}/%{repo_gvproxy}-%{commit_gvproxy}.tar.gz
Provides: %{name}-manpages = %{epoch}:%{version}-%{release}
BuildRequires: go-md2man
Requires: catatonit
Requires: iptables
Requires: nftables
%if "%{_vendor}" == "debbuild"
BuildRequires: git
BuildRequires: libassuan-dev
BuildRequires: libglib2.0-dev
BuildRequires: libgpg-error-dev
BuildRequires: libgpgme-dev
BuildRequires: libseccomp-dev
BuildRequires: libsystemd-dev
BuildRequires: pkg-config
%if (0%{?debian} && 0%{?debian} <= 11) || (0%{?ubuntu} && 0%{?ubuntu} < 2204)
BuildRequires: golang-1.16
BuildRequires: libc6 < 2.32
%else
BuildRequires: golang
BuildRequires: libc6
%endif
Requires: conmon >= 2:2.0.30
Requires: containers-common >= 4:1
Requires: uidmap
%else
%if ! 0%{?centos}
BuildRequires: btrfs-progs-devel
%endif
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: golang
BuildRequires: git-core
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: go-rpm-macros
%endif
BuildRequires: gpgme-devel
BuildRequires: libassuan-devel
BuildRequires: libgpg-error-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: shadow-utils-subid-devel
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: ostree-devel
BuildRequires: systemd
BuildRequires: systemd-devel
Requires: conmon >= 2:2.0.30-2
Requires: containers-common >= 4:1-46
Requires: netavark >= 1.0.3-1
Recommends: %{name}-gvproxy = %{epoch}:%{version}-%{release}
Suggests: containernetworking-plugins >= 0.9.1-1
Suggests: qemu-user-static
# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.1.0
Provides: bundled(golang(github.com/blang/semver/v4)) = v4.0.0
Provides: bundled(golang(github.com/buger/goterm)) = v1.0.4
Provides: bundled(golang(github.com/checkpoint_restore/checkpointctl)) = v0.0.0_20220321135231_33f4a66335f0
Provides: bundled(golang(github.com/checkpoint_restore/go_criu/v5)) = v5.3.0
Provides: bundled(golang(github.com/container_orchestrated_devices/container_device_interface)) = v0.4.0
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.1.1
Provides: bundled(golang(github.com/containernetworking/plugins)) = v1.1.1
Provides: bundled(golang(github.com/containers/buildah)) = v1.26.1_0.20220716095526_d31d27c357ab
Provides: bundled(golang(github.com/containers/common)) = v0.48.1_0.20220718075257_ecddf87b3840
Provides: bundled(golang(github.com/containers/conmon)) = v2.0.20+incompatible
Provides: bundled(golang(github.com/containers/image/v5)) = v5.21.2_0.20220721072459_bf19265865b7
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.5
Provides: bundled(golang(github.com/containers/psgo)) = v1.7.2
Provides: bundled(golang(github.com/containers/storage)) = v1.41.1_0.20220714115232_fc9b0ff5272a
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.3.2
Provides: bundled(golang(github.com/coreos/stream_metadata_go)) = v0.0.0_20210225230131_70edb9eb47b3
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.2.3
Provides: bundled(golang(github.com/digitalocean/go_qemu)) = v0.0.0_20210326154740_ac9e0b687001
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.1+incompatible
Provides: bundled(golang(github.com/docker/docker)) = v20.10.17+incompatible
Provides: bundled(golang(github.com/docker/go_connections)) = v0.4.1_0.20210727194412_58542c764a11
Provides: bundled(golang(github.com/docker/go_plugins_helpers)) = v0.0.0_20211224144127_6eecb7beb651
Provides: bundled(golang(github.com/docker/go_units)) = v0.4.0
Provides: bundled(golang(github.com/dtylman/scp)) = v0.0.0_20181017070807_f3000a34aef4
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = v1.5.4
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.1.0
Provides: bundled(golang(github.com/google/gofuzz)) = v1.2.0
Provides: bundled(golang(github.com/google/shlex)) = v0.0.0_20191202100458_e7afc7fbc510
Provides: bundled(golang(github.com/google/uuid)) = v1.3.0
Provides: bundled(golang(github.com/gorilla/handlers)) = v1.5.1
Provides: bundled(golang(github.com/gorilla/mux)) = v1.8.0
Provides: bundled(golang(github.com/gorilla/schema)) = v1.2.0
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/json_iterator/go)) = v1.1.12
Provides: bundled(golang(github.com/mattn/go_isatty)) = v0.0.14
Provides: bundled(golang(github.com/moby/term)) = v0.0.0_20210619224110_3f7ff695adc6
Provides: bundled(golang(github.com/nxadm/tail)) = v1.4.8
Provides: bundled(golang(github.com/onsi/ginkgo)) = v1.16.5
Provides: bundled(golang(github.com/onsi/gomega)) = v1.19.0
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.0.3_0.20220114050600_8b9d41f48198
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.1.3
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20211214071223_8958f93039ab
Provides: bundled(golang(github.com/opencontainers/runtime_tools)) = v0.9.1_0.20220714195903_17b3287fafb7
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.10.1
Provides: bundled(golang(github.com/rootless_containers/rootlesskit)) = v1.0.1
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.0
Provides: bundled(golang(github.com/spf13/cobra)) = v1.5.0
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stretchr/testify)) = v1.8.0
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/uber/jaeger_client_go)) = v2.30.0+incompatible
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.10
Provides: bundled(golang(github.com/vbauerster/mpb/v7)) = v7.4.2
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.1.1_0.20220115184804_dd687eb2f2d4
%endif

%description
%{name} (Pod Manager) is a fully featured container engine that is a simple
daemonless tool.  %{name} provides a Docker-CLI comparable command line that
eases the transition from other container engines and allows the management of
pods, containers and images.  Simply put: alias docker=%{name}.
Most %{name} commands can be run as a regular user, without requiring
additional privileges.

%{name} uses Buildah(1) internally to create container images.
Both tools share image (not container) storage, hence each can use or
manipulate images (but not containers) created by the other.

%{summary}
%{repo} Simple management tool for pods, containers and images

%package docker
Summary: Emulate Docker CLI using %{name}
BuildArch: noarch
Requires: %{name} = %{epoch}:%{version}-%{release}
Conflicts: docker
Conflicts: docker-latest
Conflicts: docker-ce
Conflicts: docker-ee
Conflicts: moby-engine

%description docker
This package installs a script named docker that emulates the Docker CLI by
executes %{name} commands, it also creates links between all Docker CLI man
pages and %{name}.

%package tests
Summary: Tests for %{name}

Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: bats
Requires: jq
Requires: skopeo
Requires: nmap-ncat
Requires: httpd-tools
Requires: openssl
Requires: socat
Requires: buildah
Requires: gnupg

%description tests
%{summary}

This package contains system tests for %{name}

%package remote
Summary: (Experimental) Remote client for managing %{name} containers

%description remote
Remote client for managing %{name} containers.

This experimental remote client is under heavy development. Please do not
run %{name}-remote in production.

%{name}-remote uses the version 2 API to connect to a %{name} client to
manage pods, containers and container images. %{name}-remote supports ssh
connections as well.

%package plugins
Summary: Plugins for %{name}
Requires: dnsmasq
Recommends: %{name}-gvproxy = %{epoch}:%{version}-%{release}

%description plugins
This plugin sets up the use of dnsmasq on a given CNI network so
that Pods can resolve each other by name.  When configured,
the pod and its IP address are added to a network specific hosts file
that dnsmasq will read in.  Similarly, when a pod
is removed from the network, it will remove the entry from the hosts
file.  Each CNI network will have its own dnsmasq instance.

%package gvproxy
Summary: Go replacement for libslirp and VPNKit

%description gvproxy
A replacement for libslirp and VPNKit, written in pure Go.
It is based on the network stack of gVisor. Compared to libslirp,
gvisor-tap-vsock brings a configurable DNS server and
dynamic port forwarding.

%prep
%autosetup -Sgit -n %{name}-%{built_tag_strip}
sed -i 's;@@PODMAN@@\;$(BINDIR);@@PODMAN@@\;%{_bindir};' Makefile

# untar dnsname
tar zxf %{SOURCE1}

# untar %%{name}-gvproxy
tar zxf %{SOURCE2}

%build
%if "%{_vendor}" != "debbuild"
%set_build_flags
export CGO_CFLAGS=$CFLAGS
# These extra flags present in $CFLAGS have been skipped for now as they break the build
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')

%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif
%endif

export GO111MODULE=off
export GOPATH=$(pwd)/_build:$(pwd)

mkdir _build
cd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path}
cd ..
ln -s vendor src

# build date. FIXME: Makefile uses '/v2/libpod', that doesn't work here?
LDFLAGS="-X %{import_path}/libpod/define.buildInfo=$(date +%s)"

# build rootlessport first
%gobuild -o bin/rootlessport %{import_path}/cmd/rootlessport

# build %%{name}
export BUILDTAGS="seccomp exclude_graphdriver_devicemapper $(hack/btrfs_installed_tag.sh) $(hack/btrfs_tag.sh) $(hack/libdm_tag.sh) $(hack/selinux_tag.sh) $(hack/systemd_tag.sh) $(hack/libsubid_tag.sh)"

%gobuild -o bin/%{name} %{import_path}/cmd/%{name}

# build %%{name}-remote
export BUILDTAGS="seccomp exclude_graphdriver_devicemapper exclude_graphdriver_btrfs btrfs_noversion $(hack/selinux_tag.sh) $(hack/systemd_tag.sh) $(hack/libsubid_tag.sh) remote"
%gobuild -o bin/%{name}-remote %{import_path}/cmd/%{name}

cd %{repo_plugins}-%{commit_plugins}
mkdir _build
cd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path_plugins}
cd ..
ln -s vendor src
export GOPATH=$(pwd)/_build:$(pwd)
%gobuild -o bin/dnsname %{import_path_plugins}/plugins/meta/dnsname
cd ..

cd %{repo_gvproxy}-%{commit_gvproxy}
mkdir _build
cd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path_gvproxy}
cd ..
ln -s vendor src
export GOPATH=$(pwd)/_build:$(pwd)
%gobuild -o bin/gvproxy %{import_path_gvproxy}/cmd/gvproxy
cd ..

%{__make} docs docker-docs

%install
install -dp %{buildroot}%{_unitdir}
PODMAN_VERSION=%{version} %{__make} PREFIX=%{buildroot}%{_prefix} ETCDIR=%{buildroot}%{_sysconfdir} \
       install.bin \
       install.man \
       install.systemd \
       install.completions \
       install.docker \
       install.docker-docs \
       install.remote \
%if 0%{?fedora} >= 36
        install.modules-load
%endif

# install dnsname plugin
cd %{repo_plugins}-%{commit_plugins}
%{__make} PREFIX=%{_prefix} DESTDIR=%{buildroot} install
cd ..

# install gvproxy
cd %{repo_gvproxy}-%{commit_gvproxy}
install -dp %{buildroot}%{_libexecdir}/%{name}
install -p -m0755 bin/gvproxy %{buildroot}%{_libexecdir}/%{name}
cd ..

# do not include docker and podman-remote man pages in main package
for file in `find %{buildroot}%{_mandir}/man[15] -type f | sed "s,%{buildroot},," | grep -v -e remote -e docker`; do
    echo "$file*" >> podman.file-list
done

rm -f %{buildroot}%{_mandir}/man5/docker*.5

install -d -p %{buildroot}/%{_datadir}/%{name}/test/system
cp -pav test/system %{buildroot}/%{_datadir}/%{name}/test/

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

# PACKIT PACKIT PACKIT PACKIT PACKIT PACKIT PACKIT PACKIT PACKIT PACKIT
# These files will be installed by unreleased versions of %%{name} and upstream is
# not comfy with a patch using packit's fix-spec-files action so let's remove the file here.
# The packager will need to revisit this section on every upstream release.
# See: https://github.com/containers/podman/pull/15457#discussion_r955423853
rm -f %{buildroot}%{_datadir}/user-tmpfiles.d/%{name}-docker.conf

%files -f %{name}.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md install.md transfer.md
%{_bindir}/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/rootlessport
%{_datadir}/bash-completion/completions/%{name}
# By "owning" the site-functions dir, we don't need to Require zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_unitdir}/%{name}*
%{_userunitdir}/%{name}*
%{_tmpfilesdir}/%{name}.conf
%if 0%{?fedora} >= 36
%{_modulesloaddir}/%{name}-iptables.conf
%endif

%files docker
%{_bindir}/docker
%{_mandir}/man1/docker*.1*
%{_tmpfilesdir}/%{name}-docker.conf

%files remote
%license LICENSE
%{_bindir}/%{name}-remote
%{_mandir}/man1/%{name}-remote*.*
%{_datadir}/bash-completion/completions/%{name}-remote
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}-remote.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}-remote

%files tests
%license LICENSE
%{_datadir}/%{name}/test

%files plugins
%license %{repo_plugins}-%{commit_plugins}/LICENSE
%doc %{repo_plugins}-%{commit_plugins}/{README.md,README_PODMAN.md}
%dir %{_libexecdir}/cni
%{_libexecdir}/cni/dnsname

%files gvproxy
%license %{repo_gvproxy}-%{commit_gvproxy}/LICENSE
%doc %{repo_gvproxy}-%{commit_gvproxy}/README.md
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/gvproxy

%changelog
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
