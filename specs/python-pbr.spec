%global pypi_name pbr

# EPEL does not have the necessary testing dependencies
# During the bootstrap the test dependencies are not ready yet
%bcond tests %[%{defined fedora} && %{without bootstrap}]

Name:           python-%{pypi_name}
Version:        7.0.3
Release:        %autorelease
Summary:        Python Build Reasonableness

License:        Apache-2.0
URL:            https://docs.openstack.org/pbr/latest/
Source:         %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  git-core
%if %{with tests}
BuildRequires:  gcc
BuildRequires:  gnupg2
%endif

%global _description %{expand:
PBR is a library that injects some useful and sensible default behaviors
into your setuptools run. It started off life as the chunks of code that
were copied between all of the OpenStack projects. Around the time that
OpenStack hit 18 different projects each with at least 3 active branches, it
seemed like a good time to make that code into a proper reusable library.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        Python Build Reasonableness
Requires:       git-core

%description -n python3-%{pypi_name} %_description


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}


%prep
%autosetup -n %{pypi_name}-%{version} -p1

sed -i '/^coverage.*/d' test-requirements.txt
sed -i '/^six.*/d' test-requirements.txt
sed -i '/^testrepository.*/d' test-requirements.txt
sed -i 's/hacking.*/hacking/' test-requirements.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
mv %{buildroot}%{_bindir}/pbr %{buildroot}%{_bindir}/pbr-3
ln -s ./pbr-3 %{buildroot}%{_bindir}/pbr


%if %{with tests}
%check
# Exclude tests that require networking
%tox -- -- -E 'test_requirement_parsing|test_pep_517_support'
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/pbr
%{_bindir}/pbr-3


%changelog
%autochangelog
