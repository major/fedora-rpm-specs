# Tests are enabled by default
%bcond_without tests

%global         srcname     flask-basicauth
%global         forgeurl    https://github.com/jpvanhal/%{srcname}
Version:        0.2.0
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        7%{?dist}
Summary:        HTTP basic authentication for Flask

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

# https://github.com/jpvanhal/flask-basicauth/pull/29
Patch:          29.patch

%global _description %{expand:
HTTP basic authentication for Flask}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flask_basicauth


%if %{with tests}
%check
rm -f flask_basicauth.py
%pytest --pyargs
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.* CHANGES.rst


%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.2.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Major Hayden <major@redhat.com> - 0.2.0-3
- Switch to force macros
- Use pyproject_save_files macro

* Tue Aug 23 2022 Jonathan Wright <jonathan@almalinux.org> - 0.2.0-2
- Improve patching of tests

* Sun Aug 07 2022 Jonathan Wright <jonathan@almalinux.org> - 0.2.0-1
- Initial package build
- rhbz#2116257
