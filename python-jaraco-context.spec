# TODO adjust once this is implemented:
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%global modname  jaraco
%global projname %{modname}.context
%global pkgname  %{modname}-context

%bcond_without tests

Name:           python-%{pkgname}
Version:        4.3.0
Release:        %autorelease
Summary:        Context managers by jaraco

License:        MIT
URL:            https://github.com/jaraco/%{projname}
Source0:        %{pypi_source %{projname}}

Patch1:         0001-Disable-linters.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Context managers by jaraco.}

%description %_description

%package     -n python3-%{pkgname}
Summary:        %{summary}

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
%pyproject_check_import
%endif

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGES.rst

%changelog
%autochangelog
