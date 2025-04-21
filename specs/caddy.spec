%global goipath         github.com/caddyserver/caddy

%if %{defined el8}
%global gotest() go test -short -compiler gc -ldflags "${LDFLAGS:-}" %{?**};
%else
%global gotestflags %{gocompilerflags} -short
%endif

Name:           caddy
Version:        2.10.0
Release:        %autorelease
Summary:        Web server with automatic HTTPS
URL:            https://caddyserver.com

# main source code is Apache-2.0
# Apache-2.0:
#   cel.dev/expr
#   github.com/Masterminds/goutils
#   github.com/caddyserver/certmagic
#   github.com/dgraph-io/badger
#   github.com/dgraph-io/badger/v2
#   github.com/go-logr/logr
#   github.com/go-logr/stdr
#   github.com/google/cel-go
#   github.com/google/certificate-transparency-go
#   github.com/google/go-tpm
#   github.com/google/go-tspi
#   github.com/google/pprof
#   github.com/inconshreveable/mousetrap
#   github.com/pires/go-proxyproto
#   github.com/prometheus/client_model
#   github.com/prometheus/procfs
#   github.com/smallstep/go-attestation
#   github.com/smallstep/nosql
#   github.com/smallstep/truststore
#   github.com/spf13/cobra
#   go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
#   go.opentelemetry.io/contrib/propagators/autoprop
#   go.opentelemetry.io/contrib/propagators/aws
#   go.opentelemetry.io/contrib/propagators/b3
#   go.opentelemetry.io/contrib/propagators/jaeger
#   go.opentelemetry.io/contrib/propagators/ot
#   go.opentelemetry.io/otel
#   go.opentelemetry.io/otel/exporters/otlp/otlptrace
#   go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc
#   go.opentelemetry.io/otel/metric
#   go.opentelemetry.io/otel/sdk
#   go.opentelemetry.io/otel/trace
#   go.opentelemetry.io/proto/otlp
#   go.step.sm/linkedca
#   go.uber.org/mock
#   google.golang.org/genproto/googleapis/api
#   google.golang.org/genproto/googleapis/rpc
#   google.golang.org/grpc
# BSD-2-Clause:
#   github.com/pkg/errors
#   github.com/russross/blackfriday/v2
# BSD-3-Clause:
#   dario.cat/mergo
#   github.com/antlr4-go/antlr/v4
#   github.com/cloudflare/circl
#   github.com/golang/protobuf
#   github.com/golang/snappy
#   github.com/google/uuid
#   github.com/grpc-ecosystem/grpc-gateway/v2
#   github.com/manifoldco/promptui
#   github.com/miekg/dns
#   github.com/pbnjay/memory
#   github.com/pmezard/go-difflib
#   github.com/spf13/pflag
#   github.com/tailscale/tscert
#   golang.org/x/crypto
#   golang.org/x/crypto/x509roots/fallback
#   golang.org/x/exp
#   golang.org/x/mod
#   golang.org/x/net
#   golang.org/x/sync
#   golang.org/x/sys
#   golang.org/x/term
#   golang.org/x/text
#   golang.org/x/time
#   golang.org/x/tools
#   google.golang.org/protobuf
# CC0-1.0:
#   github.com/zeebo/blake3
# ISC:
#   github.com/davecgh/go-spew
# MIT:
#   github.com/BurntSushi/toml
#   github.com/KimMachineGun/automemlimit
#   github.com/Masterminds/semver/v3
#   github.com/Masterminds/sprig/v3
#   github.com/Microsoft/go-winio
#   github.com/alecthomas/chroma/v2
#   github.com/aryann/difflib
#   github.com/beorn7/perks
#   github.com/caddyserver/zerossl
#   github.com/cenkalti/backoff/v4
#   github.com/cespare/xxhash
#   github.com/cespare/xxhash/v2
#   github.com/chzyer/readline
#   github.com/cpuguy83/go-md2man/v2
#   github.com/dgryski/go-farm
#   github.com/dlclark/regexp2
#   github.com/dustin/go-humanize
#   github.com/felixge/httpsnoop
#   github.com/francoispqt/gojay
#   github.com/fxamacker/cbor/v2
#   github.com/go-chi/chi/v5
#   github.com/go-kit/kit
#   github.com/go-kit/log
#   github.com/go-logfmt/logfmt
#   github.com/go-task/slim-sprig
#   github.com/huandu/xstrings
#   github.com/jackc/chunkreader/v2
#   github.com/jackc/pgconn
#   github.com/jackc/pgio
#   github.com/jackc/pgpassfile
#   github.com/jackc/pgproto3/v2
#   github.com/jackc/pgservicefile
#   github.com/jackc/pgtype
#   github.com/klauspost/cpuid/v2
#   github.com/libdns/libdns
#   github.com/mattn/go-colorable
#   github.com/mattn/go-isatty
#   github.com/mgutz/ansi
#   github.com/mitchellh/copystructure
#   github.com/mitchellh/go-ps
#   github.com/mitchellh/reflectwalk
#   github.com/onsi/ginkgo/v2
#   github.com/quic-go/qpack
#   github.com/quic-go/quic-go
#   github.com/rs/xid
#   github.com/shopspring/decimal
#   github.com/shurcooL/sanitized_anchor_name
#   github.com/sirupsen/logrus
#   github.com/slackhq/nebula
#   github.com/smallstep/pkcs7
#   github.com/spf13/cast
#   github.com/stoewer/go-strcase
#   github.com/stretchr/testify
#   github.com/urfave/cli
#   github.com/x448/float16
#   github.com/yuin/goldmark
#   github.com/yuin/goldmark-highlighting/v2
#   go.etcd.io/bbolt
#   go.uber.org/automaxprocs
#   go.uber.org/multierr
#   go.uber.org/zap
#   go.uber.org/zap/exp
#   gopkg.in/natefinch/lumberjack.v2
# MPL-2.0:
#   github.com/go-sql-driver/mysql
# Apache-2.0 AND BSD-2-Clause:
#   go.step.sm/cli-utils
#   go.step.sm/crypto
# Apache-2.0 AND BSD-3-Clause:
#   github.com/go-jose/go-jose/v3
#   github.com/mholt/acmez/v3
#   github.com/prometheus/common
#   github.com/smallstep/certificates
# Apache-2.0 AND MIT:
#   github.com/dgraph-io/ristretto
#   github.com/prometheus/client_golang
#   gopkg.in/yaml.v3
# BSD-2-Clause-Views AND BSD-3-Clause:
#   howett.net/plist
# BSD-3-Clause AND Apache-2.0 AND MIT:
#   github.com/klauspost/compress
# BSD-3-Clause AND BSD-1-Clause:
#   filippo.io/edwards25519
# MIT AND BSD-3-Clause:
#   github.com/jackc/pgx/v4
#   github.com/smallstep/scep
# MIT AND CC0-1.0:
#   github.com/AndreasBriese/bbloom
License:        Apache-2.0 AND BSD-1-Clause AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND MPL-2.0

Source0:        https://%{goipath}/archive/v%{version}/caddy-%{version}.tar.gz
Source1:        caddy-%{version}-vendor.tar.gz
Source2:        create-vendor-tarball.sh

# based on reference files upstream
# https://github.com/caddyserver/dist
Source10:       Caddyfile
Source20:       caddy.service
Source21:       caddy-api.service
Source22:       caddy.sysusers
Source30:       poweredby-white.png
Source31:       poweredby-black.png

# downstream only patch to disable commands that can alter the binary
Patch1:         0001-Disable-commands-that-can-alter-the-binary.patch

%if %{defined el8}
ExclusiveArch:  %{golang_arches}
%else
BuildRequires:  go-rpm-macros
ExclusiveArch:  %{golang_arches_future}
%endif

BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%{?sysusers_requires_compat}

# https://github.com/caddyserver/caddy/commit/172136a0a0f6aa47be4eab3727fa2482d7af6617
BuildRequires:  golang >= 1.24
Requires:       system-logos-httpd
Provides:       webserver

Provides:       bundled(golang(cel.dev/expr)) = 0.19.1
Provides:       bundled(golang(dario.cat/mergo)) = 1.0.1
Provides:       bundled(golang(filippo.io/edwards25519)) = 1.1.0
Provides:       bundled(golang(github.com/AndreasBriese/bbloom)) = 46b345b
Provides:       bundled(golang(github.com/BurntSushi/toml)) = 1.4.0
Provides:       bundled(golang(github.com/KimMachineGun/automemlimit)) = 0.7.1
Provides:       bundled(golang(github.com/Masterminds/goutils)) = 1.1.1
Provides:       bundled(golang(github.com/Masterminds/semver/v3)) = 3.3.0
Provides:       bundled(golang(github.com/Masterminds/sprig/v3)) = 3.3.0
Provides:       bundled(golang(github.com/Microsoft/go-winio)) = 0.6.0
Provides:       bundled(golang(github.com/alecthomas/chroma/v2)) = 2.15.0
Provides:       bundled(golang(github.com/antlr4-go/antlr/v4)) = 4.13.0
Provides:       bundled(golang(github.com/aryann/difflib)) = ff5ff6d
Provides:       bundled(golang(github.com/beorn7/perks)) = 1.0.1
Provides:       bundled(golang(github.com/caddyserver/certmagic)) = 0.23.0
Provides:       bundled(golang(github.com/caddyserver/zerossl)) = 0.1.3
Provides:       bundled(golang(github.com/cenkalti/backoff/v4)) = 4.3.0
Provides:       bundled(golang(github.com/cespare/xxhash)) = 1.1.0
Provides:       bundled(golang(github.com/cespare/xxhash/v2)) = 2.3.0
Provides:       bundled(golang(github.com/chzyer/readline)) = 1.5.1
Provides:       bundled(golang(github.com/cloudflare/circl)) = 1.6.0
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2)) = 2.0.6
Provides:       bundled(golang(github.com/davecgh/go-spew)) = 1.1.1
Provides:       bundled(golang(github.com/dgraph-io/badger)) = 1.6.2
Provides:       bundled(golang(github.com/dgraph-io/badger/v2)) = 2.2007.4
Provides:       bundled(golang(github.com/dgraph-io/ristretto)) = 0.2.0
Provides:       bundled(golang(github.com/dgryski/go-farm)) = a6ae236
Provides:       bundled(golang(github.com/dlclark/regexp2)) = 1.11.4
Provides:       bundled(golang(github.com/dustin/go-humanize)) = 1.0.1
Provides:       bundled(golang(github.com/felixge/httpsnoop)) = 1.0.4
Provides:       bundled(golang(github.com/francoispqt/gojay)) = 1.2.13
Provides:       bundled(golang(github.com/fxamacker/cbor/v2)) = 2.6.0
Provides:       bundled(golang(github.com/go-chi/chi/v5)) = 5.2.1
Provides:       bundled(golang(github.com/go-jose/go-jose/v3)) = 3.0.4
Provides:       bundled(golang(github.com/go-kit/kit)) = 0.13.0
Provides:       bundled(golang(github.com/go-kit/log)) = 0.2.1
Provides:       bundled(golang(github.com/go-logfmt/logfmt)) = 0.6.0
Provides:       bundled(golang(github.com/go-logr/logr)) = 1.4.2
Provides:       bundled(golang(github.com/go-logr/stdr)) = 1.2.2
Provides:       bundled(golang(github.com/go-sql-driver/mysql)) = 1.7.1
Provides:       bundled(golang(github.com/go-task/slim-sprig)) = 52ccab3
Provides:       bundled(golang(github.com/golang/protobuf)) = 1.5.4
Provides:       bundled(golang(github.com/golang/snappy)) = 0.0.4
Provides:       bundled(golang(github.com/google/cel-go)) = 0.24.1
Provides:       bundled(golang(github.com/google/certificate-transparency-go)) = 74a5dd3
Provides:       bundled(golang(github.com/google/go-tpm)) = 0.9.0
Provides:       bundled(golang(github.com/google/go-tspi)) = 0.3.0
Provides:       bundled(golang(github.com/google/pprof)) = ec68065
Provides:       bundled(golang(github.com/google/uuid)) = 1.6.0
Provides:       bundled(golang(github.com/grpc-ecosystem/grpc-gateway/v2)) = 2.22.0
Provides:       bundled(golang(github.com/huandu/xstrings)) = 1.5.0
Provides:       bundled(golang(github.com/inconshreveable/mousetrap)) = 1.1.0
Provides:       bundled(golang(github.com/jackc/chunkreader/v2)) = 2.0.1
Provides:       bundled(golang(github.com/jackc/pgconn)) = 1.14.3
Provides:       bundled(golang(github.com/jackc/pgio)) = 1.0.0
Provides:       bundled(golang(github.com/jackc/pgpassfile)) = 1.0.0
Provides:       bundled(golang(github.com/jackc/pgproto3/v2)) = 2.3.3
Provides:       bundled(golang(github.com/jackc/pgservicefile)) = 091c0ba
Provides:       bundled(golang(github.com/jackc/pgtype)) = 1.14.0
Provides:       bundled(golang(github.com/jackc/pgx/v4)) = 4.18.3
Provides:       bundled(golang(github.com/klauspost/compress)) = 1.18.0
Provides:       bundled(golang(github.com/klauspost/cpuid/v2)) = 2.2.10
Provides:       bundled(golang(github.com/libdns/libdns)) = 1.0.0-beta.1
Provides:       bundled(golang(github.com/manifoldco/promptui)) = 0.9.0
Provides:       bundled(golang(github.com/mattn/go-colorable)) = 0.1.13
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides:       bundled(golang(github.com/mgutz/ansi)) = d51e80e
Provides:       bundled(golang(github.com/mholt/acmez/v3)) = 3.1.2
Provides:       bundled(golang(github.com/miekg/dns)) = 1.1.63
Provides:       bundled(golang(github.com/mitchellh/copystructure)) = 1.2.0
Provides:       bundled(golang(github.com/mitchellh/go-ps)) = 1.0.0
Provides:       bundled(golang(github.com/mitchellh/reflectwalk)) = 1.0.2
Provides:       bundled(golang(github.com/onsi/ginkgo/v2)) = 2.13.2
Provides:       bundled(golang(github.com/pbnjay/memory)) = 7b4eea6
Provides:       bundled(golang(github.com/pires/go-proxyproto)) = b718e7c
Provides:       bundled(golang(github.com/pkg/errors)) = 0.9.1
Provides:       bundled(golang(github.com/pmezard/go-difflib)) = 1.0.0
Provides:       bundled(golang(github.com/prometheus/client_golang)) = 1.19.1
Provides:       bundled(golang(github.com/prometheus/client_model)) = 0.5.0
Provides:       bundled(golang(github.com/prometheus/common)) = 0.48.0
Provides:       bundled(golang(github.com/prometheus/procfs)) = 0.12.0
Provides:       bundled(golang(github.com/quic-go/qpack)) = 0.5.1
Provides:       bundled(golang(github.com/quic-go/quic-go)) = 0.50.1
Provides:       bundled(golang(github.com/rs/xid)) = 1.5.0
Provides:       bundled(golang(github.com/russross/blackfriday/v2)) = 2.1.0
Provides:       bundled(golang(github.com/shopspring/decimal)) = 1.4.0
Provides:       bundled(golang(github.com/shurcooL/sanitized_anchor_name)) = 1.0.0
Provides:       bundled(golang(github.com/sirupsen/logrus)) = 1.9.3
Provides:       bundled(golang(github.com/slackhq/nebula)) = 1.6.1
Provides:       bundled(golang(github.com/smallstep/certificates)) = 0.26.1
Provides:       bundled(golang(github.com/smallstep/go-attestation)) = 413678f
Provides:       bundled(golang(github.com/smallstep/nosql)) = 0.6.1
Provides:       bundled(golang(github.com/smallstep/pkcs7)) = 3b98ecc
Provides:       bundled(golang(github.com/smallstep/scep)) = aee96d7
Provides:       bundled(golang(github.com/smallstep/truststore)) = 0.13.0
Provides:       bundled(golang(github.com/spf13/cast)) = 1.7.0
Provides:       bundled(golang(github.com/spf13/cobra)) = 1.9.1
Provides:       bundled(golang(github.com/spf13/pflag)) = 1.0.6
Provides:       bundled(golang(github.com/stoewer/go-strcase)) = 1.2.0
Provides:       bundled(golang(github.com/stretchr/testify)) = 1.10.0
Provides:       bundled(golang(github.com/tailscale/tscert)) = d3f8340
Provides:       bundled(golang(github.com/urfave/cli)) = 1.22.14
Provides:       bundled(golang(github.com/x448/float16)) = 0.8.4
Provides:       bundled(golang(github.com/yuin/goldmark)) = 1.7.8
Provides:       bundled(golang(github.com/yuin/goldmark-highlighting/v2)) = 37449ab
Provides:       bundled(golang(github.com/zeebo/blake3)) = 0.2.4
Provides:       bundled(golang(go.etcd.io/bbolt)) = 1.3.9
Provides:       bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = 0.56.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/autoprop)) = 0.42.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/aws)) = 1.17.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/b3)) = 1.17.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/jaeger)) = 1.17.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/ot)) = 1.17.0
Provides:       bundled(golang(go.opentelemetry.io/otel)) = 1.31.0
Provides:       bundled(golang(go.opentelemetry.io/otel/exporters/otlp/otlptrace)) = 1.31.0
Provides:       bundled(golang(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)) = 1.31.0
Provides:       bundled(golang(go.opentelemetry.io/otel/metric)) = 1.31.0
Provides:       bundled(golang(go.opentelemetry.io/otel/sdk)) = 1.31.0
Provides:       bundled(golang(go.opentelemetry.io/otel/trace)) = 1.31.0
Provides:       bundled(golang(go.opentelemetry.io/proto/otlp)) = 1.3.1
Provides:       bundled(golang(go.step.sm/cli-utils)) = 0.9.0
Provides:       bundled(golang(go.step.sm/crypto)) = 0.45.0
Provides:       bundled(golang(go.step.sm/linkedca)) = 0.20.1
Provides:       bundled(golang(go.uber.org/automaxprocs)) = 1.6.0
Provides:       bundled(golang(go.uber.org/mock)) = 0.5.0
Provides:       bundled(golang(go.uber.org/multierr)) = 1.11.0
Provides:       bundled(golang(go.uber.org/zap)) = 1.27.0
Provides:       bundled(golang(go.uber.org/zap/exp)) = 0.3.0
Provides:       bundled(golang(golang.org/x/crypto)) = 0.36.0
Provides:       bundled(golang(golang.org/x/crypto/x509roots/fallback)) = 49bf5b8
Provides:       bundled(golang(golang.org/x/exp)) = 9bf2ced
Provides:       bundled(golang(golang.org/x/mod)) = 0.24.0
Provides:       bundled(golang(golang.org/x/net)) = 0.38.0
Provides:       bundled(golang(golang.org/x/sync)) = 0.12.0
Provides:       bundled(golang(golang.org/x/sys)) = 0.31.0
Provides:       bundled(golang(golang.org/x/term)) = 0.30.0
Provides:       bundled(golang(golang.org/x/text)) = 0.23.0
Provides:       bundled(golang(golang.org/x/time)) = 0.11.0
Provides:       bundled(golang(golang.org/x/tools)) = 0.31.0
Provides:       bundled(golang(google.golang.org/genproto/googleapis/api)) = 5fefd90
Provides:       bundled(golang(google.golang.org/genproto/googleapis/rpc)) = 5fefd90
Provides:       bundled(golang(google.golang.org/grpc)) = 1.67.1
Provides:       bundled(golang(google.golang.org/protobuf)) = 1.35.1
Provides:       bundled(golang(gopkg.in/natefinch/lumberjack.v2)) = 2.2.1
Provides:       bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
Provides:       bundled(golang(howett.net/plist)) = 1.0.0


%description
Caddy is an extensible server platform that uses TLS by default.


%prep
%autosetup -p 1 -a 1
mkdir -p src/$(dirname %{goipath})
ln -s $PWD src/%{goipath}


%build
%if %{defined el8}
export GO111MODULE=off
%endif
export GOPATH=$PWD
export LDFLAGS="-X %{goipath}.CustomVersion=v%{version}"
%gobuild -o bin/caddy %{goipath}/cmd/caddy


%install
# command
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/caddy

# man pages
./bin/caddy manpage --directory %{buildroot}%{_mandir}/man8

# config
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/caddy %{S:10}
install -d -m 0755 %{buildroot}%{_sysconfdir}/caddy/Caddyfile.d

# systemd units
install -D -p -m 0644 -t %{buildroot}%{_unitdir} %{S:20} %{S:21}

# sysusers
install -D -p -m 0644 %{S:22} %{buildroot}%{_sysusersdir}/caddy.conf

# data directory
install -d -m 0750 %{buildroot}%{_sharedstatedir}/caddy

# welcome page
%if %{defined fedora}
install -D -p -m 0644 %{S:30} %{buildroot}%{_datadir}/caddy/poweredby.png
ln -s ../fedora-testpage/index.html %{buildroot}%{_datadir}/caddy/index.html
%else
install -D -p -m 0644 %{S:31} %{buildroot}%{_datadir}/caddy/poweredby.png
ln -s ../testpage/index.html %{buildroot}%{_datadir}/caddy/index.html
%endif
install -d -m 0755 %{buildroot}%{_datadir}/caddy/icons
ln -s ../../pixmaps/poweredby.png %{buildroot}%{_datadir}/caddy/icons/poweredby.png
%if %{defined rhel} && 0%{?rhel} >= 9
ln -s ../pixmaps/system-noindex-logo.png %{buildroot}%{_datadir}/caddy/system_noindex_logo.png
%endif

# shell completions
install -d -m 0755 %{buildroot}%{bash_completions_dir}
./bin/caddy completion bash > %{buildroot}%{bash_completions_dir}/caddy
install -d -m 0755 %{buildroot}%{zsh_completions_dir}
./bin/caddy completion zsh > %{buildroot}%{zsh_completions_dir}/_caddy
install -d -m 0755 %{buildroot}%{fish_completions_dir}
./bin/caddy completion fish > %{buildroot}%{fish_completions_dir}/caddy.fish


%check
# ensure that the version was embedded correctly
[[ "$(./bin/caddy version)" == "v%{version}" ]] || exit 1

# run the upstream tests
export GOPATH=$PWD
cd src/%{goipath}
%gotest ./...


%pre
%sysusers_create_compat %{S:22}


%post
%systemd_post caddy.service

if [ -x /usr/sbin/getsebool ]; then
    # connect to ACME endpoint to request certificates
    setsebool -P httpd_can_network_connect on
fi
if [ -x /usr/sbin/semanage -a -x /usr/sbin/restorecon ]; then
    # file contexts
    semanage fcontext --add --type httpd_exec_t        '%{_bindir}/caddy'               2> /dev/null || :
    semanage fcontext --add --type httpd_sys_content_t '%{_datadir}/caddy(/.*)?'        2> /dev/null || :
    semanage fcontext --add --type httpd_config_t      '%{_sysconfdir}/caddy(/.*)?'     2> /dev/null || :
    semanage fcontext --add --type httpd_var_lib_t     '%{_sharedstatedir}/caddy(/.*)?' 2> /dev/null || :
    restorecon -r %{_bindir}/caddy %{_datadir}/caddy %{_sysconfdir}/caddy %{_sharedstatedir}/caddy || :
fi
if [ -x /usr/sbin/semanage ]; then
    # QUIC
    semanage port --add --type http_port_t --proto udp 80   2> /dev/null || :
    semanage port --add --type http_port_t --proto udp 443  2> /dev/null || :
    # admin endpoint
    semanage port --add --type http_port_t --proto tcp 2019 2> /dev/null || :
fi


%preun
%systemd_preun caddy.service


%postun
%systemd_postun_with_restart caddy.service

if [ $1 -eq 0 ]; then
    if [ -x /usr/sbin/getsebool ]; then
        # connect to ACME endpoint to request certificates
        setsebool -P httpd_can_network_connect off
    fi
    if [ -x /usr/sbin/semanage ]; then
        # file contexts
        semanage fcontext --delete --type httpd_exec_t        '%{_bindir}/caddy'               2> /dev/null || :
        semanage fcontext --delete --type httpd_sys_content_t '%{_datadir}/caddy(/.*)?'        2> /dev/null || :
        semanage fcontext --delete --type httpd_config_t      '%{_sysconfdir}/caddy(/.*)?'     2> /dev/null || :
        semanage fcontext --delete --type httpd_var_lib_t     '%{_sharedstatedir}/caddy(/.*)?' 2> /dev/null || :
        # QUIC
        semanage port     --delete --type http_port_t --proto udp 80   2> /dev/null || :
        semanage port     --delete --type http_port_t --proto udp 443  2> /dev/null || :
        # admin endpoint
        semanage port     --delete --type http_port_t --proto tcp 2019 2> /dev/null || :
    fi
fi


%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/caddy
%{_mandir}/man8/caddy*.8*
%{_datadir}/caddy
%{_unitdir}/caddy.service
%{_unitdir}/caddy-api.service
%{_sysusersdir}/caddy.conf
%dir %{_sysconfdir}/caddy
%config(noreplace) %{_sysconfdir}/caddy/Caddyfile
%dir %{_sysconfdir}/caddy/Caddyfile.d
%attr(0750,caddy,caddy) %dir %{_sharedstatedir}/caddy
%if %{defined el8}
# this is normally owned by filesystem
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%endif
%{bash_completions_dir}/caddy
%{zsh_completions_dir}/_caddy
%{fish_completions_dir}/caddy.fish


%changelog
%autochangelog
