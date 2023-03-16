# TODO adjust once this is implemented:
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%global modname  jaraco
%global projname %{modname}.stream
%global pkgname  %{modname}-stream

%bcond_without tests

Name:           python-%{pkgname}
Version:        3.0.3
Release:        %autorelease
Summary:        Routines for dealing with data streams

License:        MIT
URL:            https://github.com/jaraco/%{projname}
Source0:        %{pypi_source %{projname}}

# https://github.com/jaraco/jaraco.stream/pull/5
Patch1:         0001-Require-more_itertools.patch
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch2:         0002-Disable-linters.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Routines for handling streaming data, including a set of generators for
loading gzip data on the fly.}

%description %_description

%package     -n python3-%{pkgname}
Summary:        %{summary}
Requires:       python3-jaraco

%description -n python3-%{pkgname} %_description

%prep
%autosetup -n %{projname}-%{version}

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%if %{with tests}
%tox
%else
%pyproject_check_import -e jaraco.stream.test_gzip
%endif

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGES.rst
# Owned by python3dist(jaraco)
%exclude %dir %{python3_sitelib}/jaraco

%changelog
%autochangelog
