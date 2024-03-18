%bcond_without check
%bcond_without bundled
%if 0%{?rhel}
%bcond_without bundled
%endif

%if %{defined rhel} && !%{defined eln}
%define gobuild(o:) go build -buildmode pie -compiler gc -tags="rpm_crashtraceback libtrust_openssl ${BUILDTAGS:-}" -ldflags "-linkmode=external -compressdwarf=false ${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags'" -a -v -x %{?**};
%endif

%if %{with bundled}
%global gomodulesmode   GO111MODULE=on
%endif

# https://github.com/containers/podman-tui
%global goipath github.com/containers/podman-tui
Version: 0.18.0
%gometa

%global goname podman-tui

%global common_description %{expand:
%{goname} is a terminal user interface for Podman v4.
%{goname} is using podman.socket service to communicate with podman environment
and SSH to connect to remote podman machines.
}

%global golicenses LICENSE
%global godocs CODE-OF-CONDUCT.md CONTRIBUTING.md README.md

%global godevelheader %{expand:
Requires:  %{name} = %{version}-%{release}
}

Name: %{goname}
Release: %autorelease
Summary: Podman Terminal User Interface

# License for dario.cat/mergo: BSD 3-Clause License
# License for github.com/Azure/go-ansiterm: MIT License
# License for github.com/Microsoft/go-winio: MIT License
# License for github.com/Microsoft/hcsshim: MIT License
# License for github.com/VividCortex/ewma: MIT License
# License for github.com/acarl005/stripansi: MIT License
# License for github.com/asaskevich/govalidator: MIT License
# License for github.com/blang/semver/v4: MIT License
# License for github.com/chzyer/readline: MIT License
# License for github.com/container-orchestrated-devices/container-device-interface: Apache License 2.0
# License for github.com/containerd/cgroups/v3: Apache License 2.0
# License for github.com/containerd/containerd: Apache License 2.0
# License for github.com/containerd/stargz-snapshotter/estargz: Apache License 2.0
# License for github.com/containers/buildah: Apache License 2.0
# License for github.com/containers/common: Apache License 2.0
# License for github.com/containers/image/v5: Apache License 2.0
# License for github.com/containers/libtrust: Apache License 2.0
# License for github.com/containers/ocicrypt: Apache License 2.0
# License for github.com/containers/podman/v4: Apache License 2.0
# License for github.com/containers/psgo: Apache License 2.0
# License for github.com/containers/storage: Apache License 2.0
# License for github.com/coreos/go-systemd/v22: Apache License 2.0
# License for github.com/cyberphone/json-canonicalization: Apache License 2.0
# License for github.com/cyphar/filepath-securejoin: BSD 3-Clause License
# License for github.com/disiqueira/gotree/v3: MIT License
# License for github.com/distribution/reference: Apache License 2.0
# License for github.com/docker/distribution: Apache License 2.0
# License for github.com/docker/docker-credential-helpers: MIT License
# License for github.com/docker/docker: Apache License 2.0
# License for github.com/docker/go-connections: Apache License 2.0
# License for github.com/docker/go-units: Apache License 2.0
# License for github.com/fsnotify/fsnotify: BSD 3-Clause License
# License for github.com/gdamore/encoding: Apache License 2.0
# License for github.com/gdamore/tcell/v2: Apache License 2.0
# License for github.com/go-jose/go-jose/v3: Apache License 2.0
# License for github.com/go-jose/go-jose/v3/json: BSD 3-Clause License
# License for github.com/go-logr/logr: Apache License 2.0
# License for github.com/go-openapi/analysis: Apache License 2.0
# License for github.com/go-openapi/errors: Apache License 2.0
# License for github.com/go-openapi/jsonpointer: Apache License 2.0
# License for github.com/go-openapi/jsonreference: Apache License 2.0
# License for github.com/go-openapi/loads: Apache License 2.0
# License for github.com/go-openapi/runtime: Apache License 2.0
# License for github.com/go-openapi/spec: Apache License 2.0
# License for github.com/go-openapi/strfmt: Apache License 2.0
# License for github.com/go-openapi/swag: Apache License 2.0
# License for github.com/go-openapi/validate: Apache License 2.0
# License for github.com/godbus/dbus/v5: BSD 2-Clause License
# License for github.com/gogo/protobuf: BSD 3-Clause License
# License for github.com/golang/groupcache: Apache License 2.0
# License for github.com/golang/protobuf: BSD 3-Clause License
# License for github.com/google/go-cmp: BSD 3-Clause License
# License for github.com/google/go-containerregistry: Apache License 2.0
# License for github.com/google/go-intervals: Apache License 2.0
# License for github.com/google/pprof: Apache License 2.0
# License for github.com/google/uuid: BSD 3-Clause License
# License for github.com/gorilla/mux: BSD 3-Clause License
# License for github.com/gorilla/schema: BSD 3-Clause License
# License for github.com/hashicorp/errwrap: Mozilla Public License 2.0
# License for github.com/hashicorp/go-multierror: Mozilla Public License 2.0
# License for github.com/hinshun/vt10x: UNKNOWN
# License for github.com/inconshreveable/mousetrap: Apache License 2.0
# License for github.com/json-iterator/go: MIT License
# License for github.com/klauspost/compress: Apache License 2.0 and/or BSD 3-Clause License
# License for github.com/klauspost/compress/internal/snapref: BSD 3-Clause License
# License for github.com/klauspost/pgzip/GO_LICENSE: BSD 3-Clause License
# License for github.com/klauspost/pgzip: MIT License
# License for github.com/kr/fs: BSD 3-Clause License
# License for github.com/lucasb-eyer/go-colorful: MIT License
# License for github.com/mailru/easyjson: MIT License
# License for github.com/manifoldco/promptui/LICENSE.md: BSD 3-Clause License
# License for github.com/mattn/go-colorable: MIT License
# License for github.com/mattn/go-isatty: MIT License
# License for github.com/mattn/go-runewidth: MIT License
# License for github.com/mattn/go-shellwords: MIT License
# License for github.com/mattn/go-sqlite3: MIT License
# License for github.com/miekg/pkcs11: BSD 3-Clause License
# License for github.com/mistifyio/go-zfs/v3: Apache License 2.0
# License for github.com/mitchellh/mapstructure: MIT License
# License for github.com/moby/sys/mountinfo: Apache License 2.0
# License for github.com/moby/term: Apache License 2.0
# License for github.com/modern-go/concurrent: Apache License 2.0
# License for github.com/modern-go/reflect2: Apache License 2.0
# License for github.com/navidys/tvxwidgets: MIT License
# License for github.com/nxadm/tail: MIT License
# License for github.com/oklog/ulid: Apache License 2.0
# License for github.com/onsi/ginkgo/v2: MIT License
# License for github.com/onsi/gomega: MIT License
# License for github.com/opencontainers/go-digest: Apache License 2.0
# License for github.com/opencontainers/image-spec: Apache License 2.0
# License for github.com/opencontainers/runc: Apache License 2.0
# License for github.com/opencontainers/runtime-spec: Apache License 2.0
# License for github.com/opencontainers/runtime-tools: Apache License 2.0
# License for github.com/opencontainers/selinux: Apache License 2.0
# License for github.com/ostreedev/ostree-go: ISC License
# License for github.com/pkg/errors: BSD 2-Clause License
# License for github.com/pkg/sftp: BSD 2-Clause License
# License for github.com/proglottis/gpgme: BSD 3-Clause License
# License for github.com/rs/zerolog: MIT License
# License for github.com/secure-systems-lab/go-securesystemslib: MIT License
# License for github.com/sigstore/fulcio: Apache License 2.0
# License for github.com/sigstore/rekor: Apache License 2.0
# License for github.com/sigstore/sigstore: Apache License 2.0
# License for github.com/sirupsen/logrus: MIT License
# License for github.com/spf13/pflag: BSD 3-Clause License
# License for github.com/stefanberger/go-pkcs11uri: Apache License 2.0
# License for github.com/sylabs/sif/v2/LICENSE.md: BSD 3-Clause License
# License for github.com/syndtr/gocapability: BSD 2-Clause License
# License for github.com/tchap/go-patricia/v2: MIT License
# License for github.com/theupdateframework/go-tuf: BSD 3-Clause License
# License for github.com/titanous/rocacheck: MIT License
# License for github.com/ulikunitz/xz: UNKNOWN
# License for github.com/vbatts/tar-split: BSD 3-Clause License
# License for github.com/vbauerster/mpb/v8/UNLICENSE: The Unlicense
# License for go.mongodb.org/mongo-driver: Apache License 2.0
# License for go.mozilla.org/pkcs7: MIT License
# License for go.opencensus.io: Apache License 2.0
# License for golang.org/x/crypto: BSD 3-Clause License
# License for golang.org/x/exp: BSD 3-Clause License
# License for golang.org/x/mod: BSD 3-Clause License
# License for golang.org/x/net: BSD 3-Clause License
# License for golang.org/x/sync: BSD 3-Clause License
# License for golang.org/x/sys: BSD 3-Clause License
# License for golang.org/x/term: BSD 3-Clause License
# License for golang.org/x/text: BSD 3-Clause License
# License for golang.org/x/tools: BSD 3-Clause License
# License for google.golang.org/genproto/googleapis/rpc: Apache License 2.0
# License for google.golang.org/grpc: Apache License 2.0
# License for google.golang.org/protobuf: BSD 3-Clause License
# License for gopkg.in/go-jose/go-jose.v2: Apache License 2.0
# License for gopkg.in/go-jose/go-jose.v2/json: BSD 3-Clause License
# License for gopkg.in/tomb.v1: BSD 3-Clause License
# License for gopkg.in/yaml.v2: Apache License 2.0
# License for gopkg.in/yaml.v3: Apache License 2.0 and/or MIT License
# License for sigs.k8s.io/yaml: BSD 3-Clause License and/or MIT License

License: ASL 2.0 and BSD and ISC and MIT and MPLv2.0
URL: %{gourl}
Source:         %{gosource}
Source:         vendor-%{version}.tar.gz
Source:         bundle_go_deps_for_rpm.sh

BuildRequires: gcc
BuildRequires: golang
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: git-core
BuildRequires: go-rpm-macros
BuildRequires: make

%if 0%{?fedora} >= 35
BuildRequires: shadow-utils-subid-devel
%endif

%description
%{common_description}

%prep
%goprep %{?with_bundledc:-k}
%if %{with bundled}
%setup -q -T -D -a 1 -n %{name}-%{version}
%endif
%autopatch -p1

%if %{without bundled}
%generate_buildrequires
%go_generate_buildrequires
%endif

%build
%if %{with bundled}
export GOFLAGS="-mod=vendor"
%endif

export BUILDTAGS="exclude_graphdriver_devicemapper exclude_graphdriver_btrfs btrfs_noversion containers_image_openpgp remote"

%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%endif

%files
%license %{golicenses}
%doc     
%{_bindir}/*

%changelog
%autochangelog
