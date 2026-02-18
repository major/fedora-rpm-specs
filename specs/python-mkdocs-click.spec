Name:           python-mkdocs-click
Version:        0.9.0
Release:        %autorelease
Summary:        MkDocs extension to generate documentation for Click CLIs

License:        Apache-2.0
URL:            https://pypi.org/project/mkdocs-click/
Source:         %{pypi_source mkdocs_click}

# Fix compatibility with click 8.3.0+
# Sent upstream
Patch: https://github.com/mkdocs/mkdocs-click/pull/95.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides an MkDocs extension to generate documentation for Click
command line applications.}

%description %_description

%package -n     python3-mkdocs-click
Summary:        %{summary}

%description -n python3-mkdocs-click %_description

%prep
%autosetup -p1 -n mkdocs_click-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_click

%check
%pytest

%files -n python3-mkdocs-click -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
