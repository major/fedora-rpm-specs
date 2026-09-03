%global srcname fsspec-xrootd

Name:		python-%{srcname}
Version:	0.5.5
Release:	1%{?dist}
Summary:	An XRootD implementation for fsspec
License:	BSD-3-Clause
URL:		https://github.com/scikit-hep/%{srcname}
Source0:	%{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch

#		For testing
BuildRequires:	xrootd-server

%description
To allow fsspec to use XRootD accessible storage systems. Install
fsspec-xrootd alongside fsspec and have easy access to files stored on
XRootD servers. Once installed, fsspec will be able to work with URLs
with the 'root' protocol.

%package -n python3-%{srcname}
Summary:	%{summary}
%py_provides	python3-%{srcname}

%description -n python3-%{srcname}
To allow fsspec to use XRootD accessible storage systems. Install
fsspec-xrootd alongside fsspec and have easy access to files stored on
XRootD servers. Once installed, fsspec will be able to work with URLs
with the 'root' protocol.

%prep
%setup -q -n %{srcname}-%{version}

%if %{?rhel}%{!?rhel:0} == 10
# setuptools versions < 77 don't support PEP 639
# convert license key in pyproject.toml to old format for older versions
sed -e 's!\(setuptools\)>=77!\1!' \
    -e 's!^\(license\)\s*=\s*\(.*\)$!\1 = { text = \2 }!' \
    -e '/license-files/d' -i pyproject.toml
%endif

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_FSSPEC_XROOTD=%{version}
%pyproject_buildrequires -x test

%build
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_FSSPEC_XROOTD=%{version}
%pyproject_wheel

%install
%pyproject_install

%check
# The test_broken_server test checks that trying to contact a
# non-existing server eventually times out. The default timeout is
# very long though, so the check just sits doing nothing for a long
# time.
# The test_touch_modified relies on the filesystem keeping track of
# file access times. The filesystem in a mock chroot is mounted with
# the relatime option which is incompatible with the expectations of
# the check.
%pytest -k 'not test_touch_modified and not test_broken_server'

%files -n python3-%{srcname}
%{python3_sitelib}/fsspec_xrootd/
%{python3_sitelib}/fsspec_xrootd-%{version}.dist-info/
%license LICENSE
%doc README.md

%changelog
* Mon Aug 31 2026 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.5.5-1
- Initial package
