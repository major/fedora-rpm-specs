Name:           python-poetry-core
Version:        1.2.0
Release:        1%{?dist}
Summary:        Poetry PEP 517 Build Backend

# We bundle a lot of libraries with poetry, which itself is under MIT license.
# Here is the list of the libraries with corresponding licenses:

# attrs: MIT
# jsonschema: MIT
# lark: MIT
# packaging: ASL 2.0 or BSD
# pkgutil-resolve-name: MIT
# pyparsing: MIT
# pyrsistent: MIT
# tomlkit: MIT
# typing-extensions: Python

License:        MIT and (ASL 2.0 or BSD) and Python
URL:            https://github.com/python-poetry/poetry-core
Source0:        %{url}/archive/%{version}/poetry-core-%{version}.tar.gz

# This patch moves the vendored requires definition
# from vendors/pyproject.toml to pyproject.toml
# Intentionally contains the removed hunk to prevent patch aging

# poetry is broken with packaging 21+ (https://github.com/python-poetry/poetry/issues/4264).
# We are temporarily disabling this patch so installed poetry works again.
#Patch1:         poetry-core-1.0.2-devendor.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# for tests (only specified via poetry poetry.dev-dependencies with pre-commit etc.)
BuildRequires:  python3-build
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pep517
BuildRequires:  python3-virtualenv
BuildRequires:  gcc
BuildRequires:  git-core


%global _description %{expand:
A PEP 517 build backend implementation developed for Poetry.
This project is intended to be a light weight, fully compliant, self-contained
package allowing PEP 517 compatible build frontends to build Poetry managed
projects.}

%description %_description


%package -n python3-poetry-core
Summary:        %{summary}

# Previous versions of poetry included poetry-core in it
Conflicts:      python%{python3_version}dist(poetry) < 1.1
# The bundled versions are taken from src/poetry/core/_vendor/vendor.txt
Provides:       bundled(python3dist(attrs)) = 22.1
Provides:       bundled(python3dist(jsonschema)) = 4.10
Provides:       bundled(python3dist(lark)) = 1.1.2
Provides:       bundled(python3dist(packaging)) = 21.3
Provides:       bundled(python3dist(pkgutil-resolve-name)) = 1.3.10
Provides:       bundled(python3dist(pyparsing)) = 3.0.9
Provides:       bundled(python3dist(pyrsistent)) = 0.18.1
Provides:       bundled(python3dist(tomlkit)) = 0.11.4
Provides:       bundled(python3dist(typing-extensions)) = 4.3.0

%description -n python3-poetry-core %_description


%prep
%autosetup -p1 -n poetry-core-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
# we debundle the deps after we use the bundled deps in previous step to parse the deps 🤯
#rm -r poetry/core/_vendor

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files poetry


%check
# don't use %%tox here because tox.ini runs "poetry install"
# TODO investigate failures in test_default_with_excluded_data, test_default_src_with_excluded_data
%pytest -k "not with_excluded_data"


%files -n python3-poetry-core -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Fri Sep 30 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.8-2
- Rebuilt for Python 3.11

* Mon Mar 07 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.0.8-1
- Update to 1.0.8

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.0.7-1
- Update to 1.0.7

* Fri Oct 01 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.0.6-1
- Update to 1.0.6

* Tue Sep 07 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.0.4-1
- Update to 1.0.4

* Thu Aug 19 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.0.3-5
- Bundle vendored libraries again, to fix poetry install

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Lumír Balhar <lbalhar@redhat.com> - 1.0.3-3
- Allow newer packaging version
- Allow newer pyrsistent version

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.10

* Thu Apr 15 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Thu Feb 25 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-1
- Initial package
