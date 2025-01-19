
Name:    kde-baseapps
Summary: KDE Core Applications 
Version: 16.12.2
Release: 20%{?dist}

# Automatically converted from old format: GPLv2 and GFDL - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     http://kde.org/
BuildArch: noarch

Obsoletes: kdebase < 6:4.7.97-10
#Provides: kdebase = 6:%{version}-%{release}

Obsoletes: kdebase4 < %{version}-%{release}
#Provides: kdebase4 = %{version}-%{release}

Requires: %{name}-common = %{version}-%{release}

Requires: kdialog >= %{version}
Requires: keditbookmarks >= %{version}
Requires: kfind >= %{version}
%ifarch %{?qt5_qtwebengine_arches}%{?!qt5_qtwebengine_arches:%{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}
Requires: konqueror >= %{version}
%endif

%description
Metapackage for Core KDE applications.

%package common
Summary: Common files for %{name}
#Conflicts: kde-baseapps < 4.12.0-2
Obsoletes: dolphin4 < 16.12
Obsoletes: dolphin4-libs < 16.12
Obsoletes: kde-baseapps-libs < 16.12
Obsoletes: kde-baseapps-devel < 16.12
Obsoletes: kde-plasma-folderview = 6:16.12
Obsoletes: kdepasswd < 16.12
Obsoletes: libkonq < 16.12
%description common
%{summary}


%prep
# blank


%build
# blank


%install
#blank


%files
# empty metapackage

%files common
# empty


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 16.12.2-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 23 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-2
- Requires: konqueror only on arch's that provide it

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2, Obsoletes not complete (#1420534)

* Mon Jan 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-2
- re-introduce -common, move Obsoletes there

* Mon Jan 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- (empty) metapackage, help transition to kf5-based packages

* Wed Nov 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Tue Sep 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Tue Aug 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-3
- rebuild

* Tue Aug 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-2
- rebuild

* Fri Aug 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sat Aug 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.90-1
- 16.07.90

* Fri Jul 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.80-1
- 16.07.80

* Fri Jul 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Wed Apr 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-3
- rebuild (qt)

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-2
- rebuild (qt)

* Fri Apr 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0
