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
%global commit_gvproxy aab0ac9367fc5142f5857c36ac2352bcb3c60ab7

%global built_tag v4.4.3
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: podman
Epoch: 5
Version: %{gen_version}
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and MIT and MPL-2.0
Release: %autorelease
ExclusiveArch: %{golang_arches_future}
Summary: Manage Pods, Containers and Container Images
URL: https://%{name}.io/
# All SourceN files fetched from upstream
Source0: %{git0}/archive/%{built_tag}.tar.gz
Source1: %{git_plugins}/archive/%{commit_plugins}/%{repo_plugins}-%{commit_plugins}.tar.gz
Source2: %{git_gvproxy}/archive/%{commit_gvproxy}/%{repo_gvproxy}-%{commit_gvproxy}.tar.gz
Provides: %{name}-manpages = %{epoch}:%{version}-%{release}
BuildRequires: go-md2man
BuildRequires: btrfs-progs-devel
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: golang
BuildRequires: git-core
BuildRequires: go-rpm-macros
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
Requires: catatonit
Requires: conmon >= 2:2.0.30-2
%if 0%{?fedora} > 37
Requires: containers-common-extra >= 4:1-84
%else
%if 0%{?fedora} == 37
Requires: containers-common-extra >= 4:1-78
%else
Requires: containers-common-extra >= 4:1-66
%endif
%endif
Recommends: %{name}-gvproxy = %{epoch}:%{version}-%{release}
Provides: %{name}-quadlet
Obsoletes: %{name}-quadlet <= 5:4.4.0-1
Provides: %{name}-quadlet = %{epoch}:%{version}-%{release}
# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20210617225240_d185dfc1b5a1
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.2.1
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.6.0
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.9.6
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0
Provides: bundled(golang(github.com/acarl005/stripansi)) = v0.0.0_20180116102854_5a71ef0e047d
Provides: bundled(golang(github.com/asaskevich/govalidator)) = v0.0.0_20210307081110_f21760c49a8d
Provides: bundled(golang(github.com/blang/semver/v4)) = v4.0.0
Provides: bundled(golang(github.com/buger/goterm)) = v1.0.4
Provides: bundled(golang(github.com/checkpoint_restore/checkpointctl)) = v0.0.0_20220321135231_33f4a66335f0
Provides: bundled(golang(github.com/checkpoint_restore/go_criu/v6)) = v6.3.0
Provides: bundled(golang(github.com/chzyer/readline)) = v1.5.1
Provides: bundled(golang(github.com/container_orchestrated_devices/container_device_interface)) = v0.5.3
Provides: bundled(golang(github.com/containerd/cgroups)) = v1.0.4
Provides: bundled(golang(github.com/containerd/containerd)) = v1.6.15
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.13.0
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.1.2
Provides: bundled(golang(github.com/containernetworking/plugins)) = v1.2.0
Provides: bundled(golang(github.com/containers/buildah)) = v1.29.0
Provides: bundled(golang(github.com/containers/common)) = v0.51.0
Provides: bundled(golang(github.com/containers/conmon)) = v2.0.20+incompatible
Provides: bundled(golang(github.com/containers/image/v5)) = v5.24.0
Provides: bundled(golang(github.com/containers/libtrust)) = v0.0.0_20230121012942_c1716e8a8d01
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.7
Provides: bundled(golang(github.com/containers/psgo)) = v1.8.0
Provides: bundled(golang(github.com/containers/storage)) = v1.45.3
Provides: bundled(golang(github.com/coreos/go_oidc/v3)) = v3.5.0
Provides: bundled(golang(github.com/coreos/go_systemd)) = v0.0.0_20190719114852_fd7a80b32e1f
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.5.0
Provides: bundled(golang(github.com/coreos/stream_metadata_go)) = v0.0.0_20210225230131_70edb9eb47b3
Provides: bundled(golang(github.com/cyberphone/json_canonicalization)) = v0.0.0_20220623050100_57a0ce2678a7
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.2.3
Provides: bundled(golang(github.com/davecgh/go_spew)) = v1.1.1
Provides: bundled(golang(github.com/digitalocean/go_libvirt)) = v0.0.0_20201209184759_e2a69bcd5bd1
Provides: bundled(golang(github.com/digitalocean/go_qemu)) = v0.0.0_20210326154740_ac9e0b687001
Provides: bundled(golang(github.com/disiqueira/gotree/v3)) = v3.0.2
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.1+incompatible
Provides: bundled(golang(github.com/docker/docker)) = v20.10.23+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.7.0
Provides: bundled(golang(github.com/docker/go_connections)) = v0.4.1_0.20210727194412_58542c764a11
Provides: bundled(golang(github.com/docker/go_plugins_helpers)) = v0.0.0_20211224144127_6eecb7beb651
Provides: bundled(golang(github.com/docker/go_units)) = v0.5.0
Provides: bundled(golang(github.com/felixge/httpsnoop)) = v1.0.3
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = v1.6.0
Provides: bundled(golang(github.com/fsouza/go_dockerclient)) = v1.9.3
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
Provides: bundled(golang(github.com/go_jose/go_jose/v3)) = v3.0.0
Provides: bundled(golang(github.com/go_openapi/analysis)) = v0.21.4
Provides: bundled(golang(github.com/go_openapi/errors)) = v0.20.3
Provides: bundled(golang(github.com/go_openapi/jsonpointer)) = v0.19.5
Provides: bundled(golang(github.com/go_openapi/jsonreference)) = v0.20.0
Provides: bundled(golang(github.com/go_openapi/loads)) = v0.21.2
Provides: bundled(golang(github.com/go_openapi/runtime)) = v0.24.1
Provides: bundled(golang(github.com/go_openapi/spec)) = v0.20.7
Provides: bundled(golang(github.com/go_openapi/strfmt)) = v0.21.3
Provides: bundled(golang(github.com/go_openapi/swag)) = v0.22.3
Provides: bundled(golang(github.com/go_openapi/validate)) = v0.22.0
Provides: bundled(golang(github.com/go_playground/locales)) = v0.14.0
Provides: bundled(golang(github.com/go_playground/universal_translator)) = v0.18.0
Provides: bundled(golang(github.com/go_playground/validator/v10)) = v10.11.1
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.1.1_0.20221029134443_4b691ce883d5
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20210331224755_41bb18bfe9da
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.2
Provides: bundled(golang(github.com/google/go_cmp)) = v0.5.9
Provides: bundled(golang(github.com/google/go_containerregistry)) = v0.12.1
Provides: bundled(golang(github.com/google/go_intervals)) = v0.0.2
Provides: bundled(golang(github.com/google/gofuzz)) = v1.2.0
Provides: bundled(golang(github.com/google/shlex)) = v0.0.0_20191202100458_e7afc7fbc510
Provides: bundled(golang(github.com/google/trillian)) = v1.5.0
Provides: bundled(golang(github.com/google/uuid)) = v1.3.0
Provides: bundled(golang(github.com/gorilla/handlers)) = v1.5.1
Provides: bundled(golang(github.com/gorilla/mux)) = v1.8.0
Provides: bundled(golang(github.com/gorilla/schema)) = v1.2.0
Provides: bundled(golang(github.com/hashicorp/errwrap)) = v1.1.0
Provides: bundled(golang(github.com/hashicorp/go_cleanhttp)) = v0.5.2
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/hashicorp/go_retryablehttp)) = v0.7.2
Provides: bundled(golang(github.com/imdario/mergo)) = v0.3.13
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.0.1
Provides: bundled(golang(github.com/jinzhu/copier)) = v0.3.5
Provides: bundled(golang(github.com/josharian/intern)) = v1.0.0
Provides: bundled(golang(github.com/json_iterator/go)) = v1.1.12
Provides: bundled(golang(github.com/klauspost/compress)) = v1.15.15
Provides: bundled(golang(github.com/klauspost/pgzip)) = v1.2.6_0.20220930104621_17e8dac29df8
Provides: bundled(golang(github.com/kr/fs)) = v0.1.0
Provides: bundled(golang(github.com/leodido/go_urn)) = v1.2.1
Provides: bundled(golang(github.com/letsencrypt/boulder)) = v0.0.0_20221109233200_85aa52084eaf
Provides: bundled(golang(github.com/mailru/easyjson)) = v0.7.7
Provides: bundled(golang(github.com/manifoldco/promptui)) = v0.9.0
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.14
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/miekg/pkcs11)) = v1.1.1
Provides: bundled(golang(github.com/mistifyio/go_zfs/v3)) = v3.0.0
Provides: bundled(golang(github.com/mitchellh/mapstructure)) = v1.5.0
Provides: bundled(golang(github.com/moby/sys/mount)) = v0.3.3
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.6.2
Provides: bundled(golang(github.com/moby/term)) = v0.0.0_20210619224110_3f7ff695adc6
Provides: bundled(golang(github.com/modern_go/concurrent)) = v0.0.0_20180306012644_bacd9c7ef1dd
Provides: bundled(golang(github.com/modern_go/reflect2)) = v1.0.2
Provides: bundled(golang(github.com/morikuni/aec)) = v1.0.0
Provides: bundled(golang(github.com/nxadm/tail)) = v1.4.8
Provides: bundled(golang(github.com/oklog/ulid)) = v1.3.1
Provides: bundled(golang(github.com/onsi/ginkgo)) = v1.16.5
Provides: bundled(golang(github.com/onsi/gomega)) = v1.26.0
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.1.0_rc2
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.1.4
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20220825212826_86290f6a00fb
Provides: bundled(golang(github.com/opencontainers/runtime_tools)) = v0.9.1_0.20221014010322_58c91d646d86
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.10.2
Provides: bundled(golang(github.com/openshift/imagebuilder)) = v1.2.4_0.20220711175835_4151e43600df
Provides: bundled(golang(github.com/opentracing/opentracing_go)) = v1.2.0
Provides: bundled(golang(github.com/ostreedev/ostree_go)) = v0.0.0_20210805093236_719684c64e4f
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/pkg/sftp)) = v1.13.5
Provides: bundled(golang(github.com/pmezard/go_difflib)) = v1.0.0
Provides: bundled(golang(github.com/proglottis/gpgme)) = v0.1.3
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.4.3
Provides: bundled(golang(github.com/rootless_containers/rootlesskit)) = v1.1.0
Provides: bundled(golang(github.com/seccomp/libseccomp_golang)) = v0.10.0
Provides: bundled(golang(github.com/segmentio/ksuid)) = v1.0.4
Provides: bundled(golang(github.com/sigstore/fulcio)) = v1.0.0
Provides: bundled(golang(github.com/sigstore/rekor)) = v1.0.1
Provides: bundled(golang(github.com/sigstore/sigstore)) = v1.5.1
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.0
Provides: bundled(golang(github.com/skratchdot/open_golang)) = v0.0.0_20200116055534_eef842397966
Provides: bundled(golang(github.com/spf13/cobra)) = v1.6.1
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stefanberger/go_pkcs11uri)) = v0.0.0_20201008174630_78d3cae3a980
Provides: bundled(golang(github.com/stretchr/testify)) = v1.8.1
Provides: bundled(golang(github.com/sylabs/sif/v2)) = v2.9.0
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/tchap/go_patricia)) = v2.3.0+incompatible
Provides: bundled(golang(github.com/theupdateframework/go_tuf)) = v0.5.2_0.20221207161717_9cb61d6e65f5
Provides: bundled(golang(github.com/titanous/rocacheck)) = v0.0.0_20171023193734_afe73141d399
Provides: bundled(golang(github.com/uber/jaeger_client_go)) = v2.30.0+incompatible
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.11
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.2
Provides: bundled(golang(github.com/vbauerster/mpb/v7)) = v7.5.3
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.2.1_beta.2
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.0_20210104183010_2eb08e3e575f
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0_20190905194746_02993c407bfb
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0_20180127040603_bd5ef7bd5415
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0
Provides: bundled(golang(sigs.k8s.io/yaml)) = v1.3.0

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

export BASEBUILDTAGS="seccomp exclude_graphdriver_devicemapper $(hack/selinux_tag.sh) $(hack/systemd_tag.sh) $(hack/libsubid_tag.sh)"

# build %%{name}
export BUILDTAGS="$BASEBUILDTAGS $(hack/btrfs_installed_tag.sh) $(hack/btrfs_tag.sh) $(hack/libdm_tag.sh)"

%gobuild -o bin/%{name} %{import_path}/cmd/%{name}

# build %%{name}-remote
export BUILDTAGS="$BASEBUILDTAGS exclude_graphdriver_btrfs btrfs_noversion remote"
%gobuild -o bin/%{name}-remote %{import_path}/cmd/%{name}

# build quadlet
export BUILDTAGS="$BASEBUILDTAGS $(hack/btrfs_installed_tag.sh) $(hack/btrfs_tag.sh)"
%gobuild -o bin/quadlet %{import_path}/cmd/quadlet

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
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 10
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

# Sanitize paths in %%{_bindir}/docker
sed -i 's;%{buildroot}%{_sysconfdir};%{_sysconfdir}/containers;g' %{buildroot}%{_bindir}/docker

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
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 10
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

%changelog
%autochangelog
