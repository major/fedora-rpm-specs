%global srcname robot-detection

Name:           python-%{srcname}
Version:        0.4
%global gh_ver %{version}.0
Release:        %autorelease
Summary:        Library for detecting bot HTTP UA headers
License:        GPLv3+
URL:            https://github.com/rory/robot-detection
# PyPI source does not have tests and license text
# Source0:        %%{pypi_source %%{srcname}}
Source0:        %{url}/archive/v%{gh_ver}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description %{expand:
robot_detection is a python module to detect if a given HTTP User Agent is a web
crawler. It uses the list of registered robots from http://www.robotstxt.org:
[Robots Database](http://www.robotstxt.org/db.html).}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{gh_ver}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files robot_detection


%check
%tox


%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENCE
%doc README.md


%changelog
%autochangelog
