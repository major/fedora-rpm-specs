Name:           gns3-net-converter
Version:        1.3.0
Release:        %autorelease
Summary:        Convert old ini-style GNS3 topologies to v1+ JSON format

# This project is archived by upstream, thus downstream patch
Patch1:         0001-Explicitly-require-setuptools-utils-get_resource.py-.patch

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://pypi.org/project/gns3-net-converter/
Source0:        https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires: python3-configobj

%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple 
workstations to powerful routers. 

GNS3 Converter is designed to convert old ini-style GNS3 topologies (<=0.8.7)
to the newer version v1+ JSON format for use in GNS3 v1+.

%prep
%autosetup 

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l gns3converter


%check
%pyproject_check_import
# Does not have one


%files -f %{pyproject_files}
%doc README.rst ChangeLog
%{_bindir}/gns3-converter


%changelog
%autochangelog
