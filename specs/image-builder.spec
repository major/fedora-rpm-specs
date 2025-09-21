# The minimum required osbuild version, note that this used to be 129
# but got bumped to 138 for librepo support which is not strictly
# required. So if this needs backport to places where there is no
# recent osbuild available we could simply make --use-librepo false
# and go back to 129.
%global min_osbuild_version 157

%global goipath         github.com/osbuild/image-builder-cli

Version:        35

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
Provides: bundled(golang(dario.cat/mergo)) = 1.0.2
Provides: bundled(golang(github.com/BurntSushi/toml)) = 3d3abc2
Provides: bundled(golang(github.com/Microsoft/go-winio)) = 0.6.2
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = 0.13.0
Provides: bundled(golang(github.com/VividCortex/ewma)) = 1.2.0
Provides: bundled(golang(github.com/acarl005/stripansi)) = 5a71ef0
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2)) = 1.38.3
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream)) = 1.7.1
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/config)) = 1.31.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/credentials)) = 1.18.10
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)) = 1.18.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/feature/s3/manager)) = 1.19.4
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/configsources)) = 1.4.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)) = 2.7.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/ini)) = 1.8.3
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/internal/v4a)) = 1.4.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/ec2)) = 1.249.0
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)) = 1.13.1
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/checksum)) = 1.8.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)) = 1.13.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/s3shared)) = 1.19.6
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/s3)) = 1.87.3
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/sso)) = 1.29.1
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/ssooidc)) = 1.34.2
Provides: bundled(golang(github.com/aws/aws-sdk-go-v2/service/sts)) = 1.38.2
Provides: bundled(golang(github.com/aws/smithy-go)) = 1.23.0
Provides: bundled(golang(github.com/cheggaaa/pb/v3)) = 3.1.7
Provides: bundled(golang(github.com/containerd/cgroups/v3)) = 3.0.5
Provides: bundled(golang(github.com/containerd/errdefs)) = 1.0.0
Provides: bundled(golang(github.com/containerd/errdefs/pkg)) = 0.3.0
Provides: bundled(golang(github.com/containerd/stargz-snapshotter/estargz)) = 0.16.3
Provides: bundled(golang(github.com/containerd/typeurl/v2)) = 2.2.3
Provides: bundled(golang(github.com/containers/common)) = 0.64.1
Provides: bundled(golang(github.com/containers/image/v5)) = 5.36.1
Provides: bundled(golang(github.com/containers/libtrust)) = c1716e8
Provides: bundled(golang(github.com/containers/ocicrypt)) = 1.2.1
Provides: bundled(golang(github.com/containers/storage)) = 1.59.1
Provides: bundled(golang(github.com/coreos/go-semver)) = 0.3.1
Provides: bundled(golang(github.com/cyberphone/json-canonicalization)) = 19d51d7
Provides: bundled(golang(github.com/cyphar/filepath-securejoin)) = 0.4.1
Provides: bundled(golang(github.com/davecgh/go-spew)) = d8f796a
Provides: bundled(golang(github.com/distribution/reference)) = 0.6.0
Provides: bundled(golang(github.com/docker/distribution)) = 2.8.3+incompatible
Provides: bundled(golang(github.com/docker/docker)) = 28.3.3+incompatible
Provides: bundled(golang(github.com/docker/docker-credential-helpers)) = 0.9.3
Provides: bundled(golang(github.com/docker/go-connections)) = 0.5.0
Provides: bundled(golang(github.com/docker/go-units)) = 0.5.0
Provides: bundled(golang(github.com/fatih/color)) = 1.18.0
Provides: bundled(golang(github.com/felixge/httpsnoop)) = 1.0.4
Provides: bundled(golang(github.com/go-jose/go-jose/v4)) = 4.0.5
Provides: bundled(golang(github.com/go-logr/logr)) = 1.4.3
Provides: bundled(golang(github.com/go-logr/stdr)) = 1.2.2
Provides: bundled(golang(github.com/gobwas/glob)) = 0.2.3
Provides: bundled(golang(github.com/gogo/protobuf)) = 1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = 2c02b82
Provides: bundled(golang(github.com/golang/protobuf)) = 1.5.4
Provides: bundled(golang(github.com/google/go-containerregistry)) = 0.20.3
Provides: bundled(golang(github.com/google/go-intervals)) = 0.0.2
Provides: bundled(golang(github.com/google/uuid)) = 1.6.0
Provides: bundled(golang(github.com/gorilla/mux)) = 1.8.1
Provides: bundled(golang(github.com/hashicorp/errwrap)) = 1.1.0
Provides: bundled(golang(github.com/hashicorp/go-multierror)) = 1.1.1
Provides: bundled(golang(github.com/hashicorp/go-version)) = 1.7.0
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = 1.1.0
Provides: bundled(golang(github.com/json-iterator/go)) = 1.1.12
Provides: bundled(golang(github.com/klauspost/compress)) = 1.18.0
Provides: bundled(golang(github.com/klauspost/pgzip)) = 1.2.6
Provides: bundled(golang(github.com/letsencrypt/boulder)) = de9c061
Provides: bundled(golang(github.com/mattn/go-colorable)) = 0.1.14
Provides: bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides: bundled(golang(github.com/mattn/go-runewidth)) = 0.0.16
Provides: bundled(golang(github.com/mattn/go-sqlite3)) = 1.14.28
Provides: bundled(golang(github.com/miekg/pkcs11)) = 1.1.1
Provides: bundled(golang(github.com/mistifyio/go-zfs/v3)) = 3.0.1
Provides: bundled(golang(github.com/moby/docker-image-spec)) = 1.3.1
Provides: bundled(golang(github.com/moby/sys/capability)) = 0.4.0
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = 0.7.2
Provides: bundled(golang(github.com/moby/sys/user)) = 0.4.0
Provides: bundled(golang(github.com/modern-go/concurrent)) = bacd9c7
Provides: bundled(golang(github.com/modern-go/reflect2)) = 1.0.2
Provides: bundled(golang(github.com/opencontainers/go-digest)) = 1.0.0
Provides: bundled(golang(github.com/opencontainers/image-spec)) = 1.1.1
Provides: bundled(golang(github.com/opencontainers/runtime-spec)) = 1.2.1
Provides: bundled(golang(github.com/opencontainers/selinux)) = 1.12.0
Provides: bundled(golang(github.com/osbuild/blueprint)) = 1.13.0
Provides: bundled(golang(github.com/osbuild/images)) = 0.193.0
Provides: bundled(golang(github.com/pkg/errors)) = 0.9.1
Provides: bundled(golang(github.com/pmezard/go-difflib)) = 5d4384e
Provides: bundled(golang(github.com/proglottis/gpgme)) = 0.1.4
Provides: bundled(golang(github.com/prometheus/client_golang)) = 1.23.0
Provides: bundled(golang(github.com/rivo/uniseg)) = 0.4.7
Provides: bundled(golang(github.com/secure-systems-lab/go-securesystemslib)) = 0.9.0
Provides: bundled(golang(github.com/sigstore/fulcio)) = 1.6.6
Provides: bundled(golang(github.com/sigstore/protobuf-specs)) = 0.4.1
Provides: bundled(golang(github.com/sigstore/sigstore)) = 1.9.5
Provides: bundled(golang(github.com/sirupsen/logrus)) = 1.9.3
Provides: bundled(golang(github.com/smallstep/pkcs7)) = 0.1.1
Provides: bundled(golang(github.com/spf13/cobra)) = 1.9.1
Provides: bundled(golang(github.com/spf13/pflag)) = 1.0.7
Provides: bundled(golang(github.com/stefanberger/go-pkcs11uri)) = 7828495
Provides: bundled(golang(github.com/stretchr/testify)) = 1.11.1
Provides: bundled(golang(github.com/sylabs/sif/v2)) = 2.21.1
Provides: bundled(golang(github.com/tchap/go-patricia/v2)) = 2.3.3
Provides: bundled(golang(github.com/titanous/rocacheck)) = afe7314
Provides: bundled(golang(github.com/ulikunitz/xz)) = 0.5.12
Provides: bundled(golang(github.com/vbatts/tar-split)) = 0.12.1
Provides: bundled(golang(github.com/vbauerster/mpb/v8)) = 8.10.2
Provides: bundled(golang(go.opencensus.io)) = 0.24.0
Provides: bundled(golang(go.opentelemetry.io/auto/sdk)) = 1.1.0
Provides: bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = 0.61.0
Provides: bundled(golang(go.opentelemetry.io/otel)) = 1.36.0
Provides: bundled(golang(go.opentelemetry.io/otel/metric)) = 1.36.0
Provides: bundled(golang(go.opentelemetry.io/otel/trace)) = 1.36.0
Provides: bundled(golang(go.yaml.in/yaml/v2)) = 2.4.2
Provides: bundled(golang(golang.org/x/crypto)) = 0.41.0
Provides: bundled(golang(golang.org/x/exp)) = 7d7fa50
Provides: bundled(golang(golang.org/x/net)) = 0.43.0
Provides: bundled(golang(golang.org/x/sync)) = 0.16.0
Provides: bundled(golang(golang.org/x/sys)) = 0.35.0
Provides: bundled(golang(golang.org/x/term)) = 0.34.0
Provides: bundled(golang(golang.org/x/text)) = 0.28.0
Provides: bundled(golang(google.golang.org/genproto/googleapis/api)) = 3122310
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc)) = 3122310
Provides: bundled(golang(google.golang.org/grpc)) = 1.74.2
Provides: bundled(golang(google.golang.org/protobuf)) = 1.36.7
Provides: bundled(golang(gopkg.in/ini.v1)) = 1.67.0
Provides: bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
Provides: bundled(golang(sigs.k8s.io/yaml)) = 1.5.0
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

export LDFLAGS="${LDFLAGS} -X 'main.version=%{version}'"
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
* Fri Sep 19 2025 Packit <hello@packit.dev> - 35-1
Changes with 35
----------------
  - cmd/upload: add fedora ami to aws upload (HMS-9388) (#307)
    - Author: Gianluca Zuccarelli, Reviewers: Lukáš Zapletal, Michael Vogt
  - deps: update to images 0.193.0 (#308)
    - Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Michael Vogt
  - main: update to latest images API changes in imgfilter (#295)
    - Author: Michael Vogt, Reviewers: Simon de Vlieger, Tomáš Hozza

— Somewhere on the Internet, 2025-09-19


* Tue Sep 16 2025 Packit <hello@packit.dev> - 34-1
Changes with 34
----------------
  - Install openssl in cli container (#292)
    - Author: Justin Sherrill, Reviewers: Brian C. Lane, Michael Vogt
  - build(deps): bump actions/setup-python from 5 to 6 (#296)
    - Author: dependabot[bot], Reviewers: Achilleas Koutsou, Tomáš Hozza
  - deps: update to images 0.191.0 (#302)
    - Author: Simon de Vlieger, Reviewers: Michael Vogt, Tomáš Hozza
  - github: add CODEOWNERS (#291)
    - Author: Achilleas Koutsou, Reviewers: Lukáš Zapletal, Tomáš Hozza
  - go.mod: update osbuild/images to 0.190.0 (dnfjson -> depsolvednf rename) (HMS-9366) (#301)
    - Author: Tomáš Hozza, Reviewers: Lukáš Zapletal, Simon de Vlieger
  - go.mod: update to images v0.186.0 (#294)
    - Author: Michael Vogt, Reviewers: Ondřej Budai, Tomáš Hozza
  - image-builder: use `manifesttest` from `images` (#293)
    - Author: Michael Vogt, Reviewers: Lukáš Zapletal, Ondřej Budai
  - main: add support disk based bootc images via --bootc-ref  (HMS-8845) (#245)
    - Author: Michael Vogt, Reviewers: Lukáš Zapletal, Ondřej Budai, Simon de Vlieger

— Somewhere on the Internet, 2025-09-16


* Thu Aug 28 2025 Packit <hello@packit.dev> - 33-1
Changes with 33
----------------
  - deps: images 0.182.0 (#288)
    - Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Gianluca Zuccarelli, Michael Vogt

— Somewhere on the Internet, 2025-08-28


* Tue Aug 19 2025 Packit <hello@packit.dev> - 31-1
Changes with 31
----------------
  - build(deps): bump actions/checkout from 3 to 5 (#278)
    - Author: dependabot[bot], Reviewers: Brian C. Lane, Simon de Vlieger
  - build(deps): bump github.com/docker/docker from 28.3.2+incompatible to 28.3.3+incompatible (#270)
    - Author: dependabot[bot], Reviewers: Achilleas Koutsou, Lukáš Zapletal
  - image-builder: use manifest.{Build,Payload}Pipelines (#279)
    - Author: Michael Vogt, Reviewers: Brian C. Lane, Lukáš Zapletal, Simon de Vlieger, Tomáš Hozza
  - main: fix --extra-repos support when cross building (#281)
    - Author: Michael Vogt, Reviewers: Brian C. Lane, Lukáš Zapletal, Simon de Vlieger, Tomáš Hozza
  - setup: Fix a typo carried over from bib (#277)
    - Author: Brian C. Lane, Reviewers: Lukáš Zapletal, Michael Vogt

— Somewhere on the Internet, 2025-08-19


* Fri Aug 15 2025 Maxwell G <maxwell@gtmx.me> - 30-2
- Rebuild for golang-1.25.0

* Mon Aug 11 2025 Packit <hello@packit.dev> - 30-1
Changes with 30
----------------
  * image-builder: move to latest images library (#272)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * image-builder: use `github.com/osbuild/blueprint` (#273)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Gianluca Zuccarelli

— Somewhere on the Internet, 2025-08-11


* Fri Aug 01 2025 Packit <hello@packit.dev> - 29-1
Changes with 29
----------------
  * deps: fix images 0.168 (#266)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Lukáš Zapletal

— Somewhere on the Internet, 2025-08-01


* Thu Jul 31 2025 Packit <hello@packit.dev> - 28-1
Changes with 28
----------------
  * README.md: document `--ignore-warnings` (#254)
    * Author: Michael Vogt, Reviewers: Lukáš Zapletal, Simon de Vlieger
  * ci/packit: remove EPEL release automation (#258)
    * Author: Simon de Vlieger, Reviewers: Ondřej Budai, Tomáš Hozza
  * ci: upgrade golangci-lint to 2.3.0 (#257)
    * Author: Lukáš Zapletal, Reviewers: Michael Vogt, Simon de Vlieger
  * deps: update `images` to 0.168 (HMS-8949, HMS-8922) (#262)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Michael Vogt, Tomáš Hozza
  * spec: fix up version number (#259)
    * Author: Simon de Vlieger, Reviewers: Lukáš Zapletal, Ondřej Budai, Tomáš Hozza

— Somewhere on the Internet, 2025-07-31


* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 23 2025 Packit <hello@packit.dev> - 27-1
Changes with 27
----------------
  * chore: set specfile version at build (#253)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Lukáš Zapletal

— Somewhere on the Internet, 2025-07-23


* Mon Jul 21 2025 Packit <hello@packit.dev> - 26-1
Changes with 26
----------------
  * deps: bump images to 0.164 (#252)
    * Author: Simon de Vlieger, Reviewers: Michael Vogt, Ondřej Budai
  * main: add `--ignore-warnings` cmdline option (#250)
    * Author: Michael Vogt, Reviewers: Lukáš Zapletal, Sanne Raymaekers, Simon de Vlieger
  * testutil: trivial cleanup/rename (#249)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger

— Somewhere on the Internet, 2025-07-21


* Wed Jul 16 2025 Packit <hello@packit.dev> - 25-1
Changes with 25
----------------
  * deps: update images to 0.162.0 (#247)
    * Author: Simon de Vlieger, Reviewers: Lukáš Zapletal, Michael Vogt, Ondřej Budai
  * main: `--version` includes git commit (#230)
    * Author: Simon de Vlieger, Reviewers: Brian C. Lane, Michael Vogt
  * packit: enable RHEL 10 builds (HMS-8829) (#246)
    * Author: Ondřej Budai, Reviewers: Florian Schüller, Sanne Raymaekers, Simon de Vlieger

— Somewhere on the Internet, 2025-07-16


* Mon Jul 14 2025 Packit <hello@packit.dev> - 24-1
Changes with 24
----------------
  * Always set rhsm.Facts when generating manifests (#239)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * doc/01-usage.md: avoid multiple h1 in one document (#235)
    * Author: Florian Schüller, Reviewers: Michael Vogt, Simon de Vlieger
  * doc/10-faq.md: add image types documentation (#236)
    * Author: Florian Schüller, Reviewers: Michael Vogt, Simon de Vlieger
  * docs: subscription basic info (#205)
    * Author: Lukáš Zapletal, Reviewers: Brian C. Lane, Michael Vogt
  * readme: mention mount for container (#232)
    * Author: Simon de Vlieger, Reviewers: Brian C. Lane, Jelle van der Waa, Michael Vogt

— Somewhere on the Internet, 2025-07-09


* Wed Jun 25 2025 Packit <hello@packit.dev> - 23-1
Changes with 23
----------------
  * cmd/describe: ensure that all image types can be described (HMS-7044) (#231)
    * Author: Tomáš Hozza, Reviewers: Achilleas Koutsou, Simon de Vlieger

— Somewhere on the Internet, 2025-06-25


* Sun Jun 22 2025 Packit <hello@packit.dev> - 22-1
Changes with 22
----------------
  * GHA: add the common-stale-action (#225)
    * Author: Tomáš Hozza, Reviewers: Lukáš Zapletal, Simon de Vlieger
  * chore: bump `images` (#228)
    * Author: Simon de Vlieger, Reviewers: Tomáš Hozza

— Somewhere on the Internet, 2025-06-22


* Wed Jun 11 2025 Packit <hello@packit.dev> - 21-1
Changes with 21
----------------
  * image-builder: fix cross-arch uploading (#218)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * packit: rename epel9-next (#224)
    * Author: Simon de Vlieger, Reviewers: Lukáš Zapletal

— Somewhere on the Internet, 2025-06-11


* Fri May 30 2025 Packit <hello@packit.dev> - 20-1
Changes with 20
----------------
  * deps: update (#219)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou

— Somewhere on the Internet, 2025-05-30


* Wed May 14 2025 Packit <hello@packit.dev> - 19-1
Changes with 19
----------------
  * refactor: use standard logger instead of logrus (#214)
    * Author: Lukáš Zapletal, Reviewers: Michael Vogt

— Somewhere on the Internet, 2025-05-14


* Thu Apr 17 2025 Packit <hello@packit.dev> - 17-1
Changes with 17
----------------
  * deps: bump images (#207)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou

— Somewhere on the Internet, 2025-04-17


* Wed Apr 02 2025 Packit <hello@packit.dev> - 15-1
Changes with 15
----------------
  * README: document that cross building works (#168)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * Revert "blueprintload: enable strict checking for toml" (#174)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Michael Vogt
  * blueprintload: enable strict checking for toml (#163)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Brian C. Lane
  * go.mod: update to latest version of `github.com/osbuild/blueprint` (#172)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou
  * import: `progress` from `bootc-image-builder` (#179)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou
  * import: `setup`, `util`, `podmanutil` from `bootc-image-builder` (#178)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou
  * main: Add a --version flag to show the build version (#175)
    * Author: Brian C. Lane, Reviewers: Michael Vogt, Simon de Vlieger
  * main: allow seed setting (#176)
    * Author: Simon de Vlieger, Reviewers: Achilleas Koutsou, Michael Vogt
  * main: automatically cross build when --arch <foreign> is passed (#164)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * main: show output directory content after image build (#162)
    * Author: Michael Vogt, Reviewers: Brian C. Lane
  * main: tweak handling of --output-name to avoid adding double extensions (#161)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * main: tweak how ibcli determines if bootstraping is needed (#167)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou
  * many: move to use the new github.com/osbuild/blueprint module (HMS-5804) (#169)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou
  * progress: set --cache-max-size in osbuild (#182)
    * Author: Simon de Vlieger, Reviewers: Michael Vogt

— Somewhere on the Internet, 2025-04-02


* Fri Mar 14 2025 Packit <hello@packit.dev> - 14-1
Changes with 14
----------------
  * build(deps): bump github.com/cheggaaa/pb/v3 from 3.1.6 to 3.1.7 in the go-deps group (#147)
    * Author: dependabot[bot], Reviewers: Simon de Vlieger
  * doc: fix typo (#152)
    * Author: Simon de Vlieger, Reviewers: Michael Vogt
  * ibcli: add new --output-name flag and predictable default names (#158)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * main: fix creating output dir for `--with-buildlog` (#150)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou, Simon de Vlieger
  * main: show "success" message with output dir when build finishes (#154)
    * Author: Michael Vogt, Reviewers: Simon de Vlieger
  * main: skip arch checks on`IMAGE_BUILDER_EXPERIMENTAL=bootstrap` (#155)
    * Author: Michael Vogt, Reviewers: Achilleas Koutsou
  * packit: enable epel-9 and epel-10 (#149)
    * Author: Simon de Vlieger, Reviewers: Michael Vogt, Ondřej Budai

— Somewhere on the Internet, 2025-03-14


* Wed Mar 05 2025 Packit <hello@packit.dev> - 13-1
Changes with 13
----------------
  * chore: bump deps (#146)
    * Author: Simon de Vlieger, Reviewers: Brian C. Lane
  * main: add build --with-buildlog (#106)
    * Author: Michael Vogt, Reviewers: Ondřej Budai, Simon de Vlieger
  * main: argument names (#138)
    * Author: Simon de Vlieger, Reviewers: Michael Vogt, Tomáš Hozza
  * more doc updates (#132)
    * Author: Simon de Vlieger, Reviewers: Michael Vogt
  * readme: update installation instructions (#143)
    * Author: Simon de Vlieger, Reviewers: Ondřej Budai

— Somewhere on the Internet, 2025-03-05


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
