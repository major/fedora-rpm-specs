%global commit d203a4d2bfb32a7a414abc0d4321a6672c428de6
%global date 20210623

%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     x2gowswrapper
Version:  0.0.0.1
Release:  0.7%{?dist}
Summary:  Helper utility for X2Go HTML5 client
License:  GPL-2.0-or-later
URL:      http://www.x2go.org
# git clone git://code.x2go.org/x2gowswrapper
# cd x2gowswrapper
# git archive --prefix=x2gowswrapper-0.0.0.1-20210623gitd203a4d/ d203a4d2bfb32a7a414abc0d4321a6672c428de6 | gzip >../x2gowswrapper-0.0.0.1-20210623gitd203a4d.tar.gz
Source0:        %{name}/%{name}-%{version}-%{date}git%{shortcommit}.tar.gz

BuildRequires: gcc
BuildRequires: qt5-qtbase-devel

%description
The helper utility x2gowswrapper provides server-side facilities necessary
to support the X2Go HTML5 client.

%prep
%autosetup -n %{name}-%{version}-%{date}git%{shortcommit}

%build
%qmake_qt5
%make_build

%install
install -D -p --mode=755 x2gowswrapper %{buildroot}%{_sbindir}/x2gowswrapper
install -D -p --mode=644 man/man1/x2gowswrapper.1 %{buildroot}%{_mandir}/man1/x2gowswrapper.1

%files
%license COPYING
%{_sbindir}/x2gowswrapper
%{_mandir}/man1/x2gowswrapper.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.1-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.1-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.1-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.1-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.1-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 21 2022 W. Michael Petullo <mike@flyn.org> - 0.0.0.1-0.2
- BuildRequires gcc
- Use wildcard with man page path
- Use qtmake macro and build debuginfo

* Thu Jan 13 2022 W. Michael Petullo <mike@flyn.org> - 0.0.0.1-0.1
- Initial version of the package
