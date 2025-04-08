# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute (but we no longer do).
%bcond doc %[ %{defined fc42} || %{defined fc41} || %{defined fc40} || %{defined el10} ]

Name:           python-plac
Version:        1.4.5
Release:        %autorelease
Summary:        The smartest command line arguments parser in the world

License:        BSD-2-Clause
URL:            https://github.com/ialbert/plac
# GitHub archive contains full documentation sources; PyPI sdist does not
Source0:        %{url}/archive/v%{version}/plac-%{version}.tar.gz
# Man page written for Fedora in groff_man(7) format based on --help output
Source1:        plac_runner.py.1

BuildSystem:            pyproject
BuildOption(install):   -l plac_core plac_ext plac_tk plac

# Fix Tkinter imports on Python 3
# https://github.com/ialbert/plac/pull/85
Patch:          %{url}/pull/85.patch

BuildArch:      noarch

# Required for plac_tk:
BuildRequires:  python3-tkinter

%if %{with doc}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
plac is a Python package that can generate command line parameters from
function signatures.

plac works on Python 2.6 through all versions of Python 3.

plac has no dependencies beyond modules already present in the Python standard
library.

plac implements most of its functionality in a single file that may be included
in your source code.}

%description %{common_description}


%package -n python3-plac
Summary:        %{summary}

# Required for plac_tk:
Recommends:     python3-tkinter

%if %{without doc}
Obsoletes:      python-plac-doc < 1.4.5-1
%endif

%description -n python3-plac %{common_description}


%if %{with doc}
%package        doc
Summary:        Documentation for plac

%description doc %{common_description}
%endif


%build -a
%if %{with doc}
PYTHONPATH="${PWD}" sphinx-build -b latex -j%{?_smp_build_ncpus} \
    doc %{_vpath_builddir}/_latex
%make_build -C %{_vpath_builddir}/_latex LATEXMKOPTS='-quiet'
%endif


%install -a
install -t '%{buildroot}%{_mandir}/man1' -m 0644 -p -D '%{SOURCE1}'


%check -a
%{py3_test_envvars} '%{python3}' doc/test_plac.py


%files -n python3-plac -f %{pyproject_files}
%if %{without doc}
%doc CHANGES.md README.md RELEASE.md
%endif
%{_bindir}/plac_runner.py
%{_mandir}/man1/plac_runner.py.1*


%if %{with doc}
%files doc
%license LICENSE.txt
%doc CHANGES.md README.md RELEASE.md
%doc %{_vpath_builddir}/_latex/plac.pdf
%endif


%changelog
%autochangelog
