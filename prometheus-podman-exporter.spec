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

# https://github.com/containers/prometheus-podman-exporter
%global goipath         github.com/containers/prometheus-podman-exporter
Version:                1.7.0

%gometa -f

%global goname prometheus-podman-exporter

%global common_description %{expand:
Prometheus exporter for podman environments exposing containers, pods, images,
volumes and networks information.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md MAINTAINERS.md\\\
                        README.md SECURITY.md

Name:           %{goname}
Release:        %autorelease
Summary:        Prometheus exporter for podman environment

# License for github.com/containers/prometheus-podman-exporter: Apache-2.0
# License for dario.cat/mergo: BSD-3-Clause
# License for github.com/acarl005/stripansi: MIT
# License for github.com/asaskevich/govalidator: MIT
# License for github.com/Azure/go-ansiterm: MIT
# License for github.com/beorn7/perks: MIT
# License for github.com/blang/semver/v4: MIT
# License for github.com/BurntSushi/toml: MIT
# License for github.com/cespare/xxhash/v2: MIT
# License for github.com/checkpoint-restore/checkpointctl: Apache-2.0
# License for github.com/checkpoint-restore/go-criu/v6: Apache-2.0
# License for github.com/chzyer/readline: MIT
# License for github.com/cilium/ebpf: MIT
# License for github.com/container-orchestrated-devices/container-device-interface: Apache-2.0
# License for github.com/containerd/containerd: Apache-2.0
# License for github.com/containernetworking/cni: Apache-2.0
# License for github.com/containernetworking/plugins: Apache-2.0
# License for github.com/containers/buildah: Apache-2.0
# License for github.com/containers/common: Apache-2.0
# License for github.com/containers/conmon: Apache-2.0
# License for github.com/containers/image/v5: Apache-2.0
# License for github.com/containers/libtrust: Apache-2.0
# License for github.com/containers/ocicrypt: Apache-2.0
# License for github.com/containers/podman/v4: Apache-2.0
# License for github.com/containers/psgo: Apache-2.0
# License for github.com/coreos/go-systemd: Apache-2.0
# License for github.com/coreos/go-systemd/v22: Apache-2.0
# License for github.com/cyberphone/json-canonicalization: Apache-2.0
# License for github.com/cyphar/filepath-securejoin: BSD-3-Clause
# License for github.com/davecgh/go-spew: ISC
# License for github.com/disiqueira/gotree/v3: MIT
# License for github.com/docker/distribution: Apache-2.0
# License for github.com/docker/docker: Apache-2.0
# License for github.com/docker/docker-credential-helpers: MIT
# License for github.com/docker/go-connections: Apache-2.0
# License for github.com/docker/go-plugins-helpers: Apache-2.0
# License for github.com/docker/go-units: Apache-2.0
# License for github.com/fsnotify/fsnotify: BSD-3-Clause
# License for github.com/fsouza/go-dockerclient: BSD-2-Clause
# License for github.com/go-kit/log: MIT
# License for github.com/go-logfmt/logfmt: MIT
# License for github.com/go-openapi/analysis: Apache-2.0
# License for github.com/go-openapi/errors: Apache-2.0
# License for github.com/go-openapi/jsonpointer: Apache-2.0
# License for github.com/go-openapi/jsonreference: Apache-2.0
# License for github.com/go-openapi/loads: Apache-2.0
# License for github.com/go-openapi/runtime: Apache-2.0
# License for github.com/go-openapi/spec: Apache-2.0
# License for github.com/go-openapi/strfmt: Apache-2.0
# License for github.com/go-openapi/swag: Apache-2.0
# License for github.com/go-openapi/validate: Apache-2.0
# License for github.com/godbus/dbus/v5: BSD-2-Clause
# License for github.com/gogo/protobuf: BSD-3-Clause
# License for github.com/golang/protobuf: BSD-3-Clause
# License for github.com/google/go-containerregistry: Apache-2.0
# License for github.com/google/gofuzz: Apache-2.0
# License for github.com/google/shlex: Apache-2.0
# License for github.com/google/uuid: BSD-3-Clause
# License for github.com/gorilla/mux: BSD-3-Clause
# License for github.com/gorilla/schema: BSD-3-Clause
# License for github.com/hashicorp/errwrap: MPL-2.0
# License for github.com/hashicorp/go-multierror: MPL-2.0
# License for github.com/inconshreveable/mousetrap: Apache-2.0
# License for github.com/jinzhu/copier: MIT
# License for github.com/josharian/intern: MIT
# License for github.com/jpillora/backoff: MIT
# License for github.com/json-iterator/go: MIT
# License for github.com/klauspost/compress: BSD-3-Clause AND Apache-2.0 AND MIT
# License for github.com/klauspost/pgzip: MIT AND BSD-3-Clause
# License for github.com/kr/fs: BSD-3-Clause
# License for github.com/letsencrypt/boulder: MPL-2.0
# License for github.com/mailru/easyjson: MIT
# License for github.com/manifoldco/promptui: BSD-3-Clause
# License for github.com/mattn/go-runewidth: MIT
# License for github.com/mattn/go-shellwords: MIT
# License for github.com/mattn/go-sqlite3: MIT
# License for github.com/matttproud/golang_protobuf_extensions: Apache-2.0
# License for github.com/Microsoft/go-winio: MIT
# License for github.com/miekg/pkcs11: BSD-3-Clause
# License for github.com/mitchellh/mapstructure: MIT
# License for github.com/moby/patternmatcher: Apache-2.0
# License for github.com/moby/sys/mountinfo: Apache-2.0
# License for github.com/moby/sys/sequential: Apache-2.0
# License for github.com/moby/term: Apache-2.0
# License for github.com/modern-go/concurrent: Apache-2.0
# License for github.com/modern-go/reflect2: Apache-2.0
# License for github.com/morikuni/aec: MIT
# License for github.com/mwitkow/go-conntrack: Apache-2.0
# License for github.com/nxadm/tail: MIT
# License for github.com/oklog/ulid: Apache-2.0
# License for github.com/opencontainers/go-digest: Apache-2.0 AND CC-BY-SA-4.0
# License for github.com/opencontainers/image-spec: Apache-2.0
# License for github.com/opencontainers/runc: Apache-2.0
# License for github.com/opencontainers/runtime-spec: Apache-2.0
# License for github.com/opencontainers/runtime-tools: Apache-2.0
# License for github.com/opencontainers/selinux: Apache-2.0
# License for github.com/openshift/imagebuilder: Apache-2.0
# License for github.com/ostreedev/ostree-go: ISC
# License for github.com/pkg/errors: BSD-2-Clause
# License for github.com/pkg/sftp: BSD-2-Clause
# License for github.com/pmezard/go-difflib: BSD-3-Clause
# License for github.com/proglottis/gpgme: BSD-3-Clause
# License for github.com/prometheus/client_golang: Apache-2.0
# License for github.com/prometheus/client_model: Apache-2.0
# License for github.com/prometheus/common: Apache-2.0
# License for github.com/prometheus/exporter-toolkit: Apache-2.0
# License for github.com/prometheus/procfs: Apache-2.0
# License for github.com/rivo/uniseg: MIT
# License for github.com/seccomp/libseccomp-golang: BSD-2-Clause
# License for github.com/sigstore/fulcio: Apache-2.0
# License for github.com/sigstore/rekor: Apache-2.0
# License for github.com/sigstore/sigstore: Apache-2.0
# License for github.com/sirupsen/logrus: MIT
# License for github.com/spf13/cobra: Apache-2.0
# License for github.com/spf13/pflag: BSD-3-Clause
# License for github.com/stefanberger/go-pkcs11uri: Apache-2.0
# License for github.com/sylabs/sif/v2: BSD-3-Clause
# License for github.com/syndtr/gocapability: BSD-2-Clause
# License for github.com/theupdateframework/go-tuf: BSD-3-Clause
# License for github.com/titanous/rocacheck: MIT
# License for github.com/ulikunitz/xz: BSD-3-Clause
# License for github.com/vbatts/tar-split: BSD-3-Clause
# License for github.com/vbauerster/mpb/v8: Unlicense
# License for github.com/vishvananda/netlink: Apache-2.0
# License for github.com/vishvananda/netns: Apache-2.0
# License for github.com/VividCortex/ewma: MIT
# License for go.etcd.io/bbolt: MIT
# License for go.mongodb.org/mongo-driver: Apache-2.0
# License for go.mozilla.org/pkcs7: MIT
# License for golang.org/x/crypto: BSD-3-Clause
# License for golang.org/x/exp: BSD-3-Clause
# License for golang.org/x/mod: BSD-3-Clause
# License for golang.org/x/net: BSD-3-Clause
# License for golang.org/x/oauth2: BSD-3-Clause
# License for golang.org/x/sync: BSD-3-Clause
# License for golang.org/x/sys: BSD-3-Clause
# License for golang.org/x/term: BSD-3-Clause
# License for golang.org/x/text: BSD-3-Clause
# License for golang.org/x/tools: BSD-3-Clause
# License for google.golang.org/appengine: Apache-2.0
# License for google.golang.org/genproto: Apache-2.0
# License for google.golang.org/grpc: Apache-2.0
# License for google.golang.org/protobuf: BSD-3-Clause
# License for gopkg.in/go-jose/go-jose.v2: Apache-2.0
# License for gopkg.in/inf.v0: BSD-3-Clause
# License for gopkg.in/square/go-jose.v2: Apache-2.0
# License for gopkg.in/tomb.v1: BSD-3-Clause
# License for gopkg.in/yaml.v2: Apache-2.0 AND MIT
# License for gopkg.in/yaml.v3: MIT AND Apache-2.0
# License for sigs.k8s.io/yaml: MIT AND BSD-3-Clause
License:        Apache-2.0 AND MPL-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT AND Unlicense AND CC-BY-SA-4.0 AND ISC
URL:            %{gourl}
Source:         %{gosource}
Source:         vendor-%{version}.tar.gz
Source:         bundle_go_deps_for_rpm.sh

%if 0%{?fedora} && ! 0%{?rhel}
BuildRequires: pkgconfig(libbtrfsutil)
%endif
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: git-core
%if 0%{?rhel} >= 9
BuildRequires: go-rpm-macros
%endif
BuildRequires: golang
BuildRequires: make
BuildRequires: pkgconfig(devmapper)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gpgme)
BuildRequires: pkgconfig(libassuan)
%if 0%{?fedora} >= 37
BuildRequires: shadow-utils-subid-devel
%endif

%description %{common_description}

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

%if 0%{?rhel} >= 9
export BUILDTAGS="exclude_graphdriver_btrfs btrfs_noversion"
%endif

export LDFLAGS="-X %{goipath}/cmd.buildVersion=%{version} -X %{goipath}/cmd.buildRevision=%{release} -X %{goipath}/cmd.buildBranch=main"

%gobuild -o %{gobuilddir}/bin/prometheus-podman-exporter %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_unitdir}
install -m 0755 -vd                     %{buildroot}%{_userunitdir}
install -m 0644 -vp ./contrib/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -m 0644 -vp ./contrib/systemd/%{name}.service %{buildroot}%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service
%systemd_post %{name}.service

%preun
%systemd_user_preun %{name}.service
%systemd_preun %{name}.service

%if %{with check}
%check
%if 0%{?fedora}
%gocheck
%endif
%endif

%files
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md MAINTAINERS.md README.md SECURITY.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_userunitdir}/%{name}.service

%changelog
%autochangelog
