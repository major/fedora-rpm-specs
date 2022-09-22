Name:           python-requests-exoscale-auth
Version:        1.1.2
Release:        5%{?dist}
Summary:        Exoscale APIs support for Python-Requests

License:        BSD
URL:            https://github.com/exoscale/requests-exoscale-auth
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Exoscale APIs support for Python-Requests}

%description %_description

%package -n python3-requests-exoscale-auth
Summary:        %{summary}

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)

%description -n python3-requests-exoscale-auth %_description

%prep
%autosetup -p1 -n requests-exoscale-auth-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files exoscale_auth


%check
%pytest


%files -n python3-requests-exoscale-auth -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 Roman Inflianskas <rominf@aiven.io> - 1.1.2-2
- Fix summary
* Tue Oct 26 2021 Roman Inflianskas <rominf@aiven.io> - 1.1.2-1
- Initial package
