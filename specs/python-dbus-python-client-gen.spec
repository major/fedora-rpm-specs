%global srcname dbus-python-client-gen

Name:           python-%{srcname}
Version:        0.8.4
Release:        %autorelease
Summary:        Python Library for Generating dbus-python Client Code

License:        MPL-2.0
URL:            https://github.com/stratis-storage/dbus-python-client-gen
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dbus_python_client_gen

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
