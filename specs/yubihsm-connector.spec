# Run tests in check section
%bcond_without check

# https://github.com/Yubico/yubihsm-connector
%global goipath         github.com/Yubico/yubihsm-connector
Version:                3.0.5
%global tag             %{version}

%gometa

%global common_description %{expand:
Backend to talk to YubiHSM 2}

Name:           yubihsm-connector
Release:        7%{?dist}
Summary:        YubiHSM Connector

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{gosource}.sig
Source2:        gpgkey-9588EA0F.gpg
%if 0%{?rhel}
# In RHEL, there are no separate dependencies as packages so we need to "vendor" them
# created using
# $ cd yubihsm-connector-x.y.z
# $ go mod vendor
# $ tar -cvJf ../yubihsm-connector-vendor-x.y.z.tar.gz vendor/
Source3:        %{name}-vendor-%{version}.tar.gz
%endif

%{?systemd_requires}
Requires(pre):  shadow-utils
BuildRequires:  compiler(go-compiler)
BuildRequires:  systemd-rpm-macros
#BuildRequires:  git
%if 0%{?fedora}
BuildRequires:  golang(github.com/google/gousb)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/kardianos/service)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/sirupsen/logrus/hooks/syslog)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/viper)
BuildRequires:  golang(gopkg.in/yaml.v2)
%else
BuildRequires: libusb-devel
%endif
BuildRequires:  gnupg2
Recommends:     yubihsm-shell

%description
%{common_description}

%gopkg

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%if 0%{?fedora}
%goprep
%else
%setup -q -a 3
rm -rf go.mod

mkdir -p "%{_builddir}/src/github.com/Yubico/"
cp -r %{_builddir}/%{name}-%{version} %{_builddir}/src/github.com/Yubico/%{name}
mkdir -p %{_builddir}/%{name}-%{version}/_build
mv %{_builddir}/src %{_builddir}/%{name}-%{version}/_build/src
%endif

%build
export GO111MODULE=off
%if 0%{?fedora}
go generate
%gobuild -o %{gobuilddir}/bin/yubihsm-connector %{goipath}
%else
export GOPATH="%{_builddir}/%{name}-%{version}/_build"
pushd $GOPATH/src/github.com/Yubico/yubihsm-connector/
go generate
popd
%gobuild -o bin/yubihsm-connector github.com/Yubico/yubihsm-connector/
%endif

%install
%if 0%{?fedora}
install -Dpm 0755 %{gobuilddir}/bin/yubihsm-connector %{buildroot}%{_bindir}/yubihsm-connector
%else
install -Dpm 0755 bin/yubihsm-connector %{buildroot}%{_bindir}/yubihsm-connector
%endif
install -Dpm 0644  deb/yubihsm-connector.yaml %{buildroot}%{_sysconfdir}/yubihsm-connector.yaml
install -Dpm 0644  deb/yubihsm-connector.service %{buildroot}%{_unitdir}/yubihsm-connector.service
install -Dpm 0644  deb/70-yubihsm-connector.rules %{buildroot}%{_udevrulesdir}/70-yubihsm-connector.rules

%if %{with check}
%check
%if 0%{?fedora}
%gocheck
%else
export GO111MODULE=off
export GOPATH="%{_builddir}/%{name}-%{version}/_build"
cd "_build/src/github.com/Yubico/%{name}"
go test -v
%endif
%endif

%pre
getent group yubihsm-connector >/dev/null || groupadd -r yubihsm-connector
getent passwd yubihsm-connector >/dev/null || \
    useradd -r -g yubihsm-connector -M -s /sbin/nologin \
    -c "YubiHSM connector account" yubihsm-connector \
    --system
exit 0

%post
%systemd_post yubihsm-connector.service

%preun
%systemd_preun yubihsm-connector.service

%postun
%systemd_postun_with_restart yubihsm-connector.service

%files
%license LICENSE
%{_bindir}/yubihsm-connector
%config(noreplace) %{_sysconfdir}/yubihsm-connector.yaml
%{_unitdir}/yubihsm-connector.service
%{_udevrulesdir}/70-yubihsm-connector.rules

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 11 2024 Jakub Jelen <jjelen@redhat.com> - 3.0.5-6
- New upstream release (#2311423)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.4-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 3.0.4-4
- Rebuild for golang 1.22.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Jakub Jelen <jjelen@redhat.com> - 3.0.4-1
- New upstream release (#2165238)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 3.0.3-4
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Mon Jun 27 2022 Jakub Jelen <jjelen@redhat.com> - 3.0.3-3
- New upstream release (#2100541)

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.2-3
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 24 2021 Jakub Jelen <jjelen@redhat.com> - 3.0.2-1
- New upstream release (#1995879)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Jakub Jelen <jjelen@redhat.com> - 3.0.1-1
- New upstream release fixing YSA-2021-02 / CVE-2021-28484

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.0-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 17 2021 Jakub Jelen <jjelen@redhat.com> - 3.0.0-1
- New upstream release (#1929041)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Jakub Jelen <jjelen@redhat.com> - 2.2.0-1
- New upstream release (#1788637)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Jakub Jelen <jjelen@redhat.com> - 2.1.0-1
- New upstream release (#1788637)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-2
- Update to latest Go macros

* Thu Jan 31 2019 Jakub Jelen <jjelen@redhat.com> - 2.0.0-1
- First package for Fedora
