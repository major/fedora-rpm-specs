Summary:           Milter to check mails for suspicious Microsoft VBA macro code
Name:              macromilter
URL:               https://github.com/sbidy/MacroMilter
Version:           3.7.0
License:           MIT
%global            baserelease      16

# Build from release or from git snapshot
%bcond_without     snapshot

# Build python2 up till fc31 and rhel7, use python3 on fc32+ and rhel8+
%if ( 0%{?fedora} && 0%{?fedora} >= 32 ) || ( 0%{?rhel} && 0%{?rhel} >= 8 )
%bcond_without     python3
%else
%bcond_with        python3
%endif

%global            gituser         sbidy
%global            gitname         MacroMilter
#                                  3.7 branch pre-release
%global            gitdate         20191111
%global            commit          2761838f0358995828e38cdcce06f845162cc55f
%global            shortcommit     %(c=%{commit}; echo ${c:0:7})


%if ! 0%{?with_snapshot}
#Build from release
Source0:           https://github.com/%{gituser}/%{gitname}/archive/%{version}/%{name}-%{version}.tar.gz
Release:           %{baserelease}%{?dist}
%else
#Build from git snapshot
Source0:           https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Release:           0.%{baserelease}.%{gitdate}git%{shortcommit}%{?dist}
%endif

Source1:           macromilter.service
Source2:           macromilter.logrotate
Source3:           macromilter.tmpfilesd
Source4:           README.fedora
#Patch0:            macromilter-3.4.3-var-lib.patch

BuildArch:         noarch

BuildRequires:     systemd

Requires(pre):     shadow-utils
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%if 0%{?with_python3}
BuildRequires:     python%{python3_pkgversion}-devel
Requires:          python%{python3_pkgversion}-oletools
Requires:          python%{python3_pkgversion}-pymilter

%else
BuildRequires:     python2-devel
Requires:          python2-oletools

# No python3-pymilter package yet
%if 0%{?rhel} > 7 || 0%{?fedora} > 27
Requires:          python2-pymilter
%else
Requires:          python-pymilter
%endif
%endif

Provides:          MacroMilter = %{version}-%{release}

%description
Python based milter for Sendmail and Postfix MTA servers to check incoming
e-mails for Microsoft Office attachments. If a Microsoft Office document is
attached to the e-mail, it will be scanned for suspicious VBA macro code.
Files with malicious macros are, depending on configuration, either removed
and replaced by harmless text files or alternatively the whole e-mail will
be rejected.


%prep
%if ! 0%{?with_snapshot}
%autosetup -n MacroMilter-%{version}
%else
%autosetup -n MacroMilter-%{commit}
%endif
cp -pf %{SOURCE4} .


%build
# Empty build section, most likely nothing required.


%install
install -D -p -m 755 %{name}/macromilter.py %{buildroot}%{_bindir}/%{name}
%if 0%{?with_python3}
sed -e '1i #!%{_bindir}/python3' -i %{buildroot}%{_bindir}/%{name}
%else
sed -e '1i #!%{_bindir}/python2' -i %{buildroot}%{_bindir}/%{name}
%endif
touch -c -r %{name}/macromilter.py %{buildroot}%{_bindir}/%{name}
install -D -p -m 644 %{name}/config.yaml %{buildroot}%{_sysconfdir}/%{name}/config.yaml
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}{/run,%{_localstatedir}/{lib,log}}/%{name}/


%pre
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "MacroMilter service" %{name}
exit 0


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE.md
%doc README.fedora README.md
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/config.yaml
%dir %{_sysconfdir}/logrotate.d/
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0755,%{name},%{name}) /run/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.16.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.15.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.14.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.13.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.12.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.11.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.10.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.9.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.8.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.7.0-0.7.20191111git2761838
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.6.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.5.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Robert Scheck <robert@fedoraproject.org> 3.7.0-0.4.20191111git2761838
- Removed unnecessary dependency on python configparser package (#1825543)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-0.3.20191111git2761838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Robert Scheck <robert@fedoraproject.org> 3.7.0-0.2.20191111git2761838
- Correct Python 3 conditionals in spec file (thanks to Michal Ambroz)

* Fri Nov 15 2019 Michal Ambroz <rebus AT_ seznam.cz> - 3.7.0-0.1.20191111git2761838
- Upgrade to 3.7.0 (GIT 20191111) (#1738083, #1770551)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Robert Scheck <robert@fedoraproject.org> 3.4.3-1
- Upgrade to 3.4.3

* Mon Oct 09 2017 Robert Scheck <robert@fedoraproject.org> 3.3-1.20171009git4e8295f
- Upgrade to 3.3 (GIT 20171009)

* Sat Oct 07 2017 Robert Scheck <robert@fedoraproject.org> 3.3-1.20171007giteae1667
- Upgrade to 3.3 (GIT 20171007)
- Initial spec file for Fedora and Red Hat Enterprise Linux
