Name:           fedora-packager
Version:        1.1
Release:        %autorelease
Summary:        Tools for setting up a Fedora maintainer environment

License:        GPL-2.0-or-later
URL:            https://pagure.io/fedora-packager

Source0:        COPYING
Source2:        pkgname.py
Source3:        rpmbuild-md5
Source4:        secondary-koji
Source5:        fkinit

Source10:       fedora.conf
Source11:       s390.conf
Source12:       stg.conf
Source13:       fedoraproject_org
Source14:       stg_fedoraproject_org
Source15:       fedoraproject_ipa_ca.crt
Source16:       stg_fedoraproject_ipa_ca.crt

BuildRequires:  python3-devel

Requires:       koji >= 1.11.0
Requires:       python3-koji-cli-plugins
Requires:       bodhi-client
Requires:       rpm-build rpmdevtools rpmlint
Requires:       rpmautospec
Requires:       mock curl openssh-clients
Requires:       redhat-rpm-config
Requires:       fedpkg >= 1.0
Requires:       systemd
Obsoletes:      fedora-cert < 0.6.0.3-4
Obsoletes:      fedora-packager-yubikey < 0.6.0.7-3
Recommends:     fedora-packager-kerberos
Requires:       (fedora-packager-kerberos = %{version}-%{release} if fedora-packager-kerberos)

# A CLI tool to query Fedora and EPEL repositories
Recommends:     fedrq
# Another CLI tool to query Fedora, EPEL, ELN, and CentOS Stream repositories
Recommends:     fedora-repoquery
# Yet another CLI tool to query Fedora, ELN, Alma, CentoOS Stream, etc.
Recommends:     rpmdistro-repoquery

# Needed for koji edit-sidetag
Recommends:     python3-koji-cli-plugins

# A CLI tool that helps conduct package reviews
Recommends:     fedora-review

BuildArch:      noarch

%description
Set of utilities and configuration to set up a working Fedora packager
environment.

%package kerberos
Summary:        Configuration to connect via kerberos to Fedora
# This is the version in which SNI was fixed
%if 0%{?fedora}
Requires:       krb5-workstation >= 1.14.3-4
%elif 0%{?rhel} >= 7
Requires:       krb5-workstation  >= 1.14.1-24
%else
# Older rhels won't fully work without configuration, but lets make
# sure they have krb we should be able to assume newer RHELs's will
# have a new enough version.
Requires:       krb5-workstation
%endif
Requires:       krb5-pkinit

%description kerberos
%{summary}.

%prep
# nada

%build
# nada

%install
install -D %{SOURCE0} %{buildroot}%{_licensedir}/%{name}/COPYING
install -D %{SOURCE2} %{buildroot}%{_bindir}/pkgname
install -D %{SOURCE3} %{buildroot}%{_bindir}/rpmbuild-md5
install -D %{SOURCE4} %{buildroot}%{_bindir}/s390-koji
install -D %{SOURCE4} %{buildroot}%{_bindir}/stg-koji
install -D %{SOURCE5} %{buildroot}%{_bindir}/fkinit

install -m0644 -Dt %{buildroot}%{_sysconfdir}/koji.conf.d/ \
  %{SOURCE10} %{SOURCE11} %{SOURCE12}
install -m0644 -Dt %{buildroot}%{_sysconfdir}/krb5.conf.d/ \
  %{SOURCE13} %{SOURCE14}
install -m0644 -Dt %{buildroot}%{_sysconfdir}/pki/ipa/ \
  %{SOURCE15} %{SOURCE16}

%files
%license %{_licensedir}/%{name}/
%{_bindir}/pkgname
%{_bindir}/rpmbuild-md5
%{_bindir}/s390-koji
%{_bindir}/stg-koji
%config(noreplace) %{_sysconfdir}/koji.conf.d/*

%files kerberos
%license %{_licensedir}/%{name}/
%{_bindir}/fkinit
%config %{_sysconfdir}/krb5.conf.d/*
%{_sysconfdir}/pki/ipa/*

%changelog
%autochangelog
