%global nagiospluginsdir %{_libdir}/nagios/plugins
Name:           nagios-plugins-systemd
Version:        4.1.1
Release:        %autorelease
Summary:        Nagios Plugin - check_systemd

License:        LGPL-2.1-only
URL:            https://exchange.icinga.com/joseffriedrich/check_systemd
Source:         https://github.com/Josef-Friedrich/check_systemd/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel

# Require the package that owns the plugins dir, as we install the plugin there.
Requires: nagios-common

# The package does not contain any architecture-dependent things, but installs
# into an arch-dependend directory. Thus, it cannot be noarch, but it does not
# provide any debuginfo.
%global debug_package %{nil}

%description
This systemd check for nagios compatible monitoring systems will report a
degraded systemd to your monitoring solution. It can also be used to monitor
individual systemd services and timers units.

%prep
%autosetup -p1 -n check_systemd-%{version}
# Do not pin test dependencies to exact versions; we cannot respect these!
sed -r -i 's/==/>=/' tox.ini


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files check_systemd

# The nagios plugin binaries must be in the nagiospluginsdir.
mkdir -p %{buildroot}/%{nagiospluginsdir}
mv %{buildroot}/%{_bindir}/check_systemd %{buildroot}/%{nagiospluginsdir}


%check
PYTHONPATH=%{buildroot}/%{nagiospluginsdir}:${PYTHONPATH} PATH=%{buildroot}/%{nagiospluginsdir}:${PATH} %tox


%files -f %{pyproject_files}
%doc README.*
%license LICENSE
%{nagiospluginsdir}/check_systemd


%changelog
%autochangelog
