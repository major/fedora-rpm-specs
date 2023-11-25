%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           fedora-packager
Version:        0.6.0.7
Release:        %autorelease
Summary:        Tools for setting up a fedora maintainer environment

License:        GPLv2+
URL:            https://pagure.io/fedora-packager
Source0:        https://releases.pagure.org/fedora-packager/fedora-packager-%{version}.tar.bz2

BuildRequires:  python3-devel
BuildRequires:  make
BuildRequires:  automake
Requires:       koji >= 1.11.0
Requires:       bodhi-client
Requires:       rpm-build rpmdevtools rpmlint
Requires:       rpmautospec
Requires:       mock curl openssh-clients
Requires:       redhat-rpm-config
Requires:       fedpkg >= 1.0
Obsoletes:      fedora-cert < 0.6.0.3-4
Obsoletes:      fedora-packager-yubikey < 0.6.0.7-3
Recommends:     fedora-packager-kerberos

BuildArch:      noarch

%description
Set of utilities useful for a fedora packager in setting up their environment.

%package kerberos
Summary:        files for connecting via kerberos to Fedora
# This is the version in which SNI was fixed
%if 0%{?fedora}
Requires:       krb5-workstation >= 1.14.3-4
%else
%if 0%{?rhel} >= 7
Requires:       krb5-workstation  >= 1.14.1-24
%else
# older rhels wont fully work without configuration, but lets make sure they have krb
# we should be able to assume newer RHELs's will have a new enough version
Requires:       krb5-workstation
%endif
%endif
Requires:       krb5-pkinit

BuildArch:      noarch

%description kerberos
Files for connecting via kerberos to Fedora

%prep
%setup -q

%build
%configure PYTHON=%{__python3}
%make_build

%install
%make_install
sed -i -r 's|#!/usr/bin/python$|#!%{__python3}|' %{buildroot}/usr/*bin/*
# The fedora-burn-yubikey utility only worked with fas2, which is now retired.
rm -f %{buildroot}/usr/sbin/fedora-burn-yubikey

%files
%license COPYING
%doc TODO AUTHORS ChangeLog
%{_bindir}/*
%exclude %{_bindir}/fedora-hosted
%exclude %{_bindir}/fedora-packager-setup
%exclude %{_bindir}/fedoradev-pkgowners
%exclude %{_bindir}/fedora-cert
%exclude %{_bindir}/fkinit
%exclude %{python3_sitelib}/fedora_cert

%config(noreplace) %{_sysconfdir}/koji.conf.d/*


%files kerberos
%license COPYING
%{_bindir}/fkinit
%config %{_sysconfdir}/krb5.conf.d/*
%{_sysconfdir}/pki/ipa/*

%changelog
%autochangelog
