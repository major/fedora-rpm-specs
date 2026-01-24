Name:           python-asttokens
Version:        3.0.1
Release:        %autorelease
Summary:        Module to annotate Python abstract syntax trees with source code positions

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/asttokens
Source:         https://github.com/gristlabs/asttokens/archive/v%{version}/asttokens-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The asttokens module annotates Python abstract syntax trees (ASTs) with the
positions of tokens and text in the source code that generated them. This makes
it possible for tools that work with logical AST nodes to find the particular
text that resulted in those nodes, for example for automated refactoring or
highlighting.}

%description %_description

%package     -n python3-asttokens
Summary:        %{summary}

%description -n python3-asttokens %_description

%prep
%autosetup -p1 -n asttokens-%{version}

# Drop dependency on pytest-cov, not useful for distro builds
sed -r -i '/pytest-cov/d' setup.cfg

%generate_buildrequires
# Let setuptools_scm determine version outside of SCM
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x test

%build
# Let setuptools_scm determine version outside of SCM
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l asttokens

%check
%pytest tests/ -v "${TEST_ARGS[@]}"

%files -n python3-asttokens -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
