Name: bandit
Version: 1.7.5
Release: %autorelease
Summary: A framework for performing security analysis of Python source code

License: ASL 2.0
URL: https://github.com/PyCQA/bandit
Source0: https://files.pythonhosted.org/packages/source/b/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# for checks, cherry-picked from test-requirements.txt (mixes coverage and linting)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(fixtures)
BuildRequires:  python3dist(testscenarios)
BuildRequires:  python3dist(testtools)
BuildRequires:  python3dist(toml)

%description
Bandit provides a framework for performing security analysis of Python source
code, utilizing the ast module from the Python standard library.

The ast module is used to convert source code into a parsed tree of Python
syntax nodes. Bandit allows users to define custom tests that are performed
against those nodes. At the completion of testing, a report is generated
that lists security issues identified within the target source code.

%prep
%autosetup

# remove test that requires bs4
rm tests/unit/formatters/test_html.py

# Add missing requirement on pbr
# https://github.com/PyCQA/bandit/pull/959
echo "pbr" >> requirements.txt

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files bandit

%check
%pytest tests

%files -f %{pyproject_files}
%doc AUTHORS ChangeLog README.rst
%doc doc
%doc examples
%license LICENSE
%{_bindir}/bandit
%{_bindir}/bandit-baseline
%{_bindir}/bandit-config-generator

%changelog
%autochangelog
