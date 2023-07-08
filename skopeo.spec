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
%endif

%global gomodulesmode GO111MODULE=on

# No btrfs on RHEL
%if %{defined fedora}
%define build_with_btrfs 1
%endif

# Only used in official koji builds
# Copr builds set a separate epoch for all environments
%if %{defined fedora}
%define conditional_epoch 1
%else
%define conditional_epoch 2
%endif

Name: skopeo
%if %{defined copr_username}
Epoch: 102
%else
Epoch: %{conditional_epoch}
%endif
# DO NOT TOUCH the Version string!
# The TRUE source of this specfile is:
# https://github.com/containers/skopeo/blob/main/rpm/skopeo.spec
# If that's what you're reading, Version must be 0, and will be updated by Packit for
# copr and koji builds.
# If you're reading this on dist-git, the version is automatically filled in by Packit.
Version: 1.13.0
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and MIT and MPL-2.0
Release: %autorelease
%if %{defined golang_arches_future}
ExclusiveArch: %{golang_arches_future}
%else
ExclusiveArch: aarch64 ppc64le s390x x86_64
%endif
Summary: Inspect container images and repositories on registries
URL: https://github.com/containers/%{name}
# Tarball fetched from upstream
Source0: %{url}/archive/v%{version}.tar.gz
BuildRequires: %{_bindir}/go-md2man
%if %{defined build_with_btrfs}
BuildRequires: btrfs-progs-devel
%endif
BuildRequires: git-core
BuildRequires: golang
%if !%{defined gobuild}
BuildRequires: go-rpm-macros
%endif
BuildRequires: gpgme-devel
BuildRequires: libassuan-devel
BuildRequires: pkgconfig(devmapper)
BuildRequires: ostree-devel
BuildRequires: glib2-devel
BuildRequires: make
BuildRequires: shadow-utils-subid-devel
Requires: containers-common >= 4:1-21
# DO NOT DELETE BELOW LINE - used for updating downstream goimports
# vendored libraries
Provides: bundled(golang(github.com/containers/common/pkg/auth))
Provides: bundled(golang(github.com/containers/common/pkg/flag))
Provides: bundled(golang(github.com/containers/common/pkg/report))
Provides: bundled(golang(github.com/containers/common/pkg/retry))
Provides: bundled(golang(github.com/containers/image/v5/copy))
Provides: bundled(golang(github.com/containers/image/v5/directory))
Provides: bundled(golang(github.com/containers/image/v5/docker))
Provides: bundled(golang(github.com/containers/image/v5/docker/archive))
Provides: bundled(golang(github.com/containers/image/v5/docker/reference))
Provides: bundled(golang(github.com/containers/image/v5/image))
Provides: bundled(golang(github.com/containers/image/v5/manifest))
Provides: bundled(golang(github.com/containers/image/v5/oci/layout))
Provides: bundled(golang(github.com/containers/image/v5/pkg/blobinfocache))
Provides: bundled(golang(github.com/containers/image/v5/pkg/cli))
Provides: bundled(golang(github.com/containers/image/v5/pkg/cli/sigstore))
Provides: bundled(golang(github.com/containers/image/v5/pkg/compression))
Provides: bundled(golang(github.com/containers/image/v5/signature))
Provides: bundled(golang(github.com/containers/image/v5/signature/signer))
Provides: bundled(golang(github.com/containers/image/v5/signature/sigstore))
Provides: bundled(golang(github.com/containers/image/v5/transports))
Provides: bundled(golang(github.com/containers/image/v5/transports/alltransports))
Provides: bundled(golang(github.com/containers/image/v5/types))
Provides: bundled(golang(github.com/containers/ocicrypt/config))
Provides: bundled(golang(github.com/containers/ocicrypt/helpers))
Provides: bundled(golang(github.com/containers/storage/pkg/homedir))
Provides: bundled(golang(github.com/containers/storage/pkg/reexec))
Provides: bundled(golang(github.com/containers/storage/pkg/unshare))
Provides: bundled(golang(github.com/docker/distribution/registry/api/errcode))
Provides: bundled(golang(github.com/docker/distribution/registry/api/v2))
Provides: bundled(golang(github.com/opencontainers/go-digest))
Provides: bundled(golang(github.com/opencontainers/image-spec/specs-go/v1))
Provides: bundled(golang(github.com/sirupsen/logrus))
Provides: bundled(golang(github.com/spf13/cobra))
Provides: bundled(golang(github.com/spf13/pflag))
Provides: bundled(golang(github.com/stretchr/testify/assert))
Provides: bundled(golang(github.com/stretchr/testify/require))
Provides: bundled(golang(github.com/syndtr/gocapability/capability))
Provides: bundled(golang(golang.org/x/exp/maps))
Provides: bundled(golang(golang.org/x/exp/slices))
Provides: bundled(golang(golang.org/x/term))
Provides: bundled(golang(gopkg.in/yaml.v3))

%description
Command line utility to inspect images and repositories directly on Docker
registries without the need to pull them

%package tests
Summary: Tests for %{name}

Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: bats
Requires: gnupg
Requires: jq
Requires: golang
Requires: podman
Requires: crun
Requires: httpd-tools
Requires: openssl
Requires: fakeroot
Requires: squashfs-tools

%description tests
%{summary}

This package contains system tests for %{name}

%prep
%autosetup -Sgit %{name}-%{version}
# The %%install stage should not rebuild anything but only install what's
# built in the %%build stage. So, remove any dependency on build targets.
sed -i 's/^install-binary: bin\/%{name}.*/install-binary:/' Makefile
sed -i 's/^completions: bin\/%{name}.*/completions:/' Makefile
sed -i 's/^install-docs: docs.*/install-docs:/' Makefile

%build
%set_build_flags
export CGO_CFLAGS=$CFLAGS

# These extra flags present in $CFLAGS have been skipped for now as they break the build
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')

%ifarch x86_64
export CGO_CFLAGS="$CGO_CFLAGS -m64 -mtune=generic -fcf-protection=full"
%endif

BASEBUILDTAGS="$(hack/libdm_tag.sh) $(hack/libsubid_tag.sh)"
%if %{defined build_with_btrfs}
export BUILDTAGS="$BASEBUILDTAGS $(hack/btrfs_tag.sh) $(hack/btrfs_installed_tag.sh)"
%else
export BUILDTAGS="$BASEBUILDTAGS btrfs_noversion exclude_graphdriver_btrfs"
%endif

# unset LDFLAGS earlier set from set_build_flags
LDFLAGS=''

%gobuild -o bin/%{name} ./cmd/%{name}
%{__make} docs

%install
make \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    install-binary install-docs install-completions

# system tests
install -d -p %{buildroot}/%{_datadir}/%{name}/test/system
cp -pav systemtest/* %{buildroot}/%{_datadir}/%{name}/test/system/

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
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%files tests
%license LICENSE
%{_datadir}/%{name}/test

%changelog
%if %{defined autochangelog}
%autochangelog
%else
# NOTE: This changelog will be visible on CentOS 8 Stream builds
# Other envs are capable of handling autochangelog
* Tue Jun 13 2023 RH Container Bot <rhcontainerbot@fedoraproject.org>
- Placeholder changelog for envs that are not autochangelog-ready.
- Contact upstream if you need to report an issue with the build.
%endif
