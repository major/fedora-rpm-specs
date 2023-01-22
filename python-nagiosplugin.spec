%global srcname nagiosplugin

Name:           python-%{srcname}
Version:        1.3.3
Release:        2%{?dist}
License:        ZPLv2.1
Summary:        Library for writing Nagios (Icinga) plugins

URL:            https://nagiosplugin.readthedocs.io
Source:         %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

BuildArch:      noarch

%global _description %{expand:
nagiosplugin is a Python class library which helps writing Nagios (or Icinga)
compatible plugins easily in Python. It cares for much of the boilerplate
code and default logic commonly found in Nagios checks, including:

- Nagios 3 Plugin API compliant parameters and output formatting
- Full Nagios range syntax support
- Automatic threshold checking
- Multiple independend measures
- Custom status line to communicate the main point quickly
- Long output and performance data
- Timeout handling
- Persistent “cookies” to retain state information between check runs
- Resume log file processing at the point where the last run left}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.txt
%{python3_sitelib}/nagiosplugin-*.egg-info/
%{python3_sitelib}/nagiosplugin/

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 09 2022 Simone Caronni <negativo17@gmail.com> - 1.3.3-1
- Update to 1.3.3.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 18 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.3.2-1
- Initial package
