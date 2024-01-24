Name:           python-pytest-localserver
Version:        0.8.0
Release:        2%{?dist}
Summary:        pytest plugin to test server connections locally

License:        MIT
URL:            https://github.com/pytest-dev/pytest-localserver
# The package uses setuptools_scm, GitHub tarball will not work
Source0:        %{pypi_source pytest-localserver}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
pytest-localserver is a plugin for the pytest testing framework which enables
you to test server connections locally.}

%description %_description

%package -n python3-pytest-localserver
Summary:        %{summary}

%description -n python3-pytest-localserver %_description

%pyproject_extras_subpkg -n python3-pytest-localserver smtp


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
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 29 2023 Roman Inflianskas <rominf@aiven.io> - 0.8.0-1
- Update to 0.8.0 (fedora#2223161)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 0.7.1-2
- Rebuilt for Python 3.12

* Sat Jul 01 2023 Roman Inflianskas <rominf@aiven.io> - 0.7.1-1
- Update to 0.7.1 (resolve rhbz#2162933)
- Add smtp extra

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 30 2022 Paul Wouters <paul.wouters@aiven.io - 0.7.0-1
- Resolves: rhbz#2122508 python-pytest-localserver-0.7.0 is available

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Roman Inflianskas <rominf@aiven.io> - 0.6.0-1
- Update to 0.6.0

* Tue Dec 28 2021 Roman Inflianskas <rominf@aiven.io> - 0.5.1.20211213.post0-1
- Initial package
