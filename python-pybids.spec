%bcond_without tests

%global _description %{expand:
PyBIDS is a Python module to interface with datasets conforming BIDS.

Documentation can be found online at https://bids-standard.github.io/pybids/
}

Name:       python-pybids
Version:    0.15.5
Release:    %autorelease
Summary:    Interface with datasets conforming to BIDS

License:    MIT
URL:        https://bids.neuroimaging.io
Source0:    https://github.com/bids-standard/pybids/archive/%{version}/pybids-%{version}.tar.gz

# included as a git-submodule upstream
%global examples_version 1.8.0
Source1:    https://github.com/bids-standard/bids-examples/archive/%{examples_version}/bids-examples.tar.gz

BuildArch:      noarch

# tests fail on 32 bit systems, so let's just drop i686
ExcludeArch:    %{ix86}

%description %{_description}

%package -n python3-pybids
Summary:    Interface with datasets conforming to BIDS
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
# unbundled
BuildRequires:  %{py3_dist inflect}
Requires:  %{py3_dist inflect}

%description -n python3-pybids %{_description}

%package doc
Summary:    Examples for pybids

%description doc
Description for %{name}.

%prep
%autosetup -n pybids-%{version}

# Remove bundled inflect
rm -rf bids/external

pushd bids
    sed -ibackup 's/from.*external import/import/' layout/layout.py
popd

# unpin formulaic requirement
# https://github.com/bids-standard/pybids/issues/915
# https://github.com/bids-standard/pybids/pull/916
sed -i 's/formulaic.*/formulaic/' setup.cfg

%{__tar} -xf %{SOURCE1}
mv bids-examples-%{examples_version} bids-examples

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files bids

%check
%if %{with tests}
PYTHONPATH=. %{pytest} -s -v .
%else
%pyproject_check_import
%endif

%files -n python3-pybids -f %{pyproject_files}
%doc README.md
%{_bindir}/pybids

%files doc
%doc bids-examples/
%license LICENSE

%changelog
%autochangelog
