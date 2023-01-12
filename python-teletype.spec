%global pypi_name teletype

Name:           python-%{pypi_name}
Version:        1.3.4
Release:        %autorelease
Summary:        High-level cross platform Python tty library

License:        MIT
URL:            https://github.com/jkwill87/teletype
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
teletype is a high-level cross platform tty library compatible with Python
3.7+. It provides a consistent interface between the terminal and cmd.exe by
building on top of terminfo and msvcrt and has no dependencies.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import -e teletype.codes.windows -e teletype.io.windows %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
