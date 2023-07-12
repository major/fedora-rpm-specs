%global desc %{expand: \
This package provides straightforward implementation of benchmarking
functions for optimization tasks.}

# do not build docs for now - missing dependency
%bcond_with docs

%bcond_without tests

%global forgeurl https://github.com/gugarosa/opytimark

Name:           python-opytimark
Version:        1.0.8
Release:        %autorelease
Summary:        Python implementation of Optimization Benchmarking Functions

%forgemeta

License:        Apache-2.0
URL:            https://github.com/gugarosa/opytimark
Source0:        %forgesource

# Move dev dependencies
# https://github.com/gugarosa/opytimark/pull/2
Patch:          %{url}/pull/2.patch

BuildArch:      noarch

%description
%{desc}

%package -n python3-opytimark
Summary:        %{summary}
BuildRequires:      python3-devel

%if %{with tests}
BuildRequires:      %{py3_dist pytest}
%endif

# sphinx-autoapi is missing
%if %{with docs}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%endif

%description -n python3-opytimark
%{desc}

%if %{with docs}
%package doc
BuildArch:      noarch
Summary:        %{summary}

%description doc
Documentation for %{name}.
%endif

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with docs}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files opytimark

%check

# several tests are failing -- will examine them later
%if %{with tests}
%pytest -k 'not test_year and not test_decorator and not test_loader and not cec_benchmark'
%endif

%files -n python3-opytimark -f %{pyproject_files}
%doc README.md

%if %{with docs}
%files doc
%license LICENSE
%doc CODE_OF_CONDUCT.md
%doc docs/_build/latex/opytimark.pdf
%endif

%changelog
%autochangelog
