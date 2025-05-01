# We used to build with Theano support.  However, we no longer have a compatible
# version of Theano in Fedora.  If aesara is ever packaged for Fedora, we can
# use it instead.

# We are archful (see below), but there are no ELF objects in the binary RPM.
%global debug_package %{nil}

%global giturl  https://github.com/sympy/sympy
%global commit  fe935ceb303891d1f8bea4c03b19fd9ec9464b02

Name:           sympy
Version:        1.14.0
Release:        %autorelease
Summary:        A Python library for symbolic mathematics

# The project as a whole is BSD-3-Clause.
# The files in sympy/parsing/latex are MIT.
License:        BSD-3-Clause AND MIT
URL:            https://sympy.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{name}-%{version}.tar.gz
# For intersphinx
Source1:        https://matplotlib.org/stable/objects.inv#/objects-matplotlib.inv
Source2:        https://docs.scipy.org/doc/scipy/objects.inv#/objects-scipy.inv
Source3:        https://numpy.org/doc/stable/objects.inv#/objects-numpy.inv
# Do not depend on intersphinx_registry, which is not available in Fedora
Patch:          %{name}-intersphinx.patch

# This package used to be noarch, and should still be noarch.  However, because
# there is no JDK available on i686 anymore, the antlr4 package is also not
# available on i686.  When we can stop building on i686 altogether, we can bring
# this back.  In the meantime, we cannot claim to be noarch, because the i686
# build is different from the other arches in lacking BuildRequires: antlr4.
# BuildArch:      noarch

%ifarch %{java_arches}
BuildRequires:  antlr4
BuildRequires:  %{py3_dist antlr4-python3-runtime}
%endif

BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  python3-devel
BuildRequires:  python3-clang
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist gmpy2}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist numexpr}
BuildRequires:  %{py3_dist pycosat}
BuildRequires:  python3-numpy-f2py
BuildRequires:  %{py3_dist scipy}

# Documentation
BuildRequires:  graphviz
BuildRequires:  ImageMagick
BuildRequires:  librsvg2-tools
BuildRequires:  make
BuildRequires:  %{py3_dist furo}
BuildRequires:  %{py3_dist linkify-it-py}
BuildRequires:  %{py3_dist matplotlib-inline}
BuildRequires:  %{py3_dist mpmath}
BuildRequires:  %{py3_dist myst-parser}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-copybutton}
BuildRequires:  %{py3_dist sphinx-math-dollar}
BuildRequires:  %{py3_dist sphinx-reredirects}
BuildRequires:  %{py3_dist sphinxcontrib-jquery}
BuildRequires:  python-mpmath-doc
BuildRequires:  tex(latex)
BuildRequires:  tex-dvipng

# Tests
%ifarch x86_64
BuildRequires:  lfortran
%endif
BuildRequires:  %{py3_dist autowrap}
BuildRequires:  %{py3_dist cloudpickle}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist lark}
# FIXME: Crashes in llvmlite on ppc64le, s390x and riscv64
%ifnarch ppc64le s390x riscv64
BuildRequires:  %{py3_dist llvmlite}
%endif
BuildRequires:  %{py3_dist lxml}
BuildRequires:  %{py3_dist pytest-split}
BuildRequires:  %{py3_dist pytest-xdist}
BuildRequires:  %{py3_dist wurlitzer}
BuildRequires:  python3-z3

%global _description\
SymPy aims to become a full-featured computer algebra system (CAS)\
while keeping the code as simple as possible in order to be\
comprehensible and easily extensible. SymPy is written entirely in\
Python and does not require any external libraries.

%description %_description

%package -n python3-%{name}
Summary:        A Python3 library for symbolic mathematics
Recommends:     tex(latex)
Recommends:     tex(amsfonts.sty)
Recommends:     tex(amsmath.sty)
Recommends:     tex(euler.sty)
Recommends:     tex(eulervm.sty)
Recommends:     tex(standalone.cls)
%ifarch %{java_arches}
Recommends:     %{py3_dist antlr4-python3-runtime}
%endif
Recommends:     %{py3_dist cython}
Recommends:     %{py3_dist gmpy2}
Recommends:     %{py3_dist matplotlib}
Recommends:     %{py3_dist numexpr}
Recommends:     %{py3_dist pycosat}
Recommends:     %{py3_dist pyglet}
Recommends:     %{py3_dist scipy}

%description -n python3-%{name}
SymPy aims to become a full-featured computer algebra system (CAS)
while keeping the code as simple as possible in order to be
comprehensible and easily extensible. SymPy is written entirely in
Python and does not require any external libraries.

%package doc
# This project is BSD-3-Clause.  Other files bundled with the documentation
# have the following licenses:
# - searchindex.js: BSD-2-Clause
# - _static/basic.css: BSD-2-Clause
# - _static/clipboard.min.js: MIT
# - _static/copy*: MIT
# - _static/doctools.js: BSD-2-Clause
# - _static/graphviz.js: BSD-2-Clause
# - _static/jquery*.js: MIT
# - _static/language_data.js: BSD-2-Clause
# - _static/plot_directive.css: PSF-2.0 (see note)
# - _static/pygments.css: BSD-2-Clause
# - _static/scripts/*: MIT
# - _static/searchtools.js: BSD-2-Clause
# - _static/styles/*: MIT
# - _static/underscore*.js: MIT
#
# NOTE: The license of _static/plot_directive.css is the same as the license of
# matplotlib.  The matplotlib license is functionally identical to PSF-2.0, but
# uses different organization and project names.  I am using the PSF-2.0
# identifier for now, because there is no valid SPDX choice.  Revisit this.
License:        BSD-3-Clause AND BSD-2-Clause AND MIT AND PSF-2.0
Summary:        Documentation for sympy
Provides:       bundled(js-jquery)
Provides:       bundled(js-underscore)

# This can be removed when F46 reaches EOL
Obsoletes:      %{name}-examples < 1.14.0
Provides:       %{name}-examples = %{version}-%{release}

%description doc
HTML documentation for sympy.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Remove bogus shebangs
for fil in sympy/physics/mechanics/models.py \
           sympy/physics/optics/polarization.py; do
  sed -i.orig '/env python/d' $fil
  fixtimestamp $fil
done

# Do not depend on env
for fil in $(grep -rl "^#\![[:blank:]]*%{_bindir}/env" .); do
  sed -i.orig 's,^\(#\![[:blank:]]*%{_bindir}/\)env python,\1python3,' $fil
  fixtimestamp $fil
done

# Use local objects.inv for intersphinx
sed -e "s|\('https://matplotlib\.org/stable/', \)None|\1'%{SOURCE1}'|" \
    -e "s|\(.https://docs\.scipy\.org/doc/scipy/., \)None|\1'%{SOURCE2}'|" \
    -e "s|\(.https://numpy\.org/doc/stable/., \)None|\1'%{SOURCE3}'|" \
    -i doc/src/conf.py

# Help sphinx find the git commit
echo -n '%{commit}' > doc/commit_hash.txt

# Permit use of antlr4 4.13
sed -i s'/4\.11/4.13/g' sympy/parsing/autolev/_parse_autolev_antlr.py \
    sympy/parsing/latex/_parse_latex_antlr.py

%generate_buildrequires
%pyproject_buildrequires -x dev

%build
%ifarch %{java_arches}
# Regenerate the ANTLR files
%{python3} setup.py antlr
%endif

# Build
%pyproject_wheel

# Build the documentation
pushd doc
make html SPHINXOPTS=%{?_smp_mflags} PYTHON=%{python3}
make cheatsheet
popd

%install
%pyproject_install
%pyproject_save_files -l isympy sympy

## Remove extra files
rm -f %{buildroot}%{_bindir}/{,doc}test

# Fix permissions
chmod 0755 %{buildroot}%{python3_sitelib}/sympy/benchmarks/bench_symbench.py \
      %{buildroot}%{python3_sitelib}/sympy/testing/tests/diagnose_imports.py

# Install the HTML documentation and link duplicates
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
cp -a doc/_build/html %{buildroot}%{_docdir}/%{name}-doc
rm -f %{buildroot}%{_docdir}/%{name}-doc/html/.buildinfo
rm -fr %{buildroot}%{_docdir}/%{name}-doc/i18n
%fdupes %{buildroot}%{_docdir}/%{name}-doc

%check
%{python3} bin/test -v --parallel

%files -n python3-%{name} -f %{pyproject_files}
%doc AUTHORS README.md
%doc doc/_build/cheatsheet/cheatsheet.pdf
%doc doc/_build/cheatsheet/combinatoric_cheatsheet.pdf
%{_bindir}/isympy
%{_mandir}/man1/isympy.1*

%files doc
%docdir %{_docdir}/%{name}-doc/html
%{_docdir}/%{name}-doc/html

%changelog
%autochangelog
