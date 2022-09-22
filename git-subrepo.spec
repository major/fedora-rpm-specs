Name: git-subrepo
Version: 0.4.3
Release: 5%{?dist}

License: MIT
Summary: Git Submodule Alternative
URL: https://github.com/ingydotnet/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires: git-core
BuildRequires: git-core
BuildRequires: make

%description
This git command "clones" an external git repo into a subdirectory
of your repo. Later on, upstream changes can be pulled in, and local
changes can be pushed back. Simple.

%prep
%autosetup -p1
sed -e 's@/usr/bin/env bash@/usr/bin/bash@g' -i {ext/bashplus/bin/bash+,lib/git-subrepo,lib/git-subrepo.d/help-functions.bash}
sed -e '1 i #!/usr/bin/bash' -i ext/bashplus/lib/bash+.bash

%build
# Nothing to build...

%install
%make_install PREFIX=%{_prefix}

%files
%license License
%doc ReadMe.pod Intro.pod Changes
%{_libexecdir}/git-core/%{name}
%{_libexecdir}/git-core/%{name}.d
%{_mandir}/man1/*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.3-1
- Updated to version 0.4.3.

* Sat Nov 21 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.2-1
- Updated to version 0.4.2.

* Wed Nov 11 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.1-1
- Updated to version 0.4.1.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2.20170206gita7ee886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.1-1.20170206gita7ee886
- Initial release.
