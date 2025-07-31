Name:           python-rich-click
Version:        1.8.9
Release:        %autorelease
Summary:        Format click help output nicely with rich

License:        MIT
URL:            https://github.com/ewels/rich-click
Source:         %{pypi_source rich_click}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
rich-click is a shim around Click that renders help output nicely using Rich.
The intention of rich-click is to provide attractive help output from Click,
formatted with Rich, with minimal customization required.}

%description %_description

%package -n     python3-rich-click
Summary:        %{summary}

%description -n python3-rich-click %_description


%prep
%autosetup -p1 -n rich_click-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l rich_click


%check
%pyproject_check_import
# Revisit running upstream tests when
# https://github.com/ewels/rich-click/pull/247 is merged


%files -n python3-rich-click -f %{pyproject_files}
%_bindir/rich-click
%doc README.md


%changelog
%autochangelog
