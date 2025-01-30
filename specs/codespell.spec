Name:           codespell
Version:        2.4.1
Release:        %autorelease
Summary:        Fix common misspellings in text files

License:        GPL-2.0-only AND CC-BY-SA-3.0
URL:            https://github.com/codespell-project/codespell/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
# For checks
BuildRequires:  python3dist(chardet)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-dependency)
BuildRequires:  aspell-en

%description
codespell fixes common misspellings in text files. It's designed primarily for
checking misspelled words in source code, but it can be used with other files
as well.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files codespell_lib

%check
# Skip coverage tests
sed -i -e 's/--cov=codespell_lib//' pyproject.toml
sed -i -e 's/--cov-report=//' pyproject.toml
%pytest

%files -f %{pyproject_files}
%doc README.rst
%license COPYING
%{_bindir}/codespell

%changelog
%autochangelog
