%global pypi_name postfix_mta_sts_resolver

Name:           postfix-mta-sts-resolver
Version:        1.0.0
Release:        9%{?dist}
Summary:        Daemon providing MTA-STS map to Postfix

License:        MIT
URL:            https://github.com/Snawoot/%{name}

# pypi version is stripped down without manpages, doc and examples
Source0:        https://github.com/Snawoot/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        mta-sts-daemon.yml
Source2:        postfix-mta-sts-resolver.service
# since python3-aioredis is unavailable
Patch0:         postfix-mta-sts-resolver_tests_without_redis.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel >= 3.5.3
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
%if 0%{?fedora} || 0%{?rhel} < 8
BuildRequires:  rubygem-asciidoctor
BuildRequires:  make
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif
#BuildRequires:  python%%{python3_pkgversion}-pytest
#BuildRequires:  python%%{python3_pkgversion}-pytest-asyncio
#BuildRequires:  python%%{python3_pkgversion}-pytest-timeout
#BuildRequires:  python%%{python3_pkgversion}-pytest-cov
BuildRequires:  python%{python3_pkgversion}-async-generator
BuildRequires:  python%{python3_pkgversion}-aiodns
BuildRequires:  python%{python3_pkgversion}-aiohttp
BuildRequires:  python%{python3_pkgversion}-yaml
BuildRequires:  python%{python3_pkgversion}-aiosqlite

Requires(pre):  shadow-utils
Requires:       python%{python3_pkgversion}-async-generator
Requires:       python%{python3_pkgversion}-aiodns
Requires:       python%{python3_pkgversion}-aiohttp
Requires:       python%{python3_pkgversion}-yaml
Recommends:     python%{python3_pkgversion}-aiosqlite
# optional deps:
#   - python3-aioredis is not packaged in Fedora or EL
#   - python3-uvloop is not packaged in EL


%description
postfix-mta-sts-resolver provides a lookup daemon and command line
query utility for MTA-STS policies (RFC 8461).  The daemon provides TLS
client policy to Postfix via socketmap.


%prep
%autosetup -p1 -n %{name}-%{version}
# remove useless shebangs
sed -i '/^#!\/usr\/bin\/env/ d' postfix_mta_sts_resolver/*.py


%build
  %py3_build
%if 0%{?fedora} || 0%{?rhel} < 8
  make doc
%endif


%install
  %py3_install

  install -p -D -m 0640 %{SOURCE1} %{buildroot}%{_sysconfdir}/mta-sts-daemon.yml
  install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

  mkdir -p %{buildroot}%{_sharedstatedir}/mta-sts

  %if 0%{?fedora} || 0%{?rhel} < 8
  mkdir -p %{buildroot}%{_mandir}/man1
  install -p -D -m 0644 man/*.1 %{buildroot}%{_mandir}/man1/
  mkdir -p %{buildroot}%{_mandir}/man5
  install -p -D -m 0644 man/*.5 %{buildroot}%{_mandir}/man5/
  %endif


# these include runtime tests using DNS/WEB services which are not separate from unit tests
#%%check
#  TOXENV= i%%{__python3} -m pytest


%files
%license LICENSE
%doc README.md config_examples
%if 0%{?fedora} || 0%{?rhel} < 8
%{_mandir}/man*/*
%endif
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info
%{_bindir}/mta-sts-query
%{_bindir}/mta-sts-daemon
%config(noreplace) %attr(0640,root,mta-sts) %{_sysconfdir}/mta-sts-daemon.yml
%{_unitdir}/%{name}.service
%dir %attr(0755,mta-sts,mta-sts) %{_sharedstatedir}/mta-sts


%pre
getent group mta-sts >/dev/null || groupadd -r mta-sts
getent passwd mta-sts >/dev/null || \
    useradd -r -g mta-sts -d %{_sharedstatedir}/mta-sts -s /sbin/nologin \
    -c "Postfix MTA-STS Map Daemon" mta-sts


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.10

* Mon Mar 08 2021 Marc Dequènes (Duck) <duck@redhat.com> - 1.0.0-4
- add BuildRequires on make for the doc

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Marc Dequènes (Duck) <duck@redhat.com> - 1.0.0-1
- NUR
- preserve file timestamps when installing files
- remove useless shebangs
- remove now useless systemd_requires macro
- don't install manpages as %%doc, it's now automatic
- use _sharedstatedir macro when appropriate
- fix typo in description
- use systemd-rpm-macros for newer systems

* Mon May 11 2020 Marc Dequènes (Duck) <duck@redhat.com> - 0.8.2-1
- initial packaging

