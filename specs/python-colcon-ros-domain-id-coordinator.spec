%global srcname colcon-ros-domain-id-coordinator

Name:           python-%{srcname}
Version:        0.2.1
Release:        2%{?dist}
Summary:        Extension for colcon to coordinate different DDS domain IDs

License:        Apache-2.0
URL:            https://github.com/colcon/colcon-ros-domain-id-coordinator
Source0:        https://github.com/colcon/colcon-ros-domain-id-coordinator/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
An extension for colcon-core to coordinate different DDS domain IDs for
concurrently running tasks.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l colcon_ros_domain_id_coordinator


%check
# The package has no non-linter tests right now
%pyproject_check_import


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Scott K Logan <logans@cottsay.net> - 0.2.0-1
- Initial package (rhbz#2317437)
