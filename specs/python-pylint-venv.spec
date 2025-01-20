Name:           python-pylint-venv
Version:        3.0.2
Release:        6%{?dist}
Summary:        Make pylint respect virtualenvs

License:        MIT
URL:            https://github.com/jgosmann/pylint-venv/
Source0:        %{url}/archive/v%{version}/pylint-venv-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pylint

%description
%summary


%package -n python3-pylint-venv
Summary:        %{summary}
%description -n python3-pylint-venv
%summary


%prep
%autosetup -n pylint-venv-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files pylint_venv


%check
%pyproject_check_import


%files -n python3-pylint-venv -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 3.0.2-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 24 2023 Sandro <devel@penguinpee.nl> - 3.0.2-1
- Update to 3.0.2 (RHBZ#2214334)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 3.0.1-2
- Rebuilt for Python 3.12

* Tue Apr 11 2023 Jonathan Wright <jonathan@knownhost.com> - 3.0.1
- initial package build
