%global pypi_name docstring-to-markdown
%global module_name docstring_to_markdown

# Use forge macros for pulling from GitHub
%global forgeurl https://github.com/python-lsp/docstring-to-markdown

Name:           python-%{pypi_name}
Version:        0.15
Release:        %{autorelease}
Summary:        On the fly conversion of Python docstrings to Markdown
%forgemeta
License:        LGPL-2.1-or-later
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
On the fly conversion of Python docstrings to markdown

- Python 3.6+
- Recognises reStructuredText and converts multiple of its features to Markdown
- since v0.13 includes initial support for Google-formatted docstrings
}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1
# Disable coverage and linter
sed -i -e '/--[cov|flake]/d' setup.cfg


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{module_name}


%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
