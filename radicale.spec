%global selinux_types %(%{__awk} '/^#[[:space:]]*SELINUXTYPE=/,/^[^#]/ { if ($3 == "-") printf "%s ", $2 }' /etc/selinux/config 2>/dev/null)
%global selinux_variants %([ -z "%{selinux_types}" ] && echo mls targeted || echo %{selinux_types})

# unfortunately, radicale major version upgrades are breakable updates, therefore
# Fedora >= 31: introduce radicale3
#
# Note: this is the simplified spec file for Fedora

%define	radicale_major	3

%if %{?radicale_major} >= 3
%define	radicale_version	3.1.8
%else
%if %{?radicale_major} >= 2
%define	radicale_version	2.1.12
%endif
%endif

%define	radicale_name	radicale

%if %{?radicale_major} >= 3
%define	radicale_package_name	radicale3
%else
%define	radicale_package_name	radicale2
%endif

Name:             radicale
Version:          %{radicale_version}
Release:          39%{?dist}
Summary:          A simple CalDAV (calendar) and CardDAV (contact) server
License:          GPLv3+
URL:              https://radicale.org
%if %{?radicale_major} >= 3
Source0:          https://github.com/Kozea/Radicale/archive/v%{version}/%{name}-%{version}.tar.gz
%else
%if %{?radicale_major} >= 2
Source0:          https://github.com/Kozea/Radicale/archive/%{version}/%{name}-%{version}.tar.gz
%endif
%endif
Source1:          %{name}.service
Source2:          %{name}-logrotate
Source3:          %{name}-httpd
Source4:          %{name}.te
Source5:          %{name}.fc
Source6:          %{name}.if
Source7:          %{name}-tmpfiles.conf

Source50:	  %{name}-test-example.ics
Source51:	  %{name}-test-example.vcf

Patch0:           %{name}-config-storage-hooks-SELinux-note.patch
Patch1:           %{name}-3.1.8-20230322-6ae831a3.patch

BuildArch:        noarch


%package -n %{radicale_package_name}
Summary:          %{summary}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    systemd
BuildRequires:    checkpolicy
BuildRequires:    selinux-policy-devel
BuildRequires:    hardlink

# for 'make check' of major version 3.0.6
BuildRequires:    python3-defusedxml
BuildRequires:    python3-passlib
BuildRequires:    python3-vobject >= 0.9.6
BuildRequires:    python3-dateutil >= 2.7.3

%if "%{?radicale_major}" == "3"
Conflicts:        radicale < 3.0.0
Conflicts:        radicale2
%endif

%if "%{?radicale_major}" == "2"
Conflicts:        radicale < 2.0.0
Conflicts:        radicale >= 3.0.0
Conflicts:        radicale3
%endif

%if "%{?radicale_major}" == "1"
Conflicts:        radicale >= 2.0.0
Conflicts:        radicale3
%endif

Requires:         python3-%{radicale_package_name} = %{version}-%{release}
Requires(pre):    shadow-utils
%{?systemd_requires}
Suggests:         %{radicale_package_name}-selinux = %{version}-%{release}


%description
The Radicale Project is a CalDAV (calendar) and CardDAV (contact) server. It
aims to be a light solution, easy to use, easy to install, easy to configure.
As a consequence, it requires few software dependencies and is pre-configured
to work out-of-the-box.

The Radicale Project runs on most of the UNIX-like platforms (Linux, BSD,
MacOS X) and Windows. It is known to work with Evolution, Lightning, iPhone
and Android clients. It is free and open-source software, released under GPL
version 3.


%description -n %{radicale_package_name}
The Radicale Project is a CalDAV (calendar) and CardDAV (contact) server. It
aims to be a light solution, easy to use, easy to install, easy to configure.
As a consequence, it requires few software dependencies and is pre-configured
to work out-of-the-box.

The Radicale Project runs on most of the UNIX-like platforms (Linux, BSD,
MacOS X) and Windows. It is known to work with Evolution, Lightning, iPhone
and Android clients. It is free and open-source software, released under GPL
version 3.

THIS IS MAJOR VERSION %{?radicale_major}

UPGRADE BETWEEN MAJOR VERSIONS IS NOT SUPPORTED
	-> deinstall old major version
	-> install new version
	-> follow migration hints
%if "%{?radicale_major}" == "3"
Upgrade hints from major version 2 -> 3 can be found here:
 https://github.com/Kozea/Radicale/blob/v3.1.0/NEWS.md
  (section '3.0.0')
%endif
%if "%{?radicale_major}" == "2"
Upgrade hints from major version 1 -> 2 can be found here:
 https://radicale.org/v2.html#migration-from-1xx-to-2xx
%endif


%package -n python3-%{radicale_package_name}
Summary:          Python module for Radicale
Recommends:       python3-bcrypt
Recommends:       python3-passlib
%{?python_provide:%python_provide python3-%{name}}
Obsoletes:        python-%{radicale_package_name} < %{version}-%{release}

%if "%{?radicale_major}" == "3"
Conflicts:        python3-radicale < 3.0.0
Conflicts:        python3-radicale2
%endif

%if "%{?radicale_major}" == "2"
Conflicts:        python3-radicale < 2.0.0
Conflicts:        python3-radicale3
%endif

%if "%{?radicale_major}" == "1"
Conflicts:        python3-radicale >= 2.0.0
Conflicts:        python3-radicale2
Conflicts:        python3-radicale3
%endif

%description -n python3-%{radicale_package_name}
Python module for Radicale


%package -n %{radicale_package_name}-httpd
Summary:        httpd config for Radicale
Requires:       %{radicale_package_name} = %{version}-%{release}
Requires:       httpd
Requires:       python3-mod_wsgi

%if "%{?radicale_major}" == "3"
Conflicts:        radicale-httpd < 3.0.0
Conflicts:        radicale2-httpd
%endif

%if "%{?radicale_major}" == "2"
Conflicts:        radicale-httpd < 2.0.0
Conflicts:        radicale3-httpd
%endif

%if "%{?radicale_major}" == "1"
Conflicts:        radicale-httpd >= 2.0.0
Conflicts:        radicale2-httpd
Conflicts:        radicale3-httpd
%endif

%description -n %{radicale_package_name}-httpd
httpd example config for Radicale (Python3).


%package -n %{radicale_package_name}-selinux
Summary:        SELinux definitions for Radicale
Requires:       %{radicale_package_name} = %{version}-%{release}
%if "%{_selinux_policy_version}" != ""
Requires:         selinux-policy >= %{_selinux_policy_version}
%endif
Requires(post):   /usr/sbin/semodule
Requires(post):   /usr/sbin/fixfiles
Requires(post):   /usr/sbin/restorecon
Requires(post):   policycoreutils-python-utils
Requires(postun): /usr/sbin/semodule
Requires(postun): /usr/sbin/fixfiles
Requires(postun): /usr/sbin/restorecon
Requires(postun): policycoreutils-python-utils

%description -n %{radicale_package_name}-selinux
SELinux definitions for Radicale (Python3).

Note: storage hooks configuration is currently not supported by packaged
 SELinux policy and requires a local custom policy extension (RHBZ#1928899)


%prep
%autosetup -n Radicale-%{version} -p 1
mkdir SELinux
cp -p %{SOURCE4} %{SOURCE5} %{SOURCE6} SELinux

# adjust _rundir according to definition
sed -i 's|\(/var/run\)|%{_rundir}|' SELinux/%{name}.fc

%if %{?radicale_major} >= 3
# remove log directory (no longer supported since major version 3)
sed -i 's|^/var/log/.*||' SELinux/%{name}.fc
%endif


%build
%py3_build
cd SELinux

for selinuxvariant in %{selinux_variants}
do
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
    mv %{name}.pp %{name}.pp.${selinuxvariant}
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -


%install
%py3_install

# Install configuration files
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 640 config %{buildroot}%{_sysconfdir}/%{name}/
sed -i 's|^#\(level = \).*|\1 info|' %{buildroot}%{_sysconfdir}/%{name}/config
%if %{?radicale_major} < 3
install -p -m 644 logging %{buildroot}%{_sysconfdir}/%{name}/
%endif
install -p -m 644 rights %{buildroot}%{_sysconfdir}/%{name}/

# Install wsgi file
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 radicale.wsgi %{buildroot}%{_datadir}/%{name}/
sed -i 's|^#!/usr/bin/env python3$|#!/usr/bin/python3|' %{buildroot}%{_datadir}/%{name}/radicale.wsgi
%if %{?radicale_major} < 3
install -p -m 644 radicale.fcgi %{buildroot}%{_datadir}/%{name}/
sed -i 's|^#!/usr/bin/env python3$|#!/usr/bin/python3|' %{buildroot}%{_datadir}/%{name}/radicale.fcgi
%endif

# Install apache's configuration file
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Create folder where the calendar will be stored
mkdir -p  %{buildroot}%{_sharedstatedir}/%{name}/

install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%if %{?radicale_major} >= 3
## 3.0.0: Remove daemonization (should be handled by service managers)
# change start type
sed -i 's|\(Type=\).*|\1exec|' %{buildroot}%{_unitdir}/%{name}.service
# disable PIDfile
sed -i 's|\(PIDFile=\)|#NoLongerUsed in major version >=3#\1|' %{buildroot}%{_unitdir}/%{name}.service
# remove daemon options
sed -i 's|\(ExecStart=/usr/bin/radicale\).*|\1|' %{buildroot}%{_unitdir}/%{name}.service
%endif


%if %{?radicale_major} < 3
install -D -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%endif
install -D -p -m 644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_rundir}/%{name}

# adjust _rundir
sed -i 's|\(/var/run\)|%{_rundir}|' %{buildroot}%{_tmpfilesdir}/%{name}.conf
sed -i 's|\(/var/run\)|%{_rundir}|' %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_rundir}/%{name}

%if %{?radicale_major} < 3
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
%endif

for selinuxvariant in %{selinux_variants}
do
    install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
    install -p -m 644 SELinux/%{name}.pp.${selinuxvariant} \
        %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{name}.pp
done

%if 0%{?rhel}
/usr/sbin/hardlink -cv %{buildroot}%{_datadir}/selinux
%else
/usr/bin/hardlink -cv %{buildroot}%{_datadir}/selinux
%endif


%check
# check whether radicale binary is at least displaying help
echo "Check whether 'radicale' is at least able to display online help"
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/%{name} --help >/dev/null
if [ $? -eq 0 ]; then
  echo "Check whether 'radicale' is at least able to display online help - SUCCESSFUL"
else
  exit 1
fi

# create radicale collections with examples
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-ics
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-vcf
cp %{SOURCE50} %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-ics/
cp %{SOURCE51} %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-vcf/
echo '{"tag": "VADDRESSBOOK"}' >%{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-vcf/.Radicale.props
echo '{"tag": "VCALENDAR"}'    >%{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-ics/.Radicale.props

PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/%{name} -D --verify-storage --storage-filesystem-folder /%{buildroot}%{_sharedstatedir}/%{name}
if [ $? -eq 0 ]; then
  echo "Check whether 'radicale' is able to verify example storage - SUCCESSFUL"
else
  exit 1
fi

# cleanup before packaging
rm -rf %{buildroot}%{_sharedstatedir}/%{name}/collection-root
rm -rf %{buildroot}%{_sharedstatedir}/%{name}/.Radicale.lock


%pre -n %{radicale_package_name}
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_sharedstatedir}/%{name} -s /sbin/nologin \
    -c "Radicale service account" %{name}
exit 0


%post -n %{radicale_package_name}
%systemd_post %{name}.service


%post -n %{radicale_package_name}-selinux
for selinuxvariant in %{selinux_variants}
do
  if rpm -q selinux-policy-$selinuxvariant >/dev/null 2>&1; then
    echo "SELinux semodule store for %{radicale_package_name} ($selinuxvariant)"
    /usr/sbin/semodule -s ${selinuxvariant} -i \
      %{_datadir}/selinux/${selinuxvariant}/%{name}.pp
  else
    echo "SELinux semodule store for %{radicale_package_name} ($selinuxvariant) SKIPPED - policy not installed"
  fi
done
# http://danwalsh.livejournal.com/10607.html
if semanage port -l | grep -q "^radicale_port_t\s*tcp\s*5232$"; then
  echo "SELinux adjustments for %{radicale_package_name} port tcp/5232 already done"
else
  echo "SELinux adjustments for %{radicale_package_name} port tcp/5232"
  semanage port -a -t radicale_port_t -p tcp 5232
fi

echo "SELinux fixfiles for: %{radicale_package_name}"
/usr/sbin/fixfiles -R %{radicale_package_name} restore >/dev/null

if [ -d %{_localstatedir}/log/%{name} ]; then
  echo "SELinux restorecon for: %{_localstatedir}/log/%{name}"
  /usr/sbin/restorecon -R %{_localstatedir}/log/%{name}
fi


%post -n %{radicale_package_name}-httpd
# nothing related included so far in radicale.fc
#echo "SELinux fixfiles for: %{radicale_package_name}-httpd"
#/usr/sbin/fixfiles -R %{radicale_package_name}-httpd restore >/dev/null


%post -n python3-%{radicale_package_name}
# nothing related included so far in radicale.fc
#echo "SELinux fixfiles for: python3-%{radicale_package_name}"
#/usr/sbin/fixfiles -R python3-%{radicale_package_name} restore >/dev/null


%preun -n %{radicale_package_name}
%systemd_preun %{name}.service


%postun -n %{radicale_package_name}
%systemd_postun_with_restart %{name}.service 


%postun -n %{radicale_package_name}-selinux
if [ $1 -eq 0 ] ; then
  if semanage port -l | grep -q "^radicale_port_t\s*tcp\s*5232$"; then
    echo "SELinux delete for %{radicale_package_name} port tcp/5232"
    semanage port -d -p tcp 5232
  fi
  for selinuxvariant in %{selinux_variants}
  do
    if rpm -q selinux-policy-$selinuxvariant >/dev/null 2>&1; then
      echo "SELinux semodule reset %{radicale_package_name} ($selinuxvariant)"
      /usr/sbin/semodule -s ${selinuxvariant} -r %{name}
    else
      echo "SELinux semodule reset %{radicale_package_name} ($selinuxvariant) SKIPPED - policy not installed"
    fi
  done

  if [ -d %{_localstatedir}/log/%{name} ]; then
    echo "SELinux restorecon for: %{_localstatedir}/log/%{name}"
    /usr/sbin/restorecon -R %{_localstatedir}/log/%{name}
  fi
fi


%files -n %{radicale_package_name}
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640, root, %{name}) %{_sysconfdir}/%{name}/config
%if %{?radicale_major} < 3
%config(noreplace) %{_sysconfdir}/%{name}/logging
%endif
%config(noreplace) %{_sysconfdir}/%{name}/rights
%if %{?radicale_major} < 3
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%endif
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%if %{?radicale_major} < 3
%dir %attr(750, %{name}, %{name}) %{_localstatedir}/log/%{name}
%endif
%dir %attr(750, %{name}, %{name}) %{_sharedstatedir}/%{name}/
%dir %{_datadir}/%{name}
%dir %attr(755, %{name}, %{name}) %{_rundir}/%{name}


%files -n %{radicale_package_name}-selinux
%doc SELinux/*
%{_datadir}/selinux/*/%{name}.pp


%files -n python3-%{radicale_package_name}
%license COPYING.md
%{python3_sitelib}/%{name}
%{python3_sitelib}/Radicale-*.egg-info


%files -n %{radicale_package_name}-httpd
%{_datadir}/%{name}/%{name}.wsgi
%if %{?radicale_major} < 3
%{_datadir}/%{name}/%{name}.fcgi
%endif
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf


%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.1.8-39
- Rebuilt for Python 3.12

* Tue Mar 21 2023 Peter Bieringer <pb@bieringer.de> - 3.1.8-38
- Add patch against upstream 6ae831a3
- Extend SELinux policy to allow native journald logging
- Update to 3.1.8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Peter Bieringer <pb@bieringer.de> - 3.1.7-37
- Add radicale-disable-timestamp-if-started-by-systemd-PR-1276.patch
- Fix still unsolved SELinux issues (#2156633)
- Add radicale-fix-move-behind-proxy-PR-1271.patch

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 3.1.7-31
- Rebuilt for Python 3.11

* Wed Apr 20 2022 Peter Bieringer <pb@bieringer.de> - 3.1.7-30
- Update to 3.1.7 (#2077126)

* Tue Apr 19 2022 Peter Bieringer <pb@bieringer.de> - 3.1.6-29
- Update to 3.1.6 (#2076547)

* Tue Feb 08 2022 Peter Bieringer <pb@bieringer.de> - 3.1.5-29
- Update to 3.1.5 (#2052179)

* Thu Feb 03 2022 Peter Bieringer <pb@bieringer.de> - 3.1.4-28
- Update to 3.1.4 (#2049932)

* Fri Jan 28 2022 Peter Bieringer <pb@bieringer.de> - 3.1.3-27
- Update to 3.1.3 (#2047522)

* Sun Jan 23 2022 Peter Bieringer <pb@bieringer.de> - 3.1.2-26
- Update to 3.1.2 (#2043986)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Peter Bieringer <pb@bieringer.de> - 3.1.1-24
- Version 3.1.1
- Fix URLs to major version upgrade notes
- Replace NEWS.md by CHANGELOG.md

* Mon Dec 27 2021 Peter Bieringer <pb@bieringer.de> - 3.1.0-23
- SELinux policy: add notes in subpackage description and default config file that storage hooks are not supported so far (RHBZ#1928899)
- add required init_nnp_daemon_domain to radicale.te (1.0.9): (RHBZ#2020942)

* Mon Dec 27 2021 Peter Bieringer <pb@bieringer.de> - 3.1.0-22
- Version 3.1.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.6-18
- Rebuilt for Python 3.10

* Fri Mar 05 2021 Peter Bieringer <pb@bieringer.de> - 3.0.6-17
- Move SELinux into dedicated subpackage and add as suggestion to main package (RHBZ#1934895)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.6-15
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-13
- Only SELinux relabel log directory if existing
- Remove no longer required/supported log directory from SELinux file context

* Tue Sep 22 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-10
- Disable -D in systemd unit file for major version 3
- Toggle loglevel to info by default
- No longer package /var/log/radicale and the logrotate config for major version 3 (logs only to stdout/stderr now)
- Replace /var/run with _rundir (additional leftovers found)

* Tue Sep 22 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-9
- Add additional test with an example collection

* Tue Sep 22 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-8
- Cosmetic cleanup

* Mon Sep 21 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-7
- Do not use fixfiles in subpackages which have nothing related defined so far
- Enable -D in systemd unit file for major version 3
- Add 'check' section and related build requirements

* Mon Sep 21 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-6
- Remove additional failsafe checks to prevent manual upgrade from major version 2 (no longer needed)
- Revert use of radicale_package name (no no longer needed)
- Fix hidden SELinux post-install/post-uninstall issues
- Fix attributes for wsgi/fcgi
- Fix not working pre/post with new major version in package

* Sun Sep 20 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-5
- Include major version in package name
- Adjust systemd unit file for major version 3

* Sun Sep 20 2020 Peter Bieringer <pb@bieringer.de> - 3.0.6-4
- Version 3.0.6 (obsoletes fcgi and logging config file)
- Add additional failsafe checks to prevent manual upgrade from major version 2
- Replace /var/run with _rundir

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.12-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.12-1
- Version 2.1.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.11-2
- Fix hardlink path on epel

* Sun Jan 05 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.11-1
- Version 2.1.11

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.10-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.10-6
- Use autogenerated python dependencies

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.10-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.10-3
- hardlink moved to /usr/bin

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.10-1
- Version 2.1.10

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.9-4
- Rebuilt for Python 3.7

* Thu May 31 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.9-3
- Add versioned dependencies

* Wed May 23 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.9-2
- Recommends: python3-bcrypt, python3-passlib

* Wed May 16 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.9-1
- Version 2.1.9

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.8-3
- SELinux rule to allow connection to POP port

* Sun Oct 08 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.8-2
- Run in daemon mode so it creates the PID file

* Mon Sep 25 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.8-1
- Version 2.1.8

* Wed Sep 20 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.7-1
- Version 2.1.7

* Tue Sep 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.6-2
- Upload 2.1.6 sources

* Tue Sep 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.6-1
- Version 2.1.6

* Sun Aug 27 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.5-1
- Version 2.1.5

* Mon Aug 07 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.4-1
- Version 2.1.4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.2-1
- Version 2.1.2

* Sat Jul 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.1-1
- Version 2.1.1

* Fri Jun 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.0-3
- Update SELinux policy

* Fri Jun 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.0-2
- Remove PrivateDevices=true (RHBZ#1452328)

* Sun Jun 25 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.0-1
- Version 2.1.0

* Sun May 28 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.0-1
- Version 2.0.0

* Wed May 03 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.0rc2-2
- Run in foreground

* Wed May 03 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.0rc2-1
- Version 2.0.0rc2
- Drop python2 support

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-10
- Rebuild for Python 3.6

* Fri Dec 09 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-9
- Allow radicale_t to execute bin_t in SELinux policy RHBZ#1393569

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 01 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-7
- Additional systemd hardening

* Fri Jun 24 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-6
- Correctly label the files

* Wed Jun 22 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-5
- Add /var/run/radicale directory

* Tue Jun 21 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-4
- Update dependencies

* Tue Jun 21 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-3
- Create python2 subpackage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (#1296746)

* Fri Jan 01 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1-1
- Version 1.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-3
- Fix radicale-httpd for python3

* Thu Sep 24 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-2
- Unify spec for Fedora and epel7

* Tue Sep 22 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-1
- Version 1.0.1

* Tue Sep 15 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0-1
- Version 1.0
- Merge SELinux subpackage into the main package

* Mon Sep 07 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-7
- Drop old _selinux_policy_version hack
- Require radicale-selinux

* Fri Jul 24 2015 Tomas Radej <tradej@redhat.com> - 0.10-6
- Updated dep on policycoreutils-python-utils

* Wed Jun 17 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-5
- Switch to python3

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-4
- Use license macro

* Mon Apr 06 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-3
- Add patch1 to fix rhbz#1206813

* Tue Feb 24 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-2
- Add radicale_var_run_t to SELinux policy 1.0.3

* Tue Jan 13 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-1
- Version 0.10

* Mon Aug 18 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9-2
- Hide error when re-adding SELinux port label.

* Thu Aug 14 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9-1
- Version 0.9
- Automatically restart service if it dies.
- Update systemwide patch

* Mon Aug 04 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-11
- Handle PID file.

* Thu Jul 17 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-10
- Add network-online.target dependency. Bug #1119818

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-8
- Add PrivateDevices to unit file

* Wed Dec 25 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-7
- SELinux policy 1.0.2

* Fri Nov 29 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-6
- SELinux policy 1.0.1 fix bug #1035925

* Fri Nov 08 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-5
- Hardcode _selinux_policy_version in F20 because of #999584

* Thu Oct 03 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-4
- Update httpd config file and add SELinux policy. Bug #1014408

* Tue Aug 27 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-3
- Move .wsgi and .fcgi to main package

* Sun Jul 21 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-2
- BuildRequire python2-devel

* Thu Jul 18 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-1
- Update to version 0.8
- Merge Till Maas's spec file. Bug #922276

* Mon Jul 08 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.7.1-1
- Initial packaging
