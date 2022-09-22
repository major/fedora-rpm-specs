# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-lazyarray
Version:        0.5.2
%forgemeta
Release:        %autorelease
Summary:        A lazily-evaluated numerical array class

License:        BSD
URL:            https://github.com/NeuralEnsemble/lazyarray
# The GitHub archive contains documentation build files that are not in the
# PyPI archive.
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{py3_dist pytest}
# Optional dependency, used in tests
BuildRequires:  %{py3_dist scipy}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  /usr/bin/xindy
BuildRequires:  tex-xetex-bin
%endif

%global _description %{expand:
lazyarray is a Python package that provides a lazily-evaluated numerical array
class, larray, based on and compatible with NumPy arrays.

Lazy evaluation means that any operations on the array (potentially including
array construction) are not performed immediately, but are delayed until
evaluation is specifically requested. Evaluation of only parts of the array is
also possible.

Use of an larray can potentially save considerable computation time and
memory in cases where:

• arrays are used conditionally (i.e. there are cases in which the array is
  never used)
• only parts of an array are used (for example in distributed computation,
  in which each MPI node operates on a subset of the elements of the array)

Documentation: http://lazyarray.readthedocs.org}

%description %_description


%package -n python3-lazyarray
Summary:        A lazily-evaluated numerical array class
BuildRequires:  python3-devel

# We don’t need a Recommends for the optional scipy dependency, because its
# only value is to enable support for scipy sparse arrays. Programs that use
# those will already need to depend on scipy directly.

%description -n python3-lazyarray %_description


%package docs
Summary:    Documentation for %{name}
BuildArch:  noarch

%description docs
This package contains generated HTML documentation for %{name}.


%prep
%autosetup -n lazyarray-%{version}

# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> doc/conf.py


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C doc latex SPHINXBUILD='sphinx-build' SPHINXOPTS='%{?_smp_mflags}'
%make_build -C doc/_build/latex
%endif


%install
%pyproject_install
%pyproject_save_files lazyarray


%check
%{pytest}


%files -n python3-lazyarray -f %{pyproject_files}
# pyproject-rpm-macros takes care of LICENSE; verify with “rpm -qL -p …”
%doc changelog.txt README.rst


%files docs
%license LICENSE
%if %{with doc_pdf}
%doc doc/_build/latex/lazyarray.pdf
%endif


%changelog
%autochangelog
