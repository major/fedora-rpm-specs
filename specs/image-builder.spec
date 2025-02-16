# The minimum required osbuild version, note that this used to be 129
# but got bumped to 138 for librepo support which is not strictly
# required. So if this needs backport to places where there is no
# recent osbuild available we could simply make --use-librepo false
# and go back to 129.
%global min_osbuild_version 138

%global goipath         github.com/osbuild/image-builder-cli

Version:        11

%gometa

%global common_description %{expand:
A local binary for building customized OS artifacts such as VM images and
OSTree commits. Uses osbuild under the hood.
}

Name:           image-builder
Release:        1%{?dist}
Summary:        An image building executable using osbuild
ExcludeArch:    i686

# Upstream license specification: Apache-2.0
# Others generated with:
#   $ go_vendor_license -C <UNPACKED ARCHIVE> report expression
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC-BY-SA-4.0 AND ISC AND MIT AND MPL-2.0 AND Unlicense

URL:            %{gourl}
Source0:        https://github.com/osbuild/image-builder-cli/releases/download/v%{version}/image-builder-cli-%{version}.tar.gz


BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
# Build requirements of 'theproglottis/gpgme' package
BuildRequires:  gpgme-devel
BuildRequires:  libassuan-devel
# Build requirements of 'github.com/containers/storage' package
BuildRequires:  device-mapper-devel
BuildRequires:  libxcrypt-devel
%if 0%{?fedora}
# Build requirements of 'github.com/containers/storage' package
BuildRequires:  btrfs-progs-devel
# DO NOT REMOVE the BUNDLE_START and BUNDLE_END markers as they are used by 'tools/rpm_spec_add_provides_bundle.sh' to generate the Provides: bundled list
# BUNDLE_START
Provides: bundled(golang(dario.cat/mergo)) = 1.0.1
Provides: bundled(golang(github.com/BurntSushi/toml)) = 1.4.0
Provides: bundled(golang(github.com/Microsoft/go-winio)) = 0.6.2
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = 0.12.9
Provides: bundled(golang(github.com/VividCortex/ewma)) = 1.2.0
Provides: bundled(golang(github.com/acarl005/stripansi)) = 5a71ef0
Provides: bundled(golang(github.com/asaskevich/govalidator)) = a9d515a
Provides: bundled(golang(github.com/aws/aws-sdk-go)) = 1.55.6
Provides: bundled(golang(github.com/cheggaaa/pb/v3)) = 3.1.6
Provides: bundled(golang(github.com/containerd/cgroups/v3)) = 3.0.3
Provides: bundled(golang(github.com/containerd/errdefs)) = 0.3.0
Provides: bundled(golang(github.com/containerd/errdefs/pkg)) = 0.3.0
Provides: bundled(golang(github.com/containerd/stargz-snapshotter/estargz)) = 0.15.1
Provides: bundled(golang(github.com/containerd/typeurl/v2)) = 2.2.0
Provides: bundled(golang(github.com/containers/common)) = 0.61.1
Provides: bundled(golang(github.com/containers/image/v5)) = 5.33.1
Provides: bundled(golang(github.com/containers/libtrust)) = c1716e8
Provides: bundled(golang(github.com/containers/ocicrypt)) = 1.2.0
Provides: bundled(golang(github.com/containers/storage)) = 1.56.1
Provides: bundled(golang(github.com/cyberphone/json-canonicalization)) = ba74d44
Provides: bundled(golang(github.com/cyphar/filepath-securejoin)) = 0.3.4
Provides: bundled(golang(github.com/davecgh/go-spew)) = d8f796a
Provides: bundled(golang(github.com/distribution/reference)) = 0.6.0
Provides: bundled(golang(github.com/docker/distribution)) = 2.8.3+incompatible
Provides: bundled(golang(github.com/docker/docker)) = 27.3.1+incompatible
Provides: bundled(golang(github.com/docker/docker-credential-helpers)) = 0.8.2
Provides: bundled(golang(github.com/docker/go-connections)) = 0.5.0
Provides: bundled(golang(github.com/docker/go-units)) = 0.5.0
Provides: bundled(golang(github.com/fatih/color)) = 1.18.0
Provides: bundled(golang(github.com/felixge/httpsnoop)) = 1.0.4
Provides: bundled(golang(github.com/go-jose/go-jose/v4)) = 4.0.4
Provides: bundled(golang(github.com/go-logr/logr)) = 1.4.2
Provides: bundled(golang(github.com/go-logr/stdr)) = 1.2.2
Provides: bundled(golang(github.com/go-openapi/analysis)) = 0.23.0
Provides: bundled(golang(github.com/go-openapi/errors)) = 0.22.0
Provides: bundled(golang(github.com/go-openapi/jsonpointer)) = 0.21.0
Provides: bundled(golang(github.com/go-openapi/jsonreference)) = 0.21.0
Provides: bundled(golang(github.com/go-openapi/loads)) = 0.22.0
Provides: bundled(golang(github.com/go-openapi/runtime)) = 0.28.0
Provides: bundled(golang(github.com/go-openapi/spec)) = 0.21.0
Provides: bundled(golang(github.com/go-openapi/strfmt)) = 0.23.0
Provides: bundled(golang(github.com/go-openapi/swag)) = 0.23.0
Provides: bundled(golang(github.com/go-openapi/validate)) = 0.24.0
Provides: bundled(golang(github.com/gobwas/glob)) = 0.2.3
Provides: bundled(golang(github.com/gogo/protobuf)) = 1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = 41bb18b
Provides: bundled(golang(github.com/golang/protobuf)) = 1.5.4
Provides: bundled(golang(github.com/google/go-containerregistry)) = 0.20.2
Provides: bundled(golang(github.com/google/go-intervals)) = 0.0.2
Provides: bundled(golang(github.com/google/uuid)) = 1.6.0
Provides: bundled(golang(github.com/gorilla/mux)) = 1.8.1
Provides: bundled(golang(github.com/hashicorp/errwrap)) = 1.1.0
Provides: bundled(golang(github.com/hashicorp/go-multierror)) = 1.1.1
Provides: bundled(golang(github.com/hashicorp/go-version)) = 1.7.0
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = 1.1.0
Provides: bundled(golang(github.com/jmespath/go-jmespath)) = 0.4.0
Provides: bundled(golang(github.com/josharian/intern)) = 1.0.0
Provides: bundled(golang(github.com/json-iterator/go)) = 1.1.12
Provides: bundled(golang(github.com/klauspost/compress)) = 1.17.11
Provides: bundled(golang(github.com/klauspost/pgzip)) = 1.2.6
Provides: bundled(golang(github.com/letsencrypt/boulder)) = de9c061
Provides: bundled(golang(github.com/mailru/easyjson)) = 0.7.7
Provides: bundled(golang(github.com/mattn/go-colorable)) = 0.1.14
Provides: bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides: bundled(golang(github.com/mattn/go-runewidth)) = 0.0.16
Provides: bundled(golang(github.com/mattn/go-sqlite3)) = 1.14.24
Provides: bundled(golang(github.com/miekg/pkcs11)) = 1.1.1
Provides: bundled(golang(github.com/mistifyio/go-zfs/v3)) = 3.0.1
Provides: bundled(golang(github.com/mitchellh/mapstructure)) = 1.5.0
Provides: bundled(golang(github.com/moby/docker-image-spec)) = 1.3.1
Provides: bundled(golang(github.com/moby/sys/capability)) = 0.3.0
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = 0.7.2
Provides: bundled(golang(github.com/moby/sys/user)) = 0.3.0
Provides: bundled(golang(github.com/modern-go/concurrent)) = bacd9c7
Provides: bundled(golang(github.com/modern-go/reflect2)) = 1.0.2
Provides: bundled(golang(github.com/oklog/ulid)) = 1.3.1
Provides: bundled(golang(github.com/opencontainers/go-digest)) = 1.0.0
Provides: bundled(golang(github.com/opencontainers/image-spec)) = 1.1.0
Provides: bundled(golang(github.com/opencontainers/runtime-spec)) = 1.2.0
Provides: bundled(golang(github.com/opencontainers/selinux)) = 1.11.1
Provides: bundled(golang(github.com/osbuild/bootc-image-builder/bib)) = b35eaa8
Provides: bundled(golang(github.com/osbuild/images)) = fa630cd
Provides: bundled(golang(github.com/ostreedev/ostree-go)) = 719684c
Provides: bundled(golang(github.com/pkg/errors)) = 0.9.1
Provides: bundled(golang(github.com/pmezard/go-difflib)) = 5d4384e
Provides: bundled(golang(github.com/proglottis/gpgme)) = 0.1.3
Provides: bundled(golang(github.com/rivo/uniseg)) = 0.4.7
Provides: bundled(golang(github.com/secure-systems-lab/go-securesystemslib)) = 0.8.0
Provides: bundled(golang(github.com/sigstore/fulcio)) = 1.6.4
Provides: bundled(golang(github.com/sigstore/rekor)) = 1.3.6
Provides: bundled(golang(github.com/sigstore/sigstore)) = 1.8.9
Provides: bundled(golang(github.com/sirupsen/logrus)) = 1.9.3
Provides: bundled(golang(github.com/spf13/cobra)) = 1.8.1
Provides: bundled(golang(github.com/spf13/pflag)) = 1.0.5
Provides: bundled(golang(github.com/stefanberger/go-pkcs11uri)) = 7828495
Provides: bundled(golang(github.com/stretchr/testify)) = 1.10.0
Provides: bundled(golang(github.com/sylabs/sif/v2)) = 2.19.1
Provides: bundled(golang(github.com/tchap/go-patricia/v2)) = 2.3.1
Provides: bundled(golang(github.com/titanous/rocacheck)) = afe7314
Provides: bundled(golang(github.com/ulikunitz/xz)) = 0.5.12
Provides: bundled(golang(github.com/vbatts/tar-split)) = 0.11.6
Provides: bundled(golang(github.com/vbauerster/mpb/v8)) = 8.8.3
Provides: bundled(golang(go.mongodb.org/mongo-driver)) = 1.14.0
Provides: bundled(golang(go.mozilla.org/pkcs7)) = 33d0574
Provides: bundled(golang(go.opencensus.io)) = 0.24.0
Provides: bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = 0.54.0
Provides: bundled(golang(go.opentelemetry.io/otel)) = 1.32.0
Provides: bundled(golang(go.opentelemetry.io/otel/metric)) = 1.32.0
Provides: bundled(golang(go.opentelemetry.io/otel/trace)) = 1.32.0
Provides: bundled(golang(golang.org/x/crypto)) = 0.32.0
Provides: bundled(golang(golang.org/x/exp)) = f66d83c
Provides: bundled(golang(golang.org/x/net)) = 0.34.0
Provides: bundled(golang(golang.org/x/sync)) = 0.10.0
Provides: bundled(golang(golang.org/x/sys)) = 0.29.0
Provides: bundled(golang(golang.org/x/term)) = 0.28.0
Provides: bundled(golang(golang.org/x/text)) = 0.21.0
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc)) = 65684f5
Provides: bundled(golang(google.golang.org/grpc)) = 1.70.0
Provides: bundled(golang(google.golang.org/protobuf)) = 1.36.4
Provides: bundled(golang(gopkg.in/ini.v1)) = 1.67.0
Provides: bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
# BUNDLE_END
%endif

Requires:   osbuild >= %{min_osbuild_version}
Requires:   osbuild-ostree >= %{min_osbuild_version}
Requires:   osbuild-lvm2 >= %{min_osbuild_version}
Requires:   osbuild-luks2 >= %{min_osbuild_version}
Requires:   osbuild-depsolve-dnf >= %{min_osbuild_version}

%description
%{common_description}

%prep
%if 0%{?rhel}
%forgeautosetup -p1
%else
%goprep -k
%endif

%build
export GOFLAGS="-buildmode=pie"
%if 0%{?rhel}
GO_BUILD_PATH=$PWD/_build
install -m 0755 -vd $(dirname $GO_BUILD_PATH/src/%{goipath})
ln -fs $PWD $GO_BUILD_PATH/src/%{goipath}
cd $GO_BUILD_PATH/src/%{goipath}
install -m 0755 -vd _bin
export PATH=$PWD/_bin${PATH:+:$PATH}
export GOPATH=$GO_BUILD_PATH:%{gopath}
export GOFLAGS+=" -mod=vendor"
%endif

%if 0%{?fedora}
# Fedora disables Go modules by default, but we want to use them.
# Undefine the macro which disables it to use the default behavior.
%undefine gomodulesmode
%endif

# btrfs-progs-devel is not available on RHEL
%if 0%{?rhel}
GOTAGS="exclude_graphdriver_btrfs"
%endif

%gobuild ${GOTAGS:+-tags=$GOTAGS} -o %{gobuilddir}/bin/image-builder %{goipath}/cmd/image-builder

%install
install -m 0755 -vd                                 %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/image-builder %{buildroot}%{_bindir}/

%check
export GOFLAGS="-buildmode=pie"
%if 0%{?rhel}
export GOFLAGS+=" -mod=vendor -tags=exclude_graphdriver_btrfs"
export GOPATH=$PWD/_build:%{gopath}
# cd inside GOPATH, otherwise go with GO111MODULE=off ignores vendor directory
cd $PWD/_build/src/%{goipath}
%gotest ./...
%else
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/image-builder

%changelog
* Fri Feb 14 2025 Packit <hello@packit.dev> - 11-1
Changes with 11
----------------
  * describeimg: typo in describe output (#129)
    * Author: Simon de Vlieger, Reviewers: Michael Vogt
  * go.mod: update to get the latest `progress` fixes from `bib` (#127)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * main: add `-v,--verbose` switch that enables verbose build logging (#126)
    * Author: Michael Vogt, Reviewers: Ondřej Budai
  * main: add add `--force-repo` flag (#134)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger, Tomáš Hozza
  * main: add new `--extra-repo` flag (#113)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Tomáš Hozza
  * main: add new upload command (#119)
    * Author: Michael Vogt, Reviewers: Tomáš Hozza
  * main: update for new reporegistry.New() api (c.f. pr#1179) (#128)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou

— Somewhere on the Internet, 2025-02-14


* Wed Feb 05 2025 Packit <hello@packit.dev> - 10-1
Changes with 10
----------------
  * main: fix auto-detected distro that is non-visible, tweak order (#124)
    * Author: Michael Vogt, Reviewers: Ondřej Budai
  * main: reset the terminal properly on SIGINT (#125)
    * Author: Michael Vogt, Reviewers: Ondřej Budai

— Somewhere on the Internet, 2025-02-05


* Mon Feb 03 2025 Packit <hello@packit.dev> - 9-1
Changes with 9
----------------
  * ci/packit: set downstream name (#116)
    * Author: Simon de Vlieger, Reviewers: Ondřej Budai
  * specfile: build requires `libxcrypt-compat` (#117)
    * Author: Simon de Vlieger, Reviewers: Ondřej Budai

— Somewhere on the Internet, 2025-02-03


* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 7-2
- Add explicit BR: libxcrypt-devel

# the changelog is distribution-specific, therefore there's just one entry
# to make rpmlint happy.

* Fri Jan 24 2025 Image Builder team <osbuilders@redhat.com> - 0-1
- On this day, this project was born and the RPM created.
