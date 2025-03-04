# need to reconfigure logging to run tests
# FileNotFoundError: [Errno 2] No such file or directory: '/opt/mailman/web/logs/mailmanweb.log'           
%bcond tests 0

Name:           python-mailman-web
Version:        0.0.9
Release:        %autorelease
Summary:        Mailman 3 Web interface

License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/mailman-web
Source:         %{pypi_source mailman_web}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-django)
%endif

%global _description %{expand:
This is a Django project that contains default settings and URL settings
for Mailman 3 Web interface. It consists of the following sub-projects:

- Postorius
- Hyperkitty
}

%description %_description

%package -n     python3-mailman-web
Summary:        %{summary}

%description -n python3-mailman-web %_description


%prep
%autosetup -p1 -n mailman_web-%{version}

# Remove shebang from Python files
for file in mailman_web/manage.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $file > $file.new &&
 touch -r $file $file.new &&
 mv $file.new $file
done



%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files mailman_web
mkdir -p %{buildroot}%{_sysconfdir}/mailman3


%check
export DJANGO_SETTINGS_MODULE=mailman_web.settings
%pyproject_check_import -e mailman_web.tests.test_basic -e mailman_web.urls
%if %{with tests}
%pytest --ds=mailman_web.tests.settings
%endif


%files -n python3-mailman-web -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%dir %{_sysconfdir}/mailman3
%ghost %config(noreplace) %{_sysconfdir}/mailman3/settings.py
%{_bindir}/mailman-web


%changelog
%autochangelog
