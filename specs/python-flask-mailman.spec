Name:           python-flask-mailman
Version:        1.1.1
Release:        3%{?dist}
Summary:        Porting Django's email implementation to your Flask applications

License:        BSD-3-Clause
URL:            https://github.com/waynerv/flask-mailman
Source0:        https://github.com/waynerv/flask-mailman/archive/v%{version}/flask-mailman-%{version}.tar.gz
# Drop mkdocs-material-extensions dependency which is not packages
# (all mkdocs dependencies are unused as docs are not built)
# Relax test dependencies
Patch0:         flask-mailman_deps.patch

BuildArch:      noarch

%description
Flask-Mailman is a Flask extension providing simple email sending capabilities.


%package -n python3-flask-mailman
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-flask-mailman
Flask-Mailman is a Flask extension providing simple email sending capabilities.

Python 3 version.


%prep
%autosetup -p1 -n flask-mailman-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flask_mailman


%check
%tox


%files -n python3-flask-mailman -f %{pyproject_files}
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Sandro Mani <manisandro@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Wed Jul 03 2024 Sandro Mani <manisandro@gmail.com> - 1.1.0-3
- Add flask-mailman-setpayload.patch to fix py3.13 build

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.13

* Tue Apr 23 2024 Sandro Mani <manisandro@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 07 2023 Sandro Mani <manisandro@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 0.3.0-6
- Rebuilt for Python 3.12

* Fri Apr 07 2023 Sandro Mani <manisandro@gmail.com> - 0.3.0-5
- Remove reduntant license

* Fri Apr 07 2023 Sandro Mani <manisandro@gmail.com> - 0.3.0-4
- Re-add %%license

* Thu Apr 06 2023 Sandro Mani <manisandro@gmail.com> - 0.3.0-3
- Switch to GitHub source

* Wed Apr 05 2023 Sandro Mani <manisandro@gmail.com> - 0.3.0-2
- Explicitly specify pypi_source
- Remove reduntant license
- Run %%tox in %%check
- Document patch reason

* Wed Feb 08 2023 Sandro Mani <manisandro@gmail.com> - 0.3.0-1
- Initial package
