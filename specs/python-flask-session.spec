Name:           python-flask-session
Version:        0.5.0
Release:        6%{?dist}
Summary:        Server side session extension for Flask

License:        BSD-3-Clause
URL:            https://github.com/pallets-eco/flask-session
Source:         %{url}/archive/%{version}/Flask-Session-%{version}.tar.gz

# https://github.com/pallets-eco/flask-session/pull/189/commits/73166f72c34c92f92794fabe24839da10ed3670d
# Werkzeug/Flask 3.x Support
Patch01:        73166f72c34c92f92794fabe24839da10ed3670d.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Extra testing deps
BuildRequires: redis
BuildRequires: python3-redis

# These are for the remaining tests that aren't working properly at the moment
# See the check section
#BuildRequires: python3-pymongo
#BuildRequires: python3-memcached
#BuildRequires: python3-flask-sqlalchemy

%global _description %{expand:
Flask-Session is an extension for Flask that adds support for server-side
sessions to your application.}

%description %_description

%package -n python3-flask-session
Summary:        %{summary}

%description -n python3-flask-session %_description

%prep
%autosetup -p1 -n flask-session-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files flask_session

%check
redis-server &
# Enable only working backends tests:
# Mongo test doesn't work with pymongo >= 4
# Sqla test expects a pre-created DB
# Memchached just doesn't work...
%pytest -k 'test_null_session or test_redis_session or test_filesystem_session'
kill %1

%files -n python3-flask-session -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Python Maint <python-maint@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.5.0-1
- Release 0.5.0, Initial Packaging
