%global srcname ipuz
# The GitHub repo doesn't have tags, this is the commit corresponding to the
# 1.0 release in PyPI
%global commit 8dae6cff00a8269d7d29b129bc73a0233963bc60

Name:           python-%{srcname}
Version:        1.0
Release:        %autorelease
Summary:        Python library for reading and writing ipuz puzzle files

License:        MIT
URL:            https://github.com/svisser/ipuz
# The PyPI tarball doesn't include tests so use GitHub instead
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

%global _description %{expand:
Python library for reading and writing ipuz puzzle files. The specification for
the ipuz file format can be found at: http://www.ipuz.org/. The ipuz file
format supports representing various types of puzzles, including crossword,
sudoku and word search. This Python library provides validation and wrapping
around the puzzle data.

As the puzzle is inherently JSON data it is the application's responsibility to
ensure that the JSON satisfies the constraints of the PuzzleKind prior to
writing the puzzle. This library provides validation and additional
functionality that you might want to use.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
Suggests:       %{name}-doc = %{version}-%{release}

%description -n python3-%{srcname} %_description

%package        doc
Summary:        %{name} documentation

%description    doc
This package contains additional documentation for %{name}.

%prep
%autosetup -p1 -n %{srcname}-%{commit}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.rst README.rst

%files doc
%license LICENSE
%doc html

%changelog
%autochangelog
