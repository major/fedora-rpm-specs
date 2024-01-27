%global pypi_name vkbasalt-cli
%global module_name vkbasalt

%global _description %{expand:
vkbasalt-cli is a CLI utility and library in conjunction with vkBasalt.
This makes generating configuration files or running vkBasalt with
games easier. This is mainly convenient in environments where
integrating vkBasalt is wishful, for example a GUI application.
Integrating vkbasalt-cli allows a front-end to easily generate and use
specific configurations on the fly, without asking the user to manually
write a configuration file.}

Name:           python-%{pypi_name}
Version:        3.1.1.post2
Release:        %{autorelease}
Summary:        Command line interface for vkBasalt
BuildArch:      noarch

# Code in vkbasalt/lib.py (library) is licensed under lgpl-3.0-only (see COPYING.LGPLv3)
# Code in vkbasalt/cli.py (main program) is licensed under gpl-3.0-only (see COPYING.GPLv3)
License:        LGPL-3.0-only AND GPL-3.0-only
URL:            https://gitlab.com/TheEvilSkeleton/vkbasalt-cli
Source0:        %{pypi_source %{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n %{name} %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
Provides:       vkbasalt-cli = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       vkBasalt
%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module_name}


%check
# Package does not provide any tests
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{module_name}


%changelog
%autochangelog
