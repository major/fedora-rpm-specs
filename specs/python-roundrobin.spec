Name:           python-roundrobin
Version:        0.0.4
Release:        9%{?dist}
Summary:        Rather small collection of round robin utilites

License:        MIT
URL:            https://github.com/linnik/roundrobin
Source:         %{url}/archive/%{version}/roundrobin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# required for tests
BuildRequires:  python3-pytest

%global _description %{expand:
This is rather small collection of round robin utilites}

%description %_description

%package -n python3-roundrobin
Summary:        %{summary}

%description -n python3-roundrobin %_description


%prep
%autosetup -p1 -n roundrobin-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files roundrobin


%check
%pytest test.py


%files -n python3-roundrobin -f %{pyproject_files}
%doc README.*
%license LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.4-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.4-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 07 2022 Jonathan Wright <jonathan@almalinux.org> - 0.0.4-1
- Initial package build
- rhbz#2116219
