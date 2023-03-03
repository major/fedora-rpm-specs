%global pkg_name flask-security-too


Name:           python-%{pkg_name}
Version:        4.1.5
Release:        3%{?dist}
Summary:        Simple security for Flask apps
License:        MIT

BuildArch:      noarch
URL:            https://github.com/Flask-Middleware/flask-security
Source0:        %{pypi_source Flask-Security-Too}
# Drop missing test deps
Patch0:         python-flask-security-too_testdeps.patch

BuildRequires:  python3-devel

%description
Flask-Security quickly adds security features to your Flask application.


%package -n python3-%{pkg_name}
Summary:        Simple security for Flask apps

# flask_security/utils.py imports pkg_resources
# Upstream PR: https://github.com/Flask-Middleware/flask-security/pull/763
Requires:       python%{python3_version}dist(setuptools)

%description -n python3-%{pkg_name}
Flask-Security quickly adds security features to your Flask application.

# Skipping mfa extra, pyqrcode and phonenumberslite are not packaged
%pyproject_extras_subpkg -n python3-%{pkg_name} babel fsqla common


%prep
%autosetup -p1 -n Flask-Security-Too-%{version}
# Disable tests for unavailable test dependencies
sed -r -i '/\b(two_factor|unified_signin)\b/d' tests/conftest.py

%generate_buildrequires
# Skipping mfa extra, pyqrcode and phonenumberslite are not packaged
%pyproject_buildrequires -x babel,fsqla,common -r requirements/tests.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flask_security

# Work around neither %%pyproject_save_files nor %%find_lang supporting
# language files that are not in a directory named “locale”:
sed -r '/\/translations\/.*\.mo/d' '%{pyproject_files}'
cp -rp '%{buildroot}/%{python3_sitelib}/flask_security/translations' \
    '%{buildroot}/%{python3_sitelib}/flask_security/locale'
find '%{buildroot}/%{python3_sitelib}/flask_security/locale' \
    -type f ! -name '*.mo' -delete
%find_lang flask_security
rm -rf '%{buildroot}/%{python3_sitelib}/flask_security/locale'
sed -r -i 's@/locale/@/translations/@' flask_security.lang


%check
# Disable tests for unavailable test dependencies
%pytest -m 'not two_factor and not unified_signin'


%files -n python3-%{pkg_name} -f %{pyproject_files} -f flask_security.lang
%license LICENSE
%doc README.rst AUTHORS


%changelog
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
