%global pkg_name wtforms-sqlalchemy
%global module_name wtforms_sqlalchemy

Name:           python-%{pkg_name}
Version:        0.3.0
Release:        1%{?dist}
Summary:        WTForms integration for SQLAlchemy

License:        BSD
URL:            https://github.com/wtforms/%{pkg_name}
Source0:        %{url}/archive/%{version}/%{pkg_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
WTForms-SQLAlchemy is a fork of the wtforms.ext.sqlalchemy package
from WTForms. The package has been renamed to wtforms_sqlalchemy but
otherwise should function the same as wtforms.ext.sqlalchemy did.}

%description %_description

%package -n python3-%{pkg_name}
Summary:        %{summary}

%description -n python3-%{pkg_name} %_description


%prep
%autosetup -p1 -n %{pkg_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module_name}


%check
sed -i '/tests_require = coverage/d' setup.cfg
%tox


%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst
%doc CHANGES.rst
%license LICENSE.txt


%changelog
* Sun Dec 11 2022 Matěj Grabovský <mgrabovs@redhat.com> - 0.3.0-1
- Initial package
