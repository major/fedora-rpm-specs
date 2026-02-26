%global pypi_name port-for
%global name_with_underscore port_for

Name:           python-%{pypi_name}
Version:        0.7.4
Release:        %autorelease
Summary:        Utility that helps with local TCP ports management

License:        MIT
URL:            https://github.com/kmike/port-for/
Source0:        https://github.com/kmike/port-for/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)

%description
It can find an unused TCP local host port and remember the association.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
It can find an unused TCP local host port and remember the association.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name_with_underscore}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{_bindir}/%{pypi_name}

%changelog
%autochangelog
