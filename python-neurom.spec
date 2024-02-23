%global _description %{expand:
NeuroM is a Python-based toolkit for the analysis and processing of neuron
morphologies.

Documentation is available at https://neurom.readthedocs.io/
}
%global forgeurl    https://github.com/BlueBrain/NeuroM

Name:           python-neurom
Version:        3.2.8
Release:        %autorelease
Summary:        Neuronal Morphology Analysis Tool

%global tag  v%{version}
%forgemeta

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description %_description

%package -n python3-neurom
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-neurom %_description

%pyproject_extras_subpkg -n python3-neurom plotly

%package doc
Summary:        Documentation for %{name}

%description doc %_description

%prep
%forgeautosetup -p1

%py3_shebang_fix examples/

# correct config files path
# not sure why this was changed: https://github.com/BlueBrain/NeuroM/commit/dbc3bd069a6fbded6c4a64cc038adb37c0b06932
sed -i 's|graft neurom/config|graft neurom/apps/config|' MANIFEST.in

# Unpin setuptools_scm for <= f39
%if %{fedora} <= 39
sed -r -i 's/"(setuptools_scm).*"/"\1"/' pyproject.toml
%endif

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x plotly

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l neurom

# Remove spurious installed files
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/tests/

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
# tests failing
# reported upstream: https://github.com/BlueBrain/NeuroM/issues/983
k="${k-}${k+ and }not test_extract_dataframe_multiproc"  # failing with 3.2.5
k="${k-}${k+ and }not test_extract_stats_scalar_feature"  # failing with 3.2.5
k="${k-}${k+ and }not test_markers"  # failing with 3.2.5
k="${k-}${k+ and }not test_single_neurite_no_soma"  # failing with 3.2.5
k="${k-}${k+ and }not test_skip_header"  # failing with 3.2.5
PYTHONPATH=. %pytest -v -k "${k-}"

%files -n python3-neurom -f %{pyproject_files}
%doc AUTHORS.md
%doc CHANGELOG.rst
%doc README.md
%{_bindir}/neurom

%files doc
%license LICENSE.txt
%doc examples/
%doc tutorial/

%changelog
%autochangelog
