Name:           python-pytest-localserver
Version:        0.7.0
Release:        1%{?dist}
Summary:        py.test plugin to test server connections locally

License:        MIT
URL:            https://github.com/pytest-dev/pytest-localserver
# The package uses setuptools_scm, GitHub tarball will not work
Source0:        %{pypi_source pytest-localserver}
# aiosmtpd.Controller._stop is replaced with aiosmtpd.Controller.cancel_tasks in
# Fedora python-aiosmtpd::0001-Implement-Unthreaded-Controller-256.patch
Patch1:         0002-pytest-localserver-0.6.0-replace-aiosmtpd.Controller._stop.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-werkzeug

%global _description %{expand:
pytest-localserver is a plugin for the pytest testing framework which enables
you to test server connections locally.}

%description %_description

%package -n python3-pytest-localserver
Summary:        %{summary}

%description -n python3-pytest-localserver %_description


%prep
%autosetup -p1 -n pytest-localserver-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_localserver


%check
%tox


%files -n python3-pytest-localserver -f %{pyproject_files}
%doc README.rst CHANGES
%license LICENSE

%changelog
* Tue Aug 30 2022 Paul Wouters <paul.wouters@aiven.io - 0.7.0-1
- Resolves: rhbz#2122508 python-pytest-localserver-0.7.0 is available

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Roman Inflianskas <rominf@aiven.io> - 0.6.0-1
- Update to 0.6.0

* Tue Dec 28 2021 Roman Inflianskas <rominf@aiven.io> - 0.5.1.20211213.post0-1
- Initial package
