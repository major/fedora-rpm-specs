# https://github.com/caddyserver/caddy
%global goipath         github.com/caddyserver/caddy-1
%global forgeurl        https://github.com/caddyserver/caddy
%global goaltipaths     github.com/mholt/caddy-1
Version:                1.0.4

%gometa

%global common_description %{expand:
Caddy is the HTTP/2 web server with automatic HTTPS.}

%global golicenses      LICENSE.txt
%global godocs          dist/README.txt dist/CHANGES.txt

# added in F32, remove in F34
%global godevelheader %{expand:
Obsoletes:      golang-github-mholt-caddy-devel < 1.0.0-3
}

Name:           %{goname}
Release:        11%{?dist}
Summary:        HTTP/2 web server with automatic HTTPS
License:        ASL 2.0
URL:            https://caddyserver.com
Source0:        %{gosource}

BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/flynn/go-shlex)
BuildRequires:  golang(github.com/go-acme/lego/v3/certcrypto)
BuildRequires:  golang(github.com/go-acme/lego/v3/challenge)
BuildRequires:  golang(github.com/go-acme/lego/v3/challenge/tlsalpn01)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/hashicorp/go-syslog)
BuildRequires:  golang(github.com/jimstudt/http-authentication/basic)
BuildRequires:  golang(github.com/klauspost/cpuid)
BuildRequires:  golang(github.com/lucas-clemente/quic-go)
BuildRequires:  golang(github.com/lucas-clemente/quic-go/http3)
BuildRequires:  golang(github.com/mholt/certmagic-0.8)
BuildRequires:  golang(github.com/naoina/toml)
BuildRequires:  golang(gopkg.in/russross/blackfriday.v1)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
BuildRequires:  golang(golang.org/x/net/websocket)
BuildRequires:  golang(gopkg.in/mcuadros/go-syslog.v2)
BuildRequires:  golang(gopkg.in/mcuadros/go-syslog.v2/format)
%endif

%description %{common_description}

%gopkg

%prep
%goprep
sed -i "s|github.com/russross/blackfriday|gopkg.in/russross/blackfriday.v1|" $(find . -name "*.go" -type f)
sed -i "s|github.com/mholt/certmagic|github.com/mholt/certmagic-0.8|" $(find . -name "*.go" -type f)
sed -i "s|github.com/caddyserver/caddy|github.com/caddyserver/caddy-1|" $(find . -name "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Maxwell G <gotmax@e.email> - 1.0.4-10
- Rebuild to fix FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 01:27:22 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-5
- Build against github.com/go-acme/lego/v3
- Close: rhbz#1908153

* Tue Sep 22 01:59:33 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-4
- Fix FTBFS
- Compat package, library only

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
