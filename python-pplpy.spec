Name:           python-pplpy
Version:        0.8.10
Release:        %autorelease
Summary:        Python PPL wrapper

License:        GPL-3.0-or-later
URL:            https://pypi.org/project/pplpy/
VCS:            https://github.com/sagemath/pplpy
Source0:        %pypi_source pplpy

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  libmpc-devel
BuildRequires:  make
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  ppl-devel
BuildRequires:  python3-cysignals-devel
BuildRequires:  python3-devel

%description
This package provides a Python wrapper to the C++ Parma Polyhedra
Library (PPL).

%package     -n python3-pplpy
Summary:        Python 3 PPL wrapper
Recommends:     %{py3_dist cysignals}
Recommends:     %{py3_dist gmpy2}

%description -n python3-pplpy
This package provides a Python 3 wrapper to the C++ Parma Polyhedra
Library (PPL).

%package     -n python3-pplpy-devel
# The content is GPL-3.0-or-later.  Other licenses are due to files copied in
# by Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/classic.css: BSD-2-Clause
# _static/default.css: BSD-2-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sidebar.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT
Summary:        Development files for the python 3 PPL wrapper
Requires:       python3-pplpy%{?_isa} = %{version}-%{release}

%description -n python3-pplpy-devel
Development files for the python 3 PPL wrapper.

%prep
%autosetup -n pplpy-%{version}

%generate_buildrequires
%pyproject_buildrequires -t -x doc

%build
# Do not pass -pthread to the compiler or linker
export CC=gcc
export LDSHARED="gcc -shared"
%pyproject_wheel

# Build the documentation
PYTHONPATH=$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots} \
make -C docs html
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files 'ppl*'

%check
%tox

%files -n python3-pplpy -f %{pyproject_files}
%doc CHANGES.txt README.html
%exclude %{python3_sitearch}/ppl/*.hh
%exclude %{python3_sitearch}/ppl/*.pxd

%files -n python3-pplpy-devel
%doc docs/build/html/*
%{python3_sitearch}/ppl/*.hh
%{python3_sitearch}/ppl/*.pxd

%changelog
%autochangelog
