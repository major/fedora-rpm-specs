Name:           python-asttokens
Version:        2.2.1
Release:        %autorelease
Summary:        Module to annotate Python abstract syntax trees with source code positions

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/asttokens
Source0:        https://files.pythonhosted.org/packages/source/a/asttokens/asttokens-%{version}.tar.gz

BuildArch:      noarch
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
%autosetup -p1 -n asttokens-%{version}

%build
%py3_build

%install
%py3_install

%check
pytest-3 tests/ -v "${TEST_ARGS[@]}"

%files -n python3-asttokens
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
%autochangelog
