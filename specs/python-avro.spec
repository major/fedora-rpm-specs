Name:           python-avro
Version:        1.12.0
Release:        1%{?dist}
Summary:        Python bindings for Apache Avro data serialization system


License:        Apache-2.0
URL:            https://github.com/apache/avro
Source:         https://github.com/apache/avro/archive/refs/tags/release-%{version}.tar.gz
Patch0:         0001-remove-ipc-tests-as-they-require-internet-connection.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(tox)
BuildRequires:  python3dist(black)
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3dist(tox-current-env)
BuildRequires:  python3dist(coverage)

%global _description %{expand:
Apache Avro is a data serialization system.
This package is Python bindings for Apache Avro.}

%description %_description

%package -n python3-avro
Summary: %{summary}

%description -n python3-avro %_description


%prep
%autosetup -p1 -n avro-release-%{version}


%generate_buildrequires
cd lang/py
%pyproject_buildrequires


%build
cd lang/py
%pyproject_wheel


%install
cd lang/py
%pyproject_install
%pyproject_save_files avro


%check
%pyproject_check_import
cd lang/py
%tox


%files -n python3-avro -f %{pyproject_files}
%doc README.*
%license LICENSE.txt
%{_bindir}/avro


%changelog
%autochangelog
