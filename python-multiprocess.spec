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
Version:        0.70.13
Release:        %autorelease
Summary:        Better multiprocessing and multithreading in python

License:        BSD
URL:            https://pypi.org/pypi/multiprocess
Source0:        %{pypi_source multiprocess %{version} tar.gz}
BuildArch:      noarch

%description %_description

%package -n python3-multiprocess
Summary:        %{summary}
BuildRequires:  python3-devel
# required for tests
BuildRequires:  python-unversioned-command
# Not automatically generated
BuildRequires:  python3-test

%description -n python3-multiprocess %_description

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.

%prep
%autosetup -n multiprocess-%{version}
rm -rf multiprocess.egg-info

# Fix wrong end of file encoding
find py%{python3_version}/doc/ -name "*" -exec sed -i 's/\r$//' '{}' \;
find py%{python3_version}/examples/ -name "*" -exec sed -i 's/\r$//' '{}' \;

# remove shebang
sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' py%{python3_version}/multiprocess/tests/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files multiprocess _multiprocess

%check
export PYTHONPATH="$RPM_BUILD_ROOT/%{python3_sitearch}/:$RPM_BUILD_ROOT/%{python3_sitelib}/:."
pushd py%{python3_version}
# https://github.com/uqfoundation/multiprocess/blob/master/.travis.yml#L67
for test in multiprocess/tests/__init__.py; do echo $test ; %{__python3} $test > /dev/null; done

# These do not run properly in the build root: it cannot find the installed version even after PYTHONPATH is set
#for test in multiprocess/tests/*.py; do if [[ $test != *"__"* && $test != *"mp_"*  ]]; then echo $test ; %%{__python3} $test > /dev/null; fi; done
popd


%files -n python3-multiprocess -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE COPYING
%doc README.md
%doc py%{python3_version}/examples/
%doc py%{python3_version}/doc/

%changelog
%autochangelog
