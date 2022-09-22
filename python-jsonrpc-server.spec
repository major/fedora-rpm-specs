%global pypi_name python-jsonrpc-server
%global srcname jsonrpc-server

%global _description %{expand:
A Python server implementation of the JSON RPC 2.0 protocol.
}

Name:           python-%{srcname}
Version:        0.4.0
Release:        7%{?dist}
Summary:        JSON RPC 2.0 server library

License:        MIT
URL:            https://github.com/palantir/python-jsonrpc-server
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(ujson)
BuildRequires:  python3-versioneer

%description
%_description

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(ujson)

%description -n python3-%{srcname}
%_description

%prep
%autosetup -n %{pypi_name}-%{version}

# remove ujson version
sed -i 's/ujson<=1.35;/ujson;/' setup.py
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# test setup from openSUSE spec file
# ignore tests not compatible with current python versions
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-3 -v -k 'not (test_request_error or test_request_cancel or test_writer_bad_message)'

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pyls_jsonrpc
%{python3_sitelib}/python_jsonrpc_server-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-4
- Rebuilt for Python 3.9

* Sun Apr 26 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.4-3
- Removed ujson version dep

* Sun Apr 26 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.4-2
- Fix license
- Add comment about tests

* Fri Apr 24 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.4-1
- Initial package.
