Name:           python-exoscale
Version:        0.7.1
Release:        4%{?dist}
Summary:        Python bindings for Exoscale API

License:        ISC
URL:            https://exoscale.github.io/python-exoscale/
Source0:        https://github.com/exoscale/python-exoscale/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
The library to allow developers to use the Exoscale cloud platform API with
high-level Python bindings.}

%description %_description

%package -n python3-exoscale
Summary:        %{summary}

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(requests-mock)

%description -n python3-exoscale %_description

%prep
%autosetup -p1 -n python-exoscale-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files exoscale


%check
%pytest


%files -n python3-exoscale -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 Roman Inflianskas <rominf@aiven.io> - 0.7.1-1
- Initial package
