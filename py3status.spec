%bcond_without test

Name:           py3status
Version:        3.47
Release:        %autorelease
Summary:        An extensible i3status wrapper written in python

License:        BSD
URL:            https://github.com/ultrabug/py3status
Source0:        https://github.com/ultrabug/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with test}
BuildRequires:  python3-tox python3-tox-current-env python3-pytest
%endif
Requires:       i3status
Obsoletes:      %{name}-doc < 3.44-1

%description
Using py3status, you can take control of your i3bar easily by:
- writing your own modules and have their output displayed on your bar
- handling click events on your i3bar and play with them in no time
- seeing your clock tick every second whatever your i3status interval
No extra configuration file needed, just install & enjoy !


%prep
%setup -q -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with test}
%check
# disable linters
sed -i -e '/{envbindir}\/black/d' -e 's/pytest --flake8/pytest/' tox.ini
# test in install environment
sed -i -e 's#{envbindir}/##' tox.ini
%tox
%endif

%files
%license LICENSE
%doc README.md CHANGELOG
%{_bindir}/py3-cmd
%{_bindir}/py3status
%dir %{python3_sitelib}/py3status
%{python3_sitelib}/py3status/*
%{python3_sitelib}/*.egg-info


%changelog
%autochangelog
