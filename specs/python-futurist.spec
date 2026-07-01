%global sources_gpg 1
%global sources_gpg_sign 0x30566c450e41d7c91e442dfb231f942f608ddeff
%global with_doc 1
%global pypi_name futurist

%global common_desc %{expand:
Code from the future, delivered to you in the now.}

Name:           python-%{pypi_name}
Version:        3.4.0
Release:        %autorelease
Summary:        Useful additions to futures, from the future

License:        Apache-2.0
URL:            http://docs.openstack.org/developer/futurist
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  git-core

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif


%package -n python3-%{pypi_name}
Summary:        Useful additions to futures, from the future


%description -n python3-%{pypi_name}
%{common_desc}


%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        Useful additions to futures, from the future - documentation


%description -n python-%{pypi_name}-doc
%{common_desc}
%endif


%description
========
Futurist
========

%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency reno:ignore

# Eventlet is being removed from openstack, we do not need to testit.
%pyproject_patch_dependency eventlet:ignore



%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires -t -e %{default_toxenv},docs
%else
%pyproject_buildrequires -t -e %{default_toxenv}
%endif


%build
%pyproject_wheel


%if 0%{?with_doc}
# generate html docs
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import %{pypi_name} -e futurist.tests.test_executors -e futurist.tests.test_periodics -e futurist.tests.test_waiters
# to hard while waiting for evently to really go, we do not need to test
# it though
#%%tox -e %%{default_toxenv}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst ChangeLog


%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
