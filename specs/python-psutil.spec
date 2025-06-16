# pytest-xdist is not included in RHEL, and on Fedora it depends on psutil
%bcond xdist %[%{defined fedora} && %{undefined bootstrap}]

Name:           python-psutil
Version:        7.0.0
Release:        %autorelease
Summary:        A process and system utilities module for Python

License:        BSD-3-Clause
URL:            https://github.com/giampaolo/psutil
Source:         %{url}/archive/release-%{version}/psutil-%{version}.tar.gz
#
# skip tests that fail in mock chroots
#
Patch:          python-psutil-skip-tests-in-mock.patch
#
# Skip test_emulate_multi_cpu on aarch64 and ppc64le
# Failure reported upstream: https://github.com/giampaolo/psutil/issues/2373
#
Patch:          python-psutil-skip-test_emulate_multi_cpu.patch
#
# Skip test_misc.TestCommonModule.test_debug
# Failure reported upstream: https://github.com/giampaolo/psutil/issues/2374
#
Patch:          python-psutil-skip-test_debug.patch
#
# Skip test_system.TestSensorsAPIs.test_sensors_temperatures
# Failure reported upstream: https://github.com/giampaolo/psutil/issues/2434
#
Patch:          python-psutil-skip-test-sensors-temperatures.patch
#
# Don't treat sockets as paths
# Reported upstream: https://github.com/giampaolo/psutil/pull/2435
#
Patch:          python-psutil-sockets-are-not-paths.patch
#
# Skip test_all on i686
# assert f.flags > 0 fails
# TODO report upstream
#
Patch:          python-psutil-skip-test_all-i686.patch
#
# Fix tests when run with pytest-xdist
# Reported upstream: https://github.com/giampaolo/psutil/pull/2587
Patch:          0001-Ignore-environment-variables-set-by-pytest-xdist.patch

BuildRequires:  gcc
BuildRequires:  sed
BuildRequires:  python%{python3_pkgversion}-devel
# Test dependencies
BuildRequires:  procps-ng
BuildRequires:  python%{python3_pkgversion}-pytest
%if %{with xdist}
BuildRequires:  python%{python3_pkgversion}-pytest-xdist
%endif

%description
psutil is a module providing an interface for retrieving information on all
running processes and system utilization (CPU, memory, disks, network, users) in
a portable way by using Python, implementing many functionalities offered by
command line tools such as: ps, top, df, kill, free, lsof, free, netstat,
ifconfig, nice, ionice, iostat, iotop, uptime, pidof, tty, who, taskset, pmap.


%package -n python%{python3_pkgversion}-psutil
Summary:        %{summary}

%description -n python%{python3_pkgversion}-psutil
psutil is a module providing an interface for retrieving information on all
running processes and system utilization (CPU, memory, disks, network, users) in
a portable way by using Python 3, implementing many functionalities offered by
command line tools such as: ps, top, df, kill, free, lsof, free, netstat,
ifconfig, nice, ionice, iostat, iotop, uptime, pidof, tty, who, taskset, pmap.


%package -n python%{python3_pkgversion}-psutil-tests
Summary:        %{summary}, test suite
Requires:       python%{python3_pkgversion}-psutil%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python%{python3_pkgversion}-psutil-tests
The test suite for psutil.


%prep
%autosetup -p1 -n psutil-release-%{version}

# Remove shebangs
find psutil -name \*.py | while read file; do
  sed -i.orig -e '1{/^#!/d}' $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

# When running tests on Zuul CI, "/" is not mounted, hence the test fail
# We want to run it on other build systems, hence the explicit skip for
# the particular buildhost
%if "%{_buildhost}" == "zuulci-mockbuild.redhat.com"
 sed -i "s/test_disk_partitions/notest_disk_partitions/" psutil/tests/test_system.py
%endif

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files psutil


# Ignore tests when building with flatpak-module-tools to avoid build failures
# when building inside VMs or containers. Flatpaks would usually build this package
# as dependency from stable and already tested branches.
%if ! 0%{?flatpak}
%check
# Setting APPVEYOR to convince the test suite this is a CI.
# That way, some unreliable tests are skipped and some timeouts are extended.
# Previously, this was done by the CI_TESTING variable, but that works no more.
# Alternative is to set GITHUB_ACTIONS but that has undesirable side effects.

# Note: We deliberately bypass the Makefile here to test the installed modules.
GITHUB_ACTIONS=1 %{pytest} %{?with_xdist:-n auto} -k "not emulate_energy_full_0 and not emulate_energy_full_not_avail and not emulate_no_power and not emulate_power_undetermined and not test_scripts" --pyargs psutil.tests

%endif


%files -n python%{python3_pkgversion}-psutil -f %{pyproject_files}
%doc CREDITS HISTORY.rst README.rst
%exclude %{python3_sitearch}/psutil/tests

%files -n python%{python3_pkgversion}-psutil-tests
%{python3_sitearch}/psutil/tests/


%changelog
%autochangelog
