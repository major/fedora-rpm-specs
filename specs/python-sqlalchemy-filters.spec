%global pypi_name sqlalchemy-filters

Name:           python-%{pypi_name}
Version:        0.13.0
Release:        %autorelease
Summary:        A library to filter SQLAlchemy queries

License:        Apache-2.0
URL:            https://github.com/juliotrigo/sqlalchemy-filters
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel


%description
Filter, sort and paginate SQLAlchemy query
objects. Ideal for exposing these actions over a REST API.


%package -n     python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name}
Filter, sort and paginate SQLAlchemy query
objects. Ideal for exposing these actions over a REST API.


%prep
%autosetup -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l sqlalchemy_filters


%check
%pyproject_check_import sqlalchemy_filters


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE


%changelog
%autochangelog
