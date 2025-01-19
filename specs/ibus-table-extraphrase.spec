%bcond_without bootstrap

Name:           ibus-table-extraphrase
Version:        1.3.9.20110826
Release:        28%{?dist}
Summary:        Extra phrase for ibus-table
License:        GPL-3.0-or-later
URL:            http://code.google.com/p/ibus/
Source0:        http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz

BuildArch:      noarch

# for noarch pkgconfig
BuildRequires:  ibus-table-devel >= 1.1.0.20090220-5
%if %{with bootstrap}
BuildRequires:  gettext-devel >= 0.17, automake >= 1.10.2
%endif
BuildRequires: make

%description
Extra phrase data for IBus-Table engine.

%prep
%setup -q

%build
export IBUS_TABLE_CREATEDB="%{_bindir}/ibus-table-createdb --no-create-index"
%if %{with bootstrap}
./autogen.sh \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
%else
%configure \
%endif

#    --enable-extraphrase
make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
make install \
  DESTDIR=%{buildroot} \
  INSTALL="install -p" \
  pkgconfigdir=%{_datadir}/pkgconfig

%files
%doc AUTHORS ChangeLog COPYING README
%{_datadir}/pkgconfig/ibus-table-extraphrase.pc
%{_datadir}/ibus-table/data/extra_phrase.txt

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Mike FABIAN <mfabian@redhat.com> - 1.3.9.20110826-22
- Migrate license tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.3.9.20110826-14
- Remove obsolete requirement for %%post scriptlet

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9.20110826-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.20110826-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.20110826-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.20110826-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.20110826-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.20110826-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9.20110826-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 26 2011 Caius 'kaio' Chance <me@kaio.net> - 1.3.9.20110826-1
- update to upstream

* Fri Aug 13 2010 Jens Petersen <petersen@redhat.com> - 1.2.0.20100305-1
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20100305-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 13 2010 Jens Petersen <petersen@redhat.com> - 1.2.0.20100305-1
- update to 1.2.0.20100305
- BR ibus-table-devel

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.20090415-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 23 2009 Caius 'kaio' Chance <cchance@redhat.com> - 1.1.0.20090415-3.fc11
- Updated desciption.

* Wed Apr 15 2009 Caius 'kaio' Chance <cchance@redhat.com> - 1.1.0.20090415-2.fc11
- Removed invalid verification bypass of extra_phrase.txt.
- Refined spec file.

* Wed Apr 15 2009 Caius 'kaio' Chance <cchance@redhat.com> - 1.1.0.20090415-1.fc11
- Updated to latest source from upstream.

* Tue Apr 14 2009 Caius 'kaio' Chance <cchance@redhat.com> - 1.1.0.20090406-3.fc11
- Relocated pkgconfig spec file to /usr/share/pkgconfig.

* Wed Apr 08 2009 Caius 'kaio' Chance <cchance@redhat.com> - 1.1.0.20090406-2.fc11
- Fixed wrong libdir of pkgconfig spec file.

* Mon Apr 06 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090406-1.fc11
- Update to the latest source tarball.
- Added ChangeLog to be doc.

* Tue Mar 31 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090327-2.fc11
- Corrected extra_phrase.txt installation destination.
- Update license tag to GPLv3+.

* Mon Mar 27 2009 Caius Chance <cchance@redhat.com> - 1.1.0.20090327-1.fc11
- Resolves: rhbz#488175
- Splited from ibus-table.
