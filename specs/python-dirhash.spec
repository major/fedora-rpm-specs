%global srcname dirhash

Name:           python-%{srcname}
Version:        0.5.0
Release:        2%{?dist}
Summary:        Python module and CLI for hashing of file system directories

License:        MIT
URL:            https://github.com/andhus/dirhash-python
Source0:        https://github.com/andhus/dirhash-python/archive/v%{version}/%{srcname}-python-%{version}.tar.gz

# Needed to run tests outside of a venv - Not submitted upstream
Patch0:         %{srcname}-python-0.5.0-cli-test.patch

BuildArch:      noarch

%global _description %{expand:
A lightweight python module and CLI for computing the hash of any directory
based on its files' structure and content.

- Supports all hashing algorithms of Python's built-in hashlib module.
- Glob/wildcard (".gitignore style") path matching for expressive filtering
  of files to include/exclude.
- Multiprocessing for up to 6x speed-up

The hash is computed according to the Dirhash Standard, which is designed to
allow for consistent and collision resistant generation/verification of
directory hashes across implementations.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-python-%{version}

# Loosen pinned versioneer requirement
sed -i 's|versioneer==[0-9.]*|versioneer|g' pyproject.toml

# Drop shebangs from module
sed -i '1{s|^#!\(/usr\)\?/bin/\(env \)\?python\d\?$||}' src/dirhash/{cli.py,__init__.py}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%check
%tox


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/%{srcname}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Scott K Logan <logans@cottsay.net> - 0.5.0-1
- Update to 0.5.0 (rhbz#2293812)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Scott K Logan <logans@cottsay.net> - 0.4.0-1
- Update to 0.4.0 (rhbz#2275947)
- Re-enable all tests now that we have pathspec 0.12

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 16 2022 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Initial package (rhbz#2143807)
