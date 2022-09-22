%global _description %{expand:
NeuroM is a Python-based toolkit for the analysis and processing of neuron
morphologies.

Documentation is available at https://neurom.readthedocs.io/
}
%global forgeurl    https://github.com/BlueBrain/NeuroM

Name:           python-neurom
Version:        3.1.0
Release:        %autorelease
Summary:        Neuronal Morphology Analysis Tool

%global tag  v%{version}
%forgemeta

License:        BSD
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

%description %_description

%package -n python3-neurom
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-toml

%description -n python3-neurom %_description

%package doc
Summary:        Documentation for %{name}

%description doc %_description

%prep
%forgesetup

# Fix shebangs
find . -type f -exec sed -i 's|^#![  ]*/usr/bin/env.*$|#!/usr/bin/python3|' {} ';'
sed -i '/^#![  ]*\/usr\/bin\/python3.*$/ d' neurom/check/runner.py

# correct config files path
# not sure why this was changed: https://github.com/BlueBrain/NeuroM/commit/dbc3bd069a6fbded6c4a64cc038adb37c0b06932
sed -i 's|graft neurom/config|graft neurom/apps/config|' MANIFEST.in

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -t

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
%pytest -k "not test_morph_stat and not test_morph_check and not test_extract_stats_scalar_feature and not test_single_neurite_no_soma and not test_skip_header and not test_markers"

%files -n python3-neurom -f %{pyproject_files}
%doc README.md AUTHORS.md
%{_bindir}/neurom

%files doc
%license LICENSE.txt
%doc examples tutorial

%changelog
%autochangelog
