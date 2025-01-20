%global srcname django-cacheops
%global desc %{expand: \
A slick app that supports automatic or manual queryset caching
and automatic granular event-driven invalidation.

It uses redis as backend for ORM cache and redis or filesystem
for simple time-invalidated one.

And there is more to it:

  * decorators to cache any user function or view as a queryset or by time
  * extensions for django and jinja2 templates
  * transparent transaction support
  * dog-pile prevention mechanism
  * a couple of hacks to make django faster}

Name:           python-%{srcname}
Version:        6.1
Release:        9%{?dist}
Summary:        ORM cache with automatic granular event-driven invalidation for Django

License:        BSD-3-Clause
URL:            https://github.com/Suor/%{srcname}
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-django
BuildRequires:	redis

%description %{desc}

%package     -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{desc}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cacheops

%check
# Launching a redis server for the tests
mkdir -p data
pidfile=$PWD/redis.pid
%{_bindir}/redis-server \
    --bind 127.0.0.1 \
    --port 6379	\
    --daemonize yes \
    --logfile $PWD/redis.log \
    --dir $PWD/data \
    --pidfile $pidfile

export DJANGO_SETTINGS_MODULE=tests.settings
# skipping LockingTests because before_after is too old and not in Fedora
%pytest -v -k "not LockingTests"

# shutting down the server
if [ -f $pidfile ]; then
    %{_bindir}/redis-cli -p 6379 shutdown
fi
cat $PWD/redis.log

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 6.1-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 6.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 6.1-1
- Update to 6.1 (RHBZ #2090960 + #2098886)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 6.0-1
- Update to 6.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.1-1
- Update to 5.1

* Sun Aug 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1-1
- Initial package
