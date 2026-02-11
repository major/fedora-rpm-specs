%global _docdir_fmt %{name}
%global giturl  https://github.com/cvxopt/cvxopt

Name:           python-cvxopt
Version:        1.3.3
Release:        %autorelease
Summary:        A Python Package for Convex Optimization

License:        GPL-3.0-or-later
URL:            https://cvxopt.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/cvxopt-%{version}.tar.gz
# Use the flexiblas library instead of the system BLAS.
Patch:          %{name}-setup.patch
# Fix mixed signed/unsigned operations
Patch:          %{name}-signed.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    pyproject
BuildOption(install): -l cvxopt

BuildRequires:  DSDP-devel
BuildRequires:  gcc
BuildRequires:  glpk-devel
BuildRequires:  flexiblas-devel
%ifarch %{power64}
BuildRequires:  flexiblas-atlas
%endif
BuildRequires:  make
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  suitesparse-devel
BuildRequires:  tex-dvipng
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(latex)
BuildRequires:  tex(tex4ht.sty)
BuildRequires:  tex(utf8x.def)

Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

%global _desc %{expand:CVXOPT is a free software package for convex optimization based on the Python
programming language. Its main purpose is to make the development of software
for convex optimization applications straightforward by building on Python's
extensive standard library and on the strengths of Python as a high-level
programming language.}

%description
%_desc

%package -n     python3-cvxopt
Summary:        A Python3 Package for Convex Optimization
Provides:       bundled(js-jquery)

%description -n python3-cvxopt
%_desc

%package        doc
# The content is GPL-3.0-or-later.  Other licenses are due to files copied in
# by Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/css: MIT
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sphinx_highlight.js: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT
Summary:        API documentation for python3-cvxopt

%description    doc
API documentation for python3-cvxopt.

%package        examples
Summary:        Examples of using %{name}
Requires:       python3-cvxopt = %{version}-%{release}
Requires:       %{py3_dist matplotlib}
BuildArch:      noarch

%description    examples
Examples of using %{name}.

%prep
%autosetup -p1 -n cvxopt-%{version}

# Do not use env
sed -i 's,bin/env python,bin/python3,' examples/filterdemo/filterdemo_{cli,gui}

# Remove useless executable bits
find examples -name \*.py -perm /0111 -exec chmod a-x {} +

%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%build -p
export LDSHARED='gcc -shared %{build_ldflags}'
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%build -a
# Rebuild the documentation
make -C doc clean
make -C doc -B html
rm -f doc/build/html/.buildinfo

%check
export FLEXIBLAS=netlib
%pytest -v

%files -n python3-cvxopt -f %{pyproject_files}
%license LICENSE
%doc README.md

%files doc
%doc doc/build/html/

%files examples
%doc examples/

%changelog
%autochangelog
