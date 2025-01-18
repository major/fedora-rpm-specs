%global include_holidayparser  0
%{?_with_holidayparser: %{expand: %%global include_holidayparser 1}}

Name:           dayplanner
Version:        0.11
Release:        26%{?dist}
Summary:        An easy and clean Day Planner
Summary(pl):    Prosty i elegancki organizer
Summary(de):    Ein einfacher und klarer Tagesplaner
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.day-planner.org
Source0:        https://github.com/downloads/zerodogg/%{name}/%{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  gettext desktop-file-utils perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Locale::gettext)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
%if 0%{?fedora} && 0%{?fedora} >= 19
BuildRequires:  perl(autodie)
BuildRequires:  perl-generators
%endif
BuildRequires: make
Requires:       hicolor-icon-theme
Requires:       perl(Locale::gettext)

%description
Day Planner is a simple time management program.

Day Planner is designed to help you easily manage your time.
It can manage appointments, birthdays and more. It makes sure you
remember your appointments by popping up a dialog box reminding you about it.

%description -l pl
Day Planner is a prosty program do zarządzania czasem.

Day Planner jest zaprojektowany aby pomóc Tobie łatwo zarządzać Twoim czasem.
Może zarządzać spotkaniami, urodzinami i innymi. Możesz być pewnym że będziesz
pamiętał o spotkaniach przez wyskakujące okna dialogowe przypominające o nich.

%description -l de
Day Planner ist ein einfaches Zeitverwaltungsprogram.

Day Planner hilft Ihnen, Ihre Termine einfach zu verwalten. Es kann Termine, 
Geburtstage und vieles mehr speichern. Um sicherzustellen, dass Sie keine 
Termine verpassen, erinnert Sie Day Planner mit einem Dialogfenster daran.

%prep
%setup -q

# filter out all unwanted perl related Requires and Provides
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
sed -e '/perl(DP::.*)/d' |\
sed -e '/perl(Date::HolidayParser)/d'
EOF

%global __perl_provides %{_builddir}/%{name}-%{version}/%{name}-prov
chmod +x %{__perl_provides}

cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(DP::.*)/d' |\
sed -e '/perl(Date::HolidayParser)/d'
EOF

%global __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
chmod +x %{__perl_requires}	

%build
# nothing to build

%install
%if 0%{?include_holidayparser}
make install DESTDIR=%{buildroot} prefix=%{_prefix}
%else
make install DESTDIR=%{buildroot} prefix=%{_prefix}
%endif

# Install hicolor icons
for size in 16 24 32 48; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
  install -pm644 art/%{name}-${size}x${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

rm -f %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -f %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Install desktop file
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor="fedora"                    \
%endif
  --remove-category=X-MandrivaLinux-Office-TimeManagement \
  --dir=%{buildroot}%{_datadir}/applications           \
  ./doc/%{name}.desktop

# Chmod
find %{buildroot}%{_datadir}/%{name} -name \*.pm -exec chmod 0644 {} \;

# Find the localization
%find_lang %{name}

%files -f dayplanner.lang
%doc AUTHORS COPYING NEWS THANKS TODO 
%doc ./doc/{*_Spec,EnvironmentVariables,HACKING,README.*,TESTCASES,TODO_DPS}
%{_bindir}/%{name}*
%{_datadir}/%{name}
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_mandir}/man1/dayplanner*.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.11-25
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 0.11-14
- Fix string quoting for rpm >= 4.16

* Tue Mar 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-13
- Add all perl dependencies needed for build

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11-7
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Christopher Meng <rpm@cicku.me> - 0.11-1
- New version.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.10-8
- Perl 5.18 rebuild

* Mon Feb 18 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10-7
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077
- Fix build on F19

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 26 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.10-1
- Update to 0.10
- Include new manpages
- Use upstream's desktop file
- Run update-desktop-database because we now have a mime type

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 0.9.2-1
- Updated to 0.9.2

* Sat Jul 19 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.1-3
- Filter out all dayplanner related Requires and Provides

* Sat Jul 19 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.1-2
- Filter out unwanted Requires on perl(DP::CoreModules)

* Sat Jul 19 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1 to fix #446883
- Require perl(Locale::gettext)
- Add German descriptions

* Tue Mar 04 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 0.8.1-3
- Correct install section
- Fix holiday_japan
- Correct BR-s

* Mon Mar 03 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 0.8.1-2
- Correct install section
- Add holiday_japan

* Tue Feb 19 2008 Krzysztof Kurzawski <kurzawax at gmail.com> - 0.8.1-1
- First release
