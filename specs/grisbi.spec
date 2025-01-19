Name:		grisbi
Version:	2.0.5
Release:	7%{?dist}
Summary:	Personal finances manager

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.grisbi.org
Source0:	http://downloads.sourceforge.net/project/grisbi/grisbi%20stable/2.0.x/%{version}/%{name}-%{version}.tar.bz2
Source1:	%{name}.appdata.xml

BuildRequires:  gcc
BuildRequires:	gtk3-devel
BuildRequires:	libxml2-devel
BuildRequires:	glib2-devel
BuildRequires:	libgsf-devel
BuildRequires:	gettext-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libofx-devel >= 0.9.0
BuildRequires:	openssl-devel
BuildRequires:	intltool
BuildRequires:	ImageMagick
BuildRequires:	libappstream-glib
BuildRequires: make

Requires:	xdg-utils

%description
Grisbi is a very functional personal financial management program
with a lot of features: checking, cash and liabilities accounts,
several accounts with automatic contra entries, several currencies,
including euro, arbitrary currency for every operation, money
interchange fees, switch to euro account per account, description
of the transactions with third parties, categories, sub-categories,
financial year, notes, breakdown, transfers between accounts, even
for accounts of different currencies, bank reconciliation, scheduled
transactions, automatic recall of last transaction for every third
party, nice and easy user interface, user manual, QIF import/export.

%prep
%setup -q

%build
# FIXME: package should not install help files into _pkgdocdir
%configure --disable-silent-rules --docdir=%{_pkgdocdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -D -p -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

for f in AUTHORS COPYING NEWS README ABOUT-NLS; do
    cp -p $f %{buildroot}%{_pkgdocdir}/$f
done

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc %{_pkgdocdir}/
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/grisbi.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-grisbi.*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gtk.grisbi.gschema.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.5-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 26 2023 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.5-1
- Version 2.0.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.2.2-6
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Aurelien Bompard <abompard@fedoraproject.org> - 1.2.2-1
- Version 1.2.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Bill Nottingham <notting@splat.cc> - 1.0.0-8
- rebuild for libofx soname change

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-6
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Aurelien Bompard <abompard@fedoraproject.org> - 1.0.0-1
- version 1.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.8.9-7
- Make building verbose (Disable silent-rules).
- Let spec acknowledge %%{_pkgdocdir}.
- Modernize spec.

* Wed Jun 11 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.8.9-6
- Fix FTBFS due to automake-1.14 (#1106724)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 23 2013 Bill Nottingham <notting@redhat.com> - 0.8.9-4
- rebuild against new libofx
