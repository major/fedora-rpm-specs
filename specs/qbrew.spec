Name:		qbrew
Version:	0.4.1
Release:	37%{?dist}
Summary:	A Brewing Recipe Calculator

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.usermode.org/code.html
Source0:	http://www.usermode.org/code/%name-%{version}.tar.gz
Patch0:		qbrew-fix-return-type.patch
BuildRequires: make
BuildRequires:	qt-devel, desktop-file-utils

%description
QBrew is a homebrewer's recipe calculator. You can create and modify
ale and lager recipes as well as calculate gravity, color, and
bitterness. QBrew includes a database of styles, grains, hops, and
miscellaneous ingredients, plus a brewing tutorial.

%prep
%setup -q
find src -type f -exec chmod 0644 {} \;
%patch -P0 -p1

%build
# qbrew expects the docs to be %{_prefix}/share/doc/qbrew,
# NOT .../doc/qbrew-%{version}
echo "QMAKE_CFLAGS_RELEASE=\"%{optflags}\"" >> qbrew.pro
echo "QMAKE_CXXFLAGS_RELEASE=\"%{optflags}\"" >> qbrew.pro
echo "QMAKE_LFLAGS_RELEASE=\"%{optflags}\"" >> qbrew.pro

%{_configure} --prefix=%{_prefix} \
	      --bindir=%{_bindir} \
	      --datadir=%{_datadir}/%{name} \
	      --docdir=%{_defaultdocdir}/%{name}
%{__make} %{?_smp_mflags}

(
cat <<EODESKTOP
[Desktop Entry]
Name=Qbrew
GenericName=Qbrew
Comment=%{summary}
Exec=qbrew
Icon=qbrew
Terminal=false
Type=Application
Categories=Amusement;
EODESKTOP
) > %{name}.desktop

# create translation files
for ts in translations/*.ts; do
    %{_qt4_bindir}/lrelease ${ts}
done

%install
make install INSTALL_ROOT=${RPM_BUILD_ROOT}

%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps
cp pics/%{name}.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps

%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/applications
desktop-file-install \
   --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
   %{name}.desktop

%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datarootdir}/%{name}/translations
cp translations/*.ts translations/*.qm \
   ${RPM_BUILD_ROOT}%{_datarootdir}/%{name}/translations


%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datarootdir}/%{name}
%{_defaultdocdir}/%{name}

%doc AUTHORS ChangeLog TODO *.qbrew LICENSE README

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.1-36
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 10 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.4.1-17
- Added qbrew-fix-return-type.patch to fix convertion type issue
- Fixes FTBFS rhbz #1307962 plus spec clean up

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.1-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct  7 2009 Chris St. Pierre <chris.a.st.pierre@gmail.com> - 0.4.1-6
- Cleaned up changelog (https://bugzilla.redhat.com/show_bug.cgi?id=524107#c13)
- Did the right thing with LICENSE and README (also comment 13)

* Tue Oct  6 2009 Chris St. Pierre <chris.a.st.pierre@gmail.com> - 0.4.1-5
- Simplified addition of %%doc files
- Removed help files from %%doc, since they're required to make qbrew work
- Moved help files to /usr/share/doc/qbrew/, where qbrew expects them to be
  (https://bugzilla.redhat.com/show_bug.cgi?id=524107#c9)

* Mon Sep 28 2009 Chris St. Pierre <chris.a.st.pierre@gmail.com> - 0.4.1-4
- Build and install translations

* Wed Sep 23 2009 Chris St. Pierre <chris.a.st.pierre@gmail.com> - 0.4.1-3
- Added sample .qbrew files to %%doc
  (https://bugzilla.redhat.com/show_bug.cgi?id=524107#c8)

* Fri Sep 18 2009 Chris St. Pierre <chris.a.st.pierre@gmail.com> - 0.4.1-2
- Fixed a vast array of issues
  (https://bugzilla.redhat.com/show_bug.cgi?id=524107#c2)

* Thu Sep 17 2009 Chris St. Pierre <chris.a.st.pierre@gmail.com> - 0.4.1-1
- Converted specfile from SuSE
