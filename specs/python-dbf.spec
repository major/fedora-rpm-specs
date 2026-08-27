%global pypi_name dbf
%global sum Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf
%global desc Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf\
files (including memos)\
\
Currently supports dBase III, Clipper, FoxPro, and Visual FoxPro tables. Text is\
returned as unicode, and codepage settings in tables are honored. Memos and Null\
fields are supported.

Name:           python-%{pypi_name}
Version:        0.99.11
Release:        %autorelease
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         remove-distutil.patch

BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{sum}
BuildRequires:  python3-devel
Requires:       python3-aenum

%description -n python3-%{pypi_name}
%{desc}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Correct line endings for setup.py
sed -i "s|\r||g" setup.py
rm -f dbf/ver_32.py
rm -f dbf/ver_2.py
sed -i "s|\r||g" dbf/README.md


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%pyproject_check_import -e dbf.index
%{py3_test_envvars} %{python3} -m dbf.test


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc dbf/README.md
%license dbf/LICENSE

%changelog
%autochangelog
