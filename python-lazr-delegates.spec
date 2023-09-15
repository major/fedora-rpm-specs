Name:           python-lazr-delegates
Version:        2.1.0
Release:        %autorelease
Summary:        Easily write objects that delegate behavior

License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.delegates
Source:         %{pypi_source lazr.delegates}

BuildArch:      noarch
BuildRequires:  python3-devel


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
%autosetup -p1 -n lazr.delegates-%{version}


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


%changelog
%autochangelog
