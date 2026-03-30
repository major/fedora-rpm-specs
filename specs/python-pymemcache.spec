# Created by pyp2rpm-1.0.1
%global pypi_name pymemcache

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        %autorelease
Summary:        A comprehensive, fast, pure Python memcached client

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/Pinterest/pymemcache
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0001:      0001-Skip-unit-tests-resolving-domain-names.patch
Patch0002:      0002-Unpin-test-requirements-packages.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  git-core

%global _description %{expand:
pymemcache supports the following features:

* Complete implementation of the memcached text protocol.
* Configurable timeouts for socket connect and send/recv calls.
* Access to the "noreply" flag, which can significantly increase the speed of
  writes.
* Flexible, simple approach to serialization and deserialization.
* The (optional) ability to treat network and memcached errors as cache misses.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        A comprehensive, fast, pure Python memcached client



%description -n python3-%{pypi_name}
%_description


%prep
%autosetup -n %{pypi_name}-%{version} -S git


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l pymemcache


%check
py.test-3 ./pymemcache/test/


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst LICENSE.txt


%changelog
%autochangelog
