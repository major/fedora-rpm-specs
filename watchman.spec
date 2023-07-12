# some Python tests are failing
# The following tests FAILED:
#          40 - CacheTest.future (Child aborted)
#         290 - test_py::tests.integration.test_site_spawn.TestSiteSpawn.test_failingSpawner (Failed)
#         292 - test_py::tests.integration.test_site_spawn.TestSiteSpawn.test_spawner (Failed)
# Errors while running CTest
%bcond_with tests

Name:           watchman
Version:        2021.05.10.00
Release:        %autorelease
Summary:        File alteration monitoring service

%global stripped_version %(echo %{version} | sed -r 's/\\.0([[:digit:]])/.\\1/g')

License:        Apache-2.0
URL:            https://facebook.github.io/%{name}/
Source0:        https://github.com/facebook/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        tmpfiles-%{name}.conf
Patch0:         %{name}-destdir.patch
# https://github.com/facebook/folly/commit/b65ef9f8b5f9b495370b1e651732214cde8abc7d
Patch1:         watchman-2021.05.10.00-folly-new.patch
# Fix build failure on 32bit arch
Patch2:         watchman-2021.05.10.00-wordsize.patch
# Fix build failure with Python 3.12
Patch3:         watchman-fix-for-py3_12.diff
# Fix build failure with fmt 10
Patch4:         watchman-fix-for-fmt10.diff

ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  folly-devel
BuildRequires:  pcre-devel
# for %%{_tmpfilesdir}
BuildRequires:  systemd-rpm-macros
# Optional dependencies
BuildRequires:  valgrind-devel
# Test dependencies
# TODO this shouldn't be needed if tests are not enabled
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel

%description
Watchman exists to watch files and record when they actually change. It can also
trigger actions (such as rebuilding assets) when matching files change.


%package -n python3-py%{name}
Summary:        Python bindings for %{name}
License:        BSD-3-Clause and MIT
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       %{name}%{?_isa} = %{version}-%{release}
# watchman-diag shells out to ps
Requires:       procps-ng

%description -n python3-py%{name}
The python3-py%{name} package contains Python bindings for %{name}.


%prep
%autosetup -p1
# Fix pywatchman version.
sed -i "s|version=\"1.4.1\"|version=\"%{version}\"|" python/setup.py

# testsuite does not seem to compile with gtest 1.11....
# disabling for now on rawhide
%if 0%{?fedora} >= 36
sed -i CMakeLists.txt -e 's|^t_test|#t_test|'
%endif

%build
%cmake \
  -DINSTALL_WATCHMAN_STATE_DIR=ON
%cmake_build


%install
%cmake_install
mkdir -p %{buildroot}%{_tmpfilesdir}
cp -p %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf


%if %{with tests}
%check
%ctest
%endif


%files
%license LICENSE
%doc CODE_OF_CONDUCT.md README.markdown
%attr(02777,root,root) %dir %{_var}/run/%{name}
%{_bindir}/%{name}
%{_tmpfilesdir}/%{name}.conf

%files -n python3-py%{name}
%license python/LICENSE
%{_bindir}/%{name}-*
%{python3_sitearch}/py%{name}
%{python3_sitearch}/py%{name}-%{stripped_version}-py%{python3_version}.egg-info


%changelog
%autochangelog
