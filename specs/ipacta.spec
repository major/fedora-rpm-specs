%global pki_version 11.7.0

%if 0%{?rhel}
%global dogtag_name idm
%else
%global dogtag_name dogtag
%endif

Name:      ipacta
Summary:   Certificate Trust Authority
URL:       https://forge.fedoraproject.org/freeipa/ipacta
License:   GPL-3.0-or-later
Version:   0.1.1
Release:   1%{?dist}
Source0:   https://forge.fedoraproject.org/freeipa/ipacta/releases/download/v%{version}/%{name}-%{version}.tar.gz
Provides:  pki-ca = %{pki_version}
Provides:  pki-kra = %{pki_version}
Provides:  pki-acme = %{pki_version}
Provides:  group(pkiuser)
Requires:  python3-ipacta = %{version}-%{release}
Requires:  python3-ipacta-pki = %{version}-%{release}
# ipacta and dogtag should never be installed at the same time as they are
# providing the same service and also conflicting files.
Conflicts: %{dogtag_name}-pki-server
Conflicts: %{dogtag_name}-pki-base
Requires:  nss-tools
Requires:  openssl
Requires:  openldap-clients
Requires:  systemd
BuildArch:     noarch
BuildRequires: systemd
BuildRequires: python3-devel
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: git

%description
ipacta Certificate Trust Authority

Built on the cryptography library, ipacta provides a dogtag compatible
REST API, CLI tools, and Python PKI client library that FreeIPA expects,
without requiring Java, Tomcat, or the Dogtag stack.

%package -n python3-ipacta
Summary:   Python3 bindings for ipacta
Requires:  python3-ipacta-pki = %{version}-%{release}
Requires:  python3-cryptography >= 49
Requires:  python3-ldap
Requires:  python3-flask
Requires:  python3-werkzeug
Requires:  python3-cachetools
Requires:  python3-dns
Requires:  python3-ldap
Requires:  python3-pyasn1

%description -n python3-ipacta
Python3 bindings for ipacta.

%package -n python3-ipacta-pki
Summary:   Python3 bindings for pki
Provides:  python3-pki = %{pki_version}
Conflicts: python3-%{dogtag_name}-pki
Requires:  python3-cryptography
Requires:  python3-ldap
Requires:  python3-requests

%description -n python3-ipacta-pki
Python3 pki bindings for ipacta.

%prep
%autosetup
./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/pki
mkdir -p %{buildroot}%{_localstatedir}/log/pki

%check
# The upstream release does not include an automated test suite.

%files
%license COPYING
%doc README.md
%{_bindir}/ipacta-verify-certs
%{_bindir}/PKCS12Export
%{_bindir}/pki
%{_bindir}/pkidestroy
%{_bindir}/pki-server
%{_bindir}/pkispawn
%{_bindir}/tomcat
%attr(0755,root,root) %dir %{_sysconfdir}/pki
%attr(0755,root,root) %dir %{_datadir}/pki
%attr(0755,root,root) %dir %{_datadir}/pki/acme
%attr(0755,root,root) %dir %{_datadir}/pki/acme/database
%attr(0755,root,root) %dir %{_datadir}/pki/acme/database/ds
%attr(0755,root,root) %dir %{_datadir}/pki/ca
%attr(0755,root,root) %dir %{_datadir}/pki/ca/profiles
%attr(0755,root,root) %dir %{_datadir}/pki/ca/profiles/ca
%attr(0755,root,root) %dir %{_datadir}/ipacta
%attr(0755,root,root) %dir %{_datadir}/ipacta/ldap
%attr(0755,root,root) %dir %{_datadir}/ipacta/templates
%dir %{_localstatedir}/log/pki
%{_datadir}/pki/VERSION
%{_datadir}/pki/acme/database/ds/schema.ldif
%{_datadir}/pki/ca/profiles/ca/acmeServerCert.cfg
%{_datadir}/pki/ca/profiles/ca/caAuditSigningCert.cfg
%{_datadir}/pki/ca/profiles/ca/caCACert.cfg
%{_datadir}/pki/ca/profiles/ca/caInternalAuthAuditSigningCert.cfg
%{_datadir}/pki/ca/profiles/ca/caInternalAuthDRMstorageCert.cfg
%{_datadir}/pki/ca/profiles/ca/caInternalAuthOCSPCert.cfg
%{_datadir}/pki/ca/profiles/ca/caInternalAuthServerCert.cfg
%{_datadir}/pki/ca/profiles/ca/caInternalAuthTransportCert.cfg
%{_datadir}/pki/ca/profiles/ca/caIPAserviceCert.cfg
%{_datadir}/pki/ca/profiles/ca/caOCSPCert.cfg
%{_datadir}/pki/ca/profiles/ca/caServerCert.cfg
%{_datadir}/pki/ca/profiles/ca/caSignedLogCert.cfg
%{_datadir}/pki/ca/profiles/ca/caSubsystemCert.cfg
%{_datadir}/ipacta/ldap/acl.ldif
%{_datadir}/ipacta/ldap/create.ldif
%{_datadir}/ipacta/ldap/index.ldif
%{_datadir}/ipacta/ldap/indextasks.ldif
%{_datadir}/ipacta/ldap/schema.ldif
%{_datadir}/ipacta/ldap/vlv.ldif
%{_datadir}/ipacta/ldap/vlvtasks.ldif
%{_datadir}/ipacta/templates/tmpfiles.conf.template
%{_unitdir}/pki-tomcatd.target
%{_unitdir}/pki-tomcatd@.service
%{_unitdir}/pki-tomcatd@.socket
%config(noreplace) %{_sysconfdir}/systemd/journald@ipacta.conf
%{_sysusersdir}/ipacta.conf
%{_tmpfilesdir}/ipacta.conf

%files -n python3-ipacta
%doc README.md
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/cli
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/cli/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/core
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/core/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/certificate
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/certificate/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/rest_api
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/rest_api/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/storage
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/storage/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/profile
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/profile/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/install
%attr(0755,root,root) %dir %{python3_sitelib}/ipacta/install/__pycache__
%{python3_sitelib}/ipacta/__pycache__/*.py*
%{python3_sitelib}/ipacta/*.py*
%{python3_sitelib}/ipacta/cli/*.py*
%{python3_sitelib}/ipacta/cli/__pycache__/*.py*
%{python3_sitelib}/ipacta/core/*.py*
%{python3_sitelib}/ipacta/core/__pycache__/*.py*
%{python3_sitelib}/ipacta/certificate/*.py*
%{python3_sitelib}/ipacta/certificate/__pycache__/*.py*
%{python3_sitelib}/ipacta/rest_api/*.py*
%{python3_sitelib}/ipacta/rest_api/__pycache__/*.py*
%{python3_sitelib}/ipacta/storage/*.py*
%{python3_sitelib}/ipacta/storage/__pycache__/*.py*
%{python3_sitelib}/ipacta/profile/*.py*
%{python3_sitelib}/ipacta/profile/__pycache__/*.py*
%{python3_sitelib}/ipacta/install/*.py*
%{python3_sitelib}/ipacta/install/__pycache__/*.py*

%files -n python3-ipacta-pki
%doc README.md
%attr(0755,root,root) %dir %{python3_sitelib}/pki
%attr(0755,root,root) %dir %{python3_sitelib}/pki/__pycache__
%{python3_sitelib}/pki/__pycache__/*.py*
%{python3_sitelib}/pki/*.py*

%post
%sysusers_create %{_sysusersdir}/ipacta.conf
%tmpfiles_create ipacta.conf

%changelog
* Wed Sep 23 2026 Thomas Woerner <twoerner@redhat.com> - 0.1.1-1
- Initial release
