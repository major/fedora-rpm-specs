%global _description %{expand:
multiprocess is a fork of multiprocessing, and is developed as part of
pathos: https://github.com/uqfoundation/pathos

multiprocessing is a package for the Python language which supports the
spawning of processes using the API of the standard library’s threading module.
multiprocessing has been distributed in the standard library since python 2.6.

Features:

- Objects can be transferred between processes using pipes or
  multi-producer/multi-consumer queues.
- Objects can be shared between processes using a server process or
  (for simple data) shared memory.
- Equivalents of all the synchronization primitives in threading are
  available.
- A Pool class makes it easy to submit tasks to a pool of worker
  processes.

multiprocess is part of pathos, a python framework for heterogeneous
computing. multiprocess is in active development, so any user feedback,
bug reports, comments, or suggestions are highly appreciated. A list of
issues is located at
https://github.com/uqfoundation/multiprocess/issues, with a legacy list
maintained at https://uqfoundation.github.io/project/pathos/query.}

Name:           python-multiprocess
Version:        0.70.19
Release:        %autorelease
Summary:        Better multiprocessing and multithreading in python

# The entire source is BSD-3-Clause, except py*/doc/html4css1.css, which are
# LicenseRef-Fedora-Public-Domain:
#
#   :Copyright: This stylesheet has been placed in the public domain.
#
# This was added to public-domain-text.txt in fedora-license-data in commit
# 2cd8f00f97288c0d18edac6b68e3862cf6a71fdb:
# https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/211
License:        BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/uqfoundation/multiprocess
Source:         %{url}/archive/%{version}/multiprocess-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  dos2unix

%description %_description

%package -n python3-multiprocess
Summary:        %{summary}
# This subpackage does not contain the public-domain CSS file.
License:        BSD-3-Clause

BuildRequires:  python3-devel
# Required for tests; not automatically generated
BuildRequires:  python3-test
BuildRequires:  python3dist(pox)

%description -n python3-multiprocess %_description

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.

%prep
%autosetup -n multiprocess-%{version} -p1

# Convert line endings
find py%{python3_version}/{doc,examples}/ -type f \
    -exec dos2unix --keepdate '{}' '+'

# Remove shebang
sed -r -i '1{/^#!/d}' py%{python3_version}/multiprocess/tests/__main__.py

# Upstream pretends not to be a pure-Python package to “force python-, abi-,
# and platform-specific naming of bdist_wheel”; this isn’t needed here, and we
# don’t want the RPM package to have to be arched.
sed -r -i 's/^([[:blank:]]*)(distclass=BinaryDistribution,)/\1# \2/' setup.py

# These tests appear to fail because the Python interpreter subprocess called
# through test.support.script_helper.assert_python_ok() does not inherit the
# PYTHONPATH environment variable, so it cannot find the multiprocess package
# in the buildroot.
s='@unittest.skip("Does not respect PYTHONPATH")'
for t in \
    test_spawn_sys_executable_none_allows_import \
    test_global_named_resource_spawn
do
  # The find-then-modify pattern keeps us from discarding mtimes on any sources
  # that do not need modification.
  find . -type f -name '*.py' -exec \
      gawk '/^[[:blank:]]*def '"$t"'\(/ { print FILENAME; nextfile }' '{}' '+' |
    xargs -r -t sed -r -i 's/^([[:blank:]]*)def '"$t"'\(/\1'"$s"'\n&/'
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l multiprocess _multiprocess

%check
# See tox.ini (but don’t try to use %%tox unless we comment out the explicit
# pip install command there):
%{py3_test_envvars} %{python3} \
    py%{python3_version}/multiprocess/tests/__main__.py

%files -n python3-multiprocess -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE COPYING
%doc README.md
%doc py%{python3_version}/examples/
%doc py%{python3_version}/doc/

%changelog
%autochangelog
