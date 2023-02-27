%global desc %{expand: \
A collection of Benchmark functions for numerical optimization problems.

Current information can always be found from the repository - https://github.com/thieu1995/opfunu}

# enable when new Sphinx stack is available on all platforms
%bcond_with docs

%bcond_without tests

%global forgeurl https://github.com/thieu1995/opfunu

Name:           python-opfunu
Version:        1.0.0
Release:        %autorelease
Summary:        Benchmark functions for numerical optimization problems

%forgemeta

License:        GPL-3.0-only
URL:            https://github.com/thieu1995/opfunu
Source0:        %forgesource

# This patch is intended not to package tests.
# It was not submitted to the upstream since this is optional
# for the upstream to apply this.
Patch:          0001-do-not-package-tests-examples.patch
# Do not import numpy.int, which was deprecated and removed
# https://github.com/thieu1995/opfunu/pull/12
Patch:          %{url}/pull/12.patch

BuildArch:      noarch

%description
%{desc}

%package -n python3-opfunu
Summary:        %{summary}
BuildRequires:      python3-devel
BuildRequires:      %{py3_dist requests}

%if %{with tests}
BuildRequires:      %{py3_dist pytest}
%endif

%if %{with docs}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%endif

# scipy, Pillow, requests and pandas are missing in setup file
BuildRequires: %{py3_dist scipy}
BuildRequires: %{py3_dist Pillow}
BuildRequires: %{py3_dist pandas}
Requires:      %{py3_dist Pillow}
Requires:      %{py3_dist pandas}
Requires:      %{py3_dist requests}
Requires:      %{py3_dist scipy}
BuildRequires:  hardlink

%description -n python3-opfunu
%{desc}

%package doc
BuildArch:      noarch
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%forgeautosetup -p1

# Adjust shebangs and executable permissions
# https://github.com/thieu1995/opfunu/pull/9
find examples -type f -name '*.py' ! -name '__init__.py' \
    -execdir chmod +x '{}' '+'
find opfunu tests -type f -name '*.py' \
    -execdir sed -r -i '1{/^#!/d}' '{}' '+'

%py3_shebang_fix examples

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
%pyproject_save_files opfunu

hardlink '%{buildroot}%{python3_sitelib}/opfunu'

%check

%if %{with tests}
%pytest
%endif

%files -n python3-opfunu -f %{pyproject_files}
%doc README.md ChangeLog.md
%doc examples/

%files doc
%license LICENSE
%doc CODE_OF_CONDUCT.md
%if %{with docs}
%doc docs/_build/latex/opfunu.pdf
%endif

%changelog
%autochangelog
