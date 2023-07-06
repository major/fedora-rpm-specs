%global srcname parse_type

Name:           python-%{srcname}
Version:        0.6.2
Release:        %autorelease
Summary:        Simplifies to build parse types based on the parse module

License:        MIT
URL:            http://github.com/jenisys/parse_type
Source0:        %{url}/archive/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%global _description \
"parse_type" extends the "parse" module (opposite of\
"string.format()") with the following features:\
* build type converters for common use cases (enum/mapping, choice)\
* build a type converter with a cardinality constraint (0..1,\
  0..*, 1..*) from the type converter with cardinality=1.\
* compose a type converter from other type converters\
* an extended parser that supports the CardinalityField naming\
  schema and creates missing type variants (0..1, 0..*, 1..*) from\
  the primary type converter

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

# remove deps on pytest-html
sed -i -e '/^\s*"pytest-html >= /d' setup.py
sed -i -e '/^\s*"pytest-html >= /d' pyproject.toml
sed -i -e '/^pytest-html >= /d' py.requirements/testing.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# we don't care about html output from pytest, plus pytest-html isn't in fedora
sed -i \
  -e '/^addopts = --metadata PACKAGE_UNDER_TEST parse_type/d' \
  -e '/^    --metadata PACKAGE_VERSION [0-9].[0-9].[0-9]/d' \
  -e '\%    --html=build/testing/report.html --self-contained-html%d' \
  -e '\%    --junit-xml=build/testing/report.xml%d' \
  pytest.ini
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
