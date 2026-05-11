%global module python-binary-memcached
%global srcname %{module}


Name:           %{module}
Version:        0.32.0
Release:        %autorelease
Summary:        Python module python-binary-memcached

License:        MIT
URL:            https://github.com/jaysonsantos/%{module}
Source:         https://github.com/jaysonsantos/%{module}/archive/refs/tags/v%{version}.tar.gz
Patch:          https://github.com/jaysonsantos/python-binary-memcached/pull/264.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  memcached


%global _description %{expand:
A pure python module (thread safe) to access memcached via it’s binary with SASL auth support.}


%description %_description


%package -n python3-binary-memcached
Summary:        %{summary}
Requires:       memcached


%description -n python3-binary-memcached
%_description


%prep
%autosetup -p1 -n %{module}-%{version}

sed -i \
  -e '/^flake8/d' \
  -e '/^mock/d' \
  -e '/^pytest-cov/d' \
  -e '/python_version < /d' \
  -e 's/^pytest.*/pytest/' \
  -e 's/^trustme.*/trustme/' \
  requirements_test.txt

sed -i '/flake8/d' tox.ini


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l bmemcached


%check
%tox


%files -n python3-binary-memcached -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
