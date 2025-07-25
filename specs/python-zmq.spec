# Allows additional import checks (zmq.green) and tests
%bcond gevent 1

Name:           python-zmq
Version:        27.0.0
Release:        %autorelease
Summary:        Python bindings for zeromq

# As noted in https://github.com/zeromq/pyzmq/blob/v26.2.0/RELICENSE/README.md:
#   pyzmq starting with 26.0.0 is fully licensed under the 3-clause Modified
#   BSD License. A small part of the core (Cython backend only) was previously
#   licensed under LGPLv3 for historical reasons. Permission has been granted
#   by the contributors of the vast majority of those components to relicense
#   under MPLv2 or BSD. This backend has been completely replaced in pyzmq 26,
#   and the new implementation is fully licensed under BSD-3-Clause, so pyzmq
#   is now under a single license.
# Nevertheless:
#   - zmq/ssh/forward.py, which is derived from a Paramiko demo, is
#     LGPL-2.1-or-later
#   - zmq/eventloop/zmqstream.py is Apache-2.0
# See also the “Inherited licenses in pyzmq” section in CONTRIBUTING.md.
License:        %{shrink:
                BSD-3-Clause AND
                LGPL-2.1-or-later AND
                Apache-2.0
                }
# Additionally, the following do not affect the license of the binary RPMs:
#   - tools/run_with_env.cmd is CC0-1.0; for distribution in the source RPM, it
#     is covered by “Existing uses of CC0-1.0 on code files in Fedora packages
#     prior to 2022-08-01, and subsequent upstream versions of those files in
#     those packages, continue to be allowed. We encourage Fedora package
#     maintainers to ask upstreams to relicense such files.”
#     https://gitlab.com/fedora/legal/fedora-license-data/-/issues/91#note_1151947383
#   - examples/device/device.py and examples/win32-interrupt/display.py are
#     LicenseRef-Fedora-Public-Domain; approved in “Review of
#     python-zmq examples dedicated to the public domain,”
#     https://gitlab.com/fedora/legal/fedora-license-data/-/issues/616; see
#     https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/716
SourceLicense:  %{shrink:
                %{license} AND
                CC0-1.0 AND
                LicenseRef-Fedora-Public-Domain
                }
URL:            https://zeromq.org/languages/python/
%global forgeurl https://github.com/zeromq/pyzmq
Source:         %{forgeurl}/archive/v%{version}/pyzmq-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(generate_buildrequires): test-requirements-filtered.txt
# https://scikit-build-core.readthedocs.io/en/latest/configuration.html
BuildOption(build):     %{shrink:
                        -Ccmake.define.PYZMQ_LIBZMQ_RPATH:BOOL=OFF
                        -Ccmake.define.PYZMQ_NO_BUNDLE=ON
                        -Clogging.level=INFO
                        -Ccmake.verbose=true
                        -Ccmake.build-type="RelWithDebInfo"}
BuildOption(install):   -L zmq
# - The cffi backend does not apply when we build with Cython.
BuildOption(check):     %{shrink:
                        -e 'zmq.backend.cffi*'
                        %{?!with_gevent:-e 'zmq.green*'}
                        }

BuildRequires:  gcc
# This package contains no C++ code, but there are some checks in
# CMakeLists.txt that need a C++ compiler.
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libzmq)

# Add some manual test dependencies that aren’t in test-requirements.txt, but
# which enable additional tests.
#
# Tests in zmq/tests/mypy.py require mypy, but see:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# Some tests in zmq/tests/test_context.py and zmq/tests/test_socket.py require
# pyczmq, which is not packaged and has not been updated in a decade.
#
# Enable more tests in zmq/tests/test_message.py:
BuildRequires:  %{py3_dist numpy}
%if %{with gevent}
BuildRequires:  %{py3_dist gevent}
%endif

%global common_description %{expand:
This package contains Python bindings for ZeroMQ. ØMQ is a lightweight and fast
messaging implementation.}

%description %{common_description}


%package -n python3-pyzmq
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides    python3-zmq

%if %[ %{defined fc42} || %{defined fc43} || %{defined fc44} ]
# Beginning with Fedora 42, the binary packages are renamed from
# python3-zmq/python3-zmq-tests to python3-pyzmq/python3-pyzmq-tests to match
# the canonical package name. Ideally, the source package would also be called
# python-pyzmq, but it’s not worth going through the package renaming process
# for this. The Obsoletes/Conflicts provide a clean upgrade path, and can be
# removed after Fedora 44 end-of-life.
Obsoletes:      python3-zmq < 25.1.1-29
Conflicts:      python3-zmq < 25.1.1-29
Obsoletes:      python3-zmq-tests < 25.1.1-29
Conflicts:      python3-zmq-tests < 25.1.1-29
# Beginning with Fedora 42 and python-zmq 26, the tests are moved out of the
# zmq package, so we no longer package them. The Obsoletes/Conflicts provide a
# clean upgrade path, and can be removed after Fedora 44 end-of-life.
Obsoletes:      python3-pyzmq-tests < 26.2.0-1
Conflicts:      python3-pyzmq-tests < 26.2.0-1
%endif

%description -n python3-pyzmq %{common_description}


%prep -a
# Remove any Cython-generated .c files in order to regenerate them:
find . -type f -exec grep -FrinIl 'Generated by Cython' '{}' '+' |
  xargs -r -t rm -v

# Remove shebangs from non-script sources. The find-then-modify pattern
# preserves mtimes on sources that did not need to be modified.
find 'src' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# - pymongo is used only in examples/mongodb/, and we don’t run examples
sed -r \
    -e 's/^(black|codecov|coverage|flake8|mypy|pytest-cov)\b/# &/' \
    -e 's/^(pymongo)\b/# &/' \
    test-requirements.txt | tee test-requirements-filtered.txt


%check -p
# to avoid partially initialized zmq module from cwd
mkdir -p _empty
cd _empty
ln -s ../tests/ ../pytest.ini ./


%check -a
# With Python 3.14, in test_process_teardown, while spawning the multiprocess
# forkserver child:
#   ModuleNotFoundError: No module named 'tests'
# This doesn’t really make sense to report upstream because the problem doesn’t
# happen when running tests against an editable install in a virtualenv as they
# do. Adding the working directory to PYTHONPATH is a workaround.
export PYTHONPATH="%{buildroot}%{python3_sitearch}:${PWD}"

%ifarch %{power64}
# Several of the green/gevent tests fail with segmentation faults, so we
# disable all of them for simplicity.
#
# BUG: test_green_device crashes with Python 3.12 on ppc64le
# https://github.com/zeromq/pyzmq/issues/1880
k="${k-}${k+ and }not Green"
%endif

%pytest -k "${k-}" -v -rs tests/


%files -n python3-pyzmq -f %{pyproject_files}
%license LICENSE.md licenses/
%doc README.md


%changelog
%autochangelog
