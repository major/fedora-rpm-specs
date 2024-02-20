%global srcname sqlalchemy_schemadisplay
%global gittag 2.0

Name:           python-%{srcname}
Version:        2.0
Release:        %autorelease
Summary:        Turn SQLAlchemy DB Model into a graph

License:        MIT
URL:            https://github.com/fschulze/%{srcname}
Source0:        %{url}/archive/%{gittag}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# For tests
BuildRequires:  %{py3_dist pytest}

%description
Turn SQLAlchemy DB Model into a graph.


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import
%pytest -q tests


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
