%global srcname crossword
# The GitHub repo doesn't have tags, this is the commit corresponding to the
# 0.1.2 release in PyPI
%global commit 57078ad5ab5e1ef1bfaa909ca392e1c76e99be1f

Name:           python-%{srcname}
Version:        0.1.2
Release:        %autorelease
Summary:        Python library for handling crossword puzzles

License:        MIT
URL:            https://github.com/svisser/crossword
# The PyPI tarball doesn't include tests, so use GitHub instead
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
Python library for handling crossword puzzles. This library provides a
canonical data structure that can be used to represent crosswords in your
application. It provides a Pythonic way to perform common operations on the
grid, the words and the clues of the puzzle.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{commit}

# Do not pull puzpy from git and relax version pinning
sed -i test-requirements.txt -e 's/-e.*puzpy_master/puzpy/' -e 's/==.*$//g'

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst README.rst

%changelog
%autochangelog
