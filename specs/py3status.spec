%bcond_without test

Name:           py3status
Version:        3.62
Release:        %autorelease
Summary:        An extensible i3status wrapper written in python

License:        BSD-3-Clause
URL:            https://github.com/ultrabug/py3status
Source0:        https://github.com/ultrabug/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with test}
BuildRequires:  python3-pytest
%endif
Requires:       i3status
Obsoletes:      %{name}-doc < 3.44-1

%description
Using py3status, you can take control of your i3bar easily by:
- writing your own modules and have their output displayed on your bar
- handling click events on your i3bar and play with them in no time
- seeing your clock tick every second whatever your i3status interval
No extra configuration file needed, just install & enjoy !

%pyproject_extras_subpkg -n %{name} dbus
%pyproject_extras_subpkg -n %{name} udev

%prep
%setup -q -n %{name}-%{version}
# allow upwards dependency matches
sed -i -e 's/dbus-python\s*==\s*/dbus-python >= /' pyproject.toml
sed -i -e 's/PyGObject\s*==\s*/PyGObject >= /' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{name}

%if %{with test}
%check
%pytest
%endif

%files -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG
%{_bindir}/py3-cmd
%{_bindir}/py3status

%changelog
%autochangelog
