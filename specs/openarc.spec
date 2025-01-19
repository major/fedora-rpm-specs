%global systemd (0%{?fedora} >= 18) || (0%{?rhel} >= 7)
# F21+ and RHEL8+ have systemd 211+ which offers RuntimeDirectory
# use that instead of tmpfiles.d
%global systemd_runtimedir (0%{?fedora} >= 21) || (0%{?rhel} >= 8)
%global tmpfiles ((0%{?fedora} >= 15) || (0%{?rhel} == 7)) && !%{systemd_runtimedir}

%global baserelease 21
%global pre_rel Beta3

Summary: An open source library and milter for providing ARC service
Name: openarc
Version: 1.0.0
Release: %{?pre_rel:0.}%{baserelease}%{?pre_rel:.%pre_rel}%{?dist}
# Automatically converted from old format: BSD and Sendmail - review is highly recommended.
License: LicenseRef-Callaway-BSD AND Sendmail-8.23
URL: https://github.com/trusteddomainproject/OpenARC
# actually https://github.com/trusteddomainproject/OpenARC/archive/rel-openarc-1-0-0-Beta3.tar.gz but our local tarball is misnamed
Source0:  openarc-1.0.0.Beta3.tar.gz
Patch0:   openarc-headerdebug.patch
# https://github.com/trusteddomainproject/OpenARC/pull/121
# Fixes Microsoft Office 365 signature validation
Patch1:   0001-Remove-t-from-the-list-of-required-AS-tags.patch

BuildRequires: make
BuildRequires: libtool gcc
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(jansson)

# sendmail-devel renamed for F25+
%if 0%{?fedora} > 25
BuildRequires: sendmail-milter-devel
%else
BuildRequires: sendmail-devel
%endif

BuildRequires: autoconf
BuildRequires: automake

Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: libopenarc = %{version}-%{release}
Requires(pre): shadow-utils
%if %systemd
# Required for systemd
%{?systemd_requires}
BuildRequires: systemd
%else
# Required for SysV
Requires(post): chkconfig
Requires(preun): chkconfig, initscripts
%endif


%description
The Trusted Domain Project is a community effort to develop and maintain a
C library for producing ARC-aware applications and an open source milter for
providing ARC service through milter-enabled MTAs.

%package -n libopenarc
Summary: An open source ARC library

%description -n libopenarc
This package contains the library files required for running services built
using libopenarc.

%package -n libopenarc-devel
Summary: Development files for libopenarc
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n libopenarc-devel
This package contains the static libraries, headers, and other support files
required for developing applications against libopenarc.

%prep
%autosetup -n OpenARC-rel-openarc-1-0-0-Beta3 -p1


%build
autoreconf --install
%configure --disable-static
%make_build

%install
%make_install
mkdir -p -m 0700 %{buildroot}%{_sysconfdir}/%{name}
mkdir -p -m 0750 %{buildroot}%{_rundir}/%{name}
rm -r %{buildroot}%{_prefix}/share/doc/openarc
rm %{buildroot}/%{_libdir}/*.la


cat > %{buildroot}%{_sysconfdir}/openarc.conf <<EOF
## See openarc.conf(5) or %{_docdir}/%{name}%{?rhel:-%{version}}/openarc.conf.sample for more
#PidFile %{_rundir}/%{name}/%{name}.pid
Syslog  yes
UserID  openarc:openarc
Socket  local:%{_rundir}/%{name}/%{name}.sock
SignHeaders to,subject,message-id,date,from,mime-version,dkim-signature
PeerList %{_sysconfdir}/%{name}/PeerList
MilterDebug 6
EnableCoredumps yes

## After setting Mode to "sv", running
## opendkim-genkey -D %{_sysconfdir}/openarc -s key -d `hostname --domain`
## and putting %{_sysconfdir}/openarc
#Mode                    sv
#Canonicalization        relaxed/simple
#Domain                  example.com # change to domain
#Selector                key
#KeyFile                 %{_sysconfdir}/openarc/key.private
#SignatureAlgorithm rsa-sha256
EOF

# Don't sign or validate connections from localhost
cat > %{buildroot}%{_sysconfdir}/%{name}/PeerList <<EOF
127.0.0.1/32
[::1]/128
EOF
chmod 0640 %{buildroot}%{_sysconfdir}/%{name}/PeerList

%if %systemd
install -d -m 0755 %{buildroot}%{_unitdir}
cat > %{buildroot}%{_unitdir}/%{name}.service << 'EOF'
[Unit]
Description=Authenticated Receive Chain (ARC) Milter
Documentation=man:%{name}(8) man:%{name}.conf(5) http://www.trusteddomain.org/%{name}/
After=network.target nss-lookup.target syslog.target

[Service]
Type=simple
%if %{systemd_runtimedir}
RuntimeDirectory=%{name}
RuntimeDirectoryMode=0750
%endif
EnvironmentFile=-%{_sysconfdir}/sysconfig/%{name}
ExecStart=/usr/sbin/%{name} -f $OPTIONS
ExecStartPost=/sbin/restorecon -r -F %{_rundir}/%{name}
ExecReload=/bin/kill -USR1 $MAINPID
Restart=on-failure
User=%{name}
Group=%{name}
UMask=0007
ProtectSystem=strict
ProtectHome=true

[Install]
WantedBy=multi-user.target
EOF
%else
mkdir -p %{buildroot}%{_initrddir}
install -m 0755 contrib/init/redhat/%{name} %{buildroot}%{_initrddir}/%{name}
%endif

%if %{tmpfiles}
install -p -d %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
D %{_rundir}/%{name} 0750 %{name} %{name} -
EOF
%endif

%pre
if ! getent passwd %{name} >/dev/null 2>&1; then
    %{_sbindir}/useradd -M -d %{_localstatedir}/lib/%{name} -r -s /sbin/nologin %{name}
    if ! getent group %{name} >/dev/null; then
        %{_sbindir}/groupadd %{name}
        %{_sbindir}/usermod -g %{name} %{name}
    fi
    if getent group mail >/dev/null; then
        %{_sbindir}/usermod -G mail %{name}
    fi
fi
exit 0


%post

%if %systemd
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name} || :
%endif


%preun
%if %systemd
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ]; then
    service %{name} stop >/dev/null || :
    /sbin/chkconfig --del %{name} || :
fi
exit 0
%endif

%postun
%if %systemd
%systemd_postun_with_restart %{name}.service
%endif

%ldconfig_scriptlets -n libopenarc

%files
%license LICENSE LICENSE.Sendmail
%doc README RELEASE_NOTES %{name}/%{name}.conf.sample
%dir %attr(0755,root,%{name}) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0644,root,%{name}) %{_sysconfdir}/%{name}.conf
%config(noreplace) %attr(0440,%{name},%{name}) %{_sysconfdir}/%{name}/PeerList

%if %{tmpfiles}
%{_tmpfilesdir}/%{name}.conf
%endif
%if !%{tmpfiles} && !%{systemd_runtimedir}
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}
%endif

%if %{systemd}
%{_unitdir}/%{name}.service
%else
%{_initrddir}/%{name}
%endif
%{_mandir}/*/*
%{_sbindir}/*


%files -n libopenarc
%license LICENSE LICENSE.Sendmail
%{_libdir}/*.so.0
%{_libdir}/*.so.0.0.0

%files -n libopenarc-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.21.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-0.20.Beta3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.19.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.18.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.17.Beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 11 2023 Tim Landscheidt <tim@tim-landscheidt.de> - 1.0.0-0.16.Beta3
- Use %%baserelease macro so that rpmdev-bumpspec can bump release properly

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.15.Beta3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild


* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.15.Beta3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct  2 2022 Matt Domsch<mdomsch@fedoraproject.org> - 1.0.0-0.15.Beta3
- Remove PidFile from config as systemd doesn't need it
- Remove ReadWritePaths from systemd as it's not needed

* Mon Sep  5 2022 Matt Domsch<mdomsch@fedoraproject.org> - 1.0.0-0.14.Beta3
- Add Restart=on-failure to systemd service file
- add postun to restart on upgrade

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.13.Beta3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 24 2022 Matt Domsch <mdomsch@fedoraproject.org> - 1.0.0-0.13.Beta3
- Add upstream PR 121 to fix Office 365 signature validation
- Use systemd service type=simple to avoid PID file race

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.11.Beta3.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.0.0-0.11.Beta3.4
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.11.Beta3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.11.Beta3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.11.Beta3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Matt Domsch <mdomsch@fedoraproject.org> - 1.0.0-0.11.Beta3
- set selinux labels on /run/openarc
- restore selinux labels at service start

* Fri May 15 2020 Matt Domsch <mdomsch@fedoraproject.org> - 1.0.0-0.10.Beta3
- add headerdebug patch

* Fri May 1 2020 Matt Domsch <mdomsch@fedoraproject.org> - 1.0.0-0.9.Beta3
- fix typo in systemd service file
- use RuntimeDirectory and RuntimeDirectoryMode when systemd 211 or higher is present
  rather than tmpfiles.d.
- use ReadWritePaths to ensure our temp directory is writable with ProtectSystem=strict

* Tue Apr 21 2020 Matt Domsch <mdomsch@fedoraproject.org> - 1.0.0-0.8.Beta3
- packaging suggestions from
  https://github.com/trusteddomainproject/OpenARC/pull/103#issuecomment-574367733
- use systemd service ProtectHome and ProtectSystem

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.7.Beta3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.0.0-0.7.Beta3
- Remove obsolete requirement for %%postun scriptlet

* Mon Dec  2 2019 Matt Domsch <mdomsch@fedoraproject.org> - 1.0.0-0.6.Beta3
- Upstream beta3
- Add dependency on janusson-devel, needed for new SealHeaderChecks config option

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.Beta2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Matt Domsch <matt@domsch.com - 1.0.0-0.1.Beta2
- Upstream beta2, drop merged patch

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.1.Beta1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Matt Domsch <matt@domsch.com> 1.0.0-0.1.Beta1
- Upstream beta1

* Sat Sep 22 2018 Matt Domsch <matt@domsch.com> 1.0.0-0.4.Beta0
- fix ownership of openarc.conf and PeerList files

* Sat Sep 22 2018 Matt Domsch <matt@domsch.com> 1.0.0-0.3.Beta0
- replace header generation patch with upstream fix
- apply specfile fixes from https://github.com/trusteddomainproject/OpenARC/pull/103

* Mon Sep 10 2018 Matt Domsch <matt@domsch.com> 1.0.0-0.2.Beta0
- Own /etc/openarc/
- improve default config file, add default PeerList config

* Wed Jul 11 2018 Xavier Bachelot <xavier@bachelot.org> 1.0.0-0.1.Beta0
- Specfile clean up.
- Update to 1.0.0 beta 0.

* Sun Jul 23 2017  Matt Domsch <matt@domsch.com> 0.1.0-1
- update to Fedora Packaging Guidelines
