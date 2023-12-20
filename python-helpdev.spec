# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-helpdev
Version:        0.7.1
Release:        %autorelease
Summary:        HelpDev – Extracts information about the Python environment easily

# The GitLab archive contains tests and documentation; the PyPI sdist doesn’t.
%global forgeurl https://gitlab.com/dpizetta/helpdev
%global tag v%{version}
%forgemeta

# The entire source is (SPDX) MIT, except for “Images,” which are CC-BY-4.0 (an
# allowed license for content). The images in question seem to be only the
# contents of docs/images/, which are not incorporated in the helpdev.pdf file
# in the -doc subpackage (but are not present in any other subpackages).
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

# Remove useless shebang lines from package modules
# https://gitlab.com/dpizetta/helpdev/-/merge_requests/4
Patch:          %{forgeurl}/-/merge_requests/4.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel

# Selected test dependencies from req-test.txt; most entries in that file are
# for linters, code coverage, etc. Note that we use pytest directly because tox
# doesn’t add anything useful for us in this package.
BuildRequires:  %{py3_dist pytest}

# The generated man page is pretty good in this case; it’s probably not worth
# hand-writing one.
BuildRequires:  help2man

%if %{with doc_pdf}
# We don’t generate documentation dependencies from req-doc.txt because:
# - There is extra cruft in there (setuptools, wheel, etc.): no big deal
# - We don’t need sphinx_rtd_theme because we aren’t building HTML
# - We need to specify the extra BR’s for building LaTeX/PDF manually anyway
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
Helping users and developers to get information about the environment to report
bugs or even test your system without spending a day on it. It can get
information about hardware, OS, paths, Python distribution and packages,
including Qt-things.}

%description %{common_description}


%package -n python3-helpdev
Summary:        %{summary}

Recommends:     python3-helpdev+memory_info = %{version}-%{release}

%description -n python3-helpdev %{common_description}


%pyproject_extras_subpkg -n python3-helpdev memory_info


%package doc
Summary:        Documentation and examples for HelpDev

# The entire source is (SPDX) MIT, except for images incorporated in
# helpdev.pdf, which are CC-BY-4.0; see also the more verbose comment above the
# base package License field.
License:        MIT AND CC-BY-4.0

%description doc
This package includes documentation and examples for HelpDev.


%prep
%autosetup -p1 %{forgesetupargs}


%generate_buildrequires
%pyproject_buildrequires -x memory_info


%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C build/docs/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l helpdev

# Generating the man page in %%install allows us to use the installed entry
# point; horrible hacks would be required to do this in %%build.
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man \
    --no-info --output='%{buildroot}%{_mandir}/man1/helpdev.1' \
    '%{buildroot}%{_bindir}/helpdev'


%check
%pytest -v


%files -n python3-helpdev -f %{pyproject_files}
%{_bindir}/helpdev
%{_mandir}/man1/helpdev.1*


%files doc
%license LICENSE.rst

%doc CHANGES.rst
%doc README.rst

# Text files, mostly sample output
%doc examples/

%if %{with doc_pdf}
%doc build/docs/latex/helpdev.pdf
%endif


%changelog
%autochangelog
