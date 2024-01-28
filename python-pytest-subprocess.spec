Name:           python-pytest-subprocess
Version:        1.5.0
Release:        5%{?dist}
Summary:        A plugin to fake subprocess for pytest

License:        MIT
URL:            https://github.com/aklajnert/pytest-subprocess
Source0:        %{url}/archive/%{version}/pytest-subprocess-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The plugin adds the fake_subprocess fixture. It can be used it to register
subprocess results so you won't need to rely on the real processes.
The plugin hooks on the subprocess.Popen(), which is the base for other
subprocess functions. That makes the subprocess.run(), subprocess.call(),
subprocess.check_call() and subprocess.check_output() methods also functional.}

%description %_description

%package -n python3-pytest-subprocess
Summary:        %{summary}

%description -n python3-pytest-subprocess %_description


%prep
%autosetup -p1 -n pytest-subprocess-%{version}
# avoid unneeded test dependencies
sed -Ei '/\bcoverage\b/d' setup.py


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_subprocess


%check
%pytest


%files -n python3-pytest-subprocess -f %{pyproject_files}
%doc README.rst HISTORY.rst


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.12

* Wed Feb 15 2023 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-1
- Update to 1.5.0
- Fixes: rhbz#2165202

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 04 2022 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-1
- Update to 1.4.2
- Fixes: rhbz#2131525
- Drop build-time dependency on python3-coverage

* Mon Sep 19 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.4.1-1
- Update to 1.4.1
- Fixes: rhbz#2052392

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.11

* Thu Jan 27 2022 Karolina Surma <ksurma@redhat.com> - 1.4.0-1
- Update to 1.4.0
- Fixes: rhbz#2012451

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jul 26 2021 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-1
- Initial package
- Fixes: rhbz#1985993
