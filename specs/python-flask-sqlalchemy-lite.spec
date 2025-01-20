%global srcname flask_sqlalchemy_lite

Name:           python-flask-sqlalchemy-lite
Version:        0.1.0
Release:        3%{?dist}
Summary:        Adds SQLAlchemy support to Flask application

License:        MIT
URL:            https://github.com/pallets-eco/flask-sqlalchemy-lite
Source0:        %{pypi_source flask_sqlalchemy_lite}
# Tighten depenency to avoid ambiguous python3dist(sqlalchemy[asyncio]) BR
# (Fedora provides multiple python-sqlalchemyX.Y versions)
Patch0:         flask_sqlalchemy_lite-dep.patch

BuildArch:      noarch

%description
Integrate SQLAlchemy with Flask. Use Flask's config to define SQLAlchemy
database engines. Create SQLAlchemy ORM sessions that are cleaned up
automatically after requests.

Intended to be a replacement for Flask-SQLAlchemy. Unlike the prior extension,
this one does not attempt to manage the model base class, tables, metadata, or
multiple binds for sessions. This makes the extension much simpler, letting the
developer use standard SQLAlchemy instead.


%package -n python3-flask-sqlalchemy-lite
Summary:        Adds SQLAlchemy support to Flask application
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%py_provides    python3-%{srcname}

%description -n python3-flask-sqlalchemy-lite
Integrate SQLAlchemy with Flask. Use Flask's config to define SQLAlchemy
database engines. Create SQLAlchemy ORM sessions that are cleaned up
automatically after requests.

Intended to be a replacement for Flask-SQLAlchemy. Unlike the prior extension,
this one does not attempt to manage the model base class, tables, metadata, or
multiple binds for sessions. This makes the extension much simpler, letting the
developer use standard SQLAlchemy instead.

Python 3 version.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flask_sqlalchemy_lite


%check
%pyproject_check_import


%files -n python3-flask-sqlalchemy-lite -f %{pyproject_files}
%license LICENSE.txt
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 17 2024 Sandro Mani <manisandro@gmail.com> - 0.1.0-2
- Specify parameter to pypi_source

* Fri Nov 15 2024 Sandro Mani <manisandro@gmail.com> - 0.1.0-1
- Initial package
