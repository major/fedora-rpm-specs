%bcond_without vendor

%if %{without vendor}
%bcond_without check
%endif

# https://github.com/caddyserver/caddy
%global goipath         github.com/caddyserver/caddy
%global basever         2.5.2
#global prerel          rc
#global prerelnum       3
Version:                %{basever}%{?prerel:~%{prerel}%{prerelnum}}

%gometa

%global common_description %{expand:
Caddy is the web server with automatic HTTPS.}

Name:           caddy
Release:        1%{?dist}
Summary:        Web server with automatic HTTPS
%if %{with vendor}
# github.com/caddyserver/caddy ASL 2.0
# github.com/BurntSushi/toml MIT
# github.com/Masterminds/sprig/v3 MIT
# github.com/alecthomas/chroma MIT
# github.com/aryann/difflib MIT
# github.com/caddyserver/certmagic ASL 2.0
# github.com/dustin/go-humanize MIT
# github.com/go-chi/chi MIT
# github.com/google/cel-go ASL 2.0
# github.com/google/uuid BSD
# github.com/klauspost/compress BSD and ASL 2.0
# github.com/klauspost/cpuid/v2 MIT
# github.com/lucas-clemente/quic-go MIT
# github.com/mholt/acmez ASL 2.0
# github.com/prometheus/client_golang ASL 2.0
# github.com/smallstep/certificates ASL 2.0
# github.com/smallstep/cli ASL 2.0
# github.com/smallstep/nosql ASL 2.0
# github.com/smallstep/truststore ASL 2.0
# github.com/tailscale/tscert BSD
# github.com/yuin/goldmark MIT
# github.com/yuin/goldmark-highlighting MIT
# go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp ASL 2.0
# go.opentelemetry.io/otel ASL 2.0
# go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc ASL 2.0
# go.opentelemetry.io/otel/sdk ASL 2.0
# go.uber.org/zap MIT
# golang.org/x/crypto BSD
# golang.org/x/net BSD
# golang.org/x/term BSD
# google.golang.org/genproto ASL 2.0
# google.golang.org/protobuf BSD
# gopkg.in/natefinch/lumberjack.v2 MIT
# gopkg.in/yaml.v3 ASL 2.0 and MIT
License:        ASL 2.0 and MIT and BSD
%else
License:        ASL 2.0
%endif
URL:            https://caddyserver.com

%if %{with vendor}
# see create-vendor-tarball.sh in this distgit repo
Source0:        caddy-%{version}-vendored.tar.gz
%else
Source0:        %{gosource}
%endif

# based on reference files upstream
# https://github.com/caddyserver/dist
Source1:        Caddyfile
Source2:        caddy.service
Source3:        caddy-api.service
Source4:        poweredby-white.png
Source5:        poweredby-black.png
Source6:        bash-completion
Source7:        zsh-completion

# downstream only patch to disable commands that can alter the binary
Patch:          0001-Disable-commands-that-can-alter-the-binary.patch

# https://github.com/caddyserver/caddy/commit/b4f1a713978f44b6f26721bd4eaa355164e3e6f4
BuildRequires:  golang >= 1.17

%if %{with vendor}
Provides:       bundled(golang(github.com/BurntSushi/toml)) = 1.1.0
Provides:       bundled(golang(github.com/Masterminds/sprig/v3)) = 3.2.2
Provides:       bundled(golang(github.com/alecthomas/chroma)) = 0.10.0
Provides:       bundled(golang(github.com/aryann/difflib))
Provides:       bundled(golang(github.com/caddyserver/certmagic)) = 0.16.1
Provides:       bundled(golang(github.com/dustin/go-humanize))
Provides:       bundled(golang(github.com/go-chi/chi)) = 4.1.2
Provides:       bundled(golang(github.com/google/cel-go)) = 0.11.4
Provides:       bundled(golang(github.com/google/uuid)) = 1.3.0
Provides:       bundled(golang(github.com/klauspost/compress)) = 1.15.6
Provides:       bundled(golang(github.com/klauspost/cpuid/v2)) = 2.0.13
Provides:       bundled(golang(github.com/lucas-clemente/quic-go)) = 0.28.0
Provides:       bundled(golang(github.com/mholt/acmez)) = 1.0.2
Provides:       bundled(golang(github.com/prometheus/client_golang)) = 1.12.1
Provides:       bundled(golang(github.com/smallstep/certificates)) = 0.19.0
Provides:       bundled(golang(github.com/smallstep/cli)) = 0.18.0
Provides:       bundled(golang(github.com/smallstep/nosql)) = 0.4.0
Provides:       bundled(golang(github.com/smallstep/truststore)) = 0.11.0
Provides:       bundled(golang(github.com/tailscale/tscert))
Provides:       bundled(golang(github.com/yuin/goldmark)) = 1.4.12
Provides:       bundled(golang(github.com/yuin/goldmark-highlighting))
Provides:       bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = 0.29.0
Provides:       bundled(golang(go.opentelemetry.io/otel)) = 1.4.0
Provides:       bundled(golang(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)) = 1.4.0
Provides:       bundled(golang(go.opentelemetry.io/otel/sdk)) = 1.4.0
Provides:       bundled(golang(go.uber.org/zap)) = 1.21.0
Provides:       bundled(golang(golang.org/x/crypto))
Provides:       bundled(golang(golang.org/x/net))
Provides:       bundled(golang(golang.org/x/term))
Provides:       bundled(golang(google.golang.org/genproto))
Provides:       bundled(golang(google.golang.org/protobuf)) = 1.28.0
Provides:       bundled(golang(gopkg.in/natefinch/lumberjack.v2)) = 2.0.0
Provides:       bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
%else
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/Masterminds/sprig/v3)
BuildRequires:  golang(github.com/alecthomas/chroma)
BuildRequires:  golang(github.com/aryann/difflib)
BuildRequires:  golang(github.com/caddyserver/certmagic)
BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/go-chi/chi)
BuildRequires:  golang(github.com/google/cel-go)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/klauspost/compress)
BuildRequires:  golang(github.com/klauspost/cpuid/v2)
BuildRequires:  golang(github.com/lucas-clemente/quic-go)
BuildRequires:  golang(github.com/mholt/acmez)
BuildRequires:  golang(github.com/prometheus/client_golang)
BuildRequires:  golang(github.com/smallstep/certificates)
BuildRequires:  golang(github.com/smallstep/cli)
BuildRequires:  golang(github.com/smallstep/nosql)
BuildRequires:  golang(github.com/smallstep/truststore)
BuildRequires:  golang(github.com/tailscale/tscert)
BuildRequires:  golang(github.com/yuin/goldmark)
BuildRequires:  golang(github.com/yuin/goldmark-highlighting)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  golang(go.opentelemetry.io/otel)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(golang.org/x/crypto)
BuildRequires:  golang(golang.org/x/net)
BuildRequires:  golang(golang.org/x/term)
BuildRequires:  golang(google.golang.org/genproto)
BuildRequires:  golang(google.golang.org/protobuf)
BuildRequires:  golang(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  golang(gopkg.in/yaml.v3)
%endif

BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
Requires:       system-logos-httpd
Provides:       webserver


%description %{common_description}


%if %{without vendor}
%gopkg
%endif


%prep
%goprep %{?with_vendor:-k}
%autopatch -p 1

sed -e '/mod.Version/ s/unknown/%{version}-%{release}/' -i caddy.go


%build
%gobuild -o %{gobuilddir}/bin/caddy %{goipath}/cmd/caddy


%install
%if %{without vendor}
%gopkginstall
%endif

# command
install -D -p -m 0755 %{gobuilddir}/bin/caddy %{buildroot}%{_bindir}/caddy

# config
install -D -p -m 0644 %{S:1} %{buildroot}%{_sysconfdir}/caddy/Caddyfile
install -d -m 0755 %{buildroot}%{_sysconfdir}/caddy/Caddyfile.d

# systemd units
install -D -p -m 0644 %{S:2} %{buildroot}%{_unitdir}/caddy.service
install -D -p -m 0644 %{S:3} %{buildroot}%{_unitdir}/caddy-api.service

# data directory
install -d -m 0750 %{buildroot}%{_sharedstatedir}/caddy

# welcome page
%if %{defined fedora}
install -D -p -m 0644 %{S:4} %{buildroot}%{_datadir}/caddy/poweredby.png
%else
install -D -p -m 0644 %{S:5} %{buildroot}%{_datadir}/caddy/poweredby.png
%endif
ln -s ../testpage/index.html %{buildroot}%{_datadir}/caddy/index.html
install -d -m 0755 %{buildroot}%{_datadir}/caddy/icons
ln -s ../../pixmaps/poweredby.png %{buildroot}%{_datadir}/caddy/icons/poweredby.png

# shell completion
install -D -p -m 0644 %{S:6} %{buildroot}%{_datadir}/bash-completion/completions/caddy
install -D -p -m 0644 %{S:7} %{buildroot}%{_datadir}/zsh/site-functions/_caddy


%if %{with check}
%check
%gocheck
%endif


%pre
getent group caddy &> /dev/null || \
groupadd -r caddy &> /dev/null
getent passwd caddy &> /dev/null || \
useradd -r -g caddy -d %{_sharedstatedir}/caddy -s /sbin/nologin -c 'Caddy web server' caddy &> /dev/null
exit 0


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
%{_datadir}/caddy
%{_unitdir}/caddy.service
%{_unitdir}/caddy-api.service
%dir %{_sysconfdir}/caddy
%config(noreplace) %{_sysconfdir}/caddy/Caddyfile
%dir %{_sysconfdir}/caddy/Caddyfile.d
%attr(0750,caddy,caddy) %dir %{_sharedstatedir}/caddy
# filesystem owns all the parent directories here
%{_datadir}/bash-completion/completions/caddy
# own parent directories in case zsh is not installed
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_caddy


%if %{without vendor}
%gopkgfiles
%endif


%changelog
* Tue Aug 09 2022 Carl George <carl@george.computer> - 2.5.2-1
- Latest upstream, resolves rhbz#2062499 rhbz#2113136

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 2.4.6-4
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.4.6-3
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Fri Feb 25 2022 Carl George <carl@george.computer> - 2.4.6-2
- Update welcome page symlink and image to work on both Fedora and EPEL

* Wed Feb 16 2022 Carl George <carl@george.computer> - 2.4.6-1
- Latest upstream rhbz#1984163

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 03 2021 Carl George <carl@george.computer> - 2.3.0-1
- Latest upstream
- Fix vendored license handling
- Switch to white logo rhbz#1934864

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.1-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Carl George <carl@george.computer> - 2.2.1-1
- Latest upstream

* Sat Sep 26 2020 Carl George <carl@george.computer> - 2.2.0-1
- Latest upstream

* Sat Sep 19 2020 Carl George <carl@george.computer> - 2.2.0~rc3-1
- Latest upstream

* Fri Aug 14 2020 Carl George <carl@george.computer> - 2.1.1-2
- Add bash and zsh completion support

* Sun Aug 09 2020 Carl George <carl@george.computer> - 2.1.1-1
- Update to Caddy v2
- Remove all v1 plugins
- Use vendored dependencies
- Remove devel subpackage
- Rename config file per upstream request
- Use webserver test page from system-logos-httpd

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 20:56:10 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-1
- Update to 1.0.4 (#1803691)

* Mon Feb 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-3
- Rebuilt for GHSA-jf24-p9p9-4rjh

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 07 2019 Carl George <carl@george.computer> - 1.0.3-1
- Latest upstream
- Remove bundled lego and plugins
- Remove dyn, gandi, namecheap, and rfc2136 dns providers
- Add patch0 to fix `-version` flag
- Add patch1 to adjust blackfriday import path
- Add devel subpackages
- Run test suite

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Carl George <carl@george.computer> - 0.11.4-2
- Switch unit file from ProtectSystem strict to full rhbz#1706651

* Wed Mar 06 2019 Carl George <carl@george.computer> - 0.11.4-1
- Latest upstream
- Update bundled dnsproviders to 0.1.3
- Update bundled lego to 2.2.0
- Enable googlecloud, route53, and azure dns providers on epel7
- Allow custom http port with default config file rhbz#1685446

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Carl George <carl@george.computer> - 0.11.1-2
- Buildrequires at least golang 1.10

* Tue Nov 13 2018 Carl George <carl@george.computer> - 0.11.1-1
- Latest upstream
- Update bundled geoip

* Fri Oct 19 2018 Carl George <carl@george.computer> - 0.11.0-3
- Enable httpd_can_network_connect selinux boolean to connect to ACME endpoint rhbz#1641158
- Define UDP 80/443 as selinux http_port_t for QUIC rhbz#1608548
- Define TCP 5033 as selinux http_port_t for HTTP challenge rhbz#1641160

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 12 2018 Carl George <carl@george.computer> - 0.11.0-1
- Latest upstream

* Sat Apr 21 2018 Carl George <carl@george.computer> - 0.10.14-1
- Latest upstream
- Overhaul %%prep to extract everything with %%setup
- Edit lego providers to require acmev2 instead of acme
- Add provides for specific providers from %%import_path_dnsproviders and %%import_path_lego
- Add azure dns provider on f28+

* Fri Apr 20 2018 Carl George <carl@george.computer> - 0.10.11-6
- Enable geoip plugin on EL7
- Only provide bundled geoip/realip/dnsproviders/lego when the respective plugin is enabled

* Wed Apr 18 2018 Carl George <carl@george.computer> - 0.10.11-5
- Add geoip plugin

* Tue Apr 17 2018 Carl George <carl@george.computer> - 0.10.11-4
- Correct ExclusiveArch fallback

* Mon Apr 16 2018 Carl George <carl@george.computer> - 0.10.11-3
- Enable s390x
- Disable googlecloud and route53 dns providers on EL7 due to dependency issues

* Fri Mar 30 2018 Carl George <carl@george.computer> - 0.10.11-2
- Add googlecloud dns provider
- Add route53 dns provider
- Set minimum golang version to 1.9
- Set selinux labels in scriptlets

* Sat Feb 24 2018 Carl George <carl@george.computer> - 0.10.11-1
- Latest upstream

* Sat Feb 24 2018 Carl George <carl@george.computer> - 0.10.10-4
- Change ProtectSystem from strict to full in unit file on RHEL

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Carl George <carl@george.computer> - 0.10.10-2
- Add powerdns provider

* Mon Oct 09 2017 Carl George <carl@george.computer> - 0.10.10-1
- Latest upstream

* Mon Oct 02 2017 Carl George <carl@george.computer> - 0.10.9-6
- Add provides for bundled libraries

* Mon Oct 02 2017 Carl George <carl@george.computer> - 0.10.9-5
- Enable rfc2136 dns provider
- List plugins in description

* Mon Sep 18 2017 Carl George <carl@george.computer> - 0.10.9-4
- Exclude s390x

* Sun Sep 17 2017 Carl George <carl@george.computer> - 0.10.9-3
- Add realip plugin
- Add conditionals for plugins

* Sat Sep 16 2017 Carl George <carl@george.computer> - 0.10.9-2
- Add sources for caddyserver/dnsproviders and xenolf/lego
- Disable all dns providers that require additional libraries (dnsimple, dnspod, googlecloud, linode, ovh, route53, vultr)
- Rewrite default index.html

* Tue Sep 12 2017 Carl George <carl@george.computer> - 0.10.9-1
- Latest upstream
- Add config validation to unit file
- Disable exoscale dns provider https://github.com/xenolf/lego/issues/429

* Fri Sep 08 2017 Carl George <carl@george.computer> - 0.10.8-1
- Latest upstream
- Build with %%gobuild macro
- Move config subdirectory from /etc/caddy/caddy.conf.d to /etc/caddy/conf.d

* Tue Aug 29 2017 Carl George <carl@george.computer> - 0.10.7-1
- Latest upstream

* Fri Aug 25 2017 Carl George <carl@george.computer> - 0.10.6-2
- Use SIQQUIT to stop service
- Increase the process limit from 64 to 512
- Only `go get` in caddy/caddymain

* Fri Aug 11 2017 Carl George <carl@george.computer> - 0.10.6-1
- Latest upstream
- Add webserver virtual provides
- Drop tmpfiles and just own /var/lib/caddy directly
- Remove PrivateDevices setting from unit file, it prevents selinux process transitions
- Disable rfc2136 dns provider https://github.com/caddyserver/dnsproviders/issues/11

* Sat Jun 03 2017 Carl George <carl.george@rackspace.com> - 0.10.3-2
- Rename Envfile to envfile
- Rename Caddyfile to caddy.conf
- Include additional configs from caddy.conf.d directory

* Fri May 19 2017 Carl George <carl.george@rackspace.com> - 0.10.3-1
- Latest upstream

* Mon May 15 2017 Carl George <carl.george@rackspace.com> - 0.10.2-1
- Initial package
