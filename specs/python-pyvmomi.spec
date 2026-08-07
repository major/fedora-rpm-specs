%global srcname pyvmomi

%global desc %{expand:
pyVmomi is the Python SDK for the vSphere API that allows you to manage\
ESX, ESXi, and vCenter.}

Name:           python-%{srcname}
Version:        9.1.0.0
Release:        %autorelease
Summary:        vSphere Python SDK
License:        Apache-2.0
URL:            https://github.com/vmware/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Downstream only patch:
# Remove un-needed test deps.  Changed to use pytest.

Patch0:         00-test-requirements.patch
BuildRequires:  dos2unix
BuildRequires:  pytest
BuildRequires:  python3-devel
BuildArch:      noarch

%description %desc

%dnl---------------------------------------------------------------------------
%package -n     python3-%{srcname}
Summary:        vSphere SDK for Python3

%description -n python3-%{srcname} %desc

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%prep
%autosetup -n %{srcname}-%{version} -p1

# fix line endings
find . -name '*' -exec dos2unix -o {} \;

# shebang fix
find . -name '*.py' -exec sed -i 's@/usr/bin/env python@@' {} \;

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pyVmomi pyVim vsanapiutils vsanmgmtObjects


%check
%tox


%changelog
%autochangelog
