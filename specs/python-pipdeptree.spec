%global srcname pipdeptree

%global _description\
pipdeptree is a command line utility for displaying the installed python\
packages in form of a dependency tree. It works for packages installed\
globally on a machine as well as in a virtualenv.

Name:           python-%{srcname}
Version:        2.25.0
Release:        %autorelease
Summary:        Command line utility to show dependency tree of packages

License:        MIT
URL:            https://github.com/naiquevin/pipdeptree
Source0:        https://github.com/naiquevin/pipdeptree/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros >= 0-41

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%pyproject_extras_subpkg -n python3-%{srcname} graphviz

%prep
%autosetup -n %{srcname}-%{version}
# Remove unneeded testing deps
sed -i "/diff-cover/d;/covdefaults/d;/pytest-cov/d" pyproject.toml
# Remove version limits from dependencies
sed -i 's/"virtualenv.*",/"virtualenv",/' pyproject.toml
sed -i 's/"graphviz.*",/"graphviz",/' pyproject.toml
sed -i 's/"pytest>.*",/"pytest",/' pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_buildrequires -x test,graphviz

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# test_console expects /usr/bin/pipdeptree to exists
# test_custom_interpreter doesn't work
%pytest -vvv -k "not test_console and not test_custom_interpreter"

%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE
%doc README.md
%{_bindir}/pipdeptree

%changelog
%autochangelog
