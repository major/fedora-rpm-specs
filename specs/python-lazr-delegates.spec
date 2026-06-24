Name:           python-lazr-delegates
Version:        2.1.1
Release:        %autorelease
Summary:        Easily write objects that delegate behavior

License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.delegates
Source:         %{pypi_source lazr_delegates}

BuildArch:      noarch
BuildRequires:  python3-devel
%if 0%{?python3_version_nodots} >= 315
# only needed for tests
# at runtime there is a fallback if this is not available, though somehow
# pkg_resources is still tried first
# see
# src/lazr/__init__.py:    import pkg_resources
# src/lazr/delegates/tests/test_docs.py:from pkg_resources import (
BuildRequires:  python3-pkg-resources
%endif


%global _description %{expand:
The lazr.delegates package makes it easy to write objects that delegate behavior
to another object. The new object adds some property or behavior on to the other
object, while still providing the underlying interface, and delegating
behavior.}


%description %_description

%package -n     python3-lazr-delegates
Summary:        %{summary}

%description -n python3-lazr-delegates %_description


%prep
%autosetup -p1 -n lazr_delegates-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files lazr


%check
%pyproject_check_import
%tox


%files -n python3-lazr-delegates -f %{pyproject_files}
%{python3_sitelib}/lazr.delegates-%{version}-py%{python3_version}-nspkg.pth
%exclude %{python3_sitelib}/lazr/delegates/tests


%changelog
%autochangelog
