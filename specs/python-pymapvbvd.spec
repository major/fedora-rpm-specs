Name:           python-pymapvbvd
Version:        0.7.0
Release:        %autorelease
Summary:        Python twix file reader

License:        MIT
URL:            https://github.com/wtclarke/pymapvbvd
Source0:        %{pypi_source pymapvbvd}
# Generated with Source2: ./get_test_data.sh %%{version}
Source1:        pymapvbvd-test-data.tar.zst
Source2:        get_test_data.sh

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --extras tests
BuildOption(install): --assert-license mapvbvd

BuildArch:      noarch
# PyMapVBVD assumes the platform is little-endian
# https://bugzilla.redhat.com/show_bug.cgi?id=2225518
ExcludeArch:    s390x

%global common_description %{expand:
Python port of the Matlab mapVBVD tool for reading Siemens raw data 'twix'
(.dat) files.}

%description %{common_description}


%package -n python3-pymapvbvd
Summary:        %{summary}

# Provides for the actual importable module name, which is unfortunately
# different from the PyPI package name (pyMapVBVD).
%py_provides python3-mapvbvd

%description -n python3-pymapvbvd %{common_description}


%prep
%autosetup -n pymapvbvd-%{version} -p1
%setup -q -T -D -a 1 -c -n pymapvbvd-%{version}


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%check -a
%if %{undefined fc43} && %{undefined fc44}
# Test regression due to a “ValueError: object too deep for desired array” in
# scipy.interpolate.RectBivariateSpline in scipy 1.18.0 would be fixed by
# upgrading scipy to 1.18.1.
# https://bugzilla.redhat.com/show_bug.cgi?id=2521133#c3
k="${k-}${k+ and }not test_epi"
%endif

%pytest -k "${k-}" --verbose


%files -n python3-pymapvbvd -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
