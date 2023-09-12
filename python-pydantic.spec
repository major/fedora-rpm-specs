Name:           python-pydantic
Version:        1.10.12
Release:        1%{?dist}
Summary:        Data validation using Python type hinting

License:        MIT
URL:            https://github.com/pydantic/pydantic
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          Fix-Python-3.12-test-failures.patch
BuildArch:      noarch

BuildRequires:  python3-devel
# For check phase
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)

%description
Data validation and settings management using python type hinting.


%package -n     python3-pydantic
Summary:        %{summary}
Recommends:     python3-pydantic+email


%description -n python3-pydantic
Data validation and settings management using python type hinting.


%prep
%autosetup -n pydantic-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires -x email -x dotenv


%build
%pyproject_wheel


# Docs are in MarkDown, and should be added when mkdocs is packaged.

%install
%pyproject_install
%pyproject_save_files pydantic


%check
# Disable mypy plugin tests. We don't use it for downstream packaging.
%pytest -Wdefault --ignore=tests/mypy/test_mypy.py


%files -n python3-pydantic -f %{pyproject_files}
%license LICENSE
%doc README.md docs/

%pyproject_extras_subpkg email,dotenv -n python3-pydantic

%changelog
* Sat Aug 12 2023 Maxwell G <maxwell@gtmx.me> - 1.10.12-1
- Update to 1.10.12.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.10.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 07 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.10.2-1
- Update to 1.10.2.

* Thu Sep 01 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1.

* Wed Aug 24 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.9.2-1
- Update to 1.9.2.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.9.1-2
- Rebuilt for Python 3.11

* Thu Jun 09 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.9.1-1
- Update to 1.9.1.

* Wed Feb 02 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.4-2
- Rebuilt for Python 3.10

* Tue May 11 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.7.4-1
- Update to 1.7.4; fixes CVE-2021-29510

* Wed Feb 24 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.7.3-1
- Update to 1.7.3.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3-3
- python-email_validator is now packaged as python-email-validator...

* Tue Jan 07 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3-2
- Review fixes.

* Mon Jan 06 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3-1
- Update to 1.3.
- Review fixes.

* Sun Nov 24 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1.

* Sat Jul 27 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.31-1
- Initial package.
