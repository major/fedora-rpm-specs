Name:           python-commented-configparser
Version:        3.0.0
Release:        1%{?dist}
Summary:        A custom ConfigParser class that preserves comments

License:        MIT
URL:            https://github.com/Preocts/commented-configparser
Source:         %{pypi_source commented_configparser}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%global _description %{expand:
A custom ConfigParser class that preserves comments and most formatting when
writing loaded config out.

This library gives you a custom class of the standard library's
configparser.ConfigParser which will preserve the comments of a loaded config
file when writing that file back out.}

%description %_description

%package -n     python3-commented-configparser
Summary:        %{summary}

%description -n python3-commented-configparser %_description


%prep
%autosetup -p1 -n commented_configparser-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l commentedconfigparser


%check
%pyproject_check_import
%pytest

%files -n python3-commented-configparser -f %{pyproject_files}
%doc README.md

%changelog
* Thu Mar 19 2026 Shawn W Dunn <sfalken@opensuse.org> - 3.0.0-1
- Inital Packaging

