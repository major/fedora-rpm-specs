# Tests are disabled by default. 😞
# Enable if https://bugzilla.redhat.com/show_bug.cgi?id=1949502 /
# https://github.com/bitprophet/pytest-relaxed/issues/12 is resolved:
%bcond_with     tests

%global         srcname     fabric
%global         forgeurl    https://github.com/fabric/%{srcname}
Version:        3.0.0
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        High level SSH command execution

License:        BSD
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel


%if %{with tests}
# Extra pytest (a superset of extra testing)
BuildRequires:  python3dist(pytest)
# Missing from setup.py (only in requirements-dev.txt), but still needed for
# testing:
BuildRequires:  python3dist(pytest-relaxed)
%endif

BuildRequires:  help2man

%global _description %{expand:
Fabric is a high level Python (2.7, 3.4+) library designed to execute shell
commands remotely over SSH, yielding useful Python objects in return. It builds
on top of Invoke (subprocess command execution and command-line features) and
Paramiko (SSH protocol implementation), extending their APIs to complement one
another and provide additional functionality.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1

# Allow a slightly older invoke version.
sed -i 's/invoke>=2.0/invoke>=1.7/' setup.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fabric


%check
%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/fab


%changelog
%autochangelog
