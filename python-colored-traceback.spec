Name:           python-colored-traceback
Version:        0.3.0
Release:        4%{?dist}
Summary:        A library to color exception traces

License:        ISC
URL:            https://github.com/staticshock/colored-traceback.py
Source0:        %{pypi_source colored-traceback}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Colored-traceback is a python library to color exception traces.

%package -n python3-colored-traceback
Summary:        %{summary}

%description -n python3-colored-traceback
Colored-traceback is a python library to color exception traces.

%prep
%autosetup -n colored-traceback-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
%py3_check_import colored_traceback

%files -n python3-colored-traceback
%doc README.rst
%{python3_sitelib}/colored_traceback-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/colored_traceback/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 W. Michael Petullo <mike@flyn.org> - 0.3.0-1
- Initial package
