Name:           python-tomllint
Version:        0.3.6
Release:        %autorelease
Summary:        A simple TOML linter

License:        MIT-0
URL:            https://github.com/wbbradley/tomllint
Source:         %{pypi_source tomllint}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
A TOML Linter. Checks for basic syntactic errors in any TOML file.}

%description %_description

%package -n     python3-tomllint
Summary:        %{summary}

%description -n python3-tomllint %_description


%prep
%autosetup -p1 -n tomllint-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l tomllint


%check
%pyproject_check_import
%pytest

%files -n python3-tomllint -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/tomllint
%{_mandir}/man1/*

%changelog
%autochangelog
