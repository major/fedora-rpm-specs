%global module python-binary-memcached
%global srcname %{module}


Name:           %{module}
Version:        0.33.0
Release:        %autorelease
Summary:        Access memcached via its binary protocol

License:        MIT
URL:            https://github.com/jaysonsantos/%{module}
Source:         https://github.com/jaysonsantos/%{module}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  memcached
# For tests
BuildRequires:  cyrus-sasl
BuildRequires:  cyrus-sasl-plain


%global _description %{expand:
A pure python module (thread safe) to access memcached
via it’s binary with SASL authentication support.}


%description %_description


%package -n python3-binary-memcached
Summary:        %{summary}
Requires:       memcached


%description -n python3-binary-memcached
%_description


%prep
%autosetup -p1 -n %{module}-%{version}

%pyproject_patch_dependency ruff:ignore
%pyproject_patch_dependency pytest-cov:ignore

sed -i -e '/^\s*ruff /d' -e '/^\s*lint$/d' tox.ini

# README.rst is just a symlink to real docs
cp -p --remove-destination docs/intro.rst README.rst

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
