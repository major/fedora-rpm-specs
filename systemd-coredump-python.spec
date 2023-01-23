Name:           systemd-coredump-python
Version:        2
Release:        21%{?dist}
Summary:        systemd-coredump helper to log Python exceptions

License:        GPLv2+
URL:            https://github.com/systemd/systemd-coredump-python
Source0:        https://github.com/systemd/systemd-coredump-python/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         0001-In-demo-mode-do-not-install-handler-manually.patch

BuildRequires:  python3-devel

BuildArch:      noarch

%global _description \
Python module which hooks into the sys.excepthook to log backtraces \
in the journal.

%description %_description

%package -n python3-systemd-coredump
Summary:        %{summary}
Conflicts:      systemd < 233

%{?python_provide:%python_provide python3-systemd-coredump}

%description -n python3-systemd-coredump %_description

%prep
%autosetup -p1

# I messed that up, it'll be fixed in next release, pinky promise
sed -i "s/'1'/'2'/" setup.py

%build
%py3_build

%install
%py3_install

# %%check
# there are no useful checks, the stuff in tests/ is only useful for development so far

%files -n python3-systemd-coredump
%license COPYING
%doc README
%{python3_sitelib}/systemd_coredump_exception_handler.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/systemd_coredump.pth
%{python3_sitelib}/systemd_coredump_python-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2-19
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2-16
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2-13
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2-11
- Subpackage python2-systemd-coredump has been removed,
  https://fedoraproject.org/wiki/Changes/RetirePython2.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2-9
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 zbyszek <zbyszek@in.waw.pl> - 2-2
- Add small patch to avoid logging the exception twice in demo mode

* Sun Mar  5 2017 zbyszek <zbyszek@in.waw.pl> - 2-1
- Initial packaging
