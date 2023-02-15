%if 0%{?fedora} || 0%{?rhel} == 6
%global with_debug 0
%global with_check 1
%else
%global with_debug 0
%global with_check 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         estesp
%global repo            manifest-tool
# https://github.com/estesp/manifest-tool
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit         a28af2b6bf3748859149bf161eb0630e677c3906
%global shortcommit    %(c=%{commit}; echo ${c:0:7})

Name:           manifest-tool
Version:        2.0.3
Release:        6%{?dist}
#Release:        5.git{shortcommit}{?dist}
Summary:        A command line tool used for creating manifest list objects
License:        Apache-2.0
URL:            https://%{provider_prefix}
#Source:         https://{provider_prefix}/archive/{commit}/{repo}-{shortcommit}.tar.gz
Source:         https://%{provider_prefix}/%{repo}-%{version}.tar.gz
Patch0:         go-mod.patch

ExclusiveArch:  x86_64 aarch64 ppc64le s390x
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  git make
Provides:       %{repo} = %{version}-%{release}
Provides:       bundled(golang(# github.com/Azure/go-ansiterm))
Provides:       bundled(golang(github.com/Azure/go-ansiterm))
Provides:       bundled(golang(github.com/Azure/go-ansiterm/winterm))
Provides:       bundled(golang(github.com/Microsoft/go-winio))
Provides:       bundled(golang(github.com/Microsoft/go-winio/pkg/guid))
Provides:       bundled(golang(github.com/Microsoft/hcsshim/osversion))
Provides:       bundled(golang(github.com/beorn7/perks/quantile))
Provides:       bundled(golang(github.com/containerd/containerd/archive/compression))
Provides:       bundled(golang(github.com/containerd/containerd/content))
Provides:       bundled(golang(github.com/containerd/containerd/content/local))
Provides:       bundled(golang(github.com/containerd/containerd/errdefs))
Provides:       bundled(golang(github.com/containerd/containerd/filters))
Provides:       bundled(golang(github.com/containerd/containerd/images))
Provides:       bundled(golang(github.com/containerd/containerd/labels))
Provides:       bundled(golang(github.com/containerd/containerd/log))
Provides:       bundled(golang(github.com/containerd/containerd/platforms))
Provides:       bundled(golang(github.com/containerd/containerd/reference))
Provides:       bundled(golang(github.com/containerd/containerd/remotes))
Provides:       bundled(golang(github.com/containerd/containerd/remotes/docker))
Provides:       bundled(golang(github.com/containerd/containerd/remotes/docker/auth))
Provides:       bundled(golang(github.com/containerd/containerd/remotes/docker/schema1))
Provides:       bundled(golang(github.com/containerd/containerd/remotes/errors))
Provides:       bundled(golang(github.com/containerd/containerd/version))
Provides:       bundled(golang(github.com/containerd/continuity/pathdriver))
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2/md2man))
Provides:       bundled(golang(github.com/deislabs/oras/pkg/auth))
Provides:       bundled(golang(github.com/deislabs/oras/pkg/auth/docker))
Provides:       bundled(golang(github.com/deislabs/oras/pkg/content))
Provides:       bundled(golang(github.com/docker/cli/cli/config))
Provides:       bundled(golang(github.com/docker/cli/cli/config/configfile))
Provides:       bundled(golang(github.com/docker/cli/cli/config/credentials))
Provides:       bundled(golang(github.com/docker/cli/cli/config/types))
Provides:       bundled(golang(github.com/docker/distribution))
Provides:       bundled(golang(github.com/docker/distribution/digestset))
Provides:       bundled(golang(github.com/docker/distribution/manifest))
Provides:       bundled(golang(github.com/docker/distribution/manifest/manifestlist))
Provides:       bundled(golang(github.com/docker/distribution/metrics))
Provides:       bundled(golang(github.com/docker/distribution/reference))
Provides:       bundled(golang(github.com/docker/distribution/registry/api/errcode))
Provides:       bundled(golang(github.com/docker/distribution/registry/api/v2))
Provides:       bundled(golang(github.com/docker/distribution/registry/client))
Provides:       bundled(golang(github.com/docker/distribution/registry/client/auth))
Provides:       bundled(golang(github.com/docker/distribution/registry/client/auth/challenge))
Provides:       bundled(golang(github.com/docker/distribution/registry/client/transport))
Provides:       bundled(golang(github.com/docker/distribution/registry/storage/cache))
Provides:       bundled(golang(github.com/docker/distribution/registry/storage/cache/memory))
Provides:       bundled(golang(github.com/docker/docker/api/types))
Provides:       bundled(golang(github.com/docker/docker/api/types/blkiodev))
Provides:       bundled(golang(github.com/docker/docker/api/types/container))
Provides:       bundled(golang(github.com/docker/docker/api/types/filters))
Provides:       bundled(golang(github.com/docker/docker/api/types/mount))
Provides:       bundled(golang(github.com/docker/docker/api/types/network))
Provides:       bundled(golang(github.com/docker/docker/api/types/registry))
Provides:       bundled(golang(github.com/docker/docker/api/types/strslice))
Provides:       bundled(golang(github.com/docker/docker/api/types/swarm))
Provides:       bundled(golang(github.com/docker/docker/api/types/swarm/runtime))
Provides:       bundled(golang(github.com/docker/docker/api/types/versions))
Provides:       bundled(golang(github.com/docker/docker/cli/config))
Provides:       bundled(golang(github.com/docker/docker/errdefs))
Provides:       bundled(golang(github.com/docker/docker/pkg/homedir))
Provides:       bundled(golang(github.com/docker/docker/pkg/idtools))
Provides:       bundled(golang(github.com/docker/docker/pkg/ioutils))
Provides:       bundled(golang(github.com/docker/docker/pkg/jsonmessage))
Provides:       bundled(golang(github.com/docker/docker/pkg/longpath))
Provides:       bundled(golang(github.com/docker/docker/pkg/mount))
Provides:       bundled(golang(github.com/docker/docker/pkg/stringid))
Provides:       bundled(golang(github.com/docker/docker/pkg/system))
Provides:       bundled(golang(github.com/docker/docker/pkg/tarsum))
Provides:       bundled(golang(github.com/docker/docker/pkg/term))
Provides:       bundled(golang(github.com/docker/docker/pkg/term/windows))
Provides:       bundled(golang(github.com/docker/docker/registry))
Provides:       bundled(golang(github.com/docker/docker/registry/resumable))
Provides:       bundled(golang(github.com/docker/docker-credential-helpers/client))
Provides:       bundled(golang(github.com/docker/docker-credential-helpers/credentials))
Provides:       bundled(golang(github.com/docker/go-connections/nat))
Provides:       bundled(golang(github.com/docker/go-connections/sockets))
Provides:       bundled(golang(github.com/docker/go-connections/tlsconfig))
Provides:       bundled(golang(github.com/docker/go-metrics))
Provides:       bundled(golang(github.com/docker/go-units))
Provides:       bundled(golang(github.com/fatih/color))
Provides:       bundled(golang(github.com/gogo/protobuf/proto))
Provides:       bundled(golang(github.com/golang/protobuf/proto))
Provides:       bundled(golang(github.com/golang/protobuf/ptypes))
Provides:       bundled(golang(github.com/golang/protobuf/ptypes/any))
Provides:       bundled(golang(github.com/golang/protobuf/ptypes/duration))
Provides:       bundled(golang(github.com/golang/protobuf/ptypes/timestamp))
Provides:       bundled(golang(github.com/gorilla/mux))
Provides:       bundled(golang(github.com/klauspost/compress/fse))
Provides:       bundled(golang(github.com/klauspost/compress/huff0))
Provides:       bundled(golang(github.com/klauspost/compress/snappy))
Provides:       bundled(golang(github.com/klauspost/compress/zstd))
Provides:       bundled(golang(github.com/klauspost/compress/zstd/internal/xxhash))
Provides:       bundled(golang(github.com/mattn/go-colorable))
Provides:       bundled(golang(github.com/mattn/go-isatty))
Provides:       bundled(golang(github.com/matttproud/golang_protobuf_extensions/pbutil))
Provides:       bundled(golang(github.com/moby/locker))
Provides:       bundled(golang(github.com/morikuni/aec))
Provides:       bundled(golang(github.com/opencontainers/go-digest))
Provides:       bundled(golang(github.com/opencontainers/image-spec/specs-go))
Provides:       bundled(golang(github.com/opencontainers/image-spec/specs-go/v1))
Provides:       bundled(golang(github.com/opencontainers/runc/libcontainer/user))
Provides:       bundled(golang(github.com/pkg/errors))
Provides:       bundled(golang(github.com/prometheus/client_golang/prometheus))
Provides:       bundled(golang(github.com/prometheus/client_golang/prometheus/internal))
Provides:       bundled(golang(github.com/prometheus/client_golang/prometheus/promhttp))
Provides:       bundled(golang(github.com/prometheus/client_model/go))
Provides:       bundled(golang(github.com/prometheus/common/expfmt))
Provides:       bundled(golang(github.com/prometheus/common/internal/bitbucket.org/ww/goautoneg))
Provides:       bundled(golang(github.com/prometheus/common/model))
Provides:       bundled(golang(github.com/prometheus/procfs))
Provides:       bundled(golang(github.com/prometheus/procfs/internal/fs))
Provides:       bundled(golang(github.com/prometheus/procfs/internal/util))
Provides:       bundled(golang(github.com/russross/blackfriday/v2))
Provides:       bundled(golang(github.com/shurcooL/sanitized_anchor_name))
Provides:       bundled(golang(github.com/sirupsen/logrus))
Provides:       bundled(golang(github.com/urfave/cli))
Provides:       bundled(golang(golang.org/x/net/context/ctxhttp))
Provides:       bundled(golang(golang.org/x/sync/errgroup))
Provides:       bundled(golang(golang.org/x/sync/semaphore))
Provides:       bundled(golang(golang.org/x/sys/internal/unsafeheader))
Provides:       bundled(golang(golang.org/x/sys/unix))
Provides:       bundled(golang(golang.org/x/sys/windows))
Provides:       bundled(golang(google.golang.org/genproto/googleapis/rpc/status))
Provides:       bundled(golang(google.golang.org/grpc/codes))
Provides:       bundled(golang(google.golang.org/grpc/internal/status))
Provides:       bundled(golang(google.golang.org/grpc/status))
Provides:       bundled(golang(google.golang.org/protobuf/encoding/prototext))
Provides:       bundled(golang(google.golang.org/protobuf/encoding/protowire))
Provides:       bundled(golang(google.golang.org/protobuf/internal/descfmt))
Provides:       bundled(golang(google.golang.org/protobuf/internal/descopts))
Provides:       bundled(golang(google.golang.org/protobuf/internal/detrand))
Provides:       bundled(golang(google.golang.org/protobuf/internal/encoding/defval))
Provides:       bundled(golang(google.golang.org/protobuf/internal/encoding/messageset))
Provides:       bundled(golang(google.golang.org/protobuf/internal/encoding/tag))
Provides:       bundled(golang(google.golang.org/protobuf/internal/encoding/text))
Provides:       bundled(golang(google.golang.org/protobuf/internal/errors))
Provides:       bundled(golang(google.golang.org/protobuf/internal/filedesc))
Provides:       bundled(golang(google.golang.org/protobuf/internal/filetype))
Provides:       bundled(golang(google.golang.org/protobuf/internal/flags))
Provides:       bundled(golang(google.golang.org/protobuf/internal/genid))
Provides:       bundled(golang(google.golang.org/protobuf/internal/impl))
Provides:       bundled(golang(google.golang.org/protobuf/internal/order))
Provides:       bundled(golang(google.golang.org/protobuf/internal/pragma))
Provides:       bundled(golang(google.golang.org/protobuf/internal/set))
Provides:       bundled(golang(google.golang.org/protobuf/internal/strs))
Provides:       bundled(golang(google.golang.org/protobuf/internal/version))
Provides:       bundled(golang(google.golang.org/protobuf/proto))
Provides:       bundled(golang(google.golang.org/protobuf/reflect/protodesc))
Provides:       bundled(golang(google.golang.org/protobuf/reflect/protoreflect))
Provides:       bundled(golang(google.golang.org/protobuf/reflect/protoregistry))
Provides:       bundled(golang(google.golang.org/protobuf/runtime/protoiface))
Provides:       bundled(golang(google.golang.org/protobuf/runtime/protoimpl))
Provides:       bundled(golang(google.golang.org/protobuf/types/descriptorpb))
Provides:       bundled(golang(google.golang.org/protobuf/types/known/anypb))
Provides:       bundled(golang(google.golang.org/protobuf/types/known/durationpb))
Provides:       bundled(golang(google.golang.org/protobuf/types/known/timestamppb))
Provides:       bundled(golang(gopkg.in/yaml.v2))

%description
This tool was mainly created for the purpose of viewing, creating, and
pushing the new manifests list object type in the Docker registry. Manifest
lists are defined in the v2.2 image specification and exist mainly for the
purpose of supporting multi-architecture and/or multi-platform images within
a Docker registry.

%prep
#autosetup -Sgit -n {name}-{commit}
%autosetup -n %{name}-%{version}
#patch0 -p1

%build
mkdir _build
pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s $(dirs +1 -l) src/%{import_path}
popd

export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
make binary

%install
export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
make DESTDIR=%{buildroot} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Mon Feb 13 2023 Josh Boyer <jwboyer@fedoraproject.org> - 2.0.3-6
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 2.0.3-3
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.3-2
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Wed Mar 23 2022 Josh Boyer <jwboyer@fedoraproject.org> - 2.0.3-1
- New upstream release (RhBug 2064713)

* Tue Feb 15 2022 Josh Boyer <jwboyer@fedoraproject.org> - 2.0.0-1
- New upstream release (RhBug 2054676)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.3-3
- Adjust for go 1.16 temporarily

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 release

* Mon Mar 09 2020 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.rc2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.rc2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 22 2019 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.0-0.rc2
- Update to 1.0.0-rc2 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Josh Boyer <jwboyer@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0 upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5.gita28af2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4.gita28af2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Josh Boyer <jwboyer@fedoraproject.org> 0.6.0-3.gita28af2b
- Add bundled provides (rhbz 1467322)

* Wed Jul 05 2017 Josh Boyer <jwboyer@fedoraproject.org> 0.6.0-2.gita28af2b
- Cleanup with_bundled and license macro definitions (rhbz 1467322)

* Sun Jul 02 2017 Josh Boyer <jwboyer@fedoraproject.org> 0.6.0-1.gita28af2b
- Initial package for manifest-tool
