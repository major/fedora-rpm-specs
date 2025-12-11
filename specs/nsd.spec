%global _hardened_build 1
Summary: Fast and lean authoritative DNS Name Server
Name: nsd
Version: 4.14.0
Release: %autorelease
License: BSD-3-Clause
Url: http://www.nlnetlabs.nl/nsd/
Source0: http://www.nlnetlabs.nl/downloads/%{name}/%{name}-%{version}%{?prever}.tar.gz
Source1: nsd.conf
Source2: nsd.service
Source3: tmpfiles-nsd.conf
Source4: nsd.sysusers.conf
BuildRequires: gcc
BuildRequires: flex
BuildRequires: fstrm-devel
BuildRequires: libevent-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: protobuf-c-compiler
BuildRequires: protobuf-c-devel
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros

%description
NSD is a complete implementation of an authoritative DNS name server.
For further information about what NSD is and what NSD is not please
consult the REQUIREMENTS document which is a part of this distribution.

%prep
%setup -q -n %{name}-%{version}%{?prever}

%build
CFLAGS="%{optflags} -fPIE -pie"
LDFLAGS="-Wl,-z,relro,-z,now"
export CFLAGS LDFLAGS
%configure \
    --enable-bind8-stats \
    --enable-zone-stats \
    --enable-checking \
    --enable-nsec3 \
    --with-pidfile="" \
    --with-zonelistfile=%{_sharedstatedir}/nsd/zone.list \
    --with-ssl \
    --with-user=nsd \
    --with-xfrdfile=%{_sharedstatedir}/nsd/ixfr.state \
    --with-dbfile="" \
    --enable-ratelimit \
    --enable-pie \
    --enable-relro-now \
    --enable-recvmmsg \
    --enable-packed \
    --enable-memclean \
    --enable-systemd

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/nsd.conf
mkdir -p %{buildroot}%{_rundir}/nsd
mkdir -p %{buildroot}%{_sharedstatedir}/nsd
install -m 0644 -D %{SOURCE4} %{buildroot}%{_sysusersdir}/nsd.conf

# Install ghost files
for name in control server; do
    for extension in key pem; do
        touch %{buildroot}%{_sysconfdir}/nsd/nsd_${name}.${extension}
    done
done

# Take care of the configuration
mkdir -p %{buildroot}%{_sysconfdir}/nsd/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/nsd/server.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nsd/nsd.conf
rm %{buildroot}%{_sysconfdir}/nsd/nsd.conf.sample

%files
%license LICENSE
%doc doc/*
%doc contrib/nsd.zones2nsd.conf
%dir %{_sysconfdir}/nsd
%config(noreplace) %{_sysconfdir}/nsd/nsd.conf
%attr(0640,root,nsd) %ghost %{_sysconfdir}/nsd/nsd_server.key
%attr(0640,root,nsd) %ghost %{_sysconfdir}/nsd/nsd_server.pem
%attr(0640,root,nsd) %ghost %{_sysconfdir}/nsd/nsd_control.key
%attr(0640,root,nsd) %ghost %{_sysconfdir}/nsd/nsd_control.pem
%dir %{_sysconfdir}/nsd/conf.d
%dir %{_sysconfdir}/nsd/server.d
%attr(0644,root,root) %{_unitdir}/nsd.service
%attr(0644,root,root) %{_tmpfilesdir}/nsd.conf
%attr(0755,nsd,nsd) %dir %{_rundir}/nsd
%attr(0750,nsd,nsd) %dir %{_sharedstatedir}/nsd
%{_sbindir}/*
%{_mandir}/*/*
%{_sysusersdir}/nsd.conf


%post
%systemd_post nsd.service

%preun
%systemd_preun nsd.service

%postun
%systemd_postun_with_restart nsd.service

%changelog
%autochangelog
