%global pypi_name markdown-it-py

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        %autorelease
Summary:        Python port of markdown-it

# SPDX
License:        MIT
URL:            https://github.com/executablebooks/markdown-it-py
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# The plugins extras creates a bootstrap loop
%bcond plugins 1

%global _description %{expand:
Markdown parser done right. Its features:
Follows the CommonMark spec for baseline parsing.
Has configurable syntax: you can add new rules and even replace existing ones.
Pluggable: Adds syntax extensions to extend the parser.
High speed & safe by default
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%pyproject_extras_subpkg -n python3-%{pypi_name} linkify %{?with_plugins:plugins}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Remove unnecessary shebang
sed -i '1{\@^#!/usr/bin/env python@d}' markdown_it/cli/parse.py
# Remove coverage (it resides in testing extra which we want to use)
# Upstream issue to move those to another extra:
# https://github.com/executablebooks/markdown-it-py/issues/195
sed -i '/"coverage",/d' pyproject.toml
sed -i '/"pytest-cov",/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x testing,linkify%{?with_plugins:,plugins}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files markdown_it

%check
%pytest tests/

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE LICENSE.markdown-it
%doc README.md
%{_bindir}/markdown-it


%changelog
%autochangelog
