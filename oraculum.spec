Name:           oraculum
# Don't forget to also change oraculum/__init__.py
Version:        0.2.4
Release:        %autorelease
Summary:        Backend and API for Fedora QA Dashboard

License:        GPLv2+
URL:            https://pagure.io/fedora-qa/oraculum
Source0:        https://releases.pagure.org/fedora-qa/%{name}/%{name}-%{version}.tar.gz
# Backport of:
# Remove unnecessary mock dependency.
# https://pagure.io/fedora-qa/oraculum/c/03bf4dc6f3d77f8d240ffe2d6772885e642181ab?branch=master
Patch:          remove-python-mock.patch

BuildArch:      noarch


BuildRequires:  systemd-rpm-macros
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

Requires:       python3-gunicorn
Requires:       nginx
Requires:       redis

%description
Backend and API for Fedora QA Dashboard

%generate_buildrequires
%pyproject_buildrequires -r -t

%prep
%autosetup -p1

# https://bugzilla.redhat.com/show_bug.cgi?id=2019108
sed -i 's/python-igraph/igraph/g' requirements.txt
sed -i 's/python-igraph/igraph/g' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files oraculum

# Install example configuration to /etc, fix client_secrets.json location
install -d -m 755 %{buildroot}%{_sysconfdir}/oraculum
install -p -m 644 conf/settings.py.example %{buildroot}%{_sysconfdir}/oraculum/settings.py
install -p -m 644 conf/client_secrets.json.example %{buildroot}%{_sysconfdir}/oraculum/client_secrets.json
sed -i 's,./conf/client_secrets.json.example,%{_sysconfdir}/oraculum/client_secrets.json,' %{buildroot}%{_sysconfdir}/oraculum/settings.py

# Install nginx configuration to /etc
install -d -m 755 %{buildroot}%{_sysconfdir}/nginx/conf.d/
install -p -m 644 conf/oraculum.conf.nginx %{buildroot}%{_sysconfdir}/nginx/conf.d/oraculum.conf

%check
%tox

%post
%systemd_post oraculum.service
%systemd_post oraculum_worker.service
%systemd_post oraculum_beat.service

%preun
%systemd_preun oraculum.service
%systemd_preun oraculum_worker.service
%systemd_preun oraculum_beat.service

%postun
%systemd_postun_with_restart oraculum.service
%systemd_postun_with_restart oraculum_worker.service
%systemd_postun_with_restart oraculum_beat.service


%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%{_unitdir}/oraculum.service
%{_unitdir}/oraculum_worker.service
%{_unitdir}/oraculum_beat.service

%{_bindir}/oraculum
%dir %{_sysconfdir}/oraculum
%dir %{_datadir}/oraculum
%{_datadir}/oraculum/*

%doc %{_datadir}/docs/oraculum/

%config(noreplace) %{_sysconfdir}/oraculum/settings.py
%config(noreplace) %{_sysconfdir}/oraculum/client_secrets.json
%config(noreplace) %{_sysconfdir}/nginx/conf.d/oraculum.conf

%changelog
%autochangelog
