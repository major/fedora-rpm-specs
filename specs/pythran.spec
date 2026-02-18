Name:           pythran
Version:        0.18.1
Release:        %autorelease
Summary:        Ahead of Time Python compiler for numeric kernels

# pythran is BSD-3-Clause
# pythran/graph.py has bits of networkx, also BSD-3-Clause
# pythran/pythonic/patch/complex is MIT OR NCSA
License:        BSD-3-Clause AND (MIT OR NCSA)

# see pythran/pythonic/patch/README.rst
# The version is probably somewhat around 3
Provides:       bundled(libcxx) = 3

# see pythran/graph.py
# Only bundles one function from networkx
Provides:       bundled(python3dist(networkx)) = 2.6.1


%py_provides    python3-%{name}

URL:            https://github.com/serge-sans-paille/pythran
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Compatibility with 32 bits numpy
# Resolved upstream
Patch: https://github.com/serge-sans-paille/pythran/pull/2375.patch

# Compatibility with ply post-3.11 version
# Resolved upstream
Patch: https://github.com/serge-sans-paille/pythran/pull/2402.patch

# Fix directory structure for pytest discovery
# Sent upstream
Patch: https://github.com/serge-sans-paille/pythran/pull/2403.patch

# Fix 32 bit type conversion failures
# Sent upstream
Patch: https://github.com/serge-sans-paille/pythran/pull/2404.patch

# there is no actual arched content
# yet we want to test on all architectures
# and we also might need to skip some
%global debug_package %{nil}

BuildRequires:  make
BuildRequires:  boost-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  xsimd-devel >= 8

# For docs
BuildRequires:  pandoc

# For tests
BuildRequires:  /usr/bin/python
# this is used for supporting -n auto in %%pytest
BuildRequires:  python3-pytest-xdist

# This is a package that compiles code, it runtime requires devel packages
Requires:       flexiblas-devel
Requires:       gcc-c++
Requires:       python3-devel
Requires:       boost-devel
Requires:       xsimd-devel >= 8

%description
Pythran is an ahead of time compiler for a subset of the Python language, with
a focus on scientific computing. It takes a Python module annotated with a few
interface description and turns it into a native Python module with the same
interface, but (hopefully) faster. It is meant to efficiently compile
scientific programs, and takes advantage of multi-cores and SIMD
instruction units.


%prep
%autosetup -p1 -n %{name}-%{version}
find -name '*.hpp' -exec chmod -x {} +
sed -i '1{/#!/d}' pythran/run.py

# Remove bundled header libs and use the ones from system
rm -r pythran/boost pythran/xsimd

# Use FlexiBLAS
sed -i 's|blas=blas|blas=flexiblas|' pythran/pythran-linux*.cfg
sed -i 's|include_dirs=|include_dirs=/usr/include/flexiblas|' pythran/pythran-linux*.cfg

# This test explicitly tests with OpenBLAS
# But we want to avoid OpenBLAS dependency to verify everything works with FlexiBLAS
# https://github.com/serge-sans-paille/pythran/pull/2244#issuecomment-2441215988
sed -i 's/openblas/flexiblas/' pythran/tests/test_distutils/pythran.rc

# not yet available in Fedora
sed -i '/guzzle_sphinx_theme/d' docs/conf.py
sed -i 's/, "guzzle_sphinx_theme"//' pyproject.toml
sed -i 's/, "nbval"//' pyproject.toml

# The tests have some cflags in them
# We need to adapt the flags to play nicely with other Fedora's flags
# E.g. fortify source implies at least -O1
sed -i -e 's/-O0/-O1/g' -e 's/-Werror/-w/g' pythran/tests/__init__.py


%generate_buildrequires
%pyproject_buildrequires -x doc,test


%build
%pyproject_wheel

PYTHONPATH=$PWD make -C docs html
rm -rf docs/_build/html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files %{name} omp


%check
k=""
%if 0%{?__isa_bits} == 32
# These tests cause memory (address space) exhaustion; see discussion in
# https://src.fedoraproject.org/rpms/pythran/pull-request/28.
for t in test_fftn_{8,11,15,16,17,20,22} \
    test_{h,ih,ir}fft_{8,14} \
    test_{,i}fft_3d{,_axis,f64_axis,int64_axis} \
    test_numpy_random_bytes1 \
    test_convolve_2b
do
  k="${k:+$k and }not $t"
done
%endif

# Don’t run tests in parallel on 32-bit architecutres. Running tests in serial
# makes memory errors, which occur in some tests on 32-bit architectures, more
# reproducible, and makes the output when they occur less confusing: we tend to
# get individual test failures rather than a pytest INTERNALERROR.
%if 0%{?__isa_bits} != 32
%global use_pytest_xdist 1
%endif

%pytest %{?use_pytest_xdist:-n auto} ${k:+-k "$k"}


%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%doc docs/_build/html
%{_bindir}/%{name}
%{_bindir}/%{name}-config


%changelog
%autochangelog
