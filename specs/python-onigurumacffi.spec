# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (C) Fedora Project Authors
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT

%bcond tests 1

Name:           python-onigurumacffi
Version:        1.3.0
Release:        2%{?dist}
Summary:        Python cffi bindings for the Oniguruma regex engine

License:        MIT
URL:            https://github.com/asottile/onigurumacffi
Source:         %{url}/archive/v%{version}/onigurumacffi-%{version}.tar.gz

BuildRequires:  gcc
Buildrequires:  pkgconfig(oniguruma)
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
onigurumacffi provides Python cffi bindings for the Oniguruma regex engine.}

%description %{_description}


%package -n python3-onigurumacffi
Summary:    %{summary}

%description -n python3-onigurumacffi %{_description}


%prep
%autosetup -n onigurumacffi-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l onigurumacffi


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-onigurumacffi -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/_onigurumacffi.abi3.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 05 2024 Maxwell G <maxwell@gtmx.me> - 1.3.0-1
- Update to 1.3.0.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 15 2023 Maxwell G <maxwell@gtmx.me> - 1.2.0-1
- Initial package. Closes rhbz#2232782.
