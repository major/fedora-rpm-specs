Name:           python-omsdk
Version:        1.2.518
Release:        %autorelease
Summary:        Dell EMC OpenManage Python SDK 

License:        Apache-2.0
URL:            https://github.com/dell/omsdk
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Patch0:         setup-omsdk.py.patch

# https://github.com/dell/omsdk/pull/45
Patch1:         00_remove_future.patch 

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed
BuildRequires:  pyproject-rpm-macros

# Untracked upstream dependency (https://github.com/dell/omsdk/issues/36)
BuildRequires:  python%{python3_pkgversion}dist(pywinrm)

%global _description %{expand:
DellEMC OpenManage Python SDK (OMSDK) is a python library that helps 
developers and customers to automate the lifecycle management of 
PowerEdge Servers.
OMSDK module leverages the iDRAC's REST APIs based on DMTF Redfish standards 
as well as WS-Man and SNMP protocols for configuration, deployment, updates 
and monitoring of PowerEdge Servers.
}


%description %_description


%package -n python3-omsdk
Summary:        %{summary}

# Whilst omsdk and omdrivers are seperate modules, they have circular dependencies which prevent them being distributed seperately
# If you install one of them from PyPi you get a wheel containing both.
%py_provides python3-omsdk
%py_provides python3-omdrivers

# Untracked upstream dependency (https://github.com/dell/omsdk/issues/36)
Requires:       python%{python3_pkgversion}dist(pywinrm)


%description -n python3-omsdk %_description


%prep
%autosetup -p1 -n omsdk-%{version}

# Upstream provides seperate setup.py files for omdrivers and omsdk, but we only need one of them
mv setup-omsdk.py setup.py

# ipaddress was merged into Python 3.3, so it does not need to be a dependancy
sed -i '/ipaddress>=0/d' setup.py

# Wheel version is loaded from file
echo "%{version}" > _version.txt

# Upstream has shebangs on non-executable files
find omsdk -type f -exec sed -i '/\/usr\/bin\/env python3/d' {} +
find omdrivers -type f -exec sed -i '/\/usr\/bin\/env python3/d' {} +

# Fix line endings without dos2unix
sed -i 's/\r$//' README.md


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files omsdk omdrivers


%check
# omsdk.listener.sdktrapreceiver tries to start listening as soon as it is imported
# omsdk.sdksnmptrap depends on outdated SNMP support (https://github.com/dell/omsdk/issues/37)
%pyproject_check_import -e 'omsdk.listener.sdktrapreceiver' -e 'omsdk.sdksnmptrap'


%files -n python3-omsdk -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
%autochangelog
