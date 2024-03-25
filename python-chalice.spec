%global srcname chalice

Name:           python-%{srcname}
Version:        1.30.0
Release:        %autorelease
Summary:        Python Serverless Microframework for AWS

License:        Apache-2.0
URL:            https://github.com/aws/chalice
# The PyPI tarball doesn't include tests so use GitHub instead
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
Chalice is a framework for writing serverless apps in python. It allows you to
quickly create and deploy applications that use AWS Lambda.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Relax inquirer version pin
sed -i "s:'inquirer.*$:'inquirer',:" setup.py
# Unpin pip to allow newer version
sed -i "s/'pip>=9,<23.4',/'pip>=9,<24.1',/" setup.py

%generate_buildrequires
%pyproject_buildrequires -r requirements-test.in

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# Skip tests requiring Internet access or deal with packaging
%pytest \
  --ignore=chalice/templates \
  --ignore=docs \
  --ignore=tests/aws/test_websockets.py \
  --ignore=tests/unit/deploy/test_packager.py \
  --ignore=tests/integration/test_package.py \
  --ignore=tests/aws/test_features.py \
  --deselect=tests/functional/cli/test_cli.py::test_can_generate_pipeline_for_all \
  --ignore=tests/functional/test_awsclient.py \

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/%{srcname}

%changelog
%autochangelog
