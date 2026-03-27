# Created by pyp2rpm-3.2.3
%global pypi_name croniter

Name:           python-%{pypi_name}
Version:        6.2.2
Release:        %autorelease
Summary:        Iteration for datetime object with cron like format

License:        MIT
URL:            https://github.com/kiorky/croniter
Source0:        %{pypi_source}
# Maintainers, please upstream
#Patch0:         python-croniter-rm-python-mock-usage.diff
BuildArch:      noarch

BuildRequires:  python3-pytz


%global _description %{expand:
croniter provides iteration for the datetime object with a cron like format.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
Requires:       python3-dateutil
%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t

# Remove reundant script header to avoid rpmlint warnings
find -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%pyproject_check_import croniter
# There is a tox but no tests
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
