%global srcname python

Name:           python-varlink
Version:        32.1.0
Release:        %autorelease
Summary:        Python implementation of Varlink

License:        Apache-2.0
URL:            https://github.com/varlink/%{srcname}
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Install interface files for all packages
Patch:          %{url}/pull/96.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
An python module for Varlink with client and server support.}

%description %_description

%package -n python3-varlink
Summary:       %summary

%description -n python3-varlink %_description

%prep
%autosetup -n %{srcname}-%{version}

# https://github.com/varlink/python/pull/97
sed -i '1{/^#!/d}' varlink/tests/test_*.py

# setuptools in el10 still expects the now-deprecated PEP-0621 license format
%if 0%{?el10}
sed \
  -e 's/^license = .*$/license = { file = "LICENSE.txt"}/' \
  -e '/license-files = /d' \
  -i pyproject.toml
%endif

%generate_buildrequires
# https://github.com/varlink/python/issues/81
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_VARLINK=%{version}
%pyproject_buildrequires test-requirements.txt

%build
# https://github.com/varlink/python/issues/81
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_VARLINK=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l varlink

%check
%pyproject_check_import
%pytest -v

%files -n python3-varlink -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
