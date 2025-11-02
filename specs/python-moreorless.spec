%global srcname moreorless

%bcond_without tests

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        Python diff wrapper
License:        MIT
URL:            https://github.com/thatch/moreorless/
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist setuptools_scm}
%if %{with tests}
BuildRequires:  %{py3_dist coverage}
BuildRequires:  %{py3_dist parameterized}
%endif


%global _description %{expand:
This is a thin wrapper around difflib.unified_diff that Does The Right Thing for
"No newline at eof". The args are also simplified compared to difflib.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l moreorless


%check
%if %{with tests}
%{python3} -m coverage run -m moreorless.tests -v
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%exclude %{python3_sitelib}/%{srcname}/py.typed


%changelog
%autochangelog
