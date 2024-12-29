Name:       barman
Version:    3.12.1
Release:    1%{?dist}
Summary:    Backup and Recovery Manager for PostgreSQL
License:    GPL-3.0-only
URL:        http://www.pgbarman.org/
BuildArch:  noarch

Source0:    https://files.pythonhosted.org/packages/source/b/%{name}/%{name}-%{version}.tar.gz
Source1:    %{name}.cron
Source2:    %{name}.logrotate

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# https://docs.fedoraproject.org/en-US/packaging-guidelines/CronFiles/#_cron_job_files_packaging:
Requires:       cronie
Requires:       logrotate
Requires(pre):  shadow-utils
Requires:       rsync >= 3.0.4
Requires:       %{py3_dist argcomplete}
Requires:       %{py3_dist barman}

%description
Barman (Backup and Recovery Manager) is an open-source administration tool for
disaster recovery of PostgreSQL servers written in Python.

It allows your organization to perform remote backups of multiple servers in
business critical environments to reduce risk and help DBAs during the recovery
phase.

%package cli
Summary:    Client Utilities for Barman
Requires:   %{py3_dist barman}

%description cli
Client utilities for the integration of Barman in PostgreSQL clusters.

%package -n python3-barman
Summary:    Shared libraries for Barman
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-barman
Python libraries used by Barman.

%prep
%autosetup

# Change shebang in all relevant executable files in this directory and all subdirectories
find -type f -executable -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

mkdir -p %{buildroot}%{_sysconfdir}/%{name}/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/

install -p -m 644 docs/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -p -m 644 docs/%{name}.d/* %{buildroot}%{_sysconfdir}/%{name}/conf.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -p -m 644 scripts/%{name}.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}

sed -i 's|/etc/%{name}.d|/etc/%{name}/conf.d|g' %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

%files
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.5*
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(700,%{name},%{name}) %dir %{_sharedstatedir}/%{name}
%attr(755,%{name},%{name}) %dir %{_localstatedir}/log/%{name}

%files cli
%{_bindir}/%{name}-cloud-backup
%{_bindir}/%{name}-cloud-backup-delete
%{_bindir}/%{name}-cloud-backup-keep
%{_bindir}/%{name}-cloud-backup-list
%{_bindir}/%{name}-cloud-backup-show
%{_bindir}/%{name}-cloud-check-wal-archive
%{_bindir}/%{name}-cloud-restore
%{_bindir}/%{name}-cloud-wal-archive
%{_bindir}/%{name}-cloud-wal-restore
%{_bindir}/%{name}-wal-archive
%{_bindir}/%{name}-wal-restore
%{_mandir}/man1/%{name}-archive-wal.1*
%{_mandir}/man1/%{name}-backup.1*
%{_mandir}/man1/%{name}-check.1*
%{_mandir}/man1/%{name}-check-backup.1*
%{_mandir}/man1/%{name}-cloud-backup.1*
%{_mandir}/man1/%{name}-cloud-backup-delete.1*
%{_mandir}/man1/%{name}-cloud-backup-keep.1*
%{_mandir}/man1/%{name}-cloud-backup-list.1*
%{_mandir}/man1/%{name}-cloud-backup-show.1*
%{_mandir}/man1/%{name}-cloud-check-wal-archive.1*
%{_mandir}/man1/%{name}-cloud-restore.1*
%{_mandir}/man1/%{name}-cloud-wal-archive.1*
%{_mandir}/man1/%{name}-cloud-wal-restore.1*
%{_mandir}/man1/%{name}-config-switch.1*
%{_mandir}/man1/%{name}-config-update.1*
%{_mandir}/man1/%{name}-cron.1*
%{_mandir}/man1/%{name}-delete.1*
%{_mandir}/man1/%{name}-diagnose.1*
%{_mandir}/man1/%{name}-generate-manifest.1*
%{_mandir}/man1/%{name}-get-wal.1*
%{_mandir}/man1/%{name}-keep.1*
%{_mandir}/man1/%{name}-list_backups.1*
%{_mandir}/man1/%{name}-list-files.1*
%{_mandir}/man1/%{name}-list-servers.1*
%{_mandir}/man1/%{name}-lock-directory-cleanup.1*
%{_mandir}/man1/%{name}-put-wal.1*
%{_mandir}/man1/%{name}-rebuild-xlogdb.1*
%{_mandir}/man1/%{name}-receive-wal.1*
%{_mandir}/man1/%{name}-replication-status.1*
%{_mandir}/man1/%{name}-restore.1*
%{_mandir}/man1/%{name}-show-backup.1*
%{_mandir}/man1/%{name}-show-servers.1*
%{_mandir}/man1/%{name}-status.1*
%{_mandir}/man1/%{name}-switch-wal.1*
%{_mandir}/man1/%{name}-switch-xlog.1*
%{_mandir}/man1/%{name}-sync-backup.1*
%{_mandir}/man1/%{name}-sync-info.1*
%{_mandir}/man1/%{name}-sync-wals.1*
%{_mandir}/man1/%{name}-verify.1*
%{_mandir}/man1/%{name}-verify-backup.1*
%{_mandir}/man1/%{name}-wal-archive.1*
%{_mandir}/man1/%{name}-wal-restore.1*

%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS README.rst RELNOTES.md

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_sharedstatedir}/%{name} -s /bin/bash \
    -c "Backup and Recovery Manager for PostgreSQL" %{name}
exit 0

%changelog
* Fri Dec 27 2024 Simone Caronni <negativo17@gmail.com> - 3.12.1-1
- Update to 3.12.1.
- Switch to Python packaging guidelines.
- Trim changelog.

* Sun Aug 25 2024 Simone Caronni <negativo17@gmail.com> - 3.11.1-1
- Update to 3.11.1.

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.10.1-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Simone Caronni <negativo17@gmail.com> - 3.10.1-1
- Update to 3.10.1.

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.10.0-2
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Simone Caronni <negativo17@gmail.com> - 3.10.0-1
- Update to 3.10.0.

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Simone Caronni <negativo17@gmail.com> - 3.9.0-1
- Update to 3.9.0.

* Mon Sep 04 2023 Simone Caronni <negativo17@gmail.com> - 3.8.0-1
- Update to 3.8.0.

* Mon Aug 07 2023 Simone Caronni <negativo17@gmail.com> - 3.7.0-1
- Update to 3.7.0.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Python Maint <python-maint@redhat.com> - 3.6.0-2
- Rebuilt for Python 3.12

* Thu Jun 22 2023 Simone Caronni <negativo17@gmail.com> - 3.6.0-1
- Update to 3.6.0.

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.5.0-4
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Simone Caronni <negativo17@gmail.com> - 3.5.0-3
- Remove Python dependencies version, pep-0440 is enforced when building
  packages.

* Mon May 15 2023 Simone Caronni <negativo17@gmail.com> - 3.5.0-2
- Adjust Python dependencies.

* Mon May 08 2023 Simone Caronni <negativo17@gmail.com> - 3.5.0-1
- Update to 3.5.0.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild
