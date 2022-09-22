%bcond_without tests

%global forgeurl     https://github.com/numba/llvmlite

Name:           python-llvmlite
Version:        0.37.0
Release:        %{autorelease}
Summary:        Lightweight LLVM Python binding for writing JIT compilers

%forgemeta

License:        BSD
URL:            http://llvmlite.pydata.org/
Source0:        %{forgesource}

# Python 3.10
# https://github.com/numba/llvmlite/pull/769
# See also: https://github.com/numba/llvmlite/issues/740#issuecomment-937830985
Patch0:         https://github.com/numba/llvmlite/pull/769.patch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
# 0.37.0 only supports llvm11
BuildRequires:  llvm11-devel
BuildRequires:  gcc-c++

%global _description %{expand:
llvmlite provides a Python binding to LLVM for use in Numba.

Numba previously relied on llvmpy.  While llvmpy exposed large parts of the
LLVM C++ API for direct calls into the LLVM library, llvmlite takes an entirely
different approach. Llvmlite starts from the needs of a JIT compiler and splits
them into two decoupled tasks:

- Construction of a Module, function by function, Instruction by instruction.
- Compilation and optimization of the module into machine code.

The construction of an LLVM module does not call the LLVM C++ API. Rather, it
constructs the LLVM intermediate representation (IR) in pure Python. This is
the role of the IR layer.

The compilation of an LLVM module takes the IR in textual form and feeds it
into LLVM's parsing API. It then returns a thin wrapper around LLVM's C++
module object. This is the role of the binding layer.

Once parsed, the module's source code cannot be modified, which loses the
flexibility of the direct mapping of C++ APIs into Python that was provided by
llvmpy but saves a great deal of maintenance.}


%description %_description

%package -n python3-llvmlite
Summary:        %{summary}


%description -n python3-llvmlite %_description

%package doc
Summary:        %{summary}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

%description doc
Documentation for %{name}.

%prep
%forgeautosetup -p1

# seems to be fine with 3.11 but we need to loosen the guard
# see also: “python 3.10 support” https://github.com/numba/llvmlite/issues/740
sed -i 's/max_python_version =.*/max_python_version = "3.12"/' setup.py

# increase verbosity of tests to 2
sed -i 's/\(def run_tests.*verbosity=\)1/\12/' llvmlite/tests/__init__.py

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
export LLVM_CONFIG="%{_libdir}/llvm11/bin/llvm-config"
%pyproject_wheel

make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.doctrees,.buildinfo,_static/EMPTY} -vf

%install
%pyproject_install
%pyproject_save_files llvmlite

%check
%if %{with tests}
LD_LIBRARY_PATH="%{buildroot}%{python3_sitearch}/llvmlite/binding/" PYTHONPATH="$PYTHONPATH:%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}" %{python3} runtests.py
%endif

%files -n python3-llvmlite -f %{pyproject_files}
%doc CHANGE_LOG README.rst

%files doc
%license LICENSE
%doc docs/_build/html examples/

%changelog
%autochangelog
