%global sources_gpg 1
%global sources_gpg_sign 0x7f0f63951535b4d12d3fa55dece58d3984d688d7

%global with_doc 1
%global sname sushy

%global _description %{expand:
Python library to communicate with Redfish based systems 

(http://redfish.dmtf.org)}


Name: python-%{sname}
Version:       5.14.0
Release:       %autorelease
Summary:       Python library to communicate with Redfish based systems
License:       Apache-2.0
URL:           http://launchpad.net/%{sname}/

Source0:       http://tarballs.openstack.org/%{sname}/%{sname}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:     http://tarballs.openstack.org/%{sname}/%{sname}-%{version}.tar.gz.asc
Source102:     https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildRequires: git-core
BuildRequires: python3-devel

BuildArch:     noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires: gpgverify
%endif


%description
%{_description}


%package -n python3-%{sname}
Summary: %{summary}
# Drop the -tests RPM in the era F45
Provides:      python3-%{sname}-tests = %{version}-%{release}
Obsoletes:     python3-%{sname}-tests < 5.13.0-2


%description -n python3-%{sname}
%{_description}


%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary:       %{summary}


%description -n python-%{sname}-doc %_description
%endif


%prep
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{sname}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini

%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency reno:ignore


# Automatic BR generation
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


%check
%tox -e %{default_toxenv}


%install
%pyproject_install

%pyproject_save_files -l %{sname}


%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE ChangeLog


%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif


%changelog
%autochangelog
