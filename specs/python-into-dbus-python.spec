%global srcname into-dbus-python

Name:           python-%{srcname}
Version:        0.8.2
Release:        %autorelease
Summary:        Transformer to dbus-python types

License:        Apache-2.0
URL:            https://github.com/stratis-storage/into-dbus-python
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Facilities for converting an object that inhabits core Python types, e.g.,\
lists, ints, dicts, to an object that inhabits dbus-python types, e.g.,\
dbus.Array, dbus.UInt32, dbus.Dictionary based on a specified dbus signature.

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
%pyproject_save_files -l into_dbus_python

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
