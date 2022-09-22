# tests are enabled by default
%bcond_without tests

%global         srcname     javaproperties
%global         forgeurl    https://github.com/jwodder/javaproperties
Version:        0.8.1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Read & write Java .properties files
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(python-dateutil)
%endif

%global _description %{expand:
Read & write Java .properties files}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
# Environment variables come from upstream's tox.ini:
#   https://github.com/major/javaproperties/blob/master/tox.ini
# Tests fail if they are not present due to time zone shenanigans.
export LC_ALL=en_US.UTF-8
export TZ=EST5EDT,M3.2.0,M11.1.0
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
