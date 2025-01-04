%bcond_with devel

%global basever 1.28.1
#%%global rcnum   0

Name:           syncthing
Summary:        Continuous File Synchronization
Version:        %{basever}%{?rcnum:~rc%{rcnum}}
Release:        %autorelease

%global goipath github.com/syncthing/syncthing
%global tag     v%{basever}%{?rcnum:-rc.%{rcnum}}

%gometa -f

# syncthing (MPL-2.0) bundles
# - angular, bootstrap, daterangepicker, fancytree, jQuery, moment (MIT),
# - HumanizeDuration (MIT OR Unlicense),
# - ForkAwesome (MIT, OFL-1.1, CC-BY-3.0), and
# - a number of go packages (Apache-2.0, BSD-2-Clause, BSD-2-Clause-Views, BSD-3-Clause, ISC, MIT, MPL-2.0)
License:        MPL-2.0 AND Apache-2.0 AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND CC-BY-3.0 AND ISC AND MIT AND OFL-1.1 AND (Apache-2.0 OR MIT) AND (MIT OR Unlicense)

URL:            https://syncthing.net
# use official release tarball (contains vendored dependencies)
Source0:        %{gourl}/releases/download/%{tag}/%{name}-source-%{tag}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  systemd-rpm-macros

Requires:       hicolor-icon-theme

# assets in gui/default/vendor/*
Provides:       bundled(angular) = 1.3.20
Provides:       bundled(angular-dirPagination) = 759009c
Provides:       bundled(angular-sanitize) = 1.3.20
Provides:       bundled(angular-translate) = 2.9.0.1
Provides:       bundled(angular-translate-loader-static-files) = 2.11.0
Provides:       bundled(bootstrap) = 3.3.6
Provides:       bundled(daterangepicker) = 3.1
Provides:       bundled(ForkAwesome) = 1.2.0
Provides:       bundled(HumanizeDuration.js)
Provides:       bundled(jquery) = 2.2.2
Provides:       bundled(jquery-fancytree) = 2.38.0
Provides:       bundled(jquery-ui) = 1.12.1
Provides:       bundled(moment) = 2.19.4

# automatically generated Provides for bundled go dependencies
# manually check licenses for new deps and update License tag if necessary
# generate with "./vendor2provides.py path/to/vendor/modules.txt"

# github.com/AudriusButkevicius/recli : MPL-2.0
Provides:       bundled(golang(github.com/AudriusButkevicius/recli)) = d000ce8
# github.com/Azure/go-ntlmssp : MIT
Provides:       bundled(golang(github.com/Azure/go-ntlmssp)) = 754e693
# github.com/alecthomas/kong : MIT
Provides:       bundled(golang(github.com/alecthomas/kong)) = 1.2.1
# github.com/aws/aws-sdk-go : Apache-2.0
Provides:       bundled(golang(github.com/aws/aws-sdk-go)) = 1.55.5
# github.com/beorn7/perks : MIT
Provides:       bundled(golang(github.com/beorn7/perks)) = 1.0.1
# github.com/calmh/incontainer : MIT
Provides:       bundled(golang(github.com/calmh/incontainer)) = 1.0.0
# github.com/calmh/xdr : MIT
Provides:       bundled(golang(github.com/calmh/xdr)) = 1.2.0
# github.com/ccding/go-stun : Apache-2.0
Provides:       bundled(golang(github.com/ccding/go-stun)) = 0.1.5
# github.com/cenkalti/backoff : MIT
Provides:       bundled(golang(github.com/cenkalti/backoff/v4)) = 4.3.0
# github.com/certifi/gocertifi : MPL-2.0
Provides:       bundled(golang(github.com/certifi/gocertifi)) = 431795d
# github.com/cespare/xxhash : MIT
Provides:       bundled(golang(github.com/cespare/xxhash/v2)) = 2.3.0
# github.com/chmduquesne/rollinghash : MIT
Provides:       bundled(golang(github.com/chmduquesne/rollinghash)) = 4.0.0+incompatible
# github.com/cpuguy83/go-md2man : MIT
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2)) = 2.0.5
# github.com/d4l3k/messagediff : MIT
Provides:       bundled(golang(github.com/d4l3k/messagediff)) = 1.2.1
# github.com/davecgh/go-spew : ISC
Provides:       bundled(golang(github.com/davecgh/go-spew)) = 1.1.1
# github.com/ebitengine/purego : Apache-2.0
Provides:       bundled(golang(github.com/ebitengine/purego)) = 0.8.0
# github.com/fsnotify/fsnotify : BSD-3-Clause
Provides:       bundled(golang(github.com/fsnotify/fsnotify)) = 1.7.0
# github.com/getsentry/raven-go : BSD-3-Clause
Provides:       bundled(golang(github.com/getsentry/raven-go)) = 0.2.0
# github.com/go-asn1-ber/asn1-ber : MIT
Provides:       bundled(golang(github.com/go-asn1-ber/asn1-ber)) = 1.5.7
# github.com/go-ldap/ldap : MIT
Provides:       bundled(golang(github.com/go-ldap/ldap/v3)) = 3.4.8
# github.com/go-ole/go-ole : MIT
Provides:       bundled(golang(github.com/go-ole/go-ole)) = 1.3.0
# github.com/go-task/slim-sprig : MIT
Provides:       bundled(golang(github.com/go-task/slim-sprig/v3)) = 3.0.0
# github.com/gobwas/glob : MIT
Provides:       bundled(golang(github.com/gobwas/glob)) = 0.2.3
# github.com/gofrs/flock : BSD-3-Clause
Provides:       bundled(golang(github.com/gofrs/flock)) = 0.12.1
# github.com/gogo/protobuf : BSD-3-Clause
Provides:       bundled(golang(github.com/gogo/protobuf)) = 1.3.2
# github.com/golang/snappy : BSD-3-Clause
Provides:       bundled(golang(github.com/golang/snappy)) = 0.0.4
# github.com/google/pprof : Apache-2.0
Provides:       bundled(golang(github.com/google/pprof)) = a352233
# github.com/google/uuid : BSD-3-Clause
Provides:       bundled(golang(github.com/google/uuid)) = 1.6.0
# github.com/greatroar/blobloom : Apache-2.0
Provides:       bundled(golang(github.com/greatroar/blobloom)) = 0.8.0
# github.com/hashicorp/errwrap : MPL-2.0
Provides:       bundled(golang(github.com/hashicorp/errwrap)) = 1.1.0
# github.com/hashicorp/go-multierror : MPL-2.0
Provides:       bundled(golang(github.com/hashicorp/go-multierror)) = 1.1.1
# github.com/hashicorp/golang-lru : MPL-2.0
Provides:       bundled(golang(github.com/hashicorp/golang-lru/v2)) = 2.0.7
# github.com/jackpal/gateway : BSD-3-Clause
Provides:       bundled(golang(github.com/jackpal/gateway)) = 1.0.15
# github.com/jackpal/go-nat-pmp : Apache-2.0
Provides:       bundled(golang(github.com/jackpal/go-nat-pmp)) = 1.0.2
# github.com/jmespath/go-jmespath : Apache-2.0
Provides:       bundled(golang(github.com/jmespath/go-jmespath)) = 0.4.0
# github.com/julienschmidt/httprouter : BSD-3-Clause
Provides:       bundled(golang(github.com/julienschmidt/httprouter)) = 1.3.0
# github.com/kballard/go-shellquote : MIT
Provides:       bundled(golang(github.com/kballard/go-shellquote)) = 95032a8
# github.com/lib/pq : MIT
Provides:       bundled(golang(github.com/lib/pq)) = 1.10.9
# github.com/klauspost/compress : BSD-3-Clause AND Apache-2.0
Provides:       bundled(golang(github.com/klauspost/compress)) = 1.17.11
# github.com/lufia/plan9stats : BSD-3-Clause
Provides:       bundled(golang(github.com/lufia/plan9stats)) = 873cd01
# github.com/maruel/panicparse : Apache-2.0
Provides:       bundled(golang(github.com/maruel/panicparse/v2)) = 2.3.1
# github.com/maxbrunsfeld/counterfeiter : MIT
Provides:       bundled(golang(github.com/maxbrunsfeld/counterfeiter/v6)) = 6.8.1
# github.com/maxmind/geoipupdate : Apache-2.0 OR MIT
Provides:       bundled(golang(github.com/maxmind/geoipupdate/v6)) = 6.1.0
# github.com/miscreant/miscreant.go : MIT
Provides:       bundled(golang(github.com/miscreant/miscreant.go)) = 26d3763
# github.com/munnerz/goautoneg : BSD-3-Clause
Provides:       bundled(golang(github.com/munnerz/goautoneg)) = a7dc8b6
# github.com/nxadm/tail : MIT
Provides:       bundled(golang(github.com/nxadm/tail)) = 1.4.11
# github.com/onsi/ginkgo : MIT
Provides:       bundled(golang(github.com/onsi/ginkgo/v2)) = 2.20.2
# github.com/oschwald/geoip2-golang : ISC
Provides:       bundled(golang(github.com/oschwald/geoip2-golang)) = 1.11.0
# github.com/oschwald/maxminddb-golang : ISC
Provides:       bundled(golang(github.com/oschwald/maxminddb-golang)) = 1.13.1
# github.com/pierrec/lz4 : BSD-3-Clause
Provides:       bundled(golang(github.com/pierrec/lz4/v4)) = 4.1.21
# github.com/pkg/errors : BSD-2-Clause
Provides:       bundled(golang(github.com/pkg/errors)) = 0.9.1
# github.com/pmezard/go-difflib : BSD-3-Clause
Provides:       bundled(golang(github.com/pmezard/go-difflib)) = 1.0.0
# github.com/posener/complete : MIT
Provides:       bundled(golang(github.com/posener/complete)) = 1.2.3
# github.com/power-devops/perfstat : MIT
Provides:       bundled(golang(github.com/power-devops/perfstat)) = 82ca368
# github.com/prometheus/client_golang : Apache-2.0
Provides:       bundled(golang(github.com/prometheus/client_golang)) = 1.20.5
# github.com/prometheus/client_model : Apache-2.0
Provides:       bundled(golang(github.com/prometheus/client_model)) = 0.6.1
# github.com/prometheus/common : Apache-2.0
Provides:       bundled(golang(github.com/prometheus/common)) = 0.60.0
# github.com/prometheus/procfs : Apache-2.0
Provides:       bundled(golang(github.com/prometheus/procfs)) = 0.15.1
# github.com/puzpuzpuz/xsync : Apache-2.0
Provides:       bundled(golang(github.com/puzpuzpuz/xsync/v3)) = 3.4.0
# github.com/quic-go/quic-go : MIT
Provides:       bundled(golang(github.com/quic-go/quic-go)) = 0.48.0
# github.com/rabbitmq/amqp091-go : BSD-2-Clause
Provides:       bundled(golang(github.com/rabbitmq/amqp091-go)) = 1.10.0
# github.com/rcrowley/go-metrics : BSD-2-Clause-Views
Provides:       bundled(golang(github.com/rcrowley/go-metrics)) = cf1acfc
# github.com/riywo/loginshell : MIT
Provides:       bundled(golang(github.com/riywo/loginshell)) = 7d26008
# github.com/russross/blackfriday : BSD-2-Clause
Provides:       bundled(golang(github.com/russross/blackfriday/v2)) = 2.1.0
# github.com/shirou/gopsutil : BSD-3-Clause
Provides:       bundled(golang(github.com/shirou/gopsutil/v4)) = 4.24.9
# github.com/stretchr/objx : MIT
Provides:       bundled(golang(github.com/stretchr/objx)) = 0.5.2
# github.com/stretchr/testify : MIT
Provides:       bundled(golang(github.com/stretchr/testify)) = 1.9.0
# github.com/syncthing/notify : MIT
Provides:       bundled(golang(github.com/syncthing/notify)) = c6b7342
# github.com/syndtr/goleveldb : BSD-2-Clause
Provides:       bundled(golang(github.com/syndtr/goleveldb)) = 126854a
# github.com/thejerf/suture : MIT
Provides:       bundled(golang(github.com/thejerf/suture/v4)) = 4.0.5
# github.com/tklauser/go-sysconf : BSD-3-Clause
Provides:       bundled(golang(github.com/tklauser/go-sysconf)) = 0.3.14
# github.com/tklauser/numcpus : Apache-2.0
Provides:       bundled(golang(github.com/tklauser/numcpus)) = 0.9.0
# github.com/urfave/cli : MIT
Provides:       bundled(golang(github.com/urfave/cli)) = 1.22.16
# github.com/vitrun/qart : Apache-2.0 AND BSD-3-Clause
Provides:       bundled(golang(github.com/vitrun/qart)) = bf64b92
# github.com/willabides/kongplete : MIT
Provides:       bundled(golang(github.com/willabides/kongplete)) = 0.4.0
# github.com/yusufpapurcu/wmi : MIT
Provides:       bundled(golang(github.com/yusufpapurcu/wmi)) = 1.2.4
# go.uber.org/automaxprocs : MIT
Provides:       bundled(golang(go.uber.org/automaxprocs)) = 1.6.0
# go.uber.org/mock : Apache-2.0
Provides:       bundled(golang(go.uber.org/mock)) = 0.4.0
# golang.org/x/crypto : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/crypto)) = 0.28.0
# golang.org/x/exp : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/exp)) = f66d83c
# golang.org/x/mod : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/mod)) = 0.21.0
# golang.org/x/net : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/net)) = 0.30.0
# golang.org/x/sync : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/sync)) = 0.8.0
# golang.org/x/sys : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/sys)) = 0.26.0
# golang.org/x/text : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/text)) = 0.19.0
# golang.org/x/time : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/time)) = 0.7.0
# golang.org/x/tools : BSD-3-Clause
Provides:       bundled(golang(golang.org/x/tools)) = 0.26.0
# google.golang.org/protobuf : BSD-3-Clause
Provides:       bundled(golang(google.golang.org/protobuf)) = 1.35.1
# gopkg.in/yaml.v3 : MIT AND Apache-2.0
Provides:       bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
# sigs.k8s.io/yaml : MIT AND BSD-3-Clause AND (MIT OR Apache-2.0)
Provides:       bundled(golang(sigs.k8s.io/yaml)) = 1.4.0

%description
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the syncthing client binary and systemd services.


%if %{with devel}
%package        devel
Summary:        Continuous File Synchronization (development files)
BuildArch:      noarch

%description    devel
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the syncthing sources, which are needed as
dependency for building packages using syncthing.
%endif


%package        tools
Summary:        Continuous File Synchronization (server tools)

%description    tools
Syncthing replaces other file synchronization services with something
open, trustworthy and decentralized. Your data is your data alone and
you deserve to choose where it is stored, if it is shared with some
third party and how it's transmitted over the Internet. Using syncthing,
that control is returned to you.

This package contains the main syncthing server tools:

* strelaysrv / strelaypoolsrv, the syncthing relay server for indirect
  file transfers between client nodes, and
* stdiscosrv, the syncthing discovery server for discovering nodes
  to connect to indirectly over the internet.


%prep
%autosetup -n %{name} -p1


%build
export GO111MODULE=off

# remove bundled libraries
#rm -r vendor

# prepare build environment
mkdir -p ./_build/src/github.com/syncthing

TOP=$(pwd)
pushd _build/src/github.com/syncthing
ln -s $TOP syncthing
popd

export GOPATH=$(pwd)/_build:%{gopath}
export BUILDDIR=$(pwd)/_build/src/%{goipath}

# compile assets used by the build process
pushd _build/src/%{goipath}
go run build.go assets
rm build.go
popd

# set variables expected by syncthing binaries as additional FOOFLAGS
export BUILD_HOST=fedora-koji
export COMMON_LDFLAGS="-X %{goipath}/lib/build.Version=%{tag} -X %{goipath}/lib/build.Stamp=$SOURCE_DATE_EPOCH -X %{goipath}/lib/build.User=$USER -X %{goipath}/lib/build.Host=$BUILD_HOST"
export BUILDTAGS="noupgrade"

export LDFLAGS="-X %{goipath}/lib/build.Program=syncthing $COMMON_LDFLAGS"
%gobuild -o _bin/syncthing %{goipath}/cmd/syncthing

export LDFLAGS="-X %{goipath}/lib/build.Program=stdiscosrv $COMMON_LDFLAGS"
%gobuild -o _bin/stdiscosrv %{goipath}/cmd/stdiscosrv

export LDFLAGS="-X %{goipath}/lib/build.Program=strelaysrv $COMMON_LDFLAGS"
%gobuild -o _bin/strelaysrv %{goipath}/cmd/strelaysrv

export LDFLAGS="-X %{goipath}/lib/build.Program=strelaypoolsrv $COMMON_LDFLAGS"
%gobuild -o _bin/strelaypoolsrv %{goipath}/cmd/infra/strelaypoolsrv


%install
export GO111MODULE=off

# install binaries
mkdir -p %{buildroot}/%{_bindir}

cp -pav _bin/syncthing %{buildroot}/%{_bindir}/
cp -pav _bin/stdiscosrv %{buildroot}/%{_bindir}/
cp -pav _bin/strelaysrv %{buildroot}/%{_bindir}/
cp -pav _bin/strelaypoolsrv %{buildroot}/%{_bindir}/

# install man pages
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man5
mkdir -p %{buildroot}/%{_mandir}/man7

cp -pav ./man/syncthing.1 %{buildroot}/%{_mandir}/man1/
cp -pav ./man/*.5 %{buildroot}/%{_mandir}/man5/
cp -pav ./man/*.7 %{buildroot}/%{_mandir}/man7/
cp -pav ./man/stdiscosrv.1 %{buildroot}/%{_mandir}/man1/
cp -pav ./man/strelaysrv.1 %{buildroot}/%{_mandir}/man1/

# install desktop files and icons
mkdir -p %{buildroot}/%{_datadir}/applications
cp -pav etc/linux-desktop/syncthing-start.desktop %{buildroot}/%{_datadir}/applications/
cp -pav etc/linux-desktop/syncthing-ui.desktop %{buildroot}/%{_datadir}/applications/

for size in 32 64 128 256 512; do
    mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
    cp -pav assets/logo-${size}.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps/syncthing.png
done
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
cp -pav assets/logo-only.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/syncthing.svg

# install systemd units
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_userunitdir}

cp -pav etc/linux-systemd/system/syncthing@.service %{buildroot}/%{_unitdir}/
cp -pav etc/linux-systemd/user/syncthing.service %{buildroot}/%{_userunitdir}/

# unmark source files as executable
for i in $(find -name "*.go" -type f -executable -print); do
    chmod a-x $i;
done

%if %{with devel}
%goinstall
%endif


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

export LANG=C.utf8
export GOPATH=$(pwd)/_build:%{gopath}
export GO111MODULE=off

%gotest %{goipath}/cmd/stdiscosrv
%gotest %{goipath}/cmd/infra/strelaypoolsrv
%gotest %{goipath}/cmd/syncthing
%gotest %{goipath}/lib/api
%gotest %{goipath}/lib/beacon
%gotest %{goipath}/lib/config

# This test times out on s390x
%gotest %{goipath}/lib/connections || :

%gotest %{goipath}/lib/db
%gotest %{goipath}/lib/dialer
%gotest %{goipath}/lib/discover
%gotest %{goipath}/lib/events

# This test fails on SELinux-enabled systems:
# https://github.com/syncthing/syncthing/issues/8601
%gotest %{goipath}/lib/fs || :

%gotest %{goipath}/lib/ignore
%gotest %{goipath}/lib/logger

# This test sometimes fails dependent on load on some architectures:
# https://github.com/syncthing/syncthing/issues/4370
%gotest %{goipath}/lib/model || :

%gotest %{goipath}/lib/nat
%gotest %{goipath}/lib/osutil
%gotest %{goipath}/lib/pmp
%gotest %{goipath}/lib/protocol
%gotest %{goipath}/lib/rand
%gotest %{goipath}/lib/relay/client
%gotest %{goipath}/lib/relay/protocol
%gotest %{goipath}/lib/scanner
%gotest %{goipath}/lib/semaphore
%gotest %{goipath}/lib/signature
%gotest %{goipath}/lib/stats
%gotest %{goipath}/lib/stringutil
%gotest %{goipath}/lib/structutil
%gotest %{goipath}/lib/svcutil
%gotest %{goipath}/lib/sync
%gotest %{goipath}/lib/syncthing
%gotest %{goipath}/lib/tlsutil
%gotest %{goipath}/lib/upgrade
%gotest %{goipath}/lib/upnp

# This test sometimes fails dependent on load on some architectures:
# https://github.com/syncthing/syncthing/issues/4351
%gotest %{goipath}/lib/versioner || :

%gotest %{goipath}/lib/watchaggregator
%gotest %{goipath}/lib/weakhash


%post
%systemd_post 'syncthing@.service'
%systemd_user_post syncthing.service

%preun
%systemd_preun 'syncthing@*.service'
%systemd_user_preun syncthing.service

%postun
%systemd_postun_with_restart 'syncthing@*.service'
%systemd_user_postun_with_restart syncthing.service


%files
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/syncthing

%{_datadir}/applications/syncthing*.desktop
%{_datadir}/icons/hicolor/*/apps/syncthing.*

%{_mandir}/*/syncthing*

%{_unitdir}/syncthing@.service
%{_userunitdir}/syncthing.service


%files tools
%license LICENSE
%doc README.md AUTHORS

%{_bindir}/stdiscosrv
%{_bindir}/strelaysrv
%{_bindir}/strelaypoolsrv

%{_mandir}/man1/stdiscosrv*
%{_mandir}/man1/strelaysrv*


%if %{with devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS
%endif


%changelog
%autochangelog
