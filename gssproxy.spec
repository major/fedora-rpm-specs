Name:		gssproxy

Version:	0.9.2
Release:	%autorelease
Summary:	GSSAPI Proxy

License:	MIT
URL:		https://github.com/gssapi/gssproxy
Source0:	https://github.com/gssapi/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	rwtab
Source2:        gssproxy.sock.compat.conf

%global servicename gssproxy
%global pubconfpath %{_sysconfdir}/gssproxy
%global gpstatedir %{_localstatedir}/lib/gssproxy
%global gpsockpath %{_rundir}/gssproxy.default.sock

### Patches ###

### Dependencies ###
Requires: krb5-libs >= 1.12.0
Requires: keyutils-libs
Requires: libverto-module-base
Requires: libini_config >= 1.2.0
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

# We use a Conflicts: here so as not to interfere with users who make
# their own policy.  The version is the last time someone has filed a
# bug about gssproxy being broken with selinux.
Conflicts: selinux-policy < 3.13.1-283.5

### Build Dependencies ###
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: docbook-style-xsl
BuildRequires: doxygen
BuildRequires: findutils
BuildRequires: gettext-devel
BuildRequires: git
BuildRequires: keyutils-libs-devel
BuildRequires: krb5-devel >= 1.12.0
BuildRequires: libini_config-devel >= 1.2.0
BuildRequires: libselinux-devel
BuildRequires: libtool
BuildRequires: libverto-devel
BuildRequires: libxml2
BuildRequires: libxslt
BuildRequires: make
BuildRequires: m4
BuildRequires: pkgconfig
BuildRequires: popt-devel
BuildRequires: systemd-units

%description
A proxy for GSSAPI credential handling

%prep
%autosetup -S git

%build
autoreconf -f -i
%configure \
    --with-pubconf-path=%{pubconfpath} \
    --with-socket-name=%{gpsockpath} \
    --with-initscript=systemd \
    --disable-static \
    --disable-rpath \
    --with-gpp-default-behavior=REMOTE_FIRST

make %{?_smp_mflags} all
make test_proxymech

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/gssproxy/proxymech.la
install -d -m755 %{buildroot}%{_sysconfdir}/gssproxy
install -m644 examples/gssproxy.conf %{buildroot}%{_sysconfdir}/gssproxy/gssproxy.conf
install -m644 examples/99-network-fs-clients.conf %{buildroot}%{_sysconfdir}/gssproxy/99-network-fs-clients.conf
mkdir -p -m755 %{buildroot}%{_sysconfdir}/gss/mech.d
install -m644 examples/proxymech.conf %{buildroot}%{_sysconfdir}/gss/mech.d/proxymech.conf
mkdir -p %{buildroot}%{gpstatedir}/rcache
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rwtab.d
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
install -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/rwtab.d/gssproxy
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_tmpfilesdir}/%{name}.conf
ln -s %{gpsockpath} %{buildroot}%{gpstatedir}/default.sock

%files
%license COPYING
%{_unitdir}/gssproxy.service
%{_userunitdir}/gssuserproxy.service
%{_userunitdir}/gssuserproxy.socket
%{_sbindir}/gssproxy
%attr(755,root,root) %dir %{pubconfpath}
%attr(755,root,root) %dir %{gpstatedir}
%attr(700,root,root) %dir %{gpstatedir}/clients
%attr(700,root,root) %dir %{gpstatedir}/rcache
%attr(0600,root,root) %config(noreplace) /%{_sysconfdir}/gssproxy/gssproxy.conf
%attr(0600,root,root) %config(noreplace) /%{_sysconfdir}/gssproxy/99-network-fs-clients.conf
%attr(0644,root,root) %config(noreplace) /%{_sysconfdir}/gss/mech.d/proxymech.conf
%dir %{_libdir}/gssproxy
%{_libdir}/gssproxy/proxymech.so
%{_mandir}/man5/gssproxy.conf.5*
%{_mandir}/man8/gssproxy.8*
%{_mandir}/man8/gssproxy-mech.8*
%config(noreplace) %{_sysconfdir}/rwtab.d/gssproxy
%{gpstatedir}/default.sock
%{_tmpfilesdir}/%{name}.conf

%pre
if [ -S %{gpstatedir}/default.sock ]; then
    rm -f %{gpstatedir}/default.sock
fi

%post
%systemd_post gssproxy.service

%preun
%systemd_preun gssproxy.service

%postun
%systemd_postun_with_restart gssproxy.service

%changelog
%autochangelog
