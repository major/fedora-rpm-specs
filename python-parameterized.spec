Name:           python-parameterized
Version:        0.8.1
Release:        %autorelease
Summary:        Parameterized testing with any Python test framework

License:        BSD-2-Clause-Views
URL:            https://github.com/wolever/parameterized
Source:         %{pypi_source parameterized}

# pytest 4+ support
# Backported from https://github.com/wolever/parameterized/pull/116
# Removed changes for CI configuration
# Added https://github.com/wolever/parameterized/pull/116/files#r850666754
# Added https://github.com/wolever/parameterized/pull/116/files#r892932605
# Fixes test failures with pytest 7+
Patch:          pytest4.patch
# Allow running tests without nose
# https://github.com/wolever/parameterized/pull/145
#
# Rebased to apply cleanly on top of pytest4.patch.
Patch:          parameterized-0.8.1-no-nose.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Upstream supports tox, and in theory we could generate these by something like:
#   %%pyproject_buildrequires -t -e %%{toxenv}-nose2,%%{toxenv}-pytest4,%%{toxenv}-unit
# but upstream is not keeping up, and we would also have to patch in support
# for environments after py36. It’s not worth it; we can more easily run the
# tests manually and specify the BR’s manually. See %%check.
BuildRequires:  python3dist(nose2)
BuildRequires:  python3dist(pytest)

%description
%{summary}.


%package -n python3-parameterized
Summary:        %{summary}

%description -n python3-parameterized
%{summary}.


%prep
%autosetup -p1 -n parameterized-%{version}
sed -i 's|^import mock|from unittest import mock|' parameterized/test.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files parameterized


%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{python3} -m nose2 -v
%pytest parameterized/test.py
%{python3} -m unittest -v parameterized.test


%files -n python3-parameterized -f %{pyproject_files}
# pyproject_files handles LICENSE.txt; verify with “rpm -qL -p …”
%doc CHANGELOG.txt README.rst


%changelog
%autochangelog
