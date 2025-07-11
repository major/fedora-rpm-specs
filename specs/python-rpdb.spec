%global srcname rpdb

Name: python-%{srcname}
Version: 0.2.0
Release: %autorelease
BuildArch: noarch

Summary: A wrapper around pdb allowing remote debugging
License: BSD-2-Clause
# Upstream failed to tag the 2.0 release, see https://github.com/tamentis/rpdb/issues/41
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

BuildRequires: python3-devel

%global _description %{expand:
A wrapper around pdb allowing remote debugging via netcat or telnet.
This is especially useful in a Tomcat/Jython environment where little
debugging tools are available.}

%description %{_description}


%package -n python3-%{srcname}
Summary: %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files rpdb


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md


%changelog
%autochangelog
