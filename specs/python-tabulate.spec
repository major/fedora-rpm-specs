# python-pandas creates a cyclic dependency on python-Bottleneck;
# we need to be able to break it during the new Python bootstrap
%bcond bootstrap 0
%bcond pandas_tests %{without bootstrap}

%global forgeurl            https://github.com/astanin/python-tabulate

Name:           python-tabulate
Version:        0.10.0
Release:        %autorelease
Summary:        Pretty-print tabular data in Python, a library and a command-line utility

%global tag  v%{version}

%forgemeta

# SPDX
License:        MIT
URL:            %forgeurl
Source0:        %forgesource
# Hand-written for Fedora based on --help output using groff_man(7) format
Source1:        tabulate.1

BuildArch:      noarch

BuildRequires:  python3-devel

# Additional test deps; see tox.ini, not in the sdist
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)

%if %{with pandas_tests}
BuildRequires:  python3dist(pandas)
%endif

%global _description %{expand:
The main use cases of the library are:

• printing small tables without hassle: just one function call, formatting is
  guided by the data itself
• authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
• readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point}

%description %{_description}


%package -n python3-tabulate
Summary:        %{summary}

Recommends:     python3-tabulate+widechars

%description -n python3-tabulate %{_description}


%pyproject_extras_subpkg -n python3-tabulate widechars


%prep
%forgesetup


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x widechars benchmark/requirements.txt


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l tabulate

install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p '%{SOURCE1}'


%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_check_import

%pytest --doctest-modules --ignore-glob='benchmark/**' -rs


%files -n python3-tabulate -f %{pyproject_files}
%doc CHANGELOG
%doc README.md

%{_bindir}/tabulate
%{_mandir}/man1/tabulate.1*


%changelog
%autochangelog
