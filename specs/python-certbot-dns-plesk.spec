%global pypi_name certbot-dns-plesk

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        2%{?dist}
Summary:        Plesk DNS Authenticator plugin for Certbot

License:        GPL-3.0-or-later
URL:            https://pypi.org/project/%{pypi_name}
Source0:        %{pypi_source certbot_dns_plesk}

BuildArch:      noarch

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Plesk DNS Authenticator plugin for Certbot
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

# Provide the name users expect as a certbot plugin
%if 0%{?fedora}
Provides:       %{pypi_name} = %{version}-%{release}
%endif
# Recommend the CLI as that will be the interface most use
Recommends:     certbot

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n certbot_dns_plesk-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l certbot_dns_plesk

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

%autochangelog
