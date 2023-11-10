%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider github
%global provider_tld com
%global project buildpacks
%global repo pack
# https://github.com/buildpacks/pack
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}

%global built_tag v0.32.0
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: %{repo}
Version: %{gen_version}
%if 0%{?fedora} || 0%{?rhel} >= 9
Release: %autorelease
%else
Release: 1%{?dist}
%endif
Summary: Convert code into runnable images
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and MIT
URL: %{git0}
## On the upstream repo, run:
# git checkout %%{built_tag} && go mod vendor && git add vendor/* && \
# git commit -asm 'add vendor' && \                                                                  
# git archive --prefix=%%{name}-%%{version}/ -o %%{built_tag}-vendor.tar.gz HEAD
Source0: %{built_tag}-vendor.tar.gz
BuildRequires: golang
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: go-rpm-macros
%endif
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: glibc-static
BuildRequires: make
Provides: %{name}cli = %{version}-%{release}
Provides: %{name}-cli = %{version}-%{release}
# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/Azure/azure_sdk_for_go)) = v68.0.0+incompatible
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20210617225240_d185dfc1b5a1
Provides: bundled(golang(github.com/Azure/go_autorest)) = v14.2.0+incompatible
Provides: bundled(golang(github.com/Azure/go_autorest/autorest)) = v0.11.28
Provides: bundled(golang(github.com/Azure/go_autorest/autorest/adal)) = v0.9.22
Provides: bundled(golang(github.com/Azure/go_autorest/autorest/azure/auth)) = v0.5.12
Provides: bundled(golang(github.com/Azure/go_autorest/autorest/azure/cli)) = v0.4.6
Provides: bundled(golang(github.com/Azure/go_autorest/autorest/date)) = v0.3.0
Provides: bundled(golang(github.com/Azure/go_autorest/logger)) = v0.2.1
Provides: bundled(golang(github.com/Azure/go_autorest/tracing)) = v0.6.0
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.2.1
Provides: bundled(golang(github.com/Masterminds/semver)) = v1.5.0
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.6.0
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.9.6
Provides: bundled(golang(github.com/ProtonMail/go_crypto)) = v0.0.0_20221026131551_cf6655e29de4
Provides: bundled(golang(github.com/acomagu/bufpipe)) = v1.0.3
Provides: bundled(golang(github.com/apex/log)) = v1.9.0
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2)) = v1.17.3
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/config)) = v1.18.9
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/credentials)) = v1.13.9
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/feature/ec2/imds)) = v1.12.21
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/internal/configsources)) = v1.1.27
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/internal/endpoints/v2)) = v2.4.21
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/internal/ini)) = v1.3.28
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/service/ecr)) = v1.18.1
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/service/ecrpublic)) = v1.15.0
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/service/internal/presigned_url)) = v1.9.21
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/service/sso)) = v1.12.0
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/service/ssooidc)) = v1.14.0
Provides: bundled(golang(github.com/aws/aws_sdk_go_v2/service/sts)) = v1.18.1
Provides: bundled(golang(github.com/aws/smithy_go)) = v1.13.5
Provides: bundled(golang(github.com/awslabs/amazon_ecr_credential_helper/ecr_login)) = v0.0.0_20230110223219_40efa3093a22
Provides: bundled(golang(github.com/buildpacks/imgutil)) = v0.0.0_20230120191822_4d50b9a7e215
Provides: bundled(golang(github.com/buildpacks/lifecycle)) = v0.16.0
Provides: bundled(golang(github.com/chrismellard/docker_credential_acr_env)) = v0.0.0_20221129204813_6a4d6ed5d396
Provides: bundled(golang(github.com/cloudflare/circl)) = v1.1.0
Provides: bundled(golang(github.com/containerd/cgroups)) = v1.0.4
Provides: bundled(golang(github.com/containerd/containerd)) = v1.6.18
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.13.0
Provides: bundled(golang(github.com/containerd/typeurl)) = v1.0.2
Provides: bundled(golang(github.com/dimchansky/utfbom)) = v1.1.1
Provides: bundled(golang(github.com/docker/cli)) = v23.0.1+incompatible
Provides: bundled(golang(github.com/docker/distribution)) = v2.8.1+incompatible
Provides: bundled(golang(github.com/docker/docker)) = v20.10.23+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.7.0
Provides: bundled(golang(github.com/docker/go_connections)) = v0.4.0
Provides: bundled(golang(github.com/docker/go_units)) = v0.5.0
Provides: bundled(golang(github.com/dustin/go_humanize)) = v1.0.1
Provides: bundled(golang(github.com/emirpasic/gods)) = v1.18.1
Provides: bundled(golang(github.com/gdamore/encoding)) = v1.0.0
Provides: bundled(golang(github.com/gdamore/tcell/v2)) = v2.6.0
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
Provides: bundled(golang(github.com/go_git/gcfg)) = v1.5.0
Provides: bundled(golang(github.com/go_git/go_billy/v5)) = v5.4.0
Provides: bundled(golang(github.com/go_git/go_git/v5)) = v5.6.0
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang_jwt/jwt/v4)) = v4.4.3
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20210331224755_41bb18bfe9da
Provides: bundled(golang(github.com/golang/mock)) = v1.6.0
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.2
Provides: bundled(golang(github.com/google/go_cmp)) = v0.5.9
Provides: bundled(golang(github.com/google/go_containerregistry)) = v0.13.0
Provides: bundled(golang(github.com/google/go_github/v30)) = v30.1.0
Provides: bundled(golang(github.com/google/go_querystring)) = v1.0.0
Provides: bundled(golang(github.com/google/uuid)) = v1.3.0
Provides: bundled(golang(github.com/hectane/go_acl)) = v0.0.0_20190604041725_da78bae5fc95
Provides: bundled(golang(github.com/heroku/color)) = v0.0.6
Provides: bundled(golang(github.com/imdario/mergo)) = v0.3.13
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.0.1
Provides: bundled(golang(github.com/jbenet/go_context)) = v0.0.0_20150711004518_d14ea06fba99
Provides: bundled(golang(github.com/jmespath/go_jmespath)) = v0.4.0
Provides: bundled(golang(github.com/kevinburke/ssh_config)) = v1.2.0
Provides: bundled(golang(github.com/klauspost/compress)) = v1.15.15
Provides: bundled(golang(github.com/lucasb_eyer/go_colorful)) = v1.2.0
Provides: bundled(golang(github.com/mattn/go_colorable)) = v0.1.13
Provides: bundled(golang(github.com/mattn/go_isatty)) = v0.0.17
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.14
Provides: bundled(golang(github.com/mitchellh/go_homedir)) = v1.1.0
Provides: bundled(golang(github.com/mitchellh/ioprogress)) = v0.0.0_20180201004757_6a23b12fa88e
Provides: bundled(golang(github.com/moby/buildkit)) = v0.11.1
Provides: bundled(golang(github.com/moby/sys/mount)) = v0.3.3
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.6.2
Provides: bundled(golang(github.com/moby/term)) = v0.0.0_20221205130635_1aeaba878587
Provides: bundled(golang(github.com/morikuni/aec)) = v1.0.0
Provides: bundled(golang(github.com/onsi/gomega)) = v1.27.2
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.1.0_rc2
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.1.4
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.10.2
Provides: bundled(golang(github.com/pelletier/go_toml)) = v1.9.5
Provides: bundled(golang(github.com/pjbgf/sha1cd)) = v0.3.0
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/rivo/tview)) = v0.0.0_20220307222120_9994674d60a8
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.4.3
Provides: bundled(golang(github.com/sabhiram/go_gitignore)) = v0.0.0_20210923224102_525f6e181f06
Provides: bundled(golang(github.com/sclevine/spec)) = v1.4.0
Provides: bundled(golang(github.com/sergi/go_diff)) = v1.2.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.9.0
Provides: bundled(golang(github.com/skeema/knownhosts)) = v1.1.0
Provides: bundled(golang(github.com/spf13/cobra)) = v1.6.1
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.2
Provides: bundled(golang(github.com/xanzy/ssh_agent)) = v0.3.3

%description
%{name} is a CLI implementation of the Platform Interface Specification
for Cloud Native Buildpacks.

%prep
%autosetup -Sgit -n %{name}-%{gen_version}

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

mkdir _build
export GOPATH=$(pwd)/_build:$(pwd)

pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path}
popd
ln -s vendor src

%if 0%{?rhel} <= 8
# handled automatically in %%gobuild for fedora and epel9
export GO111MODULE=off
%endif

%gobuild -o out/%{name} %{import_path}/cmd/%{name}

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
%if 0%{?fedora} || 0%{?rhel} >= 9
%autochangelog
%endif
