Name:           python-rich-rst
Version:        1.3.2
Release:        %autorelease
Summary:        A beautiful reStructuredText renderer for rich
License:        MIT
URL:            https://wasi-master.github.io/rich-rst
Source:         %{pypi_source rich_rst}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%global _description %{expand:
A beautiful reStructuredText renderer for rich.}

%description %_description

%package -n     python3-rich-rst
Summary:        %{summary}

%description -n python3-rich-rst %_description

%prep
%autosetup -p1 -n rich_rst-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l rich_rst


%check
%pyproject_check_import
%pytest


%files -n python3-rich-rst -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
