%global srcname dynaconf
%global common_desc \
Dynaconf is a layered configuration system for Python applications with strong \
support for 12-factor applications and extensions for Flask and Django

Name:           %{srcname}
Version:        3.2.13
Release:        %autorelease
Summary:        A dynamic configuration system for Python projects

License:        MIT
URL:            https://github.com/dynaconf/dynaconf
Source0:        %{pypi_source}

BuildArch:      noarch

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-%{srcname}
%{common_desc}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import -e dynaconf.loaders.vault_loader -e dynaconf.vendor.dotenv.ipython -e dynaconf.vendor.ruamel.yaml.cyaml -e dynaconf.vendor.ruamel.yaml.setup

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
# Trailing slash is to ensure setuptools behavior instead of distutils since
# the project can use either and .egg-info could end up being a file or a
# directory.
%{_bindir}/%{srcname}

%changelog
%autochangelog
