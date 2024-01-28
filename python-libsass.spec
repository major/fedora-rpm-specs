# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc 1

Name:           python-libsass
Version:        0.23.0
Release:        %autorelease
Summary:        Sass for Python: A straightforward binding of libsass for Python

# SPDX
License:        MIT
URL:            https://github.com/dahlia/libsass-python
Source:         %{url}/archive/%{version}/libsass-python-%{version}.tar.gz

# 0.22.0: documentation seems is not ready for sphinx 6.1.3
# https://github.com/sass/libsass-python/issues/424
#
# doc: support sphinx 6.0 ext.extlinks
# https://github.com/sass/libsass-python/pull/433
Patch:          %{url}/pull/433.patch

BuildRequires:  python3-devel

# Selected test dependencies from requirements-dev.txt; most entries in that
# file are for linters, code coverage, etc.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  (%{py3_dist werkzeug} with %{py3_dist werkzeug} >= 0.9)

BuildRequires:  make
BuildRequires:  gcc-c++

BuildRequires:  libsass-devel >= 3.6.6

BuildRequires:  help2man
%if %{with doc}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
This package provides a simple Python extension module sass which is binding
LibSass (written in C/C++ by Hampton Catlin and Aaron Leung). It’s very
straightforward and there isn’t any headache related to Python
distribution/deployment. That means you can add just libsass into your
setup.py’s install_requires list or requirements.txt file. No need for Ruby nor
Node.js.}

%description %{common_description}


%package -n python3-libsass
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/
#   #_provides_for_importable_modules
# This package is messy; it occupies quite a few top-level names.
%py_provides python3-sass
%py_provides python3-pysassc
%py_provides python3-sasstests
%py_provides python3-sassutils

%description -n python3-libsass %{common_description}


%if %{with doc}
%package        doc
Summary:        Documentation for python-libsass

%description    doc %{common_description}
%endif


%prep
%autosetup -n libsass-python-%{version} -p1

# While upstream has the executable bit set, we will install this in
# site-packages without executable permissions; therefore, the shebang becomes
# useless, and we should remove it downstream.
sed -r -i '1{/^#!/d}' pysassc.py


%generate_buildrequires
export SYSTEM_SASS='1'
%pyproject_buildrequires


%build
export SYSTEM_SASS='1'
%pyproject_wheel

%if %{with doc}
LIB='lib.%{python3_platform}-cpython-%{python3_version_nodots}'
PYTHONPATH="${PWD}/build/${LIB}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
export SYSTEM_SASS='1'
%pyproject_install
%pyproject_save_files -l sass pysassc sasstests sassutils _sass

# We build the man page in %%install rather than %%build because we need to use
# the entry point in %%{buildroot}/%%{_bindir}.
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitearch}' \
    help2man --no-info --output='%{buildroot}%{_mandir}/man1/pysassc.1' \
    '%{buildroot}%{_bindir}/pysassc'


%check
%pytest -v sasstests.py


%files -n python3-libsass -f %{pyproject_files}
%if %{without doc}
%doc README.rst
%doc docs/changes.rst
%endif
%{_bindir}/pysassc
%{_mandir}/man1/pysassc.1*


%if %{with doc_pdf}
%files doc
%license LICENSE
%doc README.rst
%doc docs/changes.rst
%doc docs/_build/latex/libsass.pdf
%endif


%changelog
%autochangelog
