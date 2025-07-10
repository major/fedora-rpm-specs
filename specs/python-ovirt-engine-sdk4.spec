Name: python-ovirt-engine-sdk4
Summary: Python SDK for version 4 of the oVirt Engine API
Version: 4.6.2
%global major_version %(v=%{version}; echo ${v:0:3})
Release: 9%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/oVirt/python-ovirt-engine-sdk4
Source: https://github.com/oVirt/python-ovirt-engine-sdk4/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: libxml2-devel
BuildRequires: python3-devel

%global _description\
This package contains the Python SDK for version 4 of the oVirt Engine\
API.

%description %_description

%package -n python3-ovirt-engine-sdk4
Summary: %summary

%description -n python3-ovirt-engine-sdk4 %_description

%prep
%autosetup
%py3_shebang_fix examples
find examples -type f -print0 | xargs -0 chmod 0644
GENERATED_FILES="
 lib/ovirtsdk4/version.py
 setup.py
 PKG-INFO
 lib/ovirt_engine_sdk_python.egg-info/PKG-INFO
 python-ovirt-engine-sdk4.spec
"

for gen_file in ${GENERATED_FILES} ; do
  sed \
    -e "s|@RPM_VERSION@|%{version}|g" \
    -e "s|@RPM_RELEASE@|%{release}|g" \
    -e "s|@PACKAGE_NAME@|%{name}|g" \
    -e "s|@PACKAGE_VERSION@|%{package_version}|g" \
    < ${gen_file}.in > ${gen_file}
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l ovirtsdk4

%check
%pyproject_check_import

%files -n python3-ovirt-engine-sdk4 -f %{pyproject_files}
%doc README.adoc
%doc examples

%changelog
%autochangelog
