# TODO possibly adjust modname once this is implemented:
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%global modname  coherent
%global projname %{modname}.licensed
%global srcname  %{modname}_licensed
%global pkgname  %{modname}-licensed

Name:           python-%{pkgname}
Version:        0.5.2
Release:        %autorelease
Summary:        License management tooling for Coherent System and skeleton projects
License:        MIT
URL:            https://github.com/coherent-oss/%{projname}
Source:         %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This library was built for coherent.build and skeleton projects to inject a
license file at build time to reflect the license declared in the License
Expression.}

%description %_description

%package     -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%pyproject_check_import

%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
