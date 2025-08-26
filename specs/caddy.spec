%global goipath         github.com/caddyserver/caddy

%if %{defined el8}
%global gotest() go test -short -compiler gc -ldflags "${LDFLAGS:-}" %{?**};
%else
%global gotestflags %{gocompilerflags} -short
%endif

Name:           caddy
Version:        2.10.2
Release:        %autorelease
Summary:        Web server with automatic HTTPS
URL:            https://caddyserver.com

# main source code is Apache-2.0
# see comments above bundled provides for a breakdown of the rest
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

Requires:       system-logos-httpd
Provides:       webserver

# https://github.com/caddyserver/caddy/commit/05acc5131ed5c80acbd28ed8d907b166cd15b72c
BuildRequires:  golang >= 1.25

# Apache-2.0:
Provides:       bundled(golang(cel.dev/expr)) = 0.24.0
Provides:       bundled(golang(cloud.google.com/go/auth)) = 0.16.2
Provides:       bundled(golang(cloud.google.com/go/auth/oauth2adapt)) = 0.2.8
Provides:       bundled(golang(cloud.google.com/go/compute/metadata)) = 0.7.0
Provides:       bundled(golang(github.com/Masterminds/goutils)) = 1.1.1
Provides:       bundled(golang(github.com/caddyserver/certmagic)) = 0.24.0
Provides:       bundled(golang(github.com/coreos/go-oidc/v3)) = 3.14.1
Provides:       bundled(golang(github.com/dgraph-io/badger)) = 1.6.2
Provides:       bundled(golang(github.com/dgraph-io/badger/v2)) = 2.2007.4
Provides:       bundled(golang(github.com/go-logr/logr)) = 1.4.3
Provides:       bundled(golang(github.com/go-logr/stdr)) = 1.2.2
Provides:       bundled(golang(github.com/google/cel-go)) = 0.26.0
Provides:       bundled(golang(github.com/google/certificate-transparency-go)) = 74a5dd3
Provides:       bundled(golang(github.com/google/go-tpm)) = 0.9.5
Provides:       bundled(golang(github.com/google/go-tspi)) = 0.3.0
Provides:       bundled(golang(github.com/google/s2a-go)) = 0.1.9
Provides:       bundled(golang(github.com/googleapis/enterprise-certificate-proxy)) = 0.3.6
Provides:       bundled(golang(github.com/inconshreveable/mousetrap)) = 1.1.0
Provides:       bundled(golang(github.com/kylelemons/godebug)) = 1.1.0
Provides:       bundled(golang(github.com/pires/go-proxyproto)) = 0.8.1
Provides:       bundled(golang(github.com/prometheus/client_model)) = 0.6.2
Provides:       bundled(golang(github.com/prometheus/common)) = 0.65.0
Provides:       bundled(golang(github.com/prometheus/procfs)) = 0.16.1
Provides:       bundled(golang(github.com/smallstep/go-attestation)) = 2306d5b
Provides:       bundled(golang(github.com/smallstep/linkedca)) = 0.23.0
Provides:       bundled(golang(github.com/smallstep/nosql)) = 0.7.0
Provides:       bundled(golang(github.com/smallstep/truststore)) = 0.13.0
Provides:       bundled(golang(github.com/spf13/cobra)) = 1.9.1
Provides:       bundled(golang(go.opentelemetry.io/auto/sdk)) = 1.1.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = 0.61.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/autoprop)) = 0.62.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/aws)) = 1.37.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/b3)) = 1.37.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/jaeger)) = 1.37.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/propagators/ot)) = 1.37.0
Provides:       bundled(golang(go.opentelemetry.io/otel)) = 1.37.0
Provides:       bundled(golang(go.opentelemetry.io/otel/exporters/otlp/otlptrace)) = 1.37.0
Provides:       bundled(golang(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)) = 1.37.0
Provides:       bundled(golang(go.opentelemetry.io/otel/metric)) = 1.37.0
Provides:       bundled(golang(go.opentelemetry.io/otel/sdk)) = 1.37.0
Provides:       bundled(golang(go.opentelemetry.io/otel/trace)) = 1.37.0
Provides:       bundled(golang(go.opentelemetry.io/proto/otlp)) = 1.7.0
Provides:       bundled(golang(go.uber.org/mock)) = 0.5.2
Provides:       bundled(golang(google.golang.org/genproto/googleapis/api)) = 513f239
Provides:       bundled(golang(google.golang.org/genproto/googleapis/rpc)) = 513f239
Provides:       bundled(golang(google.golang.org/grpc)) = 1.73.0
Provides:       bundled(golang(google.golang.org/grpc/cmd/protoc-gen-go-grpc)) = 1.5.1

# BSD-2-Clause:
Provides:       bundled(golang(github.com/pkg/errors)) = 0.9.1
Provides:       bundled(golang(github.com/russross/blackfriday/v2)) = 2.1.0

# BSD-3-Clause:
Provides:       bundled(golang(dario.cat/mergo)) = 1.0.1
Provides:       bundled(golang(github.com/antlr4-go/antlr/v4)) = 4.13.0
Provides:       bundled(golang(github.com/cloudflare/circl)) = 1.6.1
Provides:       bundled(golang(github.com/golang/protobuf)) = 1.5.4
Provides:       bundled(golang(github.com/golang/snappy)) = 0.0.4
Provides:       bundled(golang(github.com/google/uuid)) = 1.6.0
Provides:       bundled(golang(github.com/grpc-ecosystem/grpc-gateway/v2)) = 2.27.1
Provides:       bundled(golang(github.com/manifoldco/promptui)) = 0.9.0
Provides:       bundled(golang(github.com/miekg/dns)) = 1.1.63
Provides:       bundled(golang(github.com/munnerz/goautoneg)) = a7dc8b6
Provides:       bundled(golang(github.com/pbnjay/memory)) = 7b4eea6
Provides:       bundled(golang(github.com/pmezard/go-difflib)) = 1.0.0
Provides:       bundled(golang(github.com/spf13/pflag)) = 1.0.7
Provides:       bundled(golang(github.com/tailscale/tscert)) = d3f8340
Provides:       bundled(golang(golang.org/x/crypto)) = 0.40.0
Provides:       bundled(golang(golang.org/x/crypto/x509roots/fallback)) = 49bf5b8
Provides:       bundled(golang(golang.org/x/exp)) = 7e4ce0a
Provides:       bundled(golang(golang.org/x/mod)) = 0.25.0
Provides:       bundled(golang(golang.org/x/net)) = 0.42.0
Provides:       bundled(golang(golang.org/x/oauth2)) = 0.30.0
Provides:       bundled(golang(golang.org/x/sync)) = 0.16.0
Provides:       bundled(golang(golang.org/x/sys)) = 0.34.0
Provides:       bundled(golang(golang.org/x/term)) = 0.33.0
Provides:       bundled(golang(golang.org/x/text)) = 0.27.0
Provides:       bundled(golang(golang.org/x/time)) = 0.12.0
Provides:       bundled(golang(golang.org/x/tools)) = 0.34.0
Provides:       bundled(golang(google.golang.org/api)) = 0.240.0
Provides:       bundled(golang(google.golang.org/protobuf)) = 1.36.6

# CC0-1.0:
Provides:       bundled(golang(github.com/zeebo/blake3)) = 0.2.4

# ISC:
Provides:       bundled(golang(github.com/davecgh/go-spew)) = 1.1.1

# MIT:
Provides:       bundled(golang(github.com/BurntSushi/toml)) = 1.5.0
Provides:       bundled(golang(github.com/KimMachineGun/automemlimit)) = 0.7.4
Provides:       bundled(golang(github.com/Masterminds/semver/v3)) = 3.3.0
Provides:       bundled(golang(github.com/Masterminds/sprig/v3)) = 3.3.0
Provides:       bundled(golang(github.com/Microsoft/go-winio)) = 0.6.0
Provides:       bundled(golang(github.com/alecthomas/chroma/v2)) = 2.20.0
Provides:       bundled(golang(github.com/aryann/difflib)) = ff5ff6d
Provides:       bundled(golang(github.com/beorn7/perks)) = 1.0.1
Provides:       bundled(golang(github.com/caddyserver/zerossl)) = 0.1.3
Provides:       bundled(golang(github.com/ccoveille/go-safecast)) = 1.6.1
Provides:       bundled(golang(github.com/cenkalti/backoff/v5)) = 5.0.2
Provides:       bundled(golang(github.com/cespare/xxhash)) = 1.1.0
Provides:       bundled(golang(github.com/cespare/xxhash/v2)) = 2.3.0
Provides:       bundled(golang(github.com/chzyer/readline)) = 1.5.1
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2)) = 2.0.7
Provides:       bundled(golang(github.com/dgryski/go-farm)) = a6ae236
Provides:       bundled(golang(github.com/dlclark/regexp2)) = 1.11.5
Provides:       bundled(golang(github.com/dustin/go-humanize)) = 1.0.1
Provides:       bundled(golang(github.com/felixge/httpsnoop)) = 1.0.4
Provides:       bundled(golang(github.com/francoispqt/gojay)) = 1.2.13
Provides:       bundled(golang(github.com/fxamacker/cbor/v2)) = 2.8.0
Provides:       bundled(golang(github.com/go-chi/chi/v5)) = 5.2.2
Provides:       bundled(golang(github.com/huandu/xstrings)) = 1.5.0
Provides:       bundled(golang(github.com/jackc/pgpassfile)) = 1.0.0
Provides:       bundled(golang(github.com/jackc/pgservicefile)) = 091c0ba
Provides:       bundled(golang(github.com/jackc/pgx/v5)) = 5.6.0
Provides:       bundled(golang(github.com/jackc/puddle/v2)) = 2.2.1
Provides:       bundled(golang(github.com/klauspost/cpuid/v2)) = 2.3.0
Provides:       bundled(golang(github.com/libdns/libdns)) = 1.1.0
Provides:       bundled(golang(github.com/mattn/go-colorable)) = 0.1.13
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.20
Provides:       bundled(golang(github.com/mgutz/ansi)) = d51e80e
Provides:       bundled(golang(github.com/mitchellh/copystructure)) = 1.2.0
Provides:       bundled(golang(github.com/mitchellh/go-ps)) = 1.0.0
Provides:       bundled(golang(github.com/mitchellh/reflectwalk)) = 1.0.2
Provides:       bundled(golang(github.com/quic-go/qpack)) = 0.5.1
Provides:       bundled(golang(github.com/quic-go/quic-go)) = 0.54.0
Provides:       bundled(golang(github.com/rs/xid)) = 1.6.0
Provides:       bundled(golang(github.com/shopspring/decimal)) = 1.4.0
Provides:       bundled(golang(github.com/shurcooL/sanitized_anchor_name)) = 1.0.0
Provides:       bundled(golang(github.com/sirupsen/logrus)) = 1.9.3
Provides:       bundled(golang(github.com/slackhq/nebula)) = 1.9.5
Provides:       bundled(golang(github.com/smallstep/pkcs7)) = 0.2.1
Provides:       bundled(golang(github.com/spf13/cast)) = 1.7.0
Provides:       bundled(golang(github.com/stoewer/go-strcase)) = 1.2.0
Provides:       bundled(golang(github.com/stretchr/testify)) = 1.10.0
Provides:       bundled(golang(github.com/urfave/cli)) = 1.22.17
Provides:       bundled(golang(github.com/x448/float16)) = 0.8.4
Provides:       bundled(golang(github.com/yuin/goldmark)) = 1.7.13
Provides:       bundled(golang(github.com/yuin/goldmark-highlighting/v2)) = 37449ab
Provides:       bundled(golang(go.etcd.io/bbolt)) = 1.3.10
Provides:       bundled(golang(go.uber.org/automaxprocs)) = 1.6.0
Provides:       bundled(golang(go.uber.org/multierr)) = 1.11.0
Provides:       bundled(golang(go.uber.org/zap)) = 1.27.0
Provides:       bundled(golang(go.uber.org/zap/exp)) = 0.3.0
Provides:       bundled(golang(gopkg.in/natefinch/lumberjack.v2)) = 2.2.1

# MPL-2.0:
Provides:       bundled(golang(github.com/go-sql-driver/mysql)) = 1.8.1

# Apache-2.0 AND BSD-2-Clause:
Provides:       bundled(golang(go.step.sm/crypto)) = 0.67.0
Provides:       bundled(golang(github.com/smallstep/cli-utils)) = 0.12.1

# Apache-2.0 AND BSD-3-Clause:
Provides:       bundled(golang(github.com/go-jose/go-jose/v3)) = 3.0.4
Provides:       bundled(golang(github.com/go-jose/go-jose/v4)) = 4.0.5
Provides:       bundled(golang(github.com/googleapis/gax-go/v2)) = 2.14.2
Provides:       bundled(golang(github.com/mholt/acmez/v3)) = 3.1.2
Provides:       bundled(golang(github.com/smallstep/certificates)) = 0.28.4

# Apache-2.0 AND MIT:
Provides:       bundled(golang(github.com/dgraph-io/ristretto)) = 0.2.0
Provides:       bundled(golang(gopkg.in/yaml.v3)) = 3.0.1

# BSD-1-Clause AND BSD-3-Clause:
Provides:       bundled(golang(filippo.io/edwards25519)) = 1.1.0

# BSD-2-Clause-Views AND BSD-3-Clause:
Provides:       bundled(golang(howett.net/plist)) = 1.0.0

# BSD-3-Clause AND MIT:
Provides:       bundled(golang(github.com/smallstep/scep)) = 8cf1ca4

# CC0-1.0 AND MIT:
Provides:       bundled(golang(github.com/AndreasBriese/bbloom)) = 46b345b

# Apache-2.0 AND BSD-3-Clause AND MIT:
Provides:       bundled(golang(github.com/klauspost/compress)) = 1.18.0
Provides:       bundled(golang(github.com/prometheus/client_golang)) = 1.23.0


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
