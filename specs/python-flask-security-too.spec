%global pkg_name flask-security-too


Name:           python-%{pkg_name}
Version:        5.5.2
Release:        3%{?dist}
Summary:        Simple security for Flask apps
License:        MIT

BuildArch:      noarch
URL:            https://github.com/Flask-Middleware/flask-security
Source0:        %{pypi_source flask_security_too}
# Drop missing test deps
Patch0:         python-flask-security-too_testdeps.patch
# Use phonenumbers instead of phonenumberslite
Patch1:         python-flask-security-too_phonenumbers.patch
# Don't fail on warnings in tests
Patch2:         python-flask-security-too_ignorewarnings.patch
# FIXME Temporarily drop sqlalchemy-utils dependency and bundle required functions
Patch3:         python-flask-security-too_no-sqla-utils.patch
# Relax flask-sqlalchemy version requirement
Patch4:         python-flask-security-too_flask-sqla.patch
# Flask 3.1 support
# https://github.com/pallets-eco/flask-security/pull/1040
Patch5:         1040.patch

BuildRequires:  python3-devel


%description
Flask-Security quickly adds security features to your Flask application.


%package -n python3-%{pkg_name}
Summary:        Simple security for Flask apps

%description -n python3-%{pkg_name}
Flask-Security quickly adds security features to your Flask application.

# Skip mfa extra, webauthn is not packaged
%pyproject_extras_subpkg -n python3-%{pkg_name} babel fsqla common


%prep
%autosetup -p1 -n flask_security_too-%{version}
ln -s pyproject-too.toml pyproject.toml


%generate_buildrequires
# Skip mfa extra, webauthn is not packaged
%pyproject_buildrequires -x babel,fsqla,common -r requirements/tests.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flask_security


%check
# Expected fail in DNS resolve (requires network)
%pytest -k "not test_login_email_whatever"


%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst AUTHORS


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 22 2024 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.5.2-2
- Backport fix for Flask >= 3.1

* Wed Aug 21 2024 Sandro Mani <manisandro@gmail.com> - 5.5.2-1
- Update to 5.5.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Sandro Mani <manisandro@gmail.com> - 5.4.3-2
- Rebuild (python-3.13)

* Sat Mar 23 2024 Sandro Mani <manisandro@gmail.com> - 5.4.3-1
- Update to 5.4.3

* Sat Mar 09 2024 Sandro Mani <manisandro@gmail.com> - 5.4.2-1
- Update to 5.4.2

* Tue Feb 27 2024 Sandro Mani <manisandro@gmail.com> - 5.4.1-1
- Update to 5.4.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.3.3-1
- Update to 5.3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 01 2023 Sandro Mani <manisandro@gmail.com> - 5.1.2-1
- Update to 5.1.2

* Sat Mar 04 2023 Sandro Mani <manisandro@gmail.com> - 5.1.1-1
- Update to 5.1.1

* Wed Mar 01 2023 Miro Hrončok <mhroncok@redhat.com> - 4.1.5-3
- Declare a runtime dependency on setuptools (for pkg_resources)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 29 2022 Sandro Mani <manisandro@gmail.com> - 4.1.5-1
- Update to 4.1.5

* Thu Jul 28 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.1.4-4
- Backport fix for werkzeug >= 2.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Python Maint <python-maint@redhat.com> - 4.1.4-2
- Rebuilt for Python 3.11

* Wed Apr 20 2022 Sandro Mani <manisandro@gmail.com> - 4.1.4-1
- Update to 4.1.4

* Thu Mar 03 2022 Sandro Mani <manisandro@gmail.com> - 4.1.3-1
- Update to 4.1.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Sandro Mani <manisandro@gmail.com> - 4.1.2-3
- Also include language files

* Mon Dec 27 2021 Sandro Mani <manisandro@gmail.com> - 4.1.2-2
- Run pytest
- Don't build docs
- Workaround to properly mark lang files
- Add extra metapackages

* Thu Dec 09 2021 Sandro Mani <manisandro@gmail.com> - 4.1.2-1
- Initial package
