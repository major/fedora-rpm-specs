%global srcname dirhash

Name:           python-%{srcname}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Python module and CLI for hashing of file system directories

License:        MIT
URL:            https://github.com/andhus/dirhash-python
Source0:        https://github.com/andhus/dirhash-python/archive/v%{version}/%{srcname}-python-%{version}.tar.gz

# Needed to run tests outside of a venv - Not submitted upstream
Patch0:         %{srcname}-python-0.2.1-cli-test.patch
# Submitted upstream as andhus/dirhash-python#15
Patch1:         %{srcname}-python-0.2.1-posargs.patch

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

# Drop shebangs from module
sed -i '1{s|^#!\(/usr\)\?/bin/\(env \)\?python\d\?$||}' src/dirhash/{cli.py,__init__.py}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# test_ignore_hidden_files is broken with pathspec >= 0.10.0
# See andhus/dirhash-python#14
%tox -- -- -k 'not test_ignore_hidden_files'


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/%{srcname}


%changelog
* Wed Nov 16 2022 Scott K Logan <logans@cottsay.net> - 0.2.1-1
- Initial package (rhbz#2143807)
