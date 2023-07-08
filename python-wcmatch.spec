# Created by pyp2rpm-3.3.5
%global pypi_name wcmatch

Name:           python-%{pypi_name}
Version:        8.4.1
Release:        3%{?dist}
Summary:        Wildcard/glob file name matcher

License:        MIT
URL:            https://github.com/facelessuser/wcmatch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Based on https://github.com/facelessuser/wcmatch/commit/223f9caba2a4d9ce6b796d890693773e9c5d4080
Patch:          Update-to-support-Python-3.12-alpha-203.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(bracex)
BuildRequires:  python3dist(setuptools)

%description
Wildcard Match provides an enhanced fnmatch, glob, and pathlib library in order
to provide file matching and globbing that more closely follows the features
found in Bash. In some ways these libraries are similar to Python's builtin
libraries as they provide a similar interface to match, filter, and glob the
file system. But they also include a number of features found in Bash's
globbing such as backslash escaping, brace expansion, extended glob pattern
groups, etc. They also add a number of new useful functions as well, such as
globmatch which functions like fnmatch, but for paths.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Wildcard Match provides an enhanced fnmatch, glob, and pathlib library in order
to provide file matching and globbing that more closely follows the features
found in Bash. In some ways these libraries are similar to Python's builtin
libraries as they provide a similar interface to match, filter, and glob the
file system. But they also include a number of features found in Bash's
globbing such as backslash escaping, brace expansion, extended glob pattern
groups, etc. They also add a number of new useful functions as well, such as
globmatch which functions like fnmatch, but for paths.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -vv -k "not test_tilde_user"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 8.4.1-3
- Rebuilt for Python 3.12
- Fixes: rhbz#2189489

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Parag Nemade <pnemade AT redhat DOT com> - 8.4.1-1
- Update to new version 8.4.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 8.1.2-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.2-6
- Fix tests to run against Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 8.1.2-4
- Rebuilt for Python 3.10

* Fri Mar 12 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.2-3
- Fix package as per package review comments (#1929992)

* Thu Mar 11 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.2-2
- Only skip required failing tests

* Wed Mar 10 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.2-1
- Update to 8.1.2 version
- Skip the failing tests

* Wed Feb 24 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.1-3
- Simplify URL: tag usage
- Drop unnecessary egg-info removal

* Sat Feb 20 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.1-2
- Change Source to github to use tests

* Thu Feb 18 2021 Parag Nemade <pnemade AT redhat DOT com> - 8.1.1-1
- Initial package.
