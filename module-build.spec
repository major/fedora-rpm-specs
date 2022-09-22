Name: module-build
Version: 0.2.1
Release: 2%{?dist}
Summary: Tool/library for building module streams locally.
License: MIT
BuildArch: noarch

URL: https://github.com/mcurlej/module-build
Source0: https://github.com/mcurlej/module-build/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: libmodulemd >= 2.13.0
BuildRequires: python3-gobject
BuildRequires: mock

Requires: createrepo_c
Requires: libmodulemd >= 2.13.0
Requires: mock
Requires: mock-scm


%description
A library and a cli tool for building module streams. 


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install


%check
%pytest


%files
%doc README.md
%license LICENSE
%{python3_sitelib}/module_build
%{python3_sitelib}/module_build-*.egg-info/
%{_bindir}/module-build


%changelog
* Tue Sep 20 2022 Martin Curlej <mcurlej@redhat.com> - 0.2.1-2
- Require mock-scm

* Thu Sep 08 2022 Martin Čurlej <mcurlej@redhat.com> - 0.2.1-1
- Build failure fix.
- Added MANIFEST.in file

* Fri Aug 19 2022 Marek Kulik <mkulik@redhat.com> - 0.2.0-1
- Rebase to v0.2.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.11

* Tue Feb 01 2022 Martin Čurlej <mcurlej@redhat.com> - 0.1.0-1
- Added the ability to build stand-alone module streams (mcurlej@redhat.com)
- Uses modular dependencies when building module streams (mcurlej@redhat.com)
- Resuming of a failed module stream build on the component level (mcurlej@redhat.com)
