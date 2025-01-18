%bcond_without check

%global gorepo          dataplaneapi
%global haproxy_user    haproxy
%global haproxy_group   %{haproxy_user}
%global haproxy_homedir %{_localstatedir}/lib/haproxy

%global _hardened_build 1

# https://github.com/haproxytech/dataplaneapi
%global goipath         github.com/haproxytech/dataplaneapi
Version:                2.4.4

%gometa

%global goaltipaths     %{goipath}/v2

%global common_description %{expand:
HAProxy Data Plane API.}

%global golicenses      LICENSE e2e/libs/bats-assert/LICENSE e2e/libs/bats-\\\
                        support/LICENSE
%global godocs          CONTRIBUTING.md README.md configuration/examples\\\
                        configuration/README.md discovery/AWS.md\\\
                        discovery/CONSUL.md discovery/README.md e2e/README.md\\\
                        e2e/libs/bats-assert/README.md e2e/libs/bats-\\\
                        support/CHANGELOG.md e2e/libs/bats-support/README.md

Name:           %{goname}
Release:        15%{?dist}
Summary:        HAProxy Data Plane API

Group:          System Environment/Daemons

# Upstream license specification: Apache-2.0 and CC0-1.0
# Automatically converted from old format: ASL 2.0 and CC0 - review is highly recommended.
License:        Apache-2.0 AND CC0-1.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{gorepo}.service
Source2:        %{gorepo}.logrotate
Source3:        %{gorepo}.sysconfig
Source4:        %{gorepo}.hcl
Source5:        %{gorepo}.yaml

Patch0:         dataplaneapi-go-openapi-errors.patch
Patch1:         dataplaneapi-kin-openapi-changes.patch

BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/ec2)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/ec2/types)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/dustinkirkland/golang-petname)
BuildRequires:  golang(github.com/fsnotify/fsnotify)
BuildRequires:  golang(github.com/GehirnInc/crypt)
BuildRequires:  golang(github.com/GehirnInc/crypt/md5_crypt)
BuildRequires:  golang(github.com/GehirnInc/crypt/sha256_crypt)
BuildRequires:  golang(github.com/GehirnInc/crypt/sha512_crypt)
BuildRequires:  golang(github.com/getkin/kin-openapi/openapi2)
BuildRequires:  golang(github.com/getkin/kin-openapi/openapi2conv)
BuildRequires:  golang(github.com/go-openapi/errors)
BuildRequires:  golang(github.com/go-openapi/loads)
BuildRequires:  golang(github.com/go-openapi/runtime)
BuildRequires:  golang(github.com/go-openapi/runtime/flagext)
BuildRequires:  golang(github.com/go-openapi/runtime/middleware)
BuildRequires:  golang(github.com/go-openapi/runtime/security)
BuildRequires:  golang(github.com/go-openapi/spec)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/swag)
BuildRequires:  golang(github.com/go-openapi/validate)
BuildRequires:  golang(github.com/google/renameio)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/haproxytech/client-native/v2)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/configuration)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/errors)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/misc)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/models)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/runtime)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/spoe)
BuildRequires:  golang(github.com/haproxytech/client-native/v2/storage)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/common)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/options)
BuildRequires:  golang(github.com/haproxytech/config-parser/v4/types)
BuildRequires:  golang(github.com/hashicorp/consul/api)
BuildRequires:  golang(github.com/hashicorp/hcl)
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/lestrrat-go/apache-logformat)
BuildRequires:  golang(github.com/nathanaelle/syslog5424/v2)
BuildRequires:  golang(github.com/rodaine/hclencoder)
BuildRequires:  golang(github.com/rs/cors)
BuildRequires:  golang(github.com/shirou/gopsutil/host)
BuildRequires:  golang(github.com/shirou/gopsutil/mem)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(golang.org/x/net/netutil)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  systemd-units
BuildRequires:  help2man
BuildRequires:  gzip

Requires:         haproxy >= 2.0
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

Suggests: logrotate

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
# https://github.com/haproxytech/dataplaneapi/pull/127
%patch -P0 -p1
%patch -P1 -p1
mv e2e/libs/bats-assert/LICENSE LICENSE-e2e-libs-bats-assert
mv e2e/libs/bats-support/LICENSE LICENSE-e2e-libs-bats-support
mv configuration/examples examples
mv configuration/README.md README-configuration.md
mv discovery/AWS.md AWS-discovery.md
mv discovery/CONSUL.md CONSUL-discovery.md
mv discovery/README.md README-discovery.md
mv e2e/libs/bats-assert/README.md README-e2e-libs-bats-assert.md
mv e2e/libs/bats-support/CHANGELOG.md CHANGELOG-e2e-libs-bats-support.md
mv e2e/libs/bats-support/README.md README-e2e-libs-bats-support.md
mv e2e/README.md README-e2e.md

%build
LDFLAGS="-X main.GitRepo=%{url}/archive/v%{version}/%{gorepo}-%{version}.tar.gz "
LDFLAGS+="-X main.GitTag=v%{version} -X main.GitCommit= -X main.GitDirty= "
LDFLAGS+="-X main.BuildTime=%(date '+%%Y-%%m-%%dT%%H:%%M:%%S') "
%gobuild -o %{gobuilddir}/sbin/%{gorepo} %{goipath}/cmd/%{gorepo}/
mkdir -p %{gobuilddir}/share/man/man8
help2man -n "%{summary}" -s 8 -o %{gobuilddir}/share/man/man8/%{gorepo}.8 -N --version-string="%{version}" %{gobuilddir}/sbin/%{gorepo}
gzip %{gobuilddir}/share/man/man8/%{gorepo}.8

%install
%gopkginstall
install -m 0755 -vd                      %{buildroot}%{_sbindir}
install -m 0755 -vp %{gobuilddir}/sbin/* %{buildroot}%{_sbindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man8
install -m 0644 -vp %{gobuilddir}/share/man/man8/* %{buildroot}%{_mandir}/man8/

install -d -m 0755 %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m 0755 %{buildroot}%{_sysconfdir}/haproxy
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{gorepo}.service
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{gorepo}
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{gorepo}
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/haproxy/%{gorepo}.hcl
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/haproxy/%{gorepo}.yaml

%if %{with check}
%check
%gocheck
%endif

%post
%systemd_post %{gorepo}.service

%preun
%systemd_preun %{gorepo}.service

%postun
%systemd_postun_with_restart %{gorepo}.service

%files
%license LICENSE LICENSE-e2e-libs-bats-assert LICENSE-e2e-libs-bats-support
%doc CONTRIBUTING.md README.md examples README-configuration.md AWS-discovery.md
%doc CONSUL-discovery.md README-discovery.md README-e2e.md
%doc README-e2e-libs-bats-assert.md CHANGELOG-e2e-libs-bats-support.md
%doc README-e2e-libs-bats-support.md
%{_mandir}/man8/%{gorepo}.8*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{gorepo}
%config(noreplace) %{_sysconfdir}/sysconfig/%{gorepo}
%config(noreplace) %{_sysconfdir}/haproxy/%{gorepo}.hcl
%config(noreplace) %{_sysconfdir}/haproxy/%{gorepo}.yaml
%{_unitdir}/%{gorepo}.service
%{_sbindir}/*

%gopkgfiles

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.4-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 2.4.4-12
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Maxwell G <gotmax@e.email> - 2.4.4-7
- Rebuild to fix FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 2.4.4-5
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.4.4-4
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Sat Apr 16 2022 Fabio Alessandro Locati <me@fale.io> - 2.4.4-3
- Rebuilt for CVE-2022-27191

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Brandon Perkins <bperkins@redhat.com> - 2.4.4-1
- Update to version 2.4.4 (Fixes rhbz#2029628)

* Mon Nov 01 2021 Brandon Perkins <bperkins@redhat.com> - 2.4.1-1
- Update to version 2.4.1 (Fixes rhbz#2014757)

* Fri Oct 08 2021 Brandon Perkins <bperkins@redhat.com> - 2.3.6-1
- Update to version 2.3.6 (Fixes rhbz#2011801)

* Fri Sep 17 2021 Brandon Perkins <bperkins@redhat.com> - 2.3.5-1
- Update to version 2.3.5 (Fixes rhbz#1999558)

* Mon Aug 09 2021 Brandon Perkins <bperkins@redhat.com> - 2.3.3-1
- Update to version 2.3.3 (Fixes rhbz#1984711)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Brandon Perkins <bperkins@redhat.com> - 2.3.2-1
- Update to version 2.3.2 (Fixes rhbz#1966222)

* Sun May 23 2021 Brandon Perkins <bperkins@redhat.com> - 2.3.1-1
- Update to version 2.3.1 (Fixes rhbz#1962906)

* Tue May 18 2021 Brandon Perkins <bperkins@redhat.com> - 2.3.0-2
- Changes for version 2.3.0 (Fixes rhbz#1959606)
- Include support for new HCL/YAML configuration files
- Fix logrotate.d configuration file name
- Enable new syslog support
- ExecStart service using HCL/YAML configuration file instead of command flags
- Simplify sysconfig file to only include CONFIG and OPTIONS variables

* Wed May 12 2021 Brandon Perkins <bperkins@redhat.com> - 2.3.0-1
- Update to version 2.3.0 (Fixes rhbz#1959606)
- Addition of configuration and discovery docs
- Patch for changes in kin-openapi v0.61.0
- Addition of numerous BuildRequires

* Thu Apr 08 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.1-1
- Update to version 2.2.1 (Fixes rhbz#1947127)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 16:09:32 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.0-1
- Update to 2.2.0
- Close: rhbz#1916914

* Wed Jan 13 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.0~rc1-2
- Modify gosource so that Source0 resolves correctly  (Fixes rhbz#1914254)

* Tue Jan 12 2021 Brandon Perkins <bperkins@redhat.com> - 2.2.0~rc1-1
- Update to version 2.2.0-rc1 (Fixes rhbz#1914254)

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 2.1.0-4
- Patch for changes in go-openapi/errors v0.19.6
  https://github.com/haproxytech/dataplaneapi/pull/127

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Brandon Perkins <bperkins@redhat.com> - 2.1.0-1
- Update to version 2.1.0 (Fixes rhbz#1859325)
- Add golang(github.com/getkin/kin-openapi/openapi2),
  golang(github.com/getkin/kin-openapi/openapi2conv), and
  golang(github.com/google/renameio) BuildRequires

* Mon Jun 01 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.3-1
- Update to version 2.0.3

* Mon May 18 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.2-1
- Update to version 2.0.2

* Fri May 08 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.1-1
- Update to version 2.0.1

* Tue Apr 28 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.0-2
- Add LDFLAGS for GitRepo, GitTag, GitCommit, GitDirty, and
  BuildTime variables
- Simplify gobuild action to only build dataplaneapi

* Mon Apr 27 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.0-1
- Upgrade to version 2.0.0

* Wed Apr 15 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.5-1
- Update to version 1.2.5

* Tue Apr 14 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.4-7
- Change haproxy requires to >= 2.0 as 1.9 was never packaged
- Add specific versions for haproxytech BuildRequires

* Wed Mar 04 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.4-6
- Use global instead of define macro
- Remove defattr macro that is not needed

* Mon Mar 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.4-5
- Clean changelog

* Thu Nov 21 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.4-4
- Suggest logrotate and fix logrotate configuration

* Wed Nov 20 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.4-3
- Add man page

* Wed Nov 13 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.4-2
- Implement systemd

* Wed Nov 13 2019 Brandon Perkins <bperkins@redhat.com> - 1.2.4-1
- Initial package

