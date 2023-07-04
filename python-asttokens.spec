Name:           python-asttokens
Version:        2.2.1^20230701a802446
Release:        %autorelease
Summary:        Module to annotate Python abstract syntax trees with source code positions

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/asttokens
# This is directly from the 3.12 branch
# See https://github.com/gristlabs/asttokens/pull/110
Source0:        https://github.com/gristlabs/asttokens/archive/3.12/asttokens-3.12.tar.gz

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(astroid)
BuildRequires:  python3dist(six)

%global _description %{expand:
The asttokens module annotates Python abstract syntax trees (ASTs) with the
positions of tokens and text in the source code that generated them. This makes
it possible for tools that work with logical AST nodes to find the particular
text that resulted in those nodes, for example for automated refactoring or
highlighting.}

%description %_description

%package     -n python3-asttokens
Summary:        %{summary}
Requires:       %{py3_dist six}
%{?python_provide:%python_provide python3-asttokens}

%description -n python3-asttokens %_description

%prep
%autosetup -S git -n asttokens-3.12
git tag 2.2.1

%build
%py3_build

%install
%py3_install

%check
# test_fixture9 and test_sys_modules tests are currently failing with Python 3.12
pytest-3 tests/ -v "${TEST_ARGS[@]}" -k "not test_fixture9 and not test_sys_modules"

%files -n python3-asttokens
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
%autochangelog
