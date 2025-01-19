Name:           mtn-browse
Version:        1.20
Release:        21%{?dist}
Summary:        Application for browsing Monotone VCS databases
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.coosoft.plus.com/software.html
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        mtn-browse.desktop
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Gnome2)
BuildRequires:  perl(Gnome2::Canvas)
BuildRequires:  perl(Gnome2::VFS)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Gtk2::GladeXML)
BuildRequires:  perl(Gtk2::SourceView2)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(Locale::TextDomain)
BuildRequires:  perl(Monotone::AutomateStdio) >= 1.10
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  meld graphviz
Requires:       meld graphviz
BuildArch:      noarch

%description
Monotone browser (mtn-browse) is an application for browsing Monotone
VCS databases without the need for a work space. The interface allows
one to:
* Easily select a revision from within a branch
* Find a revision using complex queries
* Navigate the contents of a revision using a built in file manager
* Display file contents, either using the internal viewer or an
  external helper application
* Compare the changes between different revisions or versions of a
  file either using the internal difference viewer or an external
  application
* Find files within a revision based on detailed search criteria
* Display file annotations and easily refer back to the corresponding
  change documentation
* Save files to disk

%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}%{_datadir}/%{name}/perl
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(AdvancedFind\\)
%global __requires_exclude %__requires_exclude|perl\\(Annotate\\)
%global __requires_exclude %__requires_exclude|perl\\(CachingAutomateStdio\\)
%global __requires_exclude %__requires_exclude|perl\\(ChangeLog\\)
%global __requires_exclude %__requires_exclude|perl\\(ComboAutoCompletion\\)
%global __requires_exclude %__requires_exclude|perl\\(Common\\)
%global __requires_exclude %__requires_exclude|perl\\(Completion\\)
%global __requires_exclude %__requires_exclude|perl\\(DateRange\\)
%global __requires_exclude %__requires_exclude|perl\\(FindFiles\\)
%global __requires_exclude %__requires_exclude|perl\\(FindTextAndGoToLine\\)
%global __requires_exclude %__requires_exclude|perl\\(Globals\\)
%global __requires_exclude %__requires_exclude|perl\\(History\\)
%global __requires_exclude %__requires_exclude|perl\\(HistoryGraph\\)
%global __requires_exclude %__requires_exclude|perl\\(LocaleEnableUtf8\\)
%global __requires_exclude %__requires_exclude|perl\\(ManageServerBookmarks\\)
%global __requires_exclude %__requires_exclude|perl\\(ManageTagWeightings\\)
%global __requires_exclude %__requires_exclude|perl\\(MultipleRevisions\\)
%global __requires_exclude %__requires_exclude|perl\\(Preferences\\)
%global __requires_exclude %__requires_exclude|perl\\(WindowManager\\)


%prep
%setup -q


%build
# empty


%install
./linux-installer \
  --destdir=%{buildroot} \
  --prefix=%{_prefix} \
  --file-comparison=meld \
  --no-use-dists-mas \
  --libdir=share/%{name}

install -m 644 -D -p \
  ./lib/ui/pixmaps/mtn-browse-small.png \
  %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

%find_lang %{name} --with-gnome


%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.20-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-9
- Add perl dependencies needed for build

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 30 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.20-1
- Update to 1.20.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun  5 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10-6
- Depend on Gtk2::SourceView2 instead of Gtk2::SourceView.
- Mark license with %%license.
- Package contents changed upstream, updating.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 1.10-3
- Perl 5.18 rebuild

* Tue Feb 19 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.10-2
- Fix requires filtering.

* Sun Feb 17 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.10-1
- Update to 1.10.

* Sun Feb 17 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.00-4
- Add BR on Pod::Usage.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.00-3
- Add .desktop file.

* Fri Oct 19 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.00-2
- Fix typo.
- Remove wrong comment.

* Thu Oct 18 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.00-1
- Update to 1.00.
- Update requirements.
- Directly call the linux-installer.
- Remove %%clean section, BuildRoot tag and %%defattr directive.
- Use RPM-4.9-style filtering.

* Sat Mar 12 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.72-1
- New package.
