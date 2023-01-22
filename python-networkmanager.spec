%global srcname networkmanager

%global _description %{expand:
python-networkmanager wraps NetworkManagers D-Bus interface so you can be less
verbose when talking to NetworkManager from python.

All interfaces have been wrapped in classes, properties are exposed as python
properties and function calls are forwarded to the correct interface.}

Name:      python-%{srcname}
Version:   2.2
Release:   9%{?dist}

License:   MIT
Summary:   Easy communication with NetworkManager
URL:       https://github.com/seveas/%{name}
Source0:   %{pypi_source %{name}}

# https://github.com/seveas/python-networkmanager/pull/85
Patch100:  %{name}-main-loop-fix.patch
# https://github.com/seveas/python-networkmanager/pull/94
Patch101: %{name}-dns-field-fix.patch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

BuildArch: noarch

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname} %_description

%package doc
Summary: Example files for %{name}

%description doc
This package provides documentation and examples for the
%{name} package.

%prep
%autosetup

# Removing executable bit from examples...
find examples -type f -exec chmod a-x '{}' \;

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel
make man -C docs

%install
%pyproject_install
%pyproject_save_files NetworkManager

# Installing manpage...
install -d %{buildroot}%{_mandir}/man1/
install -m 0644 -p docs/_build/man/%{name}.1 %{buildroot}%{_mandir}/man1/

%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING

%files doc
%doc README
%doc examples
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2-7
- Rebuilt for Python 3.11

* Mon May 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2-6
- Fixed KeyError: dns (RHBZ#2080962).

* Thu Feb 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2-5
- Backported patch to allow runing without main loop (RHBZ#1972165).
- Converted SPEC to 202x-era guidelines.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2-2
- Rebuilt for Python 3.10

* Sun May 09 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2-1
- Updated to version 2.2.
- Performed SPEC cleanup.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1-2
- Rebuilt for Python 3.7

* Sat Apr 28 2018 John Dulaney <jdulaney@fedoraproject.org> - 2.1-1
- Update to latest release

* Thu Mar 22 2018 John Dulaney <jdulaney@fedoraproject.org> - 2.0.1-5
- Drop python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 John Dulaney <jdulaney@fedoraproject.org> - 2.0.1-1
- New release 2.0.1

* Sun Feb 12 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-7
- Correct typo

* Sun Feb 12 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-6
- modify chmod making example .py files non-executable

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-4
- Update requires.

* Wed Jan 25 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-3
- move manpage to docs subpackage and set cp to preserve timestamp

* Tue Jan 17 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-2
- Add Requires:  python-dbus
- Package examples in doc subpackage
- Clean up python3
- Add Provides:

* Wed Jan 11 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.2.1-1
- Initial Packaging
