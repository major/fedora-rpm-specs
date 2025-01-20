%global qt_module qttranslations

Summary: Qt5 - QtTranslations module
Name:    qt5-%{qt_module}
Version: 5.15.16
Release: 2%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

BuildArch: noarch

%global _qt5_qmake %{_bindir}/qmake-qt5

## versioning recently dropped, but could do >= %%majmin if needed --rex
BuildRequires: make
BuildRequires: qt5-qtbase-devel
# for lrelease
BuildRequires: qt5-linguist

# help system-config-language and dnf/yum langpacks pull these in
%if 0%{?_qt5:1}
Provides: %{_qt5}-ar = %{version}-%{release}
Provides: %{_qt5}-ca = %{version}-%{release}
Provides: %{_qt5}-cs = %{version}-%{release}
Provides: %{_qt5}-da = %{version}-%{release}
Provides: %{_qt5}-de = %{version}-%{release}
Provides: %{_qt5}-es = %{version}-%{release}
Provides: %{_qt5}-fa = %{version}-%{release}
Provides: %{_qt5}-fi = %{version}-%{release}
Provides: %{_qt5}-fr = %{version}-%{release}
Provides: %{_qt5}-gl = %{version}-%{release}
Provides: %{_qt5}-gd = %{version}-%{release}
Provides: %{_qt5}-he = %{version}-%{release}
Provides: %{_qt5}-hu = %{version}-%{release}
Provides: %{_qt5}-hr = %{version}-%{release}
Provides: %{_qt5}-it = %{version}-%{release}
Provides: %{_qt5}-ja = %{version}-%{release}
Provides: %{_qt5}-ko = %{version}-%{release}
Provides: %{_qt5}-lt = %{version}-%{release}
Provides: %{_qt5}-lv = %{version}-%{release}
Provides: %{_qt5}-nl = %{version}-%{release}
Provides: %{_qt5}-nn = %{version}-%{release}
Provides: %{_qt5}-pl = %{version}-%{release}
Provides: %{_qt5}-pt = %{version}-%{release}
Provides: %{_qt5}-pt_BR = %{version}-%{release}
Provides: %{_qt5}-ru = %{version}-%{release}
Provides: %{_qt5}-sk = %{version}-%{release}
Provides: %{_qt5}-sl = %{version}-%{release}
Provides: %{_qt5}-sv = %{version}-%{release}
Provides: %{_qt5}-uk = %{version}-%{release}
Provides: %{_qt5}-zh_CN = %{version}-%{release}
Provides: %{_qt5}-zh_TW = %{version}-%{release}
%endif

%description
%{summary}.


%prep
%setup -q -n %{qt_module}-everywhere-src-%{version}


%build
%{qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

# not used currently, since we track locales manually to keep %%files/Provides sync'd -- rex
#find_lang qttranslations --all-name --with-qt --without-mo


%files
%license LICENSE.*
%lang(ar) %{_qt5_translationdir}/*_ar.qm
%lang(bg) %{_qt5_translationdir}/*_bg.qm
%lang(ca) %{_qt5_translationdir}/*_ca.qm
%lang(cs) %{_qt5_translationdir}/*_cs.qm
%lang(da) %{_qt5_translationdir}/*_da.qm
%lang(de) %{_qt5_translationdir}/*_de.qm
%lang(es) %{_qt5_translationdir}/*_es.qm
%lang(en) %{_qt5_translationdir}/*_en.qm
%lang(fa) %{_qt5_translationdir}/*_fa.qm
%lang(fi) %{_qt5_translationdir}/*_fi.qm
%lang(fr) %{_qt5_translationdir}/*_fr.qm
%lang(gd) %{_qt5_translationdir}/*_gd.qm
%lang(gl) %{_qt5_translationdir}/*_gl.qm
%lang(he) %{_qt5_translationdir}/*_he.qm
%lang(hu) %{_qt5_translationdir}/*_hu.qm
%lang(hr) %{_qt5_translationdir}/*_hr.qm
%lang(it) %{_qt5_translationdir}/*_it.qm
%lang(ja) %{_qt5_translationdir}/*_ja.qm
%lang(ko) %{_qt5_translationdir}/*_ko.qm
%lang(lt) %{_qt5_translationdir}/*_lt.qm
%lang(lv) %{_qt5_translationdir}/*_lv.qm
%lang(nn) %{_qt5_translationdir}/*_nn.qm
%lang(nl) %{_qt5_translationdir}/*_nl.qm
%lang(pl) %{_qt5_translationdir}/*_pl.qm
%lang(pt) %{_qt5_translationdir}/*_pt_PT.qm
%lang(pt_BR) %{_qt5_translationdir}/*_pt_BR.qm
%lang(ru) %{_qt5_translationdir}/*_ru.qm
%lang(sk) %{_qt5_translationdir}/*_sk.qm
%lang(sl) %{_qt5_translationdir}/*_sl.qm
%lang(sv) %{_qt5_translationdir}/*_sv.qm
%lang(tr) %{_qt5_translationdir}/*_tr.qm
%lang(uk) %{_qt5_translationdir}/*_uk.qm
%lang(zh_CN) %{_qt5_translationdir}/*_zh_CN.qm
%lang(zh_TW) %{_qt5_translationdir}/*_zh_TW.qm


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Zephyr Lykos <fedora@mochaa.ws> - 5.15.16-1
- 5.15.16

* Wed Sep 04 2024 Jan Grulich <jgrulich@redhat.com> - 5.15.15-1
- 5.15.15

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 Jan Grulich <jgrulich@redhat.com> - 5.15.14-1
- 5.15.14

* Thu Mar 14 2024 Jan Grulich <jgrulich@redhat.com> - 5.15.13-1
- 5.15.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Jan Grulich <jgrulich@redhat.com> - 5.15.12-1
- 5.15.12

* Fri Oct 06 2023 Jan Grulich <jgrulich@redhat.com> - 5.15.11-1
- 5.15.11

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Jan Grulich <jgrulich@redhat.com> - 5.15.10-1
- 5.15.10

* Tue Apr 11 2023 Jan Grulich <jgrulich@redhat.com> - 5.15.9-1
- 5.15.9

* Tue Jan 31 2023 Jan Grulich <jgrulich@redhat.com> - 5.15.8-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Jan Grulich <jgrulich@redhat.com> - 5.15.8-1
- 5.15.8

* Mon Oct 31 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.7-1
- 5.15.7

* Tue Sep 20 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.6-1
- 5.15.6

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.5-1
- 5.15.5

* Mon May 16 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.4-1
- 5.15.4

* Fri Mar 04 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.3-1
- 5.15.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 07:54:16 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.2-2
- Rebuild for qtbase with -no-reduce-relocations option

* Fri Nov 20 09:30:47 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.2-1
- 5.15.2

* Thu Sep 10 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.1-1
- 5.15.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 14 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.14.2-2
- rebuild

* Sat Apr 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.14.2-1
- 5.14.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.13.2-1
- 5.13.2

* Tue Sep 24 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.5-1
- 5.12.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.4-1
- 5.12.4

* Tue Jun 04 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.3-1
- 5.12.3

* Fri Feb 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-1
- 5.12.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.3-1
- 5.11.3

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.2-1
- 5.11.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.1-1
- 5.11.1

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.0-1
- 5.11.0
- use %%make_build
- make BR: qt5-qbase-devel unversioned

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 5.10.1-1
- 5.10.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Jan Grulich <jgrulich@redhat.com> - 5.10.0-1
- 5.10.0

* Thu Nov 23 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.3-1
- 5.9.3

* Mon Oct 09 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.2-1
- 5.9.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.1-1
- 5.9.1

* Fri Jun 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.0-2
- Source URL

* Wed May 31 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-1
- Upstream official release

* Fri May 26 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.1.rc
- Upstream Release Candidate retagged

* Tue May 09 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta.3
- Upstream beta 3

* Mon Jan 30 2017 Helio Chissini de Castro <helio@kde.org> - 5.8.0-1
- New upstream release

* Wed Nov 09 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.1-1
- New upstream version

* Wed Jul 06 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-2
- Compile with gcc

* Wed Jun 15 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-1
- Qt 5.7.0 release

* Thu Jun 09 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.1-1
- Update to 5.6.1

* Fri Mar 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.0-2
- rebuild

* Mon Mar 14 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-1
- 5.6.0 final release

* Tue Feb 23 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.7.rc
- Update to final RC

* Mon Feb 15 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.6
- Update RC release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-0.4
- drop BR: pkgconfig(Qt5Help), drop unused %%find_lang

* Sat Jan 23 2016 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-0.3
- use %%qmake_qt5 (and hack around %%_qt5_qmake noarch issue)

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.2
- Official rc release

* Tue Nov 03 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.1
- Start to implement 5.6.0 rc

* Thu Oct 15 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-2
- Update to final release 5.5.1

* Tue Sep 29 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-1
- Update to Qt 5.5.1 RC1

* Wed Jul 29 2015 Rex Dieter <rdieter@fedoraproject.org> 5.5.0-2
- BR: qt5-linguist, relax qt5-qttools dep

* Thu Jun 25 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.0-0.2.rc
- Update for official RC1 released packages

* Wed Jun 17 2015 Daniel Vrátil <dvratil@redhat.com> - 5.5.0-0.1.rc
- Qt 5.5.0 RC1

* Thu Jun 04 2015 Jan Grulich <jgrulich@redhat.com> 5.4.2-1
- 5.4.2

* Thu Mar 26 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-2
- Provides: qt5-qtbase-<locales> to aid dnf/yum langpacks plugin and system-config-language (#1170730)

* Tue Feb 24 2015 Jan Grulich <jgrulich@redhat.com> 5.4.1-1
- 5.4.1

* Wed Dec 10 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-1
- 5.4.0 (final)

* Fri Nov 28 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-0.2.rc
- 5.4.0-rc

* Mon Oct 20 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-0.1.rc
- 5.4.0-rc

* Wed Sep 17 2014 Rex Dieter <rdieter@fedoraproject.org> - 5.3.2-1
- 5.3.2

* Tue Jun 17 2014 Jan Grulich <jgrulich@redhat.com> - 5.3.1-1
- 5.3.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jan Grulich <jgrulich@redhat.com> 5.3.0-1
- 5.3.0

* Wed Feb 05 2014 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-1
- 5.2.1

* Thu Dec 12 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-1
- 5.2.0

* Mon Dec 02 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.10.rc1
- 5.2.0-rc1

* Thu Oct 24 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.2.rc1
- 5.2.0-rc1

* Wed Oct 02 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.1.alpha
- 5.2.0-alpha

* Sun Sep 22 2013 Rex Dieter <rdieter@fedoraproject.org> 5.1.1-1
- Initial packaging
