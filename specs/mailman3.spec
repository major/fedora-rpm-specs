%global pypi_name mailman

%global baseversion 3.3.9
#global prerelease rc2

Name:           mailman3
Version:        %{baseversion}%{?prerelease:~%{prerelease}}
Release:        2%{?dist}
Summary:        The GNU mailing list manager

License:        GPL-3.0-or-later
URL:            http://www.list.org
Source0:        https://pypi.python.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{baseversion}%{?prerelease}.tar.gz
Source1:        mailman3.cfg
Source2:        mailman3-tmpfiles.conf
Source3:        mailman3.service
Source4:        mailman3.logrotate
Source5:        mailman3-digests.service
Source6:        mailman3-digests.timer
Source7:        mailman3-sysusers.conf

BuildArch:      noarch

# Ensure that tests will work...
BuildRequires:  glibc-langpack-en

BuildRequires:  python3-devel >= 3.5
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros

# SELinux https://fedoraproject.org/wiki/SELinux/IndependentPolicy#Creating_the_Spec_File
Provides:  %{name}-selinux == %{version}-%{release}
%global selinux_variants mls targeted
Requires: selinux-policy %{?_selinux_policy_version: >= %{_selinux_policy_version}}
BuildRequires: git-core
BuildRequires: pkgconfig(systemd)
BuildRequires: selinux-policy
BuildRequires: selinux-policy-devel
Requires(post): selinux-policy-base %{?_selinux_policy_version: >= %{_selinux_policy_version}}
Requires(post): libselinux-utils
Requires(post): policycoreutils
Requires(post): policycoreutils-python-utils
# SELinux https://fedoraproject.org/wiki/SELinux_Policy_Modules_Packaging_Draft
BuildRequires:  checkpolicy, selinux-policy-devel
BuildRequires:  hardlink

# Scriptlets
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%{?sysusers_requires_compat}


%description
This is GNU Mailman, a mailing list management system distributed under the
terms of the GNU General Public License (GPL) version 3 or later.  The name of
this software is spelled 'Mailman' with a leading capital 'M' but with a lower
case second `m'.  Any other spelling is incorrect.


%prep
%autosetup -p1 -n %{pypi_name}-%{baseversion}%{?prerelease}

# Downgrade a few dependencies to satisfiable compatible versions
sed -e "s/flufl.i18n>=3.2/flufl.i18n>=2.0/" \
    -i setup.py

# SELinux
mkdir SELinux
echo '%{_localstatedir}/lib/%{name}/data(/.*)? gen_context(system_u:object_r:etc_mail_t,s0)' \
    > SELinux/%{name}.fc
# remember to bump the following version if the policy is updated
cat > SELinux/%{name}.te << EOF
policy_module(%{name}, 1.4)
EOF


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel

cd SELinux
for selinuxvariant in %{selinux_variants}; do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv %{name}.pp %{name}.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -


%install
%pyproject_install
%pyproject_save_files %{pypi_name}

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
echo "%{_bindir}/%{name}" >> %{pyproject_files}
echo "%%dir %{_libexecdir}/%{name}" >> %{pyproject_files}
echo "%{_libexecdir}/%{name}/mailman" >> %{pyproject_files}
echo "%{_libexecdir}/%{name}/master" >> %{pyproject_files}
echo "%{_libexecdir}/%{name}/runner" >> %{pyproject_files}

# service files
install -D -m 0640 %{SOURCE1} %{buildroot}%{_sysconfdir}/mailman.cfg
install -D -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -m 0644 %{SOURCE7} %{buildroot}%{_sysusersdir}/%{name}.conf
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
%python3 -m venv --system-site-packages --without-pip --clear venv
# Tests fail with nspawn mock due to lack of access to /dev/stdout
# TODO: Figure out a fix for this
venv/bin/python -m nose2 -v || :


%pre
# User & Group
%sysusers_create_compat %{SOURCE7}

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


%files -f %{pyproject_files}
%doc README.rst
%license COPYING
%{_unitdir}/*.service
%{_unitdir}/*.timer
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Michel Lind <salimma@fedoraproject.org>
- Update to version 3.3.9; Fixes: RHBZ#2245287

* Wed Aug 28 2024 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.3.8-9
- Use git-core instead of git
- Check if _selinux_policy_version is set

* Mon Jul 29 2024 Michel Lind <salimma@fedoraproject.org> - 3.3.8-8
- Fix FTBFS due to deprecated `python setup.py develop` not being able to find flufl.lock v8
- Fixes: rhbz#2300935

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Python Maint <python-maint@redhat.com> - 3.3.8-6
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 29 2023 Michel Lind <salimma@fedoraproject.org> - 3.3.8-3
- Restore the required versions of flufl.bounce and flufl.lock
- Use SPDX license identifier; fix license to GPL-3.0-or-later

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 13 2023 Neal Gompa <ngompa@fedoraproject.org> - 3.3.8-1
- Update to 3.3.8

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
