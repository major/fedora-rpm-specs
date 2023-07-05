%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

# RHEL 8's default %%gobuild macro doesn't account for the BUILDTAGS variable, so we
# set it separately here and do not depend on RHEL 8's go-srpm-macros package.
%if %{defined rhel} && 0%{?rhel} == 8
%define gobuild(o:) go build -buildmode pie -compiler gc -tags="rpm_crashtraceback libtrust_openssl ${BUILDTAGS:-}" -ldflags "-linkmode=external -compressdwarf=false ${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags'" -a -v -x %{?**};
%define rhel8py3 1
%endif

%global gomodulesmode GO111MODULE=on

%if %{defined rhel}
# _user_tmpfiles.d currently undefined on rhel
%global _user_tmpfilesdir %{_datadir}/user-tmpfiles.d
%endif

%if %{defined fedora}
%define build_with_btrfs 1
%endif

%global container_base_path github.com/containers
%global container_base_url https://%{container_base_path}

# For LDFLAGS
%global ld_project %{container_base_path}/%{name}/v4
%global ld_libpod %{ld_project}/libpod

# %%{name}
%global git0 %{container_base_url}/%{name}

# dnsname
%global repo_plugins dnsname
%global git_plugins %{container_base_url}/%{repo_plugins}
%global commit_plugins 18822f9a4fb35d1349eb256f4cd2bfd372474d84
%global import_path_plugins %{container_base_path}/%{repo_plugins}

# gvproxy
%global repo_gvproxy gvisor-tap-vsock
%global git_gvproxy %{container_base_url}/%{repo_gvproxy}
%global commit_gvproxy 407efb5dcdb0f4445935f7360535800b60447544

Name: podman
%if %{defined copr_username}
Epoch: 102
%else
Epoch: 5
%endif
# DO NOT TOUCH the Version string!
# The TRUE source of this specfile is:
# https://github.com/containers/podman/blob/main/rpm/podman.spec
# If that's what you're reading, Version must be 0, and will be updated by Packit for
# copr and koji builds.
# If you're reading this on dist-git, the version is automatically filled in by Packit.
Version: 4.6.0~rc1
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and MIT and MPL-2.0
Release: %autorelease
%if %{defined golang_arches_future}
ExclusiveArch: %{golang_arches_future}
%else
ExclusiveArch: aarch64 ppc64le s390x x86_64
%endif
Summary: Manage Pods, Containers and Container Images
URL: https://%{name}.io/
# All SourceN files fetched from upstream
Source0: %{git0}/archive/v4.6.0-rc1.tar.gz
Source1: %{git_plugins}/archive/%{commit_plugins}/%{repo_plugins}-%{commit_plugins}.tar.gz
Source2: %{git_gvproxy}/archive/%{commit_gvproxy}/%{repo_gvproxy}-%{commit_gvproxy}.tar.gz
Provides: %{name}-manpages = %{epoch}:%{version}-%{release}
BuildRequires: %{_bindir}/envsubst
BuildRequires: %{_bindir}/go-md2man
%if %{defined build_with_btrfs}
BuildRequires: btrfs-progs-devel
%endif
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: golang
BuildRequires: git-core
%if !%{defined gobuild}
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
%if %{defined rhel8py3}
BuildRequires: python3
%endif
Requires: catatonit
Requires: conmon >= 2:2.1.7-2
Requires: containers-common-extra
Recommends: %{name}-gvproxy = %{epoch}:%{version}-%{release}
Provides: %{name}-quadlet
Obsoletes: %{name}-quadlet <= 5:4.4.0-1
Provides: %{name}-quadlet = %{epoch}:%{version}-%{release}
# DO NOT DELETE BELOW LINE - used for updating downstream goimports
# vendored libraries
Provides: bundled(golang(github.com/blang/semver/v4))
Provides: bundled(golang(github.com/buger/goterm))
Provides: bundled(golang(github.com/BurntSushi/toml))
Provides: bundled(golang(github.com/checkpoint-restore/checkpointctl/lib))
Provides: bundled(golang(github.com/checkpoint-restore/go-criu/v6))
Provides: bundled(golang(github.com/checkpoint-restore/go-criu/v6/rpc))
Provides: bundled(golang(github.com/checkpoint-restore/go-criu/v6/stats))
Provides: bundled(golang(github.com/containernetworking/cni/pkg/types/040))
Provides: bundled(golang(github.com/containernetworking/plugins/pkg/ns))
Provides: bundled(golang(github.com/container-orchestrated-devices/container-device-interface/pkg/cdi))
Provides: bundled(golang(github.com/containers/buildah))
Provides: bundled(golang(github.com/containers/buildah/copier))
Provides: bundled(golang(github.com/containers/buildah/define))
Provides: bundled(golang(github.com/containers/buildah/imagebuildah))
Provides: bundled(golang(github.com/containers/buildah/pkg/chrootuser))
Provides: bundled(golang(github.com/containers/buildah/pkg/cli))
Provides: bundled(golang(github.com/containers/buildah/pkg/overlay))
Provides: bundled(golang(github.com/containers/buildah/pkg/parse))
Provides: bundled(golang(github.com/containers/buildah/pkg/util))
Provides: bundled(golang(github.com/containers/buildah/util))
Provides: bundled(golang(github.com/containers/common/libimage))
Provides: bundled(golang(github.com/containers/common/libimage/define))
Provides: bundled(golang(github.com/containers/common/libnetwork/cni))
Provides: bundled(golang(github.com/containers/common/libnetwork/etchosts))
Provides: bundled(golang(github.com/containers/common/libnetwork/network))
Provides: bundled(golang(github.com/containers/common/libnetwork/pasta))
Provides: bundled(golang(github.com/containers/common/libnetwork/resolvconf))
Provides: bundled(golang(github.com/containers/common/libnetwork/slirp4netns))
Provides: bundled(golang(github.com/containers/common/libnetwork/types))
Provides: bundled(golang(github.com/containers/common/libnetwork/util))
Provides: bundled(golang(github.com/containers/common/pkg/apparmor))
Provides: bundled(golang(github.com/containers/common/pkg/auth))
Provides: bundled(golang(github.com/containers/common/pkg/capabilities))
Provides: bundled(golang(github.com/containers/common/pkg/cgroups))
Provides: bundled(golang(github.com/containers/common/pkg/chown))
Provides: bundled(golang(github.com/containers/common/pkg/completion))
Provides: bundled(golang(github.com/containers/common/pkg/config))
Provides: bundled(golang(github.com/containers/common/pkg/download))
Provides: bundled(golang(github.com/containers/common/pkg/filters))
Provides: bundled(golang(github.com/containers/common/pkg/flag))
Provides: bundled(golang(github.com/containers/common/pkg/hooks))
Provides: bundled(golang(github.com/containers/common/pkg/hooks/exec))
Provides: bundled(golang(github.com/containers/common/pkg/machine))
Provides: bundled(golang(github.com/containers/common/pkg/netns))
Provides: bundled(golang(github.com/containers/common/pkg/parse))
Provides: bundled(golang(github.com/containers/common/pkg/report))
Provides: bundled(golang(github.com/containers/common/pkg/resize))
Provides: bundled(golang(github.com/containers/common/pkg/rootlessport))
Provides: bundled(golang(github.com/containers/common/pkg/seccomp))
Provides: bundled(golang(github.com/containers/common/pkg/secrets))
Provides: bundled(golang(github.com/containers/common/pkg/servicereaper))
Provides: bundled(golang(github.com/containers/common/pkg/ssh))
Provides: bundled(golang(github.com/containers/common/pkg/subscriptions))
Provides: bundled(golang(github.com/containers/common/pkg/sysinfo))
Provides: bundled(golang(github.com/containers/common/pkg/umask))
Provides: bundled(golang(github.com/containers/common/pkg/util))
Provides: bundled(golang(github.com/containers/conmon/runner/config))
Provides: bundled(golang(github.com/containers/image/v5/copy))
Provides: bundled(golang(github.com/containers/image/v5/docker))
Provides: bundled(golang(github.com/containers/image/v5/docker/reference))
Provides: bundled(golang(github.com/containers/image/v5/manifest))
Provides: bundled(golang(github.com/containers/image/v5/pkg/cli))
Provides: bundled(golang(github.com/containers/image/v5/pkg/cli/sigstore))
Provides: bundled(golang(github.com/containers/image/v5/pkg/compression))
Provides: bundled(golang(github.com/containers/image/v5/pkg/docker/config))
Provides: bundled(golang(github.com/containers/image/v5/pkg/shortnames))
Provides: bundled(golang(github.com/containers/image/v5/pkg/sysregistriesv2))
Provides: bundled(golang(github.com/containers/image/v5/signature))
Provides: bundled(golang(github.com/containers/image/v5/signature/signer))
Provides: bundled(golang(github.com/containers/image/v5/storage))
Provides: bundled(golang(github.com/containers/image/v5/transports))
Provides: bundled(golang(github.com/containers/image/v5/transports/alltransports))
Provides: bundled(golang(github.com/containers/image/v5/types))
Provides: bundled(golang(github.com/containers/ocicrypt/config))
Provides: bundled(golang(github.com/containers/ocicrypt/helpers))
Provides: bundled(golang(github.com/containers/psgo))
Provides: bundled(golang(github.com/containers/storage))
Provides: bundled(golang(github.com/containers/storage/drivers/quota))
Provides: bundled(golang(github.com/containers/storage/pkg/archive))
Provides: bundled(golang(github.com/containers/storage/pkg/chrootarchive))
Provides: bundled(golang(github.com/containers/storage/pkg/directory))
Provides: bundled(golang(github.com/containers/storage/pkg/fileutils))
Provides: bundled(golang(github.com/containers/storage/pkg/homedir))
Provides: bundled(golang(github.com/containers/storage/pkg/idmap))
Provides: bundled(golang(github.com/containers/storage/pkg/idtools))
Provides: bundled(golang(github.com/containers/storage/pkg/ioutils))
Provides: bundled(golang(github.com/containers/storage/pkg/lockfile))
Provides: bundled(golang(github.com/containers/storage/pkg/mount))
Provides: bundled(golang(github.com/containers/storage/pkg/parsers/kernel))
Provides: bundled(golang(github.com/containers/storage/pkg/reexec))
Provides: bundled(golang(github.com/containers/storage/pkg/regexp))
Provides: bundled(golang(github.com/containers/storage/pkg/stringid))
Provides: bundled(golang(github.com/containers/storage/pkg/system))
Provides: bundled(golang(github.com/containers/storage/pkg/unshare))
Provides: bundled(golang(github.com/containers/storage/types))
Provides: bundled(golang(github.com/coreos/go-systemd/v22/activation))
Provides: bundled(golang(github.com/coreos/go-systemd/v22/daemon))
Provides: bundled(golang(github.com/coreos/go-systemd/v22/dbus))
Provides: bundled(golang(github.com/coreos/stream-metadata-go/fedoracoreos))
Provides: bundled(golang(github.com/coreos/stream-metadata-go/release))
Provides: bundled(golang(github.com/coreos/stream-metadata-go/stream))
Provides: bundled(golang(github.com/cyphar/filepath-securejoin))
Provides: bundled(golang(github.com/digitalocean/go-qemu/qmp))
Provides: bundled(golang(github.com/docker/distribution/registry/api/errcode))
Provides: bundled(golang(github.com/docker/docker/api/types))
Provides: bundled(golang(github.com/docker/docker/api/types/container))
Provides: bundled(golang(github.com/docker/docker/api/types/events))
Provides: bundled(golang(github.com/docker/docker/api/types/mount))
Provides: bundled(golang(github.com/docker/docker/api/types/network))
Provides: bundled(golang(github.com/docker/docker/api/types/registry))
Provides: bundled(golang(github.com/docker/docker/api/types/swarm))
Provides: bundled(golang(github.com/docker/docker/api/types/volume))
Provides: bundled(golang(github.com/docker/docker/pkg/homedir))
Provides: bundled(golang(github.com/docker/docker/pkg/jsonmessage))
Provides: bundled(golang(github.com/docker/docker/pkg/meminfo))
Provides: bundled(golang(github.com/docker/docker/pkg/namesgenerator))
Provides: bundled(golang(github.com/docker/docker/pkg/parsers))
Provides: bundled(golang(github.com/docker/go-connections/nat))
Provides: bundled(golang(github.com/docker/go-plugins-helpers/sdk))
Provides: bundled(golang(github.com/docker/go-plugins-helpers/volume))
Provides: bundled(golang(github.com/docker/go-units))
Provides: bundled(golang(github.com/godbus/dbus/v5))
Provides: bundled(golang(github.com/google/gofuzz))
Provides: bundled(golang(github.com/google/shlex))
Provides: bundled(golang(github.com/google/uuid))
Provides: bundled(golang(github.com/gorilla/handlers))
Provides: bundled(golang(github.com/gorilla/mux))
Provides: bundled(golang(github.com/gorilla/schema))
Provides: bundled(golang(github.com/hashicorp/go-multierror))
Provides: bundled(golang(github.com/json-iterator/go))
Provides: bundled(golang(github.com/mattn/go-sqlite3))
Provides: bundled(golang(github.com/moby/term))
Provides: bundled(golang(github.com/nxadm/tail))
Provides: bundled(golang(github.com/nxadm/tail/watch))
Provides: bundled(golang(github.com/onsi/ginkgo/v2))
Provides: bundled(golang(github.com/onsi/gomega))
Provides: bundled(golang(github.com/onsi/gomega/format))
Provides: bundled(golang(github.com/onsi/gomega/gexec))
Provides: bundled(golang(github.com/onsi/gomega/matchers))
Provides: bundled(golang(github.com/onsi/gomega/types))
Provides: bundled(golang(github.com/opencontainers/go-digest))
Provides: bundled(golang(github.com/opencontainers/image-spec/specs-go/v1))
Provides: bundled(golang(github.com/opencontainers/runc/libcontainer/cgroups))
Provides: bundled(golang(github.com/opencontainers/runc/libcontainer/configs))
Provides: bundled(golang(github.com/opencontainers/runc/libcontainer/devices))
Provides: bundled(golang(github.com/opencontainers/runc/libcontainer/user))
Provides: bundled(golang(github.com/opencontainers/runtime-spec/specs-go))
Provides: bundled(golang(github.com/opencontainers/runtime-tools/generate))
Provides: bundled(golang(github.com/opencontainers/runtime-tools/validate/capabilities))
Provides: bundled(golang(github.com/opencontainers/selinux/go-selinux))
Provides: bundled(golang(github.com/opencontainers/selinux/go-selinux/label))
Provides: bundled(golang(github.com/openshift/imagebuilder))
Provides: bundled(golang(github.com/rootless-containers/rootlesskit/pkg/port))
Provides: bundled(golang(github.com/rootless-containers/rootlesskit/pkg/port/builtin))
Provides: bundled(golang(github.com/rootless-containers/rootlesskit/pkg/port/portutil))
Provides: bundled(golang(github.com/sirupsen/logrus))
Provides: bundled(golang(github.com/sirupsen/logrus/hooks/syslog))
Provides: bundled(golang(github.com/spf13/cobra))
Provides: bundled(golang(github.com/spf13/pflag))
Provides: bundled(golang(github.com/syndtr/gocapability/capability))
Provides: bundled(golang(github.com/ulikunitz/xz))
Provides: bundled(golang(github.com/vbauerster/mpb/v8))
Provides: bundled(golang(github.com/vbauerster/mpb/v8/decor))
Provides: bundled(golang(github.com/vishvananda/netlink))
Provides: bundled(golang(go.etcd.io/bbolt))
Provides: bundled(golang(golang.org/x/net/proxy))
Provides: bundled(golang(golang.org/x/sync/semaphore))
Provides: bundled(golang(golang.org/x/sys/unix))
Provides: bundled(golang(golang.org/x/term))
Provides: bundled(golang(google.golang.org/protobuf/proto))
Provides: bundled(golang(gopkg.in/inf.v0))
Provides: bundled(golang(gopkg.in/yaml.v3))
Provides: bundled(golang(sigs.k8s.io/yaml))

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

%package -n %{name}sh
Summary: Confined login and user shell using %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %{name}-shell = %{epoch}:%{version}-%{release}
Provides: %{name}-%{name}sh = %{epoch}:%{version}-%{release}

%description -n %{name}sh
%{name}sh provides a confined login and user shell with access to volumes and
capabilities specified in user quadlets.

It is a symlink to %{_bindir}/%{name} and execs into the `%{name}sh` container
when `%{_bindir}/%{name}sh is set as a login shell or set as os.Args[0].

%prep
%autosetup -Sgit -n %{name}-4.6.0-rc1
sed -i 's;@@PODMAN@@\;$(BINDIR);@@PODMAN@@\;%{_bindir};' Makefile

# untar dnsname
tar zxf %{SOURCE1}

# untar %%{name}-gvproxy
tar zxf %{SOURCE2}

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

LDFLAGS="-X %{ld_libpod}/define.buildInfo=$(date +%s) \
         -X %{ld_libpod}/config._installPrefix=%{_prefix} \
         -X %{ld_libpod}/config._etcDir=%{_sysconfdir} \
         -X %{ld_project}/pkg/systemd/quadlet._binDir=%{_bindir}"

# build rootlessport first
%gobuild -o bin/rootlessport ./cmd/rootlessport

export BASEBUILDTAGS="seccomp exclude_graphdriver_devicemapper $(hack/systemd_tag.sh) $(hack/libsubid_tag.sh)"

# build %%{name}
export BUILDTAGS="$BASEBUILDTAGS $(hack/btrfs_installed_tag.sh) $(hack/btrfs_tag.sh) $(hack/libdm_tag.sh)"
%gobuild -o bin/%{name} ./cmd/%{name}

# build %%{name}-remote
export BUILDTAGS="$BASEBUILDTAGS exclude_graphdriver_btrfs btrfs_noversion remote"
%gobuild -o bin/%{name}-remote ./cmd/%{name}

# build quadlet
export BUILDTAGS="$BASEBUILDTAGS $(hack/btrfs_installed_tag.sh) $(hack/btrfs_tag.sh)"
%gobuild -o bin/quadlet ./cmd/quadlet

# reset LDFLAGS for plugins and gvisor binaries
LDFLAGS=''

# build gvisor-tap-vsock binaries
cd %{repo_gvproxy}-%{commit_gvproxy}
%gobuild -o bin/gvproxy ./cmd/gvproxy
%gobuild -o bin/gvforwarder ./cmd/vm
cd ..

%{__make} docs docker-docs

# build dnsname the old way otherwise it fails on koji
cd %{repo_plugins}-%{commit_plugins}
mkdir _build
cd _build
mkdir -p src/%{container_base_path}
ln -s ../../../../ src/%{import_path_plugins}
cd ..
ln -s vendor src
export GOPATH=$(pwd)/_build:$(pwd)
%define gomodulesmode GO111MODULE=off
%gobuild -o bin/dnsname %{import_path_plugins}/plugins/meta/dnsname
cd ..

%install
install -dp %{buildroot}%{_unitdir}
PODMAN_VERSION=%{version} %{__make} PREFIX=%{buildroot}%{_prefix} ETCDIR=%{_sysconfdir} \
       install.bin \
       install.man \
       install.systemd \
       install.completions \
       install.docker \
       install.docker-docs \
       install.remote \
%if %{defined _modulesloaddir}
        install.modules-load
%endif

sed -i 's;%{buildroot};;g' %{buildroot}%{_bindir}/docker

# install dnsname plugin
cd %{repo_plugins}-%{commit_plugins}
%{__make} PREFIX=%{_prefix} DESTDIR=%{buildroot} install
cd ..

# install gvproxy
cd %{repo_gvproxy}-%{commit_gvproxy}
install -dp %{buildroot}%{_libexecdir}/%{name}
install -p -m0755 bin/gvproxy %{buildroot}%{_libexecdir}/%{name}
install -p -m0755 bin/gvforwarder %{buildroot}%{_libexecdir}/%{name}
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

%files -f %{name}.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md install.md transfer.md
%{_bindir}/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/rootlessport
%{_libexecdir}/%{name}/quadlet
%{_datadir}/bash-completion/completions/%{name}
# By "owning" the site-functions dir, we don't need to Require zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_unitdir}/%{name}*
%{_userunitdir}/%{name}*
%{_tmpfilesdir}/%{name}.conf
%{_systemdgeneratordir}/%{name}-system-generator
%{_systemdusergeneratordir}/%{name}-user-generator
%if %{defined _modulesloaddir}
%{_modulesloaddir}/%{name}-iptables.conf
%endif

%files docker
%{_bindir}/docker
%{_mandir}/man1/docker*.1*
%{_tmpfilesdir}/%{name}-docker.conf
%{_user_tmpfilesdir}/%{name}-docker.conf

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
%{_libexecdir}/%{name}/gvforwarder

%files -n %{name}sh
%license LICENSE
%doc README.md CONTRIBUTING.md install.md transfer.md
%{_bindir}/%{name}sh

%changelog
%if %{defined autochangelog}
%autochangelog
%else
* Mon May 01 2023 RH Container Bot <rhcontainerbot@fedoraproject.org>
- Placeholder changelog for envs that are not autochangelog-ready
%endif
