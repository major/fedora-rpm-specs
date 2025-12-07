%bcond tests 1
# It’s nice to be able to run the examples as additional tests, but we normally
# choose not to do so since some examples take as much as several hours to run.
%bcond test_examples 0
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-niaaml
Version:        2.2.0
Release:        %autorelease
Summary:        Python automated machine learning framework

License:        MIT
URL:            https://github.com/firefly-cpp/NiaAML
Source:         %{url}/archive/%{version}/NiaAML-%{version}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source10:       niaaml.1
Source11:       niaaml-infer.1
Source12:       niaaml-optimize.1

BuildSystem:            pyproject
BuildOption(install):   -l niaaml
# There exists a docs/requirements.txt, but it seems to be inaccurate, with
# many unnecessary dependencies, so we do not use it to generate BR’s.

BuildArch:      noarch

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

BuildRequires:  dos2unix
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  /usr/bin/xindy
BuildRequires:  tex-xetex-bin
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%endif

%global _description %{expand:
NiaAML is a framework for Automated Machine Learning based on nature-inspired
algorithms for optimization. The framework is written fully in Python. The name
NiaAML comes from the Automated Machine Learning method of the same name. Its
goal is to compose the best possible classification pipeline for the given task
efficiently using components on the input. The components are divided into
three groups: feature selection algorithms, feature transformation algorithms
and classifiers. The framework uses nature-inspired algorithms for optimization
to choose the best set of components for the classification pipeline, and
optimize their hyperparameters.}

%description %_description


%package -n python3-niaaml
Summary:        %{summary}

%description -n python3-niaaml %_description


%package doc
Summary:        Documentation for NiaAML

%description doc
%{summary}.


%prep
%autosetup -n NiaAML-%{version} -p1

# - Don’t bound the version of Python. We must use the system interpreter.
# - Convert SemVer pins to minimum versions, since we can’t generally respect
#   the upper bounds in Fedora.
sed -r -i -e 's/^python ?=/# &/' -e 's/([^#]+ ?= ?")\^/\1>=/' pyproject.toml

# Ensure the Python interpreter path is correct in the example runner script:
sed -r -i 's|\bpython3\b|%{python3}|' examples/run_all.sh

# Fix CRNL (DOS-style) line endings
dos2unix --keepdate paper/paper.bib

# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/conf.py


%build -a
%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install -a
install -d \
    '%{buildroot}%{bash_completions_dir}' \
    '%{buildroot}%{zsh_completions_dir}' \
    '%{buildroot}%{fish_completions_dir}'
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
export _TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION=1
'%{buildroot}%{_bindir}/niaaml' --show-completion bash \
    > '%{buildroot}%{bash_completions_dir}/niaaml'
'%{buildroot}%{_bindir}/niaaml' --show-completion zsh \
    > '%{buildroot}%{zsh_completions_dir}/_niaaml'
'%{buildroot}%{_bindir}/niaaml' --show-completion fish \
    > '%{buildroot}%{fish_completions_dir}/niaaml.fish'

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'


%check -a
%if %{with tests}
%pytest
%endif
%if %{with test_examples}
# See also: examples/run_all.sh
find examples -type f -name '*.py' |
  env %{py3_test_envvars} xargs -r -n 1 -t -P %{_smp_build_ncpus} -I '{}' \
      '%{python3}' '{}'
%endif


%files -n python3-niaaml -f %{pyproject_files}
%doc README.md CHANGELOG.md COMPONENTS.md CITATION.cff
%{_bindir}/niaaml
%{bash_completions_dir}/niaaml
%{zsh_completions_dir}/_niaaml
%{fish_completions_dir}/niaaml.fish
%{_mandir}/man1/niaaml.1*
%{_mandir}/man1/niaaml-*.1*


%files doc
%license LICENSE
%doc README.md CHANGELOG.md COMPONENTS.md CITATION.cff
%if %{with doc_pdf}
%doc docs/_build/latex/niaaml.pdf
%endif
%doc examples/
%doc paper/
%doc docs/paper/10.21105.joss.02949.pdf


%changelog
%autochangelog
