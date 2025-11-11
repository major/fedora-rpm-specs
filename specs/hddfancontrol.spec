%global pypi_name hddfancontrol

Name:           %{pypi_name}
Version:        1.6.2
Release:        %autorelease
Summary:        Control system fan speed by monitoring hard drive temperature

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/desbma/hddfancontrol

# The PyPI archives don't have unit tests in them anymore.
Source0:        https://github.com/desbma/hddfancontrol/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  hdparm
BuildRequires:  hddtemp
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-pypandoc
BuildRequires:  python3-pytest
BuildRequires:  systemd
Requires:       hdparm
Requires:       hddtemp
Requires:       python3-docutils

%py_provides    python3-%{pypi_name}

%description
HDD Fan control is a command line tool to dynamically control fan speed
according to hard drive temperature on Linux.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l hddfancontrol
cp %{buildroot}/%{_bindir}/hddfancontrol %{buildroot}/%{_bindir}/hddfancontrol-3
ln -sf %{_bindir}/hddfancontrol-3 %{buildroot}/%{_bindir}/hddfancontrol-%{python3_version}

# Remove the "tests" directory that gets installed systemwide.
rm -rf %{buildroot}%{python3_sitelib}/tests

# Install the systemd script and config file.
mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/
sed 's,conf.d/hddfancontrol,hddfancontrol.conf,' -i systemd/hddfancontrol.service
cp -a systemd/hddfancontrol.service %{buildroot}%{_unitdir}/
cp -a systemd/hddfancontrol.conf %{buildroot}%{_sysconfdir}/

%check
%pyproject_check_import
%py3_test_envvars %{python3} -m unittest -v

%files -n hddfancontrol -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/hddfancontrol
%{_bindir}/hddfancontrol-3
%{_bindir}/hddfancontrol-%{python3_version}
%{_unitdir}/hddfancontrol.service
%config(noreplace) %{_sysconfdir}/hddfancontrol.conf

%changelog
%autochangelog
