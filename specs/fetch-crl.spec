Name: fetch-crl
Version: 3.0.23
Release: %autorelease
Summary: Downloads Certificate Revocation Lists

License: Apache-2.0
URL: https://wiki.nikhef.nl/grid/FetchCRL3
Source0: https://dist.eugridpma.info/distribution/util/fetch-crl3/fetch-crl-%{version}.tar.gz

# https://github.com/dlgroep/fetch-crl/pull/6
Patch0:  sbin-to-bin.patch

# systemd files.
Source1: fetch-crl.service
Source2: fetch-crl.timer

BuildArch: noarch

Requires: openssl
%if 0%{?el7}
Requires: perl(File::Basename)
Requires: perl(File::Temp)
Requires: perl(Getopt::Long)
Requires: perl(IO::Select)
Requires: perl(IPC::Open3)
Requires: perl(LWP)
Requires: perl(POSIX)
Requires: perl(Sys::Syslog)
Requires: perl(Time::Local)
%endif

Requires: perl(LWP::Protocol::https)

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
BuildRequires:    perl-generators
BuildRequires:    systemd
BuildRequires: make

%description
This tool and associated timer entry ensure that Certificate Revocation
Lists (CRLs) are periodically retrieved from the web sites of the respective
Certification Authorities.
It assumes that the installed CA files follow the hash.crl_url convention.

%prep
%autosetup
cp -p %{SOURCE1} fetch-crl.service
cp -p %{SOURCE2} fetch-crl.timer

# The perl script contains some modules inside of
# it. These end up being rpm required but are
# not rpm provided. This is quite correct since they
# are private to this script.
# Consequence we must filter the requires of the script.
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(CRL)/d' |\
sed -e '/perl(CRLWriter)/d' |\
sed -e '/perl(ConfigTiny)/d' |\
sed -e '/perl(FCLog)/d' |\
sed -e '/perl(OSSL)/d' |\
sed -e '/perl(TrustAnchor)/d' |\
sed -e '/perl(base64)/d'
EOF

%global __perl_requires %{_builddir}/fetch-crl-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build
# Nothing to build.

%install
make install PREFIX=$RPM_BUILD_ROOT%{_usr} ETC=$RPM_BUILD_ROOT%{_sysconfdir} CACHE=$RPM_BUILD_ROOT%{_var}/cache
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644  %{name}.service $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -p -m 644  %{name}.timer $RPM_BUILD_ROOT%{_unitdir}/%{name}.timer

# Remove some files that have been duplicated as docs.
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

%post
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.timer

%postun
%systemd_postun_with_restart %{name}.timer

%files
%{_bindir}/%{name}
%{_bindir}/clean-crl
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%dir %{_var}/cache/%{name}
%dir %{_sysconfdir}/grid-security
%dir %{_sysconfdir}/grid-security/certificates
%dir %{_sysconfdir}/%{name}.d
%doc %{_mandir}/man8/%{name}.8.gz
%doc %{_mandir}/man8/clean-crl.8.gz
%doc CHANGES NOTICE README fetch-crl.cnf.example
%config(noreplace) %{_sysconfdir}/%{name}.conf
%license LICENSE

%changelog
%autochangelog
