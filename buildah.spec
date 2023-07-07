%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if %{defined rhel} && 0%{?rhel} == 8
# RHEL 8's default %%gobuild macro doesn't account for the BUILDTAGS variable, so we
# set it separately here and do not depend on RHEL 8's go-srpm-macros package.
%define gobuild(o:) go build -buildmode pie -compiler gc -tags="rpm_crashtraceback libtrust_openssl ${BUILDTAGS:-}" -ldflags "-linkmode=external -compressdwarf=false ${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags'" -a -v -x %{?**};
%endif

%global gomodulesmode GO111MODULE=on

%if 0%{defined fedora}
%define build_with_btrfs 1
%endif

%global git0 https://github.com/containers/%{name}

Name: buildah
# Set different Epoch for copr
%if %{defined copr_username}
Epoch: 102
%endif
# DO NOT TOUCH the Version string!
# The TRUE source of this specfile is:
# https://github.com/containers/skopeo/blob/main/rpm/skopeo.spec
# If that's what you're reading, Version must be 0, and will be updated by Packit for
# copr and koji builds.
# If you're reading this on dist-git, the version is automatically filled in by Packit.
Version: 1.31.0
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and MIT and MPL-2.0
Release: %autorelease
%if %{defined golang_arches_future}
ExclusiveArch: %{golang_arches_future}
%else
ExclusiveArch: aarch64 ppc64le s390x x86_64
%endif
Summary: A command line tool used for creating OCI Images
URL: https://%{name}.io
# Tarball fetched from upstream
Source: %{git0}/archive/v%{version}.tar.gz
BuildRequires: go-md2man
BuildRequires: device-mapper-devel
BuildRequires: git-core
BuildRequires: golang >= 1.16.6
BuildRequires: glib2-devel
BuildRequires: glibc-static
%if !%{defined gobuild}
BuildRequires: go-rpm-macros
%endif
BuildRequires: gpgme-devel
BuildRequires: libassuan-devel
BuildRequires: make
BuildRequires: ostree-devel
%if %{defined build_with_btrfs}
BuildRequires: btrfs-progs-devel
%endif
BuildRequires: shadow-utils-subid-devel
Requires: containers-common-extra
%if %{defined fedora}
BuildRequires: libseccomp-static
%else
BuildRequires: libseccomp-devel
%endif
Requires: libseccomp >= 2.4.1-0
Suggests: cpp
# DO NOT DELETE BELOW LINE - used for updating downstream goimports
# vendored libraries
Provides: bundled(golang(github.com/containerd/containerd/platforms))
Provides: bundled(golang(github.com/containernetworking/cni/pkg/version))
Provides: bundled(golang(github.com/containernetworking/plugins/pkg/ns))
Provides: bundled(golang(github.com/containers/common/libimage))
Provides: bundled(golang(github.com/containers/common/libimage/manifests))
Provides: bundled(golang(github.com/containers/common/libnetwork/etchosts))
Provides: bundled(golang(github.com/containers/common/libnetwork/network))
Provides: bundled(golang(github.com/containers/common/libnetwork/pasta))
Provides: bundled(golang(github.com/containers/common/libnetwork/resolvconf))
Provides: bundled(golang(github.com/containers/common/libnetwork/slirp4netns))
Provides: bundled(golang(github.com/containers/common/libnetwork/types))
Provides: bundled(golang(github.com/containers/common/libnetwork/util))
Provides: bundled(golang(github.com/containers/common/pkg/auth))
Provides: bundled(golang(github.com/containers/common/pkg/capabilities))
Provides: bundled(golang(github.com/containers/common/pkg/chown))
Provides: bundled(golang(github.com/containers/common/pkg/completion))
Provides: bundled(golang(github.com/containers/common/pkg/config))
Provides: bundled(golang(github.com/containers/common/pkg/hooks))
Provides: bundled(golang(github.com/containers/common/pkg/hooks/exec))
Provides: bundled(golang(github.com/containers/common/pkg/manifests))
Provides: bundled(golang(github.com/containers/common/pkg/parse))
Provides: bundled(golang(github.com/containers/common/pkg/retry))
Provides: bundled(golang(github.com/containers/common/pkg/subscriptions))
Provides: bundled(golang(github.com/containers/common/pkg/supplemented))
Provides: bundled(golang(github.com/containers/common/pkg/umask))
Provides: bundled(golang(github.com/containers/common/pkg/util))
Provides: bundled(golang(github.com/containers/image/v5/copy))
Provides: bundled(golang(github.com/containers/image/v5/docker))
Provides: bundled(golang(github.com/containers/image/v5/docker/reference))
Provides: bundled(golang(github.com/containers/image/v5/image))
Provides: bundled(golang(github.com/containers/image/v5/manifest))
Provides: bundled(golang(github.com/containers/image/v5/oci/layout))
Provides: bundled(golang(github.com/containers/image/v5/pkg/blobcache))
Provides: bundled(golang(github.com/containers/image/v5/pkg/compression))
Provides: bundled(golang(github.com/containers/image/v5/pkg/shortnames))
Provides: bundled(golang(github.com/containers/image/v5/pkg/strslice))
Provides: bundled(golang(github.com/containers/image/v5/pkg/sysregistriesv2))
Provides: bundled(golang(github.com/containers/image/v5/signature))
Provides: bundled(golang(github.com/containers/image/v5/storage))
Provides: bundled(golang(github.com/containers/image/v5/transports))
Provides: bundled(golang(github.com/containers/image/v5/transports/alltransports))
Provides: bundled(golang(github.com/containers/image/v5/types))
Provides: bundled(golang(github.com/containers/image/v5/version))
Provides: bundled(golang(github.com/containers/ocicrypt/config))
Provides: bundled(golang(github.com/containers/ocicrypt/helpers))
Provides: bundled(golang(github.com/containers/storage))
Provides: bundled(golang(github.com/containers/storage/pkg/archive))
Provides: bundled(golang(github.com/containers/storage/pkg/chrootarchive))
Provides: bundled(golang(github.com/containers/storage/pkg/fileutils))
Provides: bundled(golang(github.com/containers/storage/pkg/idtools))
Provides: bundled(golang(github.com/containers/storage/pkg/ioutils))
Provides: bundled(golang(github.com/containers/storage/pkg/lockfile))
Provides: bundled(golang(github.com/containers/storage/pkg/mount))
Provides: bundled(golang(github.com/containers/storage/pkg/reexec))
Provides: bundled(golang(github.com/containers/storage/pkg/stringid))
Provides: bundled(golang(github.com/containers/storage/pkg/system))
Provides: bundled(golang(github.com/containers/storage/pkg/unshare))
Provides: bundled(golang(github.com/containers/storage/types))
Provides: bundled(golang(github.com/cyphar/filepath-securejoin))
Provides: bundled(golang(github.com/docker/distribution/registry/api/errcode))
Provides: bundled(golang(github.com/docker/go-units))
Provides: bundled(golang(github.com/fsouza/go-dockerclient))
Provides: bundled(golang(github.com/hashicorp/go-multierror))
Provides: bundled(golang(github.com/mattn/go-shellwords))
Provides: bundled(golang(github.com/opencontainers/go-digest))
Provides: bundled(golang(github.com/opencontainers/image-spec/specs-go))
Provides: bundled(golang(github.com/opencontainers/image-spec/specs-go/v1))
Provides: bundled(golang(github.com/opencontainers/runc/libcontainer/apparmor))
Provides: bundled(golang(github.com/opencontainers/runc/libcontainer/devices))
Provides: bundled(golang(github.com/opencontainers/runc/libcontainer/userns))
Provides: bundled(golang(github.com/opencontainers/runtime-spec/specs-go))
Provides: bundled(golang(github.com/opencontainers/runtime-tools/generate))
Provides: bundled(golang(github.com/opencontainers/selinux/go-selinux))
Provides: bundled(golang(github.com/opencontainers/selinux/go-selinux/label))
Provides: bundled(golang(github.com/openshift/imagebuilder))
Provides: bundled(golang(github.com/openshift/imagebuilder/dockerfile/command))
Provides: bundled(golang(github.com/openshift/imagebuilder/dockerfile/parser))
Provides: bundled(golang(github.com/sirupsen/logrus))
Provides: bundled(golang(github.com/spf13/cobra))
Provides: bundled(golang(github.com/spf13/pflag))
Provides: bundled(golang(github.com/syndtr/gocapability/capability))
Provides: bundled(golang(go.etcd.io/bbolt))
Provides: bundled(golang(golang.org/x/crypto/bcrypt))
Provides: bundled(golang(golang.org/x/crypto/ssh))
Provides: bundled(golang(golang.org/x/crypto/ssh/agent))
Provides: bundled(golang(golang.org/x/sync/semaphore))
Provides: bundled(golang(golang.org/x/sys/unix))
Provides: bundled(golang(golang.org/x/term))
Provides: bundled(golang(sigs.k8s.io/yaml))

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
%autosetup -Sgit -n %{name}-%{version}

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

export CNI_VERSION=`grep '^# github.com/containernetworking/cni ' src/modules.txt | sed 's,.* ,,'`
export LDFLAGS="-X main.buildInfo=`date +%s` -X main.cniVersion=${CNI_VERSION}"

export BUILDTAGS='seccomp exclude_graphdriver_devicemapper $(hack/systemd_tag.sh) $hack/libsubid_tag.sh)'
%if !%{defined build_with_btrfs}
export BUILDTAGS+=' btrfs_noversion exclude_graphdriver_btrfs'
%endif

%gobuild -o bin/%{name} ./cmd/%{name}
%gobuild -o bin/imgtype ./tests/imgtype
%gobuild -o bin/copy ./tests/copy
%gobuild -o bin/tutorial ./tests/tutorial
GOMD2MAN=go-md2man %{__make} -C docs

%install
export GOPATH=$(pwd)/_build:$(pwd)
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install install.completions
make DESTDIR=%{buildroot} PREFIX=%{_prefix} -C docs install

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
%if %{defined autochangelog}
%autochangelog
%else
# NOTE: This changelog will be visible on CentOS 8 Stream builds
# Other envs are capable of handling autochangelog
* Fri Jun 16 2023 RH Container Bot <rhcontainerbot@fedoraproject.org>
- Placeholder changelog for envs that are not autochangelog-ready.
- Contact upstream if you need to report an issue with the build.
%endif
