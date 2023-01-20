%global pypi_name credslayer
%bcond_with local

Name:           credslayer
Version:        0.1.2
Release:        9%{?dist}
Summary:        Extract credentials and other details from network captures

License:        GPLv3
URL:            https://github.com/ShellCode33/CredSLayer
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pyshark
BuildRequires:  wireshark-cli

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
CredSLayer goal is to look for credentials and other useful stuff in network
captures. Two modes are available, pcap scanning and active processing. The
latest listens for packets on a chosen interface and dynamically extracts
everything it can.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
CredSLayer goal is to look for credentials and other useful stuff in network
captures. Two modes are available, pcap scanning and active processing. The
latest listens for packets on a chosen interface and dynamically extracts
everything it can.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{pypi_name}

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-argparse

%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -n CredSLayer-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=%{PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%if %{with local}
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests/tests.py
%endif

%files
%{_bindir}/credslayer

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/CredSLayer-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.1.2-7
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.2-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Remove shebang and Python standard module (rhbz#1856825)
- Update to latest upstream release 0.1.2

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package for Fedora
