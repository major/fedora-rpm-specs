%global pypi_name strict-rfc3339
%global _description \
Goals: \
- Convert UNIX timestamps to and from RFC3339. \
- Either produce RFC3339 strings with a UTC offset (Z) or with the offset that \
  the C time module reports is the local timezone offset. \
- Simple with minimal dependencies/libraries. \
- Avoid timezones as much as possible. \
- Be very strict and follow RFC3339.

Name:           python-%{pypi_name}
Version:        0.7
Release:        7%{?dist}
Summary:        Strict, simple, lightweight RFC3339 functions

License:        GPLv3
URL:            https://github.com/danielrichman/strict-rfc3339
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?py_provides:%py_provides python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md README.txt
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/strict_rfc3339.py
%{python3_sitelib}/strict_rfc3339-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Aurelien Bompard <abompard@fedoraproject.org> - 0.7-1
- Initial package.
