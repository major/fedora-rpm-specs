Name:           python-pyupgrade
Version:        3.3.0
Release:        9%{?dist}
Summary:        A tool to upgrade syntax of Python code for newer versions of the language

License:        MIT
URL:            https://github.com/asottile/pyupgrade
Source:         %{url}/archive/v%{version}/pyupgrade-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Testing requirements
# covdefaults (from tox.ini -> requirements-dev.txt) is not packaged
# for Fedora, using pytest directly
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A tool to upgrade syntax of Python code for newer versions of the language.}

%description %_description

%package -n python3-pyupgrade
Summary:        %{summary}

%description -n python3-pyupgrade %_description


%prep
%autosetup -p1 -n pyupgrade-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyupgrade


%check
%pytest


%files -n python3-pyupgrade -f %{pyproject_files}
%doc README.md LICENSE
%{_bindir}/pyupgrade


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Python Maint <python-maint@redhat.com> - 3.3.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0 (resolves rhbz#2150391)

* Wed Nov 30 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 3.2.3-1
- Update to 3.2.3 (resolves rhbz#2149341)

* Thu Nov 24 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 3.2.2-1
- Update to 3.2.2 (resolves rhbz#2133584)

* Tue Oct 04 2022 Roman Inflianskas <rominf@aiven.io> - 3.0.0-1
- Update to 3.0.0 (resolves rhbz#2129567)

* Mon Sep 19 2022 Roman Inflianskas <rominf@aiven.io> - 2.38.0-1
- Update to 2.38.0 (resolves rhbz#2127202)

* Thu Jul 28 2022 Roman Inflianskas <rominf@aiven.io> - 2.37.3-1
- Update to 2.37.3

* Mon Jul 25 2022 Roman Inflianskas <rominf@aiven.io> - 2.37.2-1
- Initial package

