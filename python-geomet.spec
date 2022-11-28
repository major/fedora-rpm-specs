%global srcname geomet

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        GeoJSON <-> WKT/WKB conversion utilities

License:        Apache-2.0
URL:            https://github.com/geomet/geomet
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%description
Convert GeoJSON to WKT/WKB (Well-Known Text/Binary), and vice versa.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Convert GeoJSON to WKT/WKB (Well-Known Text/Binary), and vice versa.


%prep
%autosetup -n %{srcname}-%{version}

# Remove unnecessary shebang
for file in geomet/tool.py; do
  sed -i.orig -e '1d' ${file} && \
  touch -r ${file}.orig ${file} && \
  rm ${file}.orig
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{python3} setup.py test

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%{_bindir}/geomet

%changelog
%autochangelog
