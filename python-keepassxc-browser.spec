%global pypi_name keepassxc-browser

Name:           python-%{pypi_name}
Version:        0.1.8
Release:        4%{?dist}
Summary:        Access the KeepassXC Browser API from python

License:        AGPL-3.0-or-later
URL:            https://github.com/hrehfeld/python-keepassxc-browser
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pysodium)

%global _description %{expand:
A Python package to interface with KeePassXC over the KeePassXC Browser API.}

%description
%{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{_description}

%prep
%autosetup -p1 -n keepassxc-browser-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/keepassxc_browser-%{version}-py*.egg-info
%{python3_sitelib}/keepassxc_browser

%changelog
* Sun Mar 05 2023 Andreas Schneider <asn@redhat.com> - 0.1.8-4
- Update License to SPDX expression

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 16 2022 Andreas Schneider <asn@redhat.com> - 0.1.8-1
- Initial package
