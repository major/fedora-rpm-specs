%if 0%{?rhel}
%bcond tests    0
%else
%bcond tests    1
%endif

Name:           python-flufl-bounce
Version:        4.0
Release:        %autorelease
Summary:        Email bounce detectors

License:        Apache-2.0
URL:            https://fluflbounce.readthedocs.io/en/latest/
Source:         %{pypi_source flufl.bounce}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pkg-resources


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
The flufl.bounce library provides a set of heuristics and an API for detecting
the original bouncing email addresses from a bounce message. Many formats found
in the wild are supported, as are VERP and RFC 3464 (DSN).}


%description %_description

%package -n     python3-flufl-bounce
Summary:        %{summary}

%description -n python3-flufl-bounce %_description


%prep
%autosetup -p1 -n flufl.bounce-%{version}


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
%pyproject_save_files flufl


%check
%if %{with tests}
%pyproject_check_import
%endif


%files -n python3-flufl-bounce -f %{pyproject_files}
%{python3_sitelib}/flufl.bounce-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
