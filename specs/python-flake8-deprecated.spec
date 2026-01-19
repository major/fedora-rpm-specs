%global srcname flake8-deprecated

Name:           python-%{srcname}
Version:        2.3.0
Release:        2%{?dist}
Summary:        Flake8 plugin that warns about deprecated method calls

License:        GPL-2.0-only
URL:            https://github.com/gforcada/flake8-deprecated
Source0:        https://github.com/gforcada/flake8-deprecated/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
No language, library or framework ever get everything right from the very
beginning. The project evolves, new features are added/changed/removed.

This means that projects relying on them must keep an eye on what's currently
best practices.

This flake8 plugin helps you keeping up with method deprecations and giving
hints about what they should be replaced with.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l flake8_deprecated


%check
%pytest run_tests.py


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGES.rst README.rst


%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Dec 09 2025 Scott K Logan <logans@cottsay.net> - 2.3.0-1
- Update to 2.3.0 (rhbz#2406328)

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 2.2.1-7
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 2.2.1-6
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jun 04 2025 Python Maint <python-maint@redhat.com> - 2.2.1-4
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 21 2024 Scott K Logan <logans@cottsay.net> - 2.2.1-1
- Update to 2.2.1
- Add `-l` flag to %%pyproject_save_files

* Tue Nov 22 2022 Scott K Logan <logans@cottsay.net> - 2.0.1-2
- Define _description variable to reduce duplication
- Drop macro from URL to improve ergonomics

* Thu Nov 10 2022 Scott K Logan <logans@cottsay.net> - 2.0.1-1
- Initial package (rhbz#2141870)
