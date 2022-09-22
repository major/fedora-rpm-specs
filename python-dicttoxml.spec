%global pypi_name dicttoxml

Name:           python-%{pypi_name}
Version:        1.7.4
Release:        9%{?dist}
Summary:        Converts a Python dictionary or other native data type into a valid XML string

License:        GPLv2
URL:            https://github.com/quandyfactory/dicttoxml
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Converts a Python dictionary or other native data type into a valid XML string.
Details Supports item (int, float, long, decimal.Decimal, bool, str, unicode,
datetime, none and other number-like objects) and collection (list, set, tuple
and dict, as well as iterable and dict-like objects) data types, with arbitrary
nesting for the collections.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Converts a Python dictionary or other native data type into a valid XML string.
Details Supports item (int, float, long, decimal.Decimal, bool, str, unicode,
datetime, none and other number-like objects) and collection (list, set, tuple
and dict, as well as iterable and dict-like objects) data types, with arbitrary
nesting for the collections.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.markdown
%license LICENCE.txt
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7.4-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.4-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.4-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 siddharthvipul1 <siddharthvipul1@gmail.com> - 1.7.4-1
- Initial package.
