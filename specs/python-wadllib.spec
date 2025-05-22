Name:           python-wadllib
Version:        1.3.6
Release:        %autorelease
Summary:        Navigate HTTP resources using WADL files as guides

License:        LGPL-3.0-only
URL:            https://launchpad.net/wadllib
Source0:        %{pypi_source wadllib}
BuildArch:      noarch

%global _description %{expand:
A Python library to navigate HTTP resources using WADL files as guides.}

%description %_description

%package -n     python3-wadllib
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(lazr-uri)

# doctests use the cgi module removed from Python 3.13
# https://bugs.launchpad.net/wadllib/+bug/2069619
BuildRequires:  (python3dist(legacy-cgi) if python3 >= 3.13)

%description -n python3-wadllib %_description


%prep
%autosetup -n wadllib-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l wadllib

%check
%pyproject_check_import

%{py3_test_envvars} %{python3} -m unittest src/wadllib/tests/*.py

%files -n python3-wadllib -f %{pyproject_files}
# README is installed in sitelib and used at runtime

%changelog
%autochangelog
