%global pypi_name application-properties

Name:           python-%{pypi_name}
Version:        0.8.3
Release:        4%{?dist}
Summary:        A simple, easy to use, unified manner of accessing program properties

License:        MIT
URL:            https://github.com/jackdewinter/application_properties
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pyyaml) >= 5.4.1
BuildRequires:  python3dist(tomli) >= 2.0.1
BuildRequires:  python3dist(typing-extensions) >= 4.5
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-cov)

%description
The application_properties package was born out of necessity.
During the creation of the PyMarkdown project, there was a distinct need for
a configuration subsystem that was able to handle more complex
configuration scenarios.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(pyyaml) >= 5.4.1
Requires:       python3dist(tomli) >= 2.0.1
Requires:       python3dist(typing-extensions) >= 4.5
%description -n python3-%{pypi_name}
The application_properties package was born out of necessity.
During the creation of the PyMarkdown project, there was a distinct need for
a configuration subsystem that was able to handle more complex
configuration scenarios.

%prep
%autosetup -n application_properties-%{version}
sed -i -e 's@pytest@nopytest@' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


sed -i 's/\r$//' README.md

%install
%pyproject_install
%pyproject_save_files -l application_properties

rm -f %{buildrot}%{python3_sitelib}application_properties/.external-package

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.8.3-4
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.8.3-3
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 16 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.8.3-1
- 0.8.3

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.8.2-4
- Rebuilt for Python 3.14

* Fri Apr 11 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.8.2-3
- Additional review fixes.

* Mon Apr 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.8.2-2
- review edits

* Wed May 08 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.8.2-1
- Initial package.
