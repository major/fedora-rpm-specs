%global srcname linetable

Name:           python-%{srcname}
Version:        0.0.3
Release:        8%{?dist}
Summary:        Parse and generate co_linetable attributes in code objects
License:        MIT
URL:            https://github.com/amol-/linetable
Source0:        https://github.com/amol-/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Library to parse and generate co_linetable attributes in Python code objects.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.3-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.3-2
- Rebuilt for Python 3.12

* Tue Mar 07 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.0.3-1
- Update to upstream.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.0.2-3
- Removed setuptools dependency.
- Updated description.

* Mon Nov 28 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.0.2-2
- Fix problems according to packaging guidelines.

* Fri Nov 25 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.0.2-1
- Initial release.
