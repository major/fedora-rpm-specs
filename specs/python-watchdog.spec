%global srcname watchdog

%global common_description %{expand: \
Python API and shell utilities to monitor file system events.

Works on 3.7+.}

Name:               python-%{srcname}
Version:            6.0.0
Release:            %autorelease
Summary:            File system events monitoring

License:            Apache-2.0
URL:                https://github.com/gorakhargosh/watchdog
Source0:            %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:              watchdog-6.0.0-relax-deps.patch
BuildArch:          noarch

%description %{common_description}

%package -n python3-%{srcname}
Summary:            %{summary}

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-cov
BuildRequires:      python3-pytest-rerunfailures
BuildRequires:      python3-pytest-timeout
BuildRequires:      python3-PyYAML

%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove all shebangs
find src -name "*.py" | xargs sed -i -e '/^#!\//, 1d'
# Remove +x of the README file
chmod -x README.rst


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# Need more open files for tests
ulimit -n 4096
%tox


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst changelog.rst AUTHORS
%{_bindir}/watchmedo*


%changelog
%autochangelog
