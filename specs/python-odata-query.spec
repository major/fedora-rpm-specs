%global forgeurl https://github.com/gorilla-co/odata-query
Version:        0.11.0
%forgemeta

Name:           python-odata-query
Release:        %autorelease
Summary:        An OData v4 query parser and transpiler for Python

License:        MIT
URL:            https://odata-query.readthedocs.io
Source0:        %{forgesource}
Source1:        tox.toml

BuildArch:      noarch
BuildRequires:  python3-devel
# These requirements are not picked up automatically
BuildRequires: python3-uv-build
BuildRequires: python3-sly
BuildRequires: python3dist(pytest-django)
BuildRequires: python3-tox-current-env


%global _description %{expand:
odata-query is a library that parses OData v4 filter strings, and can convert
them to other forms such as Django Queries, SQLAlchemy Queries, or just plain
SQL.}

%description %_description

%package -n python3-odata-query
Summary:        %{summary}

%description -n python3-odata-query %_description

%pyproject_extras_subpkg -n python3-odata-query django sqlalchemy

%prep
%forgeautosetup
# Unpin upper versions, if it doesn't work, the build will fail
%pyproject_patch_dependency pytest:drop_upper
%pyproject_patch_dependency dateutil:drop_upper
%pyproject_patch_dependency uv_build:drop_upper

cp -p %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files odata_query


%check
%tox

%files -n python3-odata-query -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
