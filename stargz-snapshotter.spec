%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider github
%global provider_tld com
%global project containerd
%global repo stargz-snapshotter
# https://github.com/containerd/stargz-snapshotter
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}

%global built_tag v0.14.2
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: %{repo}
Version: %{gen_version}
Release: %autorelease
Summary: Fast container image distribution plugin with lazy pulling
License: ASL 2.0 and BSD and ISC and MIT and MPLv2.0
URL: %{git0}
## On the upstream repo, run:
# git checkout %%{built_tag} && cd cmd/ && go mod vendor && git add vendor/* && \
# cd .. && git archive --prefix=%%{name}-%%{version}/ -o %%{built_tag}-vendor.tar.gz HEAD
Source0: %{built_tag}-vendor.tar.gz
BuildRequires: golang
BuildRequires: go-rpm-macros
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: glibc-static
BuildRequires: make
BuildRequires: systemd-rpm-macros
# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/containerd/containerd)) = v1.6.1
Provides: bundled(golang(github.com/containerd/go_cni)) = v1.1.3
Provides: bundled(golang(github.com/containerd/stargz_snapshotter)) = v0.11.3
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.11.3
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/ipfs)) = v0.11.3
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.3.2
Provides: bundled(golang(github.com/docker/go_metrics)) = v0.0.1
Provides: bundled(golang(github.com/goccy/go_json)) = v0.9.5
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/ipfs/go_ipfs_http_client)) = v0.2.0
Provides: bundled(golang(github.com/ipfs/interface_go_ipfs_core)) = v0.5.2
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.0.2_0.20211117181255_693428a734f5
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20210326190908_1c3f411f0417
Provides: bundled(golang(github.com/pelletier/go_toml)) = v1.9.4
Provides: bundled(golang(github.com/rs/xid)) = v1.3.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/urfave/cli)) = v1.22.5
Provides: bundled(golang(k8s.io/cri_api)) = v0.24.0_alpha.3

%description
%{summary}

%prep
%autosetup -Sgit -n %{name}-%{built_tag_strip}

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
pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s $(dirs +1 -l) src/%{import_path}
popd

mv cmd/vendor src

export GOPATH=$(pwd)/_build:$(pwd)

%gobuild -o out/%{project}-stargz-grpc %{import_path}/cmd/%{project}-stargz-grpc
%gobuild -o out/ctr-remote %{import_path}/cmd/ctr-remote
%gobuild -o out/stargz-store %{import_path}/cmd/stargz-store

%install
export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
make CMD_DESTDIR=%{buildroot}%{_prefix} install
sed -i 's/\/local//' script/config-cri-o/etc/systemd/system/stargz-store.service
install -D -m 644 script/config-cri-o/etc/systemd/system/stargz-store.service %{buildroot}%{_unitdir}/stargz-store.service

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%post
%systemd_post stargz-store.service

%preun
%systemd_preun stargz-store.service

%postun
%systemd_postun stargz-store.service

%files
%license LICENSE
%doc NOTICE.md README.md docs/{ctr-remote,overview,stargz-estargz,verification}.md
%{_bindir}/%{project}-stargz-grpc
%{_bindir}/ctr-remote
%{_bindir}/stargz-store
%{_unitdir}/stargz-store.service

%changelog
%autochangelog
