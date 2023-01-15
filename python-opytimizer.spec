%global desc %{expand: \
Opytimizer is a Python library consisting of
meta-heuristic optimization algorithms}

%bcond_without docs

%bcond_without tests

%global forgeurl https://github.com/gugarosa/opytimizer

Name:           python-opytimizer
Version:        3.1.2
Release:        %autorelease
Summary:        Python implementation of metaheuristic optimization algorithms

%forgemeta

License:        Apache-2.0
URL:            https://github.com/gugarosa/opytimizer
Source0:        %forgesource

BuildArch:      noarch

# Fix import when building docs
# PR: https://github.com/gugarosa/opytimizer/pull/33
Patch:          33.patch

# Move development dependencies out from the main dependencies
# PR: https://github.com/gugarosa/opytimizer/pull/34
Patch:          34.patch

%description
%{desc}

%package -n python3-opytimizer
Summary:        %{summary}
BuildRequires:      python3-devel

%if %{with tests}
BuildRequires:      %{py3_dist pytest}

# for several X11 tests
BuildRequires:  xorg-x11-server-Xvfb

%endif

# sphinx-autoapi is missing
%if %{with docs}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%endif

%description -n python3-opytimizer
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
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with docs}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files opytimizer

%check

# despite the use of xvfb, several plots are shown
%if %{with tests}
xvfb-run -a %{python3} -m pytest -k 'not plot'
%endif

%files -n python3-opytimizer -f %{pyproject_files}
%doc README.md

%if %{with docs}
%files doc
%license LICENSE
%doc CODE_OF_CONDUCT.md
%doc docs/_build/latex/opytimizer.pdf
%endif

%changelog
%autochangelog
