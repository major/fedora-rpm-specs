%global srcname synapse

# Version suffix in URL when building release candidates
%global rcx %{nil}

Name:       matrix-%{srcname}
Version:    1.66.0
Release:    1%{?dist}
Summary:    A Matrix reference homeserver written in Python using Twisted
License:    ASL 2.0
URL:        https://github.com/matrix-org/%{srcname}
Source0:    %{url}/archive/v%{version}%{rcx}/%{srcname}-%{version}%{rcx}.tar.gz
Source1:    synapse.sysconfig
Source2:    synapse.service
Source3:    matrix-synapse.sysusers
BuildArch:  noarch

Recommends:     %{name}+postgres
Recommends:     %{name}+systemd

BuildRequires:  python3-devel
BuildRequires:  /usr/bin/openssl
BuildRequires:  systemd-rpm-macros
# Workaround missing python-saml2 dependencies in f35 and f36.
BuildRequires:  xmlsec1
BuildRequires:  xmlsec1-openssl

%description
Matrix is an ambitious new ecosystem for open federated Instant Messaging and
VoIP. Synapse is a reference "homeserver" implementation of Matrix from the
core development team at matrix.org, written in Python/Twisted. It is intended
to showcase the concept of Matrix and let folks see the spec in the context of
a coded base and let you run your own homeserver and generally help bootstrap
the ecosystem.

%pyproject_extras_subpkg -n %{name} matrix-synapse-ldap3 postgres saml2 oidc systemd url_preview jwt cache_memory


%prep
%autosetup -p1 -n %{srcname}-%{version}%{rcx}

# We don't support the built-in client so remove all the bundled JS.
rm -rf synapse/static


%generate_buildrequires
# Missing: sentry,opentracing,redis,cache_memory
%pyproject_buildrequires -x test,matrix-synapse-ldap3,postgres,saml2,oidc,systemd,url_preview,jwt



%build
%pyproject_wheel


%install
%pyproject_install
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{srcname}/_scripts
%pyproject_save_files %{srcname}

install -p -D -T -m 0644 contrib/systemd/log_config.yaml %{buildroot}%{_sysconfdir}/synapse/log_config.yaml
install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/synapse
install -p -D -T -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/synapse.service
install -p -d -m 755 %{buildroot}/%{_sharedstatedir}/synapse
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf


%check
set -o pipefail
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:$PWD trial-3 tests | tee trial.stdout

# Guard against new types of tests being skipped.
WHITELIST="Requires hiredis
Requires jaeger_client
Requires Postgres
\`BaseFederationServlet\` does not support cancellation yet."
REASONS=$(cat trial.stdout | sed -n '/^\[SKIPPED\]$/{n;p;}')
SKIPPED=$(comm -23 <(echo "$REASONS" | sort | uniq) <(echo "$WHITELIST" | sort | uniq))
if [ ! -z "$SKIPPED" ]; then
  echo -e "Failing, because tests were skipped:\n$SKIPPED"
  exit 1
fi


%pre
%sysusers_create_compat %{SOURCE3}


%post
%systemd_post synapse.service


%preun
%systemd_preun synapse.service


%postun
%systemd_postun_with_restart synapse.service


%files -f %{pyproject_files}
%license LICENSE
%doc *.rst
%config(noreplace) %{_sysconfdir}/sysconfig/synapse
%{_bindir}/*
%{_unitdir}/synapse.service
%attr(755,synapse,synapse) %dir %{_sharedstatedir}/synapse
%attr(755,synapse,synapse) %dir %{_sysconfdir}/synapse
%attr(644,synapse,synapse) %config(noreplace) %{_sysconfdir}/synapse/*
%{_sysusersdir}/%{name}.conf


%changelog
* Wed Sep 07 2022 Kai A. Hiller <V02460@gmail.com> - 1.66.0-1
- Update to v1.66.0

* Sun Aug 14 2022 Dan Callaghan <djc@djc.id.au> - 1.63.1-2
- dropped unnecessary BuildRequires on pympler, which is broken in F37+
  (RHBZ#2113507)

* Tue Jul 26 2022 Kai A. Hiller <V02460@gmail.com> - 1.63.1-1
- Update to v1.63.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.62.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Kai A. Hiller <V02460@gmail.com> - 1.62.0-1
- Update to v1.62.0

* Wed Jun 29 2022 Kai A. Hiller <V02460@gmail.com> - 1.61.1-1
- Update to v1.61.1
- Fix CVE-2022-31052

* Tue Jun 14 2022 Kai A. Hiller <V02460@gmail.com> - 1.61.0-1
- Update to v1.61.0

* Thu Jun 09 2022 Kai A. Hiller <V02460@gmail.com> - 1.60.0-1
- Update to v1.60.0

* Thu May 19 2022 Kai A. Hiller <V02460@gmail.com> - 1.59.1-1
- Update to v1.59.1

* Wed May 18 2022 Kai A. Hiller <V02460@gmail.com> - 1.59.0-1
- Update to v1.59.0

* Wed May 04 2022 Kai A. Hiller <V02460@gmail.com> - 1.58.0-1
- Update to v1.58.0

* Thu Apr 21 2022 Dan Callaghan <djc@djc.id.au> - 1.57.0-1
- Update to v1.57.0

* Tue Apr 05 2022 Kai A. Hiller <V02460@gmail.com> - 1.56.0-1
- Update to v1.56.0

* Thu Mar 24 2022 Kai A. Hiller <V02460@gmail.com> - 1.55.0-1
- Update to v1.55.0

* Tue Mar 08 2022 Kai A. Hiller <V02460@gmail.com> - 1.54.0-1
- Update to v1.54.0

* Tue Feb 22 2022 Kai A. Hiller <V02460@gmail.com> - 1.53.0-1
- Update to v1.53.0

* Wed Feb 09 2022 Kai A. Hiller <V02460@gmail.com> - 1.52.0-2
- Backport: Fix losing incoming EDUs if debug logging enabled

* Tue Feb 08 2022 Kai A. Hiller <V02460@gmail.com> - 1.52.0-1
- Update to v1.52.0
- Create synapse user and group declaratively

* Thu Jan 27 2022 Kai A. Hiller <V02460@gmail.com> - 1.51.0-1
- Update to v1.51.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.49.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Kai A. Hiller <V02460@gmail.com> - 1.49.2-1
- Update to v1.49.2

* Tue Dec 14 2021 Kai A. Hiller <V02460@gmail.com> - 1.49.0-1
- Update to v1.49.0

* Tue Nov 30 2021 Kai A. Hiller <V02460@gmail.com> - 1.48.0-1
- Update to v1.48.0

* Wed Nov 24 2021 Kai A. Hiller <V02460@gmail.com> - 1.47.1-1
- Update to v1.47.1
- Fix CVE-2021-41281

* Fri Nov 19 2021 Kai A. Hiller <V02460@gmail.com> - 1.47.0-1
- Update to v1.47.0

* Thu Nov 04 2021 Kai A. Hiller <V02460@gmail.com> - 1.46.0-1
- Update to v1.46.0

* Thu Oct 21 2021 Kai A. Hiller <V02460@gmail.com> - 1.45.1-1
- Update to v1.45.1

* Mon Oct 18 2021 Kai A. Hiller <V02460@gmail.com> - 1.44.0-1
- Update to v1.44.0

* Thu Sep 09 2021 Kai A. Hiller <V02460@gmail.com> - 1.42.0-1
- Update to v1.42.0

* Tue Aug 31 2021 Kai A. Hiller <V02460@gmail.com> - 1.41.1-1
- Update to v1.41.1
- Fix CVE-2021-39163, CVE-2021-39164

* Tue Aug 24 2021 Kai A. Hiller <V02460@gmail.com> - 1.41.0-1
- Update to v1.41.0

* Tue Aug 10 2021 Kai A. Hiller <V02460@gmail.com> - 1.40.0-1
- Update to v1.40.0

* Thu Jul 29 2021 Kai A. Hiller <V02460@gmail.com> - 1.39.0-1
- Update to v1.39.0

* Fri Jul 23 2021 Kai A. Hiller <V02460@gmail.com> - 1.38.1-1
- Update to v1.38.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 18 2021 Dan Callaghan <djc@djc.id.au> - 1.38.0-2
- fix startup ordering of synapse.service (RHBZ#1910740)
- relax version requirement for python3-cryptography

* Wed Jul 14 2021 Kai A. Hiller <V02460@gmail.com> - 1.38.0-1
- Update to v1.38.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.26.0-3
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.26.0-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Jan 28 2021 Kai A. Hiller <V02460@gmail.com> - 1.26.0-1
- Update to v1.26.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Kai A. Hiller <V02460@gmail.com - 1.25.0-1
- Update to v1.25.0

* Wed Dec 09 2020 Kai A. Hiller <V02460@gmail.com> - 1.24.0-1
- Update to v1.24.0

* Mon Nov 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.23.0-1
- 1.23.0

* Sat Aug 29 2020 Kai A. Hiller <V02460@gmail.com> - 1.18.0-1
- Update to v1.18.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.13.0-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Dan Callaghan <djc@djc.id.au> - 1.13.0-1
- Update to v1.13.0

* Sun May 17 2020 Dan Callaghan <djc@djc.id.au> - 1.12.4-1
- Update to v1.12.4

* Wed Apr 22 2020 Kai A. Hiller <V02460@gmail.com> - 1.12.3-1
- Update to v1.12.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Arjen Heidinga <dexter@beetjevreeemd.nl> - 1.8.0-1
- Update to v1.8.0

* Tue Dec 31 2019 Dan Callaghan <djc@djc.id.au> - 1.7.2-1
- Update to v1.7.2

* Tue Dec 03 2019 Dan Callaghan <djc@djc.id.au> - 1.6.1-1
- Update to v1.6.1

* Fri Nov 08 2019 Kai A. Hiller <V02460@gmail.com> - 1.5.1-1
- Update to v1.5.1
- Add Python 3.8 compatibility

* Fri Oct 11 2019 Kai A. Hiller <V02460@gmail.com> - 1.4.0-1
- Update to v1.4.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Kai A. Hiller <V02460@gmail.com> - 1.2.1-1
- Update to v1.2.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Dan Callaghan <djc@djc.id.au> - 1.0.0-1
- Update to v1.0.0 release, including new protocol-mandated TLS
  certificate verification logic. See:
  https://github.com/matrix-org/synapse/blob/master/docs/MSC1711_certificates_FAQ.md

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jeremy Cline <jeremy@jcline.org> - 0.34.0.1-2
- synapse user should own its configuration directory (rhbz 1662672)

* Fri Jan 11 2019 Jeremy Cline <jeremy@jcline.org> - 0.34.0.1-1
- Update to v0.34.0.1, fixes CVE-2019-5885

* Fri Dec 28 2018 Jeremy Cline <jeremy@jcline.org> - 0.34.0-1
- Update to v0.34.0
- Switch to Python 3

* Thu Sep 06 2018 Jeremy Cline <jeremy@jcline.org> - 0.33.3.1-1
- Update to v0.33.3.1
- Use the Python dependency generator.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Jeremy Cline <jeremy@jcline.org> - 0.31.2-1
- Update to v0.31.2
- https://github.com/matrix-org/synapse/releases/tag/v0.31.2

* Wed Jun 13 2018 Jeremy Cline <jeremy@jcline.org> - 0.31.1-2
- Stop using Python dependency generator

* Wed Jun 13 2018 Jeremy Cline <jeremy@jcline.org> - 0.31.1-1
- Update to v0.31.1
- Fix CVE-2018-12291

* Thu May 24 2018 Jeremy Cline <jeremy@jcline.org> - 0.29.1-1
- Update to the latest upstream release.
- Use the Python dependency generator.

* Tue May 01 2018 Jeremy Cline <jeremy@jcline.org> - 0.28.1-1
- Update to the latest upstream release.

* Wed Apr 11 2018 Jeremy Cline <jeremy@jcline.org> - 0.27.3-1
- Update to the latest upstream release.

* Mon Mar 26 2018 Jeremy Cline <jeremy@jcline.org> - 0.27.2-1
- Update to the latest upstream release.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Jeremy Cline <jeremy@jcline.org> - 0.26.0-1
- Update to latest upstream

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.23.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Oct 03 2017 Jeremy Cline <jeremy@jcline.org> - 0.23.1-1
- Update to latest upstream
- Include patch to work with ujson-2.0+

* Fri Sep 29 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.1-4
- Use python2 prefix for packages whenever possible
- Add missing %%{?systemd_requires}

* Wed Aug 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.22.1-3
- Switch to python-bcrypt, BZ 1473018.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Jeremy Cline <jeremy@jcline.org> - 0.22.1-1
- Update to the latest upstream release

* Thu Jul 06 2017 Jeremy Cline <jeremy@jcline.org> - 0.22.0-1
- Update to the latest upstream release (#1462045)

* Fri Jun 23 2017 Jeremy Cline <jeremy@jcline.org> - 0.21.1-1
- Update to latest upstream release

* Tue May 30 2017 Jeremy Cline <jeremy@jcline.org> - 0.19.3-4
- use _sharedstatedir  rather than _localstatedir

* Wed May 17 2017 Jeremy Cline <jeremy@jcline.org> - 0.19.3-3
- Remove bundled JS
- Fix some typos in the summary and description

* Tue Apr 04 2017 Jeremy Cline <jeremy@jcline.org> - 0.19.3-2
- Remove the duplicate requirement on pysaml

* Tue Mar 28 2017 Jeremy Cline <jeremy@jcline.org> - 0.19.3-1
- Initial package
