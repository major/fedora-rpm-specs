Name:       ibus-table-tv
Version:    1.2.0.20100305
Release:    26%{?dist}
Summary:    The Thai and Viqr (Vietnamese) tables for IBus-Table
License:    GPLv3
URL:        http://github.com/kaio/ibus-table-tv/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:         ibus-table >= 1.2.0.20090912-3
BuildRequires:    ibus-table-devel >= 1.2.0.20090912-3
BuildRequires: make

%description
The Thai and Viqr (Vietnamese) tables for IBus-Table.

%prep
%setup -q

%build
%configure \
  --prefix=%{_prefix} \
  --disable-static \
  --enable-thai \
  --enable-viqr 
%__make %{?_smp_mflags}

%install
%__rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=${RPM_BUILD_ROOT} NO_INDEX=true install
cd /$RPM_BUILD_ROOT/%{_datadir}/ibus-table/tables/
%{_bindir}/ibus-table-createdb -i -n thai.db
%{_bindir}/ibus-table-createdb -i -n viqr.db

# %find_lang %{name}

%files
%doc AUTHORS COPYING README
%{_datadir}/ibus-table/icons/thai.png
%{_datadir}/ibus-table/icons/viqr.png
%{_datadir}/ibus-table/tables/thai.db
%{_datadir}/ibus-table/tables/viqr.db

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.20100305-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20100305-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20100305-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20100305-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20100305-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20100305-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20100305-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20100305-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 04 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100305-5
- Correct URL.

* Sun Apr 04 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100305-4
- Remove provides and obsoletes tag.

* Wed Mar 10 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100305-3
- Update Requires, Provides, Obsoletes tags.

* Fri Mar 05 2010 Caius 'kaio' Chance <cchance at redhat.com> - 1.2.0.20100305-2
- Fix source tag.
- Upgrade source from upstream.
- Move index creation to build time.
- Fix index creation source.
- Fix BuildRequires tag.

* Fri Jan 08 2010 Caius 'kaio' Chance <k at kaio.me> - 1.2.0.20100108-1
- The first version.
- Combine Thai, Viqr tables.
