# Created by pyp2rpm-3.3.4
%global pypi_name click-spinner
%global commit b27b8d1e2785ce75be1433e579e05193a9b3a782
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        0.1.10
Release:        %autorelease
Summary:        Spinner for Click

License:        MIT
URL:            https://github.com/click-contrib/click-spinner
# We *should* use the latest release + upstream's pull request #39, but versioneer plays with the output of git-archive
# This prevents us cleanly applying upstream's patch, so we have to do the next best thing and pull that commit
# If upstream publishes a new release, we can remove this
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

Provides:       python-blindspin = %{version}-%{release}
Obsoletes:      python-blindspin < 2.0.1

%description
Click Spinner shows the user some progress when a progress bar is
not suitable because you don’t know how much longer it would take.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires: sed

BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Click Spinner shows the user some progress when a progress bar is
not suitable because you don’t know how much longer it would take.

%prep
%autosetup -n %{pypi_name}-%{commit}
# These are bad and should be removed once upstream takes a release
sed -i "s/versioneer.get_version()/'%{version}'/g" setup.py
sed -i "s/description-file/description_file/g" setup.py
sed -i "/from . import _version/d" click_spinner/__init__.py
sed -i "s/_version.get_versions()\['version'\]/'%{version}'/g" click_spinner/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files click_spinner

%check
%pytest -v tests
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
