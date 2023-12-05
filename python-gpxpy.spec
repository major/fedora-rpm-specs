%global srcname gpxpy

Name:           python-%{srcname}
Version:        1.6.2
Release:        %autorelease
Summary:        GPX file parser and GPS track manipulation library

License:        Apache-2.0
URL:            https://github.com/tkrajina/gpxpy
Source0:        %pypi_source %{srcname}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{summary}

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
%{python3} test.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/gpxinfo

%changelog
%autochangelog
