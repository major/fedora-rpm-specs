# Created by pyp2rpm-3.3.0
%global pypi_name collectd_systemd
%global forgeurl https://github.com/cernops/collectd-systemd

Name:           python-%{pypi_name}
Version:        2.1.0
%forgemeta
Release:        %autorelease
Summary:        Collectd plugin to monitor systemd services


License:        MIT
URL:            %forgeurl
Source0:        %forgesource
Source1:        collectd_systemd.te
BuildArch:      noarch
 
BuildRequires:  make
BuildRequires:  python3-devel

BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros

%description
collectd-systemd A collectd plugin which checks if given systemd services
are in "running" state and sends metrics with 1.0 or 0.0.
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       collectd-python
Requires:       %{name}-selinux = %{version}-%{release}

%description -n python3-%{pypi_name}
collectd-systemd A collectd plugin which checks if given systemd services
are in "running" state and sends metrics with 1.0 or 0.0.

%package selinux
Summary:        selinux policy for collectd systemd plugin
Requires:       selinux-policy
Requires:       policycoreutils

%description selinux
This package contains selinux rules to allow the collectd
systemd plugin to access service status via dbus.

%prep
%forgesetup 
cp -p %{SOURCE1} .


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel
make -f /usr/share/selinux/devel/Makefile collectd_systemd.pp


%install
%pyproject_install

%pyproject_save_files -l collectd_systemd

mkdir -p %{buildroot}%{_datadir}/selinux/packages/%{name}
install -m 644 -p collectd_systemd.pp \
    %{buildroot}%{_datadir}/selinux/packages/%{name}/collectd_systemd.pp

%post selinux
/usr/sbin/semodule -i %{_datadir}/selinux/packages/%{name}/collectd_systemd.pp >/dev/null 2>&1 || :

%postun selinux
if [ $1 -eq 0 ] ; then
    /usr/sbin/semodule -r collectd_systemd >/dev/null 2>&1 || :
fi
%systemd_postun_with_restart collectd.service


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE


%files selinux
%{_datadir}/selinux/packages/%{name}/collectd_systemd.pp

%check
%tox

%changelog
%autochangelog
