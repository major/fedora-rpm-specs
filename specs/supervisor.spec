Name:		supervisor
Version:	4.3.0
Release:	%autorelease
Summary:	A system for allowing the control of process state on UNIX

License:	BSD-3-Clause AND MIT
URL:		http://supervisord.org
Source0:	https://github.com/Supervisor/supervisor/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}d.service
Source2:	%{name}d.conf
Source3:	%{name}.logrotate
Source4:	%{name}.tmpfiles

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	systemd-units
BuildRequires:	python3-pkg-resources
Requires:	python3-pkg-resources

%description
The supervisor is a client/server system that allows its users to control a
number of processes on UNIX-like operating systems.

%prep
%autosetup
%py3_shebang_fix supervisor/scripts
sed -i -e 's|#!<<PYTHON>>|#!%{_bindir}/python3|g' supervisor/tests/fixtures/spew.py supervisor/tests/fixtures/unkillable_spew.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

mkdir -p %{buildroot}/%{_sysconfdir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}d.d
mkdir -p %{buildroot}/%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}/%{_rundir}/%{name}
chmod 755 %{buildroot}/%{_localstatedir}/log/%{name}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}d.service
install -p -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}d.conf
install -p -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%check	
%pytest -v

%post
%systemd_post %{name}d.service

%preun
%systemd_preun %{name}d.service

%postun
%systemd_postun_with_restart %{name}d.service

%files -n supervisor -f %{pyproject_files}
%doc CHANGES.rst README.rst
%license COPYRIGHT.txt LICENSES.txt
%dir %{_localstatedir}/log/%{name}
%{_unitdir}/%{name}d.service
%{_bindir}/%{name}*
%{_bindir}/echo_supervisord_conf
%{_bindir}/pidproxy
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}d.conf
%dir %{_sysconfdir}/%{name}d.d
%dir %{_rundir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%changelog
%autochangelog
