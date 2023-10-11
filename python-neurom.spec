%global _description %{expand:
NeuroM is a Python-based toolkit for the analysis and processing of neuron
morphologies.

Documentation is available at https://neurom.readthedocs.io/
}
%global forgeurl    https://github.com/BlueBrain/NeuroM

Name:           python-neurom
Version:        3.2.4
Release:        %autorelease
Summary:        Neuronal Morphology Analysis Tool

%global tag  v%{version}
%forgemeta

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

# Remove a few useless shebang lines
# https://github.com/BlueBrain/NeuroM/pull/1083
Patch:          %{url}/pull/1083.patch

# Replace PyPI mock test dependency with unittest.mock
# https://github.com/BlueBrain/NeuroM/pull/1084
Patch:          %{url}/pull/1084.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description %_description

%package -n python3-neurom
Summary:        %{summary}

BuildRequires:  python3-devel

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

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -t -x plotly

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files neurom

# Remove spurious installed files
rm -rf $RPM_BUILD_ROOT/%{python3_sitelib}/tests/

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
# tests failing
# reported upstream: https://github.com/BlueBrain/NeuroM/issues/983
k="${k-}${k+ and }not test_extract_dataframe_multiproc"
k="${k-}${k+ and }not test_extract_stats_scalar_feature"
k="${k-}${k+ and }not test_markers"
k="${k-}${k+ and }not test_single_neurite_no_soma"
k="${k-}${k+ and }not test_skip_header"
%tox -- -- -k "${k-}"

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
