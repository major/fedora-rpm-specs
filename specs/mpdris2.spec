%global tarname mpDris2

Name:           mpdris2
Version:        0.9.1
Release:        12%{?dist}
Summary:        Provide MPRIS 2 support to mpd

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/eonpatapon/%{name}
Source0:        https://github.com/eonpatapon/%{name}/archive/%{version}.tar.gz#/%{tarname}-%{version}.tar.gz

# Submitted and accepted upstream
# https://github.com/eonpatapon/mpDris2/pull/145
Patch0:         mpdris2-0.9.1-currentsong.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel

Requires:       python3-dbus python3-mpd2 python3-gobject python3-mutagen

%description
mpDris2 provides MPRIS 2 support to mpd (Music Player Daemon).

mpDris2 is run in the user session and monitors a local or distant 
mpd server


%prep
%autosetup -n %{tarname}-%{version} -p1

%build
env NOCONFIGURE=1 ./autogen.sh
export PYTHON=%{__python3}
%configure --docdir=%{_pkgdocdir}


make %{?_smp_mflags}


%install
%make_install
# Remove so that we can use %%license
rm -fv %{buildroot}%{_docdir}/%{name}/COPYING
rm -fv %{buildroot}%{_docdir}/%{name}/README
sed -i '1 s:#!.*:#!%{__python3}:' %{buildroot}%{_bindir}/%{tarname}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{tarname}

%files -f %{tarname}.lang
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{tarname}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.mpris.MediaPlayer2.mpd.service
%{_pkgdocdir}/%{tarname}.conf
%{_prefix}/lib/systemd/user/mpDris2.service

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.1-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 12 2023 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.9.1-7
- Rename python3-mpd2 dependency to python3-mpd (see #2240352, #2240351)
- Update spec formatting

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.9.1-2
- Apply upstream patch to protect currentsong access (rhbz #1963403)

* Tue Nov 30 2021 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.9.1-1
- New upstream release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7.20200205git491588a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6.20200205git491588a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5.20200205git491588a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.8-4.20200205git491588a
- Update to latest git HEAD, for new-status patch - fixes #1798356

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3.20191223gite06bcf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.8-2.20191223gite06bcf6
- Update to latest git HEAD, includes notification-retry fix (see #1756448)

* Sat Aug 10 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.8-1.20190706git1653e15
- New upstream release 0.8
- Updated to git HEAD, includes SafeConfigParser deprecation warning fix

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-12.20190207git7bd3faa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.7-11.20190206git7bd3faa
- Latest upstream commit
- Fixes crashes with mpd 0.21, due to volume not being reported when paused/stopped

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10.20171028git3c3fe12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9.20171028git3c3fe12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7-8.20171028git3c3fe12
- Rebuilt for Python 3.7

* Sun Mar 04 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.7-7.20171028git3c3fe12
- Fix readme file - fixes #1551236

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6.20171028git3c3fe12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.7-5.20171028git3c3fe12
- Update to new upstream commit
- use Py3 - fixes #1404618

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4.20160422gita3af302
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3.20160422gita3af302
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 22 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.7-2.20160422gita3af302
- Update to latest git commit to fix rhbz #1322498

* Thu Mar 10 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.7-1
- Update to latest upstream release
- Remove patch - was accepted

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 22 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.4-1
- License updated to GPLv3+

* Wed Aug 21 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.4-1
- Mark files as doc

* Fri Jun 21 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.4-1
- #912048
- Use find_lang
- Rename to lowercase
- Patch desktop file
- Mark autostart file as config

* Sun Feb 17 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.4-1
- Initial rpmbuild
