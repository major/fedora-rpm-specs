%if "%{_vendor}" == "debbuild"
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -tags=" ${BUILDTAGS:-}" -a -v -x %{?**};
%endif

%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%if 0%{?fedora} && ! 0%{?rhel}
%define conditional_epoch 1
%else
%define conditional_epoch 2
%endif

%global provider github
%global provider_tld com
%global project containers
%global repo skopeo
# https://github.com/containers/skopeo
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}

%global built_tag_strip 1.9.2

Name: %{repo}
Epoch: %{conditional_epoch}
Version: 1.9.2
%if "%{_vendor}" == "debbuild"
Packager: Podman Debbuild Maintainers <https://github.com/orgs/containers/teams/podman-debbuild-maintainers>
License: ASL-2.0+
Release: 0%{?dist}
%else
License: ASL 2.0 and BSD and ISC and MIT
Release: %autorelease
%endif
Summary: Inspect container images and repositories on registries
URL: %{git0}
Source0: %{git0}/archive/v%{built_tag_strip}.tar.gz
BuildRequires: go-md2man
%if "%{_vendor}" == "debbuild"
BuildRequires: git
BuildRequires: golang >= 1.18
BuildRequires: libassuan-dev
BuildRequires: libbtrfs-dev
BuildRequires: libglib2.0-dev
BuildRequires: libgpgme-dev
BuildRequires: pkg-config
BuildRequires: libdevmapper-dev
Requires: containers-common >= 4:1
%else
ExclusiveArch: %{go_arches}
BuildRequires: btrfs-progs-devel
BuildRequires: git-core
BuildRequires: golang >= 1.16.6
BuildRequires: go-rpm-macros
BuildRequires: gpgme-devel
BuildRequires: libassuan-devel
BuildRequires: pkgconfig(devmapper)
BuildRequires: ostree-devel
BuildRequires: glib2-devel
BuildRequires: make
Requires: containers-common >= 4:1-21
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
# vendored provides
Provides: bundled(golang(github.com/containers/common)) = v0.47.3
Provides: bundled(golang(github.com/containers/image/v5)) = v5.19.1
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.2
Provides: bundled(golang(github.com/containers/storage)) = v1.38.2
Provides: bundled(golang(github.com/docker/docker)) = v20.10.12+incompatible
Provides: bundled(golang(github.com/dsnet/compress)) = v0.0.2_0.20210315054119_f66993602bf5
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.0.3_0.20211202193544_a5463b7f9c84
Provides: bundled(golang(github.com/opencontainers/image_tools)) = v1.0.0_rc3
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/russross/blackfriday)) = v2.0.0+incompatible
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/spf13/cobra)) = v1.3.0
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stretchr/testify)) = v1.7.0
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
%endif

%description
Command line utility to inspect images and repositories directly on Docker
registries without the need to pull them

%package tests
Summary: Tests for %{name}

Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: bats
Requires: gnupg
Requires: jq
Requires: podman
Requires: httpd-tools
Requires: openssl
Requires: fakeroot
Requires: squashfs-tools

%description tests
%{summary}

This package contains system tests for %{name}

%prep
%autosetup -Sgit %{name}-%{built_tag_strip}
sed -i 's/install-binary: bin\/%{name}/install-binary:/' Makefile
sed -i 's/completions: bin\/%{name}/completions:/' Makefile
sed -i 's/install-docs: docs/install-docs:/' Makefile

%build
%if "%{_vendor}" != "debbuild"
%set_build_flags
# These extra flags present in $CFLAGS have been skipped for now as they break the build
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')

%ifarch x86_64
export CGO_CFLAGS="$CGO_CFLAGS -m64 -mtune=generic -fcf-protection=full"
%endif
%endif

export GOPATH=$(pwd)/_build:$(pwd)
export CGO_CFLAGS=$CFLAGS

# unset LDFLAGS earlier set from set_build_flags
LDFLAGS=''

mkdir _build
cd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path}
cd ..

mv vendor src

%gobuild -o bin/%{name} %{import_path}/cmd/%{name}
%{__make} docs

%install
make \
    PREFIX=%{buildroot}%{_prefix} \
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
%if "%{_vendor}" != "debbuild"
%autochangelog
%endif
