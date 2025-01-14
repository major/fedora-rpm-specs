%bcond tests 1
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We would like to generate PDF documentation as a substitute, but have not
# been able to successfully build the Sphinx-generated LaTeX for this
# particular package.
%bcond doc_pdf 0

%global forgeurl https://github.com/NiaOrg/NiaPy

Name:           python-niapy
Version:        2.5.2
%forgemeta
Release:        %autorelease
Summary:        Microframework for building nature-inspired algorithms

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

%global _description %{expand:
Nature-inspired algorithms are a very popular tool for solving optimization
problems. Numerous variants of nature-inspired algorithms have been developed
since the beginning of their era. Those were tested in various domains on
various applications to prove their versatility, especially when
hybridized, modified, or adapted. However, the implementation of
nature-inspired algorithms is sometimes a complicated, complex, and tedious
task. In order to break this wall, NiaPy is intended for simple and quick
use without spending time implementing algorithms from scratch.}

%description %_description

%package -n python3-niapy
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-toml-adapt

%if %{with tests}
# setup.py: tests_require
#
# flake8 ~= 3.7.7
# astroid >= 2.0.4
# pytest ~= 3.7.1
# coverage ~= 4.4.2
# coverage-space ~= 1.0.2
#
# We do not run flake8:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# …nor do we care about test coverage. Furthermore, we must accept any newer
# version of pytest.
BuildRequires:  python3dist(pytest) >= 3.7.1
%endif

%description -n python3-niapy %_description

%package doc
Summary:        Documentation and examples for %{name}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex-xetex-bin
BuildRequires:  /usr/bin/xindy
%endif

%description doc
%{summary}.

Full HTML documentation is available at
https://niapy.readthedocs.io/en/stable/index.html.

%prep
%forgeautosetup -p1
# Since we aren’t building HTML documentation, we don’t need the HTML theme
# dependency:
sed -r -i 's/^(sphinx-.*theme)/#\1/' docs/requirements.txt
# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/source/conf.py
# Avoid: ! LaTeX Error: Too deeply nested.
# Normally we could add a preamble like:
#
#   cat >> docs/source/conf.py <<'EOF'
#   latex_elements['preamble'] = r'''
#   \usepackage{enumitem}
#   \setlistdepth{99}
#   '''
#   EOF
#
# but that does not work well (“Undefined control sequence”).
#
# We can also try:
#
#   echo "latex_elements['maxlistdepth'] = '10'" >> docs/source/conf.py
#
# but this produces errors like:
#
#   ! LaTeX Error: \begin{list} on input line 21785 ended by \end{itemize}.

# optional step but let's ensure that there is no problems with dependency versions
toml-adapt -path pyproject.toml -a change -dep python -ver X
toml-adapt -path pyproject.toml -a change -dep numpy -ver X
toml-adapt -path pyproject.toml -a change -dep pandas -ver X
toml-adapt -path pyproject.toml -a change -dep matplotlib -ver X
toml-adapt -path pyproject.toml -a change -dep openpyxl -ver X

%generate_buildrequires
%pyproject_buildrequires -r %{?with_pdf_doc:docs/requirements.txt}

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet -f'
%endif

%install
%pyproject_install
%pyproject_save_files niapy

%check
%if %{with tests}
#k="${k-}${k+ and }not test_to_skip_sample1"
#k="${k-}${k+ and }not test_to_skip_sample2"
%pytest -ra -k "${k-}"
%endif

%files -n python3-niapy -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md Algorithms.md Problems.md CITATION.cff

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/build/latex/NiaPy.pdf
%endif
%doc examples/
%doc paper/
%doc CONTRIBUTING.md CODE_OF_CONDUCT.md

%changelog
%autochangelog
