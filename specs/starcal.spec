%global pkg_name %{name}3

Name:           starcal
Version:        3.2.2
Release:        4%{?dist}
Summary:        A full-featured international calendar written in Python

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://ilius.github.io/starcal/
Source0:        https://github.com/ilius/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:       python3-gobject python3-httplib2 python3-psutil python3-cairo
Requires:       python3-dateutil python3-cachetools python3-requests
Requires:       libappindicator-gtk3

Recommends:     gtksourceview4 python3-igraph python3-pygit2
Suggests:       lxqt-openssh-askpass ntpdate

BuildArch:      noarch
BuildRequires:  python3-devel desktop-file-utils gettext git
BuildRequires:  python3-setuptools

%description
StarCalendar is a full-featured international calendar written in Python,
that supports Jalai(Iranian), Hijri(Islamic), and Indian National calendars,
as well as common English(Gregorian) calendar

%prep
%autosetup -S git -n %{name}-%{version}
find -type f -name "*.py*" -exec chmod a+x {} \;
find -type f -exec \
   sed -i '1s=^#!/usr/bin/\(python\|env python\)[^ ]*\(.*\)$=#!%{__python3}\2=' {} \;
find -name "*.py" -exec sh -c 'if ! grep "^#\!" {} &> /dev/null;  then \
   sed -i -e "1i#!%{__python3}" {}; fi'  \;


%build

%install
echo | ./distro/base/install.sh %{buildroot} --for-pkg --prefix=%{_prefix}

# cleanups
rm -rf %{buildroot}%{_datadir}/doc/
rm -rf      \
  %{buildroot}%{_datadir}/%{pkg_name}/{*install*,README.md,donate} \
  %{buildroot}%{_datadir}/%{pkg_name}/locale.d

desktop-file-install     \
  --delete-original \
  --remove-category=Utility --set-icon=%{pkg_name}2 \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{pkg_name}.desktop

%find_lang %{pkg_name}

%files -f %{pkg_name}.lang
%doc authors donate README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{pkg_name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/%{pkg_name}*.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.2-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 19 2024 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.2.2-1
- New upstream version, with updated calendar for 1403

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 03 2023 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.2.1-1
- New upstream version, with updated Hijri calendar

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.2.0-1
- New upstream version, with many changes

* Thu Nov 03 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.13-1
- New upstream version, fix f37 compatibility and other fixes

* Sat Aug 06 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.11-6
- Mark as compatible with python 3.11

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.11-3
- Add support for python 3.10

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.11-1
- Update calendar to latest version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.10-1
- Update to 3.1.10 upstream release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.9-1
- Update to 3.1.9, with calendar updates

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.3-1
- Update to 3.1.3

* Fri Feb 15 2019 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.7-5.20190216git9178f975
- Add python 3.7 compatibility

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.7-2
- Rebuilt for Python 3.7

* Wed Mar 28 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.7-1
- New version including updated calendar

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.6-1
- New bugfix release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.5-1
- new version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-2
- Rebuild for Python 3.6

* Sat Jun 04 2016 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.2-1
- Update calendar for Jalali year 1395; some bug fixes
- Closes #1319430
- Fix dependency on both python2 & python3, closes #1342507

* Sun Feb 21 2016 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.1-2
- Fix .desktop file
- Fix source URL from github

* Fri Feb 05 2016 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.1-1
- Update to new upstream version: 3.0.1, closes #1296760

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.4.1-1
- Update to upstream version 2.4.1: bug fixes

* Tue Jan 27 2015 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.4.0-2
- Drop gnome shell extension: doesn't work correctly with gnome shell 3.14, and
  replacements are available

* Sun Jan 25 2015 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.4.0-1
- Update to upstream version 2.4.0

* Tue Jul 15 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.3.4-1
- Update to 2.3.4, add pytz requirement

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.3.3-2
- Fix python2.4/2.5 requirements

* Fri Apr 25 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.3.3-1
- Update to 2.3.3 with new calender updates

* Sat Nov 23 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.2.5-1
- Update to 2.2.5 upstream version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.2.1-1
- Update to new upstream version 2.2.1
- Update the extension to work with gnome shell 3.8

* Mon Jan 28 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.1.0-4
- Fix a bug in gnome 3.6 extension which brought everything to top bar

* Sun Jan 27 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.1.0-3
- Gnome 3.6 compatible extension created

* Wed Jan 16 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.1.0-2
- Fix my name & email address in changelog

* Wed Jan 16 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.1.0-1
- Updated to 2.1.0

* Sun Nov 18 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.0.2-1
- Update to 2.0.2
- Add new requires

* Sat Jul 21 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.9.5-2
- The extension works with gnome shell 3.4 too

* Wed Apr 11 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.9.5-1
- Updated to 1.9.5 version

* Mon Jan 23 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.9.4-4
- Add patch to fix bug #759600
- Remove Qt gui as it doesn't work now, fix for bug #751553

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.9.4-2
- Add support gnome-shell 3.2 by starcal integration extention

* Thu Oct 13 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.9.4-1
- Updated to 1.9.4

* Thu Jul 28 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.9.3-2
- Retain license and about files in share/starcal2/ directory which is
  used in the first run

* Sat Jul 23 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.9.3-1
- Updated to 1.9.3
- removed defattr
- removed starcal daemon; doesn't seem to be reasonable (we don't have 
  system-wide events!)
- added gnome-shell extension

* Fri Jun 10 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.9.2-1
- Updated to 1.9.2 version

* Mon Feb 21 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.5.3-1
- Initial version

