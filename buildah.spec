%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if 0%{?rhel}
%bcond_with btrfs
%else
%bcond_without btrfs
%endif

%global provider github
%global provider_tld com
%global project containers
%global repo buildah
# https://github.com/containers/buildah
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}

%global built_tag v1.30.0
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: %{repo}
Version: %{gen_version}
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and MIT and MPL-2.0
Release: %autorelease
ExclusiveArch: %{golang_arches_future}
Summary: A command line tool used for creating OCI Images
URL: https://%{name}.io
# Tarball fetched from upstream
Source: %{git0}/archive/%{built_tag}.tar.gz
BuildRequires: go-md2man
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
%if %{with btrfs}
BuildRequires: btrfs-progs-devel
%endif
BuildRequires: shadow-utils-subid-devel
%if 0%{?fedora} > 37
Requires: containers-common-extra >= 4:1-78
%else
%if 0%{?fedora} == 37
Requires: containers-common-extra >= 4:1-73
%else
Requires: containers-common-extra >= 4:1-62
%endif
%endif
BuildRequires: libseccomp-static
Requires: libseccomp >= 2.4.1-0
Suggests: cpp
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20210617225240_d185dfc1b5a1
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.2.1
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.6.0
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.9.6
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0
Provides: bundled(golang(github.com/acarl005/stripansi)) = v0.0.0_20180116102854_5a71ef0e047d
Provides: bundled(golang(github.com/asaskevich/govalidator)) = v0.0.0_20210307081110_f21760c49a8d
Provides: bundled(golang(github.com/blang/semver/v4)) = v4.0.0
Provides: bundled(golang(github.com/chzyer/readline)) = v1.5.1
Provides: bundled(golang(github.com/container_orchestrated_devices/container_device_interface)) = v0.5.3
Provides: bundled(golang(github.com/containerd/cgroups)) = v1.0.4
Provides: bundled(golang(github.com/containerd/containerd)) = v1.6.15
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.13.0
Provides: bundled(golang(github.com/containernetworking/cni)) = v1.1.2
Provides: bundled(golang(github.com/containernetworking/plugins)) = v1.2.0
Provides: bundled(golang(github.com/containers/common)) = v0.51.0
Provides: bundled(golang(github.com/containers/image/v5)) = v5.24.0
Provides: bundled(golang(github.com/containers/libtrust)) = v0.0.0_20230121012942_c1716e8a8d01
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.7
Provides: bundled(golang(github.com/containers/storage)) = v1.45.3
Provides: bundled(golang(github.com/cyberphone/json_canonicalization)) = v0.0.0_20220623050100_57a0ce2678a7
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.2.3
Provides: bundled(golang(github.com/davecgh/go_spew)) = v1.1.1
Provides: bundled(golang(github.com/disiqueira/gotree/v3)) = v3.0.2
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.1+incompatible
Provides: bundled(golang(github.com/docker/docker)) = v20.10.23+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.7.0
Provides: bundled(golang(github.com/docker/go_connections)) = v0.4.1_0.20210727194412_58542c764a11
Provides: bundled(golang(github.com/docker/go_units)) = v0.5.0
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = v1.6.0
Provides: bundled(golang(github.com/fsouza/go_dockerclient)) = v1.9.3
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
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
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20210331224755_41bb18bfe9da
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.2
Provides: bundled(golang(github.com/google/go_cmp)) = v0.5.9
Provides: bundled(golang(github.com/google/go_containerregistry)) = v0.12.1
Provides: bundled(golang(github.com/google/go_intervals)) = v0.0.2
Provides: bundled(golang(github.com/google/uuid)) = v1.3.0
Provides: bundled(golang(github.com/gorilla/mux)) = v1.8.0
Provides: bundled(golang(github.com/hashicorp/errwrap)) = v1.1.0
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/imdario/mergo)) = v0.3.13
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.0.1
Provides: bundled(golang(github.com/jinzhu/copier)) = v0.3.5
Provides: bundled(golang(github.com/josharian/intern)) = v1.0.0
Provides: bundled(golang(github.com/json_iterator/go)) = v1.1.12
Provides: bundled(golang(github.com/klauspost/compress)) = v1.15.15
Provides: bundled(golang(github.com/klauspost/pgzip)) = v1.2.6_0.20220930104621_17e8dac29df8
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
Provides: bundled(golang(github.com/ostreedev/ostree_go)) = v0.0.0_20210805093236_719684c64e4f
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/pmezard/go_difflib)) = v1.0.0
Provides: bundled(golang(github.com/proglottis/gpgme)) = v0.1.3
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.4.3
Provides: bundled(golang(github.com/seccomp/libseccomp_golang)) = v0.10.0
Provides: bundled(golang(github.com/sigstore/fulcio)) = v1.0.0
Provides: bundled(golang(github.com/sigstore/rekor)) = v1.0.1
Provides: bundled(golang(github.com/sigstore/sigstore)) = v1.5.1
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.0
Provides: bundled(golang(github.com/spf13/cobra)) = v1.6.1
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stefanberger/go_pkcs11uri)) = v0.0.0_20201008174630_78d3cae3a980
Provides: bundled(golang(github.com/stretchr/testify)) = v1.8.1
Provides: bundled(golang(github.com/sylabs/sif/v2)) = v2.9.0
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/tchap/go_patricia)) = v2.3.0+incompatible
Provides: bundled(golang(github.com/theupdateframework/go_tuf)) = v0.5.2_0.20221207161717_9cb61d6e65f5
Provides: bundled(golang(github.com/titanous/rocacheck)) = v0.0.0_20171023193734_afe73141d399
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.11
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.2
Provides: bundled(golang(github.com/vbauerster/mpb/v7)) = v7.5.3
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.2.1_beta.2
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.0_20210104183010_2eb08e3e575f
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0_20190905194746_02993c407bfb
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0_20180127040603_bd5ef7bd5415
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0
Provides: bundled(golang(k8s.io/klog)) = v1.0.0
Provides: bundled(golang(sigs.k8s.io/yaml)) = v1.3.0

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
%autosetup -Sgit -n %{name}-%{built_tag_strip}

%build
%set_build_flags
# These extra flags present in $CFLAGS have been skipped for now as they break the build
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')

%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
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
export BUILDTAGS+=' libsubid selinux'
%if %{without btrfs}
export BUILDTAGS+=' btrfs_noversion exclude_graphdriver_btrfs'
%endif
%gobuild -o bin/%{name} %{import_path}/cmd/%{name}
%gobuild -o bin/imgtype %{import_path}/tests/imgtype
%gobuild -o bin/copy %{import_path}/tests/copy
%gobuild -o bin/tutorial %{import_path}/tests/tutorial
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
%autochangelog
