%global pypi_name DateTimeRange
%global module_name datetimerange

Name:           python-%{module_name}
Version:        1.2.0
Release:        9%{?dist}
Summary:        Python module DateTimeRange

License:        MIT
URL:            https://github.com/thombashi/DateTimeRange
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-typepy

#test requirements
BuildRequires:  python3-pytest
BuildRequires:  python3-pytz


%global _description %{expand:
DateTimeRange is a Python library to handle a time range. e.g. check whether
a time is within the time range, get the intersection of time ranges,
truncating a time range, iterate through a time range, and so forth.}

%description %_description

%package -n     python3-%{module_name}
Summary:        %{summary}
 
%description -n python3-%{module_name}
%_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module_name}

%check
%pytest -v

%files -n python3-%{module_name} -f %{pyproject_files} 
%license LICENSE
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.12

* Wed Feb 08 2023 Karolina Kula <kkula@redhat.com> - 1.2.0-1
- initial package build

