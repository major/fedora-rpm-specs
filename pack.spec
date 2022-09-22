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

%global built_tag_strip 0.27.0

Name: %{repo}
Version: 0.27.0
%if 0%{?fedora} || 0%{?rhel} >= 9
Release: %autorelease
%else
Release: 1%{?dist}
%endif
Summary: Convert code into runnable images
License: ASL 2.0 and BSD and ISC and MIT
URL: %{git0}
Source0: v%{built_tag_strip}-vendor.tar.gz
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
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20210617225240_d185dfc1b5a1
Provides: bundled(golang(github.com/BurntSushi/toml)) = v1.0.0
Provides: bundled(golang(github.com/Masterminds/semver)) = v1.5.0
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.5.1
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.8.23
Provides: bundled(golang(github.com/apex/log)) = v1.9.0
Provides: bundled(golang(github.com/bits_and_blooms/bitset)) = v1.2.0
Provides: bundled(golang(github.com/buildpacks/imgutil)) = v0.0.0_20211203200417_76206845baac
Provides: bundled(golang(github.com/buildpacks/lifecycle)) = v0.13.3
Provides: bundled(golang(github.com/containerd/cgroups)) = v1.0.1
Provides: bundled(golang(github.com/containerd/containerd)) = v1.5.8
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.10.1
Provides: bundled(golang(github.com/docker/cli)) = v20.10.12+incompatible
Provides: bundled(golang(github.com/docker/distribution)) = v2.7.1+incompatible
Provides: bundled(golang(github.com/docker/docker)) = v20.10.12+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.6.4
Provides: bundled(golang(github.com/docker/go_connections)) = v0.4.0
Provides: bundled(golang(github.com/docker/go_units)) = v0.4.0
Provides: bundled(golang(github.com/dustin/go_humanize)) = v1.0.0
Provides: bundled(golang(github.com/emirpasic/gods)) = v1.12.0
Provides: bundled(golang(github.com/gdamore/encoding)) = v1.0.0
Provides: bundled(golang(github.com/gdamore/tcell/v2)) = v2.4.0
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20210331224755_41bb18bfe9da
Provides: bundled(golang(github.com/golang/mock)) = v1.6.0
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.2
Provides: bundled(golang(github.com/google/go_cmp)) = v0.5.7
Provides: bundled(golang(github.com/google/go_containerregistry)) = v0.8.0
Provides: bundled(golang(github.com/google/go_github/v30)) = v30.1.0
Provides: bundled(golang(github.com/google/go_querystring)) = v1.0.0
Provides: bundled(golang(github.com/hectane/go_acl)) = v0.0.0_20190604041725_da78bae5fc95
Provides: bundled(golang(github.com/heroku/color)) = v0.0.6
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.0.0
Provides: bundled(golang(github.com/jbenet/go_context)) = v0.0.0_20150711004518_d14ea06fba99
Provides: bundled(golang(github.com/kevinburke/ssh_config)) = v0.0.0_20190725054713_01f96b0aa0cd
Provides: bundled(golang(github.com/klauspost/compress)) = v1.13.6
Provides: bundled(golang(github.com/lucasb_eyer/go_colorful)) = v1.2.0
Provides: bundled(golang(github.com/mattn/go_colorable)) = v0.1.12
Provides: bundled(golang(github.com/mattn/go_isatty)) = v0.0.14
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.10
Provides: bundled(golang(github.com/mitchellh/go_homedir)) = v1.1.0
Provides: bundled(golang(github.com/mitchellh/ioprogress)) = v0.0.0_20180201004757_6a23b12fa88e
Provides: bundled(golang(github.com/moby/sys/mount)) = v0.2.0
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.4.1
Provides: bundled(golang(github.com/moby/term)) = v0.0.0_20210619224110_3f7ff695adc6
Provides: bundled(golang(github.com/morikuni/aec)) = v1.0.0
Provides: bundled(golang(github.com/onsi/gomega)) = v1.18.1
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.0.2
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.0.2
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.8.2
Provides: bundled(golang(github.com/pelletier/go_toml)) = v1.9.4
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/rivo/tview)) = v0.0.0_20210624165335_29d673af0ce2
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.2.0
Provides: bundled(golang(github.com/sabhiram/go_gitignore)) = v0.0.0_20201211074657_223ce5d391b0
Provides: bundled(golang(github.com/sclevine/spec)) = v1.4.0
Provides: bundled(golang(github.com/sergi/go_diff)) = v1.1.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/spf13/cobra)) = v1.3.0
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/src_d/gcfg)) = v1.4.0
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.2
Provides: bundled(golang(github.com/xanzy/ssh_agent)) = v0.3.0

%description
%{name} is a CLI implementation of the Platform Interface Specification
for Cloud Native Buildpacks.

%prep
%autosetup -Sgit %{name}-%{built_tag_strip}

%build
export GOPATH=$(pwd)/_build:$(pwd)
mkdir _build
pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path}

#ln -s $(dirs +1 -l) src/%%{import_path}
popd
#mv vendor src
ln -s vendor src

%if 0%{?rhel} <= 8
# handled automatically in %%gobuild for fedora and epel9
export GO111MODULE=off
%endif
export CGO_CFLAGS="-O2 -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -ffat-lto-objects -fexceptions -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif
# These extra flags present in %%{optflags} have been skipped for now as they break the build
#export CGO_CFLAGS+=" -flto=auto -Wp,D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1"

%gobuild -o out/%{name} %{import_path}/cmd/%{name}

%install
export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
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
