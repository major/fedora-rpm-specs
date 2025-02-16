%global common_description %{expand:
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python.  Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.  A web spider that wants to fetch lots of
pages in parallel, a web server that needs to juggle lots of downloads and
websocket connections at the same time, a process supervisor monitoring
multiple subprocesses... that sort of thing.  Compared to other libraries, Trio
attempts to distinguish itself with an obsessive focus on usability and
correctness.  Concurrency is complicated; we try to make it easy to get things
right.}


Name:           python-trio
Version:        0.29.0
Release:        %autorelease
Summary:        A friendly Python library for async concurrency and I/O
License:        Apache-2.0 OR MIT
URL:            https://github.com/python-trio/trio
Source:         %pypi_source trio

# Add xfail to test_ki_protection_doesnt_leave_cyclic_garbage on Python 3.14
# https://github.com/python-trio/trio/pull/3211/commits/02b338ebab972ffe16bca14bdd5823db9ab61631
#
# From:
#
# Add xfail for issue 3209, and start testing Python 3.14
# https://github.com/python-trio/trio/pull/3211
#
# See:
#
# Python 3.14: test_ki_protection_doesnt_leave_cyclic_garbage fails
# https://github.com/python-trio/trio/issues/3209
#
# The root cause appears to be:
#
# [3.14] change in behaviour in gc.get_referrers(some_local)
# https://github.com/python/cpython/issues/125603
#
# Fixes:
#
# python-trio fails to build with Python 3.14:
# test_ki_protection_doesnt_leave_cyclic_garbage: Left contains one more item:
# <coroutine object test_ki_protection_doesnt_leave_cyclic_garbage at
# 0x7fbaa2f162c0>
# https://bugzilla.redhat.com/show_bug.cgi?id=2345516
Patch:          %{url}/pull/3211/commits/02b338ebab972ffe16bca14bdd5823db9ab61631.patch

BuildArch:      noarch


%description %{common_description}


%package -n python3-trio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-trio %{common_description}


%prep
%autosetup -p 1 -n trio-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l trio


%check
# https://github.com/python-trio/trio/issues/2863
# https://docs.pytest.org/en/stable/explanation/goodpractices.html#tests-as-part-of-application-code
%pytest \
%if %{defined el10}
    --import-mode=append \
%endif
    --pyargs trio \
    --verbose \
    --skip-optional-imports


%files -n python3-trio -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
