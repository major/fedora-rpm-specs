# NOTE(gotmax23): I do not suggest that you use this backend.
# I am only packaging it since scancode-toolkit has adopted it upstream.
# If you need a backend with more features than flit, use setuptools or hatchling.
# This build backend does not conform to standards in multiple ways,
# including lacking support for PEP 639 (better licensing metadata)
# and encouraging the usage of multiple pyproject-*.toml files in the same directory.

%bcond tests 1

Name:           python-flot
Version:        0.7.3
Release:        %autorelease
Summary:        Simplified packaging of multiple python modules (fork of flit)

License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://flot.readthedocs.io/en/latest/
Source:         https://github.com/aboutcode-org/flot/archive/v%{version}/flot-%{version}.tar.gz

# Build backend does not bootstrap itself correctly.
Patch:          https://github.com/aboutcode-org/flot/pull/4.patch#/backend-path.patch
# Tests make incorrect assumptions.
Patch:          https://github.com/aboutcode-org/flot/pull/5.patch#/fix-test_editable.patch

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist testpath}
%endif

%description
%{summary}.


%package -n python3-flot
Summary:        %{summary}

%description -n python3-flot
%{summary}.


%prep
%autosetup -p1 -n flot-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flot


%check
%pyproject_check_import
%if %{with tests}
# RPM setting SOURCE_DATE_EPOCH messes up the tests
unset SOURCE_DATE_EPOCH
%pytest
%endif


%files -n python3-flot -f %{pyproject_files}
# flot doesn't provide the standardizied License-File metadata that
# %%pyproject_save_files uses to automatically handle license files like other buildsystems do.
# We therefore have to mark the file with %%license manually.
%license %{python3_sitelib}/flot-*.dist-info/LICENSE
%doc README.rst
%{_bindir}/flot


%changelog
%autochangelog
