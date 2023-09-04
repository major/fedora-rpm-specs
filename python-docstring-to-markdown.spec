%global pypi_name docstring-to-markdown
%global module_name docstring_to_markdown

Name:           python-%{pypi_name}
Version:        0.12
Release:        %{autorelease}
Summary:        On the fly conversion of Python docstrings to markdown

License:        LGPL-2.1-or-later
URL:            https://github.com/python-lsp/docstring-to-markdown
Source:         %{pypi_source %{pypi_name}}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
On the fly conversion of Python docstrings to markdown

- Python 3.6+
- currently can recognise reStructuredText and convert multiple of its
  features to Markdown
- in the future will be able to convert Google docstrings too}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Disable coverage and linter
sed -i -e '/--[cov|flake]/d' setup.cfg


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module_name}


%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*



%changelog
%autochangelog
