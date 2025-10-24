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
# Don't treat sockets as paths
# Reported upstream: https://github.com/giampaolo/psutil/pull/2435
#
Patch:          python-psutil-sockets-are-not-paths.patch
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
Recommends:     python%{python3_pkgversion}-pytest
Requires:       procps-ng

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

# Don't run and install tests for unpackaged scripts
rm psutil/tests/test_scripts.py


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
# Deselect tests that fail in mock chroots
k="${k-}${k+ and }not (TestProcessAgainstStatus and test_cpu_affinity and not eligible_cpus)"
k="${k-}${k+ and }not (TestSystemVirtualMemory and test_used)"
k="${k-}${k+ and }not (test_process_all and test_all)"
k="${k-}${k+ and }not (test_system and test_cpu_freq)"
k="${k-}${k+ and }not TestSystemCPUCountCores"
k="${k-}${k+ and }not TestSystemCPUStats"
k="${k-}${k+ and }not TestSystemNetIfAddrs"
k="${k-}${k+ and }not test_against_nproc"
k="${k-}${k+ and }not test_against_sysdev_cpu_"
k="${k-}${k+ and }not test_disk_partitions_mocked"
k="${k-}${k+ and }not test_emulate_use_cpuinfo"
k="${k-}${k+ and }not test_emulate_use_second_file"
k="${k-}${k+ and }not test_exe_mocked"

# Failure reported upstream: https://github.com/giampaolo/psutil/issues/2374
k="${k-}${k+ and }not test_debug"

# Flaky failure reported upstream: https://github.com/giampaolo/psutil/issues/2434
k="${k-}${k+ and }not (test_system and test_sensors_temperatures and not fahreneit)"

# Skip test_emulate_multi_cpu on aarch64, ppc64le, riscv64
# Failure reported upstream: https://github.com/giampaolo/psutil/issues/2373
%ifarch aarch64 ppc64le riscv64
k="${k-}${k+ and }not test_emulate_multi_cpu"
%endif

# The following options were present in the specfile without explanation
# when the pytest -k option was expanded across multiple lines:
k="${k-}${k+ and }not emulate_energy_full_0"
k="${k-}${k+ and }not emulate_energy_full_not_avail"
k="${k-}${k+ and }not emulate_no_power"
k="${k-}${k+ and }not emulate_power_undetermined"

# Setting GITHUB_ACTIONS to convince the test suite this is a CI.
# That way, some unreliable tests are skipped and some timeouts are extended.

# Note: We deliberately bypass the Makefile here to test the installed modules.
GITHUB_ACTIONS=1 %{pytest} %{?with_xdist:-n auto} "${k:+-k $k}" --pyargs psutil.tests

%endif


%files -n python%{python3_pkgversion}-psutil -f %{pyproject_files}
%doc CREDITS HISTORY.rst README.rst
%exclude %{python3_sitearch}/psutil/tests

%files -n python%{python3_pkgversion}-psutil-tests
%{python3_sitearch}/psutil/tests/


%changelog
%autochangelog
