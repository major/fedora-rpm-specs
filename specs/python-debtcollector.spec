%global sources_gpg 1
%global sources_gpg_sign 0x2ef3fe0ec2b075ab7458b5f8b702b20b13df2318

%global pypi_name debtcollector
%global with_doc 1
%global common_desc %{expand:
It is a collection of functions/decorators which is used to signal a user when
*  a method (static method, class method, or regular instance method) or a class
    or function is going to be removed at some point in the future.
* to move a instance method/property/class from an existing one to a new one
* a keyword is renamed
* further customizing the emitted messages}

Name:        python-%{pypi_name}
Version:     3.0.0
Release:     %autorelease
Summary:     A collection of Python deprecation patterns and strategies

License:     Apache-2.0
URL:         https://pypi.python.org/pypi/%{pypi_name}
Source0:     https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildRequires: python3-devel

BuildArch:   noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires: git-core

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:     A collection of Python deprecation patterns and strategies


%description -n python3-%{pypi_name}
%{common_desc}


%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for the debtcollector module


%description -n python-%{pypi_name}-doc
Documentation for the debtcollector module
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^doc8[[:space:]]*[!><=]/d" \
    -e "/^pre-commit[[:space:]]*[!><=]/d" \
    test-requirements.txt


%generate_buildrequires
%if 0%{?with_doc}
%pyproject_buildrequires -t -e %{default_toxenv},docs
%else
%pyproject_buildrequires -t -e %{default_toxenv}
%endif


%build
%pyproject_wheel


%install
%pyproject_install


%if 0%{?with_doc}
# doc
PYTHONPATH="%{buildroot}/%{python3_sitelib}"
%tox -e docs
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif


%check
%tox

%files -n python3-%{pypi_name}
%doc README.rst CONTRIBUTING.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.dist-info
%exclude %{python3_sitelib}/%{pypi_name}/tests


%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif


%changelog
%autochangelog
