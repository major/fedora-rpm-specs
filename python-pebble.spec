%global modname pebble

Name:           python-%{modname}
Version:        4.5.3
Release:        8%{?dist}
Summary:        Threading and multiprocessing eye-candy for Python
License:        LGPLv3+
URL:            https://github.com/noxdafox/pebble
Source:         %{pypi_source Pebble}
BuildArch:      noarch

%global _description %{expand:
Pebble provides an API to manage threads and processes within an application.
It wraps Python’s standard library threading and multiprocessing objects.}

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname} %_description

%prep
%autosetup -n Pebble-%{version} -Sgit

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest

%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/pebble/
%{python3_sitelib}/Pebble-*.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.5.3-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.5.3-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Martin Liška <mliska@suse.cz> - 4.5.3-1
- Initial Fedora package
