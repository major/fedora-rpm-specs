%global         jqversion 1.8.1
Name:           python-jq
Version:        1.11.0
Release:        %autorelease
Summary:        Python bindings for jq

License:        BSD-2-Clause
URL:            https://github.com/mwilliamson/jq.py
Source:         %pypi_source jq
# Test requirements missing from sdist
# https://github.com/mwilliamson/jq.py/pull/130
Patch:          add-test-requirements.patch

BuildRequires:  python3-devel
BuildRequires:  jq-devel = %{jqversion}
BuildRequires:  oniguruma-devel
BuildRequires:  gcc


%global _description %{expand:
Python bindings for jq which is a lightweight and flexible JSON processor.}


%description %_description


%package -n python3-jq
Summary:        %{summary}


%description -n python3-jq %_description


%prep
%autosetup -p1 -n jq-%{version}
# Remove bundled sources
rm deps/jq-%{jqversion}.tar.gz

# relax cython version.
sed -i 's/"cython==.*"/"cython"/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -t


%build
export JQPY_USE_SYSTEM_LIBS=1
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l jq


%check
%tox


%files -n python3-jq -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
