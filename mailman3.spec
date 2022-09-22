%global pypi_name mailman

%global baseversion 3.3.4
#global prerelease rc2

# The user and group Mailman will run as, same values as in the mailman 2 RPM
%global mmuser       mailman
%global mmuserid     41
%global mmgroup      mailman
%global mmgroupid    41

%{?python_enable_dependency_generator}


Name:           mailman3
Version:        %{baseversion}%{?prerelease:~%{prerelease}}
Release:        7%{?dist}
Summary:        The GNU mailing list manager

License:        GPLv3
URL:            http://www.list.org
Source0:        https://pypi.python.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{baseversion}%{?prerelease}.tar.gz
Source1:        mailman3.cfg
Source2:        mailman3-tmpfiles.conf
Source3:        mailman3.service
Source4:        mailman3.logrotate
Source5:        mailman3-digests.service
Source6:        mailman3-digests.timer

# <https://gitlab.com/mailman/mailman/-/merge_requests/860>
Patch01:        %{name}-click8.patch
# <https://gitlab.com/mailman/mailman/merge_requests/721>
Patch11:        %{name}-subject-prefix.patch
# <https://gitlab.com/mailman/mailman/merge_requests/722>
Patch14:        %{name}-use-either-importlib_resources-or-directly-importlib.patch

# Fix a test failure that only fails becasue of an extra/missing space
# No idea how severe this is, but it does not appear to be
# See https://bugzilla.redhat.com/show_bug.cgi?id=1900668#c9
Patch15:        %{name}-do-not-assume-sapce-in-banner.patch

BuildArch:      noarch

%if 0%{?fedora} || 0%{?rhel} >= 8
# Ensure that tests will work...
BuildRequires:  glibc-langpack-en
%endif

BuildRequires:  python%{python3_pkgversion}-devel >= 3.5
BuildRequires:  python%{python3_pkgversion}-setuptools

%if %{undefined python_enable_dependency_generator}
Requires:       python%{python3_pkgversion} >= 3.5
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-aiosmtpd >= 1.4.1
Requires:       python%{python3_pkgversion}-alembic
Requires:       python%{python3_pkgversion}-atpublic
Requires:       python%{python3_pkgversion}-authheaders >= 0.9.2
Requires:       python%{python3_pkgversion}-authres >= 1.0.1
Requires:       python%{python3_pkgversion}-click >= 8.0
Requires:       python%{python3_pkgversion}-dateutil >= 2.0
Requires:       python%{python3_pkgversion}-dns >= 1.14.0
Requires:       python%{python3_pkgversion}-falcon > 1.0.0
Requires:       python%{python3_pkgversion}-flufl-bounce
Requires:       python%{python3_pkgversion}-flufl-i18n >= 2.0.1
Requires:       python%{python3_pkgversion}-flufl-lock >= 3.1
Requires:       python%{python3_pkgversion}-gunicorn
Requires:       python%{python3_pkgversion}-lazr-config
# Versionned dep on python-passlib, or else it fails with AttributeError in
# mailman/utilities/passwords.py", line 43: 'CryptContext' has no attribute 'from_string'
Requires:       python%{python3_pkgversion}-passlib >= 1.6.0
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-sqlalchemy1.3 >= 1.2.3
Requires:       python%{python3_pkgversion}-zope-component
Requires:       python%{python3_pkgversion}-zope-configuration
Requires:       python%{python3_pkgversion}-zope-event
Requires:       python%{python3_pkgversion}-zope-interface >= 5.0
%if (%{defined fedora} && 0%{?fedora} < 29) || (%{defined rhel} && 0%{?rhel} < 9)
Requires:       python%{python3_pkgversion}-importlib-resources
%endif
%endif

# To run the test suite:
BuildRequires:  python%{python3_pkgversion}-aiosmtpd >= 1.4.1
BuildRequires:  python%{python3_pkgversion}-alembic
BuildRequires:  python%{python3_pkgversion}-atpublic
BuildRequires:  python%{python3_pkgversion}-authheaders >= 0.9.2
BuildRequires:  python%{python3_pkgversion}-authres >= 1.0.1
BuildRequires:  python%{python3_pkgversion}-click >= 8.0
BuildRequires:  python%{python3_pkgversion}-dateutil >= 2.0
BuildRequires:  python%{python3_pkgversion}-dns >= 1.14.0
BuildRequires:  python%{python3_pkgversion}-falcon > 1.0.0
BuildRequires:  python%{python3_pkgversion}-flufl-bounce
BuildRequires:  python%{python3_pkgversion}-flufl-i18n >= 2.0.1
BuildRequires:  python%{python3_pkgversion}-flufl-lock >= 3.1
BuildRequires:  python%{python3_pkgversion}-flufl-testing
BuildRequires:  python%{python3_pkgversion}-gunicorn
BuildRequires:  python%{python3_pkgversion}-lazr-config
BuildRequires:  python%{python3_pkgversion}-lazr-smtptest
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-nose2
BuildRequires:  python%{python3_pkgversion}-passlib >= 1.6.0
BuildRequires:  python%{python3_pkgversion}-psycopg2
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-sqlalchemy1.3 >= 1.2.3
BuildRequires:  python%{python3_pkgversion}-zope-component
BuildRequires:  python%{python3_pkgversion}-zope-configuration
BuildRequires:  python%{python3_pkgversion}-zope-event
BuildRequires:  python%{python3_pkgversion}-zope-interface >= 5.0
%if (%{defined fedora} && 0%{?fedora} < 29) || (%{defined rhel} && 0%{?rhel} < 9)
BuildRequires:  python%{python3_pkgversion}-importlib-resources
%endif

# SELinux https://fedoraproject.org/wiki/SELinux/IndependentPolicy#Creating_the_Spec_File
Provides:  %{name}-selinux == %{version}-%{release}
%global selinux_variants mls targeted
Requires: selinux-policy >= %{_selinux_policy_version}
BuildRequires: git
BuildRequires: pkgconfig(systemd)
BuildRequires: selinux-policy
BuildRequires: selinux-policy-devel
Requires(post): selinux-policy-base >= %{_selinux_policy_version}
Requires(post): libselinux-utils
Requires(post): policycoreutils
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires(post): policycoreutils-python-utils
%else
Requires(post): policycoreutils-python
%endif
# SELinux https://fedoraproject.org/wiki/SELinux_Policy_Modules_Packaging_Draft
BuildRequires:  checkpolicy, selinux-policy-devel
BuildRequires:  hardlink

# Scriptlets
%{?systemd_requires}
BuildRequires:    systemd
Requires(pre):    shadow-utils


%description
This is GNU Mailman, a mailing list management system distributed under the
terms of the GNU General Public License (GPL) version 3 or later.  The name of
this software is spelled 'Mailman' with a leading capital 'M' but with a lower
case second `m'.  Any other spelling is incorrect.


%prep
%autosetup -p1 -n %{pypi_name}-%{baseversion}%{?prerelease}

# SELinux
mkdir SELinux
echo '%{_localstatedir}/lib/%{name}/data(/.*)? gen_context(system_u:object_r:etc_mail_t,s0)' \
    > SELinux/%{name}.fc
# remember to bump the following version if the policy is updated
cat > SELinux/%{name}.te << EOF
policy_module(%{name}, 1.4)
EOF


%build
%py3_build

cd SELinux
for selinuxvariant in %{selinux_variants}; do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv %{name}.pp %{name}.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -


%install
%py3_install

# move scripts away from _bindir to avoid conflicts and create a wrapper script
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libexecdir}/%{name}/
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
if [ "\$(whoami)" != "mailman" ]; then
    echo "This command must be run under the mailman user."
    exit 1
fi
%{_libexecdir}/%{name}/mailman \$@
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

# service files
install -D -m 0640 %{SOURCE1} %{buildroot}%{_sysconfdir}/mailman.cfg
install -D -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
sed -e 's,@LOGDIR@,%{_localstatedir}/log/%{name},g;s,@BINDIR@,%{_bindir},g' \
    %{SOURCE4} > %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
# periodic task
install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}-digests.service
install -D -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}-digests.timer

mkdir -p %{buildroot}%{_localstatedir}/{lib,spool,log}/%{name}
mkdir -p %{buildroot}/run/%{name} %{buildroot}/run/lock/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d
# Mailman will auto-create the following dir, but not with the correct group
# owner (MTAs such as Postfix must read and write to it). Set it here in RPM's
# file listing.
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/data

# SELinux
for selinuxvariant in %{selinux_variants}; do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 SELinux/%{name}.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{name}.pp
done
hardlink -cv %{buildroot}%{_datadir}/selinux


%check
# tests need a proper locale
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
# Mailman3 can only be tested when its installed (it starts runners and won't
# find the buildroot), so we use a venv
%{__python3} -m venv --system-site-packages --without-pip --clear venv
venv/bin/python setup.py develop
venv/bin/python -m nose2 -v


%pre
# User & Group
getent group %{mmgroup} >/dev/null || \
    groupadd -g %{mmgroupid} %{mmgroup} >/dev/null
getent passwd %{mmuser} >/dev/null || \
    useradd -r -u %{mmuserid} -g %{mmgroupid} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin \
        -c "Mailman, the mailing-list manager" %{mmuser} >/dev/null
# SELinux
for selinuxvariant in %{selinux_variants}; do
    %selinux_relabel_pre -s ${selinuxvariant}
done

%post
# Service
%systemd_post %{name}.service %{name}-digests.timer
# SELinux
for selinuxvariant in %{selinux_variants}; do
    %selinux_modules_install -s ${selinuxvariant} %{_datadir}/selinux/${selinuxvariant}/%{name}.pp || :
done

%preun
# Service
%systemd_preun %{name}.service %{name}-digests.timer

%postun
# Service
%systemd_postun_with_restart %{name}.service %{name}-digests.timer
# SELinux
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}; do
    %selinux_modules_uninstall -s ${selinuxvariant} %{_datadir}/selinux/${selinuxvariant}/%{name}.pp || :
  done
fi

%posttrans
# SELinux
for selinuxvariant in %{selinux_variants}; do
    %selinux_relabel_post -s ${selinuxvariant}
done


%files
%doc README.rst
%license COPYING
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py%{python3_version}.egg-info
%{_unitdir}/*.service
%{_unitdir}/*.timer
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%config(noreplace) %attr(640,mailman,mailman) %{_sysconfdir}/mailman.cfg
%dir %{_sysconfdir}/%{name}.d
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(755,mailman,mailman) %{_localstatedir}/lib/%{name}
%dir %attr(2775,mailman,mail)   %{_localstatedir}/lib/%{name}/data
%dir %attr(755,mailman,mailman) %{_localstatedir}/spool/%{name}
%dir %attr(755,mailman,mailman) %{_localstatedir}/log/%{name}
%dir %attr(755,mailman,mailman) /run/%{name}
%dir %attr(755,mailman,mailman) /run/lock/%{name}
# SELinux
%doc SELinux/*
%{_datadir}/selinux/*/%{name}.pp


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 Neal Gompa <ngompa@fedoraproject.org> - 3.3.4-5
- Backport fix for click >= 8.0

* Fri Sep 17 2021 Neal Gompa <ngompa@fedoraproject.org> - 3.3.4-4
- Fix sqlalchemy dependency to < 1.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.4-2
- Rebuilt for Python 3.10

* Tue Mar 30 2021 Neal Gompa <ngompa13@gmail.com> - 3.3.4-1
- Update to 3.3.4 to fix build
- Refresh patch set

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.2~rc2-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Neal Gompa <ngompa13@gmail.com> - 3.3.2~rc2-1
- Update to 3.3.2rc2 to fix build
- Refresh and clean up patch set

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Marc Dequènes (Duck) <duck@redhat.com> - 3.2.2-3
- backport patch to use new Python 3.9 files API, fixes tests hang,
  adapted for older importlib_resources library
- backport patch to fix tests failing due to quote comparison
- remove obsolete tweaking of Python macros

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.2-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Marc Dequènes (Duck) <duck@redhat.com> - 3.2.2-1
- NUR
- remove Python 3.7 support patch, applied upstream
- refreshed/adapted patches
- don't hardcode the path to `hardlink`
- update and tighten dependencies
- adapt tests after changes in mailman3-subject-prefix.patch
- backport content-type fix for tests
- use importlib.resources instead of importlib_resources is available
- fix stale lock preventing mailman3.service from starting
  (see Debian#919160)
- add upstream patch to fix compatibility with Python 3.7.4 and
  Python 3.8b4
- ported upstream patch to fix compatibility with Python 3.8
- upstream patch to fix model deletion and template init

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Aurelien Bompard <abompard@fedoraproject.org> - 3.2.0-5
- Fix hardlink

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Aurelien Bompard <abompard@fedoraproject.org> - 3.2.0-1
- Version 3.2.0
- Update dependencies
- Merge the -selinux subpackage
- Use the SELinux macros

* Tue Mar 06 2018 Aurelien Bompard <abompard@fedoraproject.org> - 3.1.1-0.7
- Rebuild

* Tue Feb 13 2018 Aurelien Bompard <abompard@fedoraproject.org> - 3.1.1-0.6
- git update to 8207caa09

* Mon May 29 2017 Aurelien Bompard <abompard@fedoraproject.org> - 3.1.1-0.1
- version 3.1.0 final

* Thu Feb 09 2017 Aurelien Bompard <abompard@fedoraproject.org> - 3.1.0-0.30
- add a cron job to send digests daily

* Wed Apr 29 2015 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.0-1
- version 3.0.0 final

* Fri Jul 18 2014 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.0-0.18.bzr7251
- add Patch11 (missing PostgreSQL upgrade file)

* Mon Nov 25 2013 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.0-0.11.bzr7226
- add SELinux policy module, according to:
  http://fedoraproject.org/wiki/SELinux_Policy_Modules_Packaging_Draft

* Sun Oct 27 2013 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.0-0.10.bzr7226
- update to BZR snapshot (rev7226)

* Thu Aug 29 2013 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.0-0.6.bzr7218
- update to BZR snapshot (rev7218)

* Wed Aug 28 2013 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.0-0.6.bzr7217
- update to BZR snapshot (rev7217)
- drop patch 0
- rename to mailman3 and make it parallel-installable with Mailman 2

* Wed Jul 24 2013 Aurelien Bompard <abompard@fedoraproject.org> - 3:3.0.0-0.6
- update to BZR snapshot (rev7215)
- drop patch 1

* Thu Mar 07 2013 Aurelien Bompard <abompard@fedoraproject.org> - 3:3.0.0-0.2.b3
- update to beta3
- add a systemd service and a default config file

* Wed Nov 28 2012 Aurelien Bompard <abompard@fedoraproject.org> - 3.0.0b2-1
- Initial package.
