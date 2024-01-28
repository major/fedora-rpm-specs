%global modname smartcols
%global libsmartcols_version 2.30.2

Name:           python-%{modname}
Version:        0.3.0
Release:        23%{?dist}
Summary:        Python bindings for util-linux libsmartcols-library

License:        GPL-3.0-or-later
URL:            https://github.com/ignatenkobrain/python-smartcols
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# git clone https://github.com/karelzak/util-linux.git
# cd util-linux
# git archive --format=tar.gz --prefix=util-linux/ -o libsmartcols-tests-%%{libsmartcols_version}.tar.gz v%%{libsmartcols_version} tests/ts/libsmartcols/ tests/expected/libsmartcols/
Source1:        libsmartcols-tests-%{libsmartcols_version}.tar.gz

# pytest 4 support
Patch1:         %{url}/pull/20.patch

BuildRequires:  gcc
BuildRequires:  glibc-langpack-en
BuildRequires:  pkgconfig(smartcols) >= %{libsmartcols_version}

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  python3-sphinx

%description doc
%{summary}.

%prep
%autosetup -a1 -p1

# Remove deprecated and problematic pytest-runner
sed 's|, "pytest-runner"\],|],|' -i setup.py

%build
%py3_build

# HACK, otherwise sphinx can't introspect dynamic library
ln -s build/lib.*-%{python3_version}/smartcols.*.so .
%{__python3} setup.py build_sphinx
rm -f doc/_build/html/.buildinfo

%install
%py3_install

%check
%pytest

%files -n python3-%{modname}
%license COPYING
%doc README.md
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}.*.so

%files doc
%doc examples doc/_build/html

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.3.0-20
- Rebuilt for Python 3.12

* Sun May 07 2023 Maxwell G <maxwell@gtmx.me> - 0.3.0-19
- Remove buildtime dependency on deprecated pytest-runner

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.0-16
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.0-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-5
- Drop python2 subpkg

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Rebuild for Python 3.6

* Fri Nov 18 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Tue Aug 23 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.1-2
- Skip continuous test as it stuck without PTY

* Tue Aug 23 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.1-1
- Initial package
