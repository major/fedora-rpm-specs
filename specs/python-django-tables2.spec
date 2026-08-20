%global srcname django_tables2
%global pkgname django-tables2

Name:           python-%{pkgname}
Version:        2.8.0
Release:        %autorelease
Summary:        Table framework for Django

License:        BSD-2-Clause
URL:            https://github.com/jieter/{%pkgname}
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
django-tables2 simplifies the task of turning sets of data into HTML tables.
It has native support for pagination and sorting. It does for HTML tables
what django.forms does for HTML forms.}

%description %{_description}

%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
Obsoletes:      python-%{pkgname} < 1.2.3-5
Obsoletes:      python2-%{pkgname} < 1.2.3-5

%description -n python3-%{pkgname} %{_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
