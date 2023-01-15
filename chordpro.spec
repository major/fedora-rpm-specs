# -*- rpm-spec -*-

%define FullName App-Music-ChordPro

Name: chordpro
Summary: Print songbooks (lyrics + chords)
License: Artistic 2.0
Version: 6.000
Release: 1%{?dist}
Source: https://cpan.metacpan.org/authors/id/J/JV/JV/%{FullName}-%{version}.tar.gz
URL: https://www.chordpro.org

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

# This package would provide many (perl) modules, but these are
# not intended for general use.
%global __provides_exclude_from /*\\.pm$
%global __requires_exclude App::Music::ChordPro

Requires: perl(:VERSION) >= 5.10.1

Requires: perl(App::Packager)               >= 1.430
Requires: perl(PDF::API2)                   >= 2.043
Requires: perl(Text::Layout)                >= 0.028
Requires: perl(JSON::PP)                    >= 2.27203
Requires: perl(String::Interpolate::Named)  >= 1.03
Requires: perl(File::HomeDir)               >= 1.004
Requires: perl(File::LoadLines)             >= 1.021
Requires: perl(Image::Info)                 >= 1.41
Requires: perl(List::Util)                  >= 1.33
Requires: perl(Storable)                    >= 3.08
Requires: perl(Hash::Util)

BuildRequires: make
BuildRequires: perl(App::Packager)               >= 1.430
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)         >= 6.76
BuildRequires: perl(File::HomeDir)               >= 1.004
BuildRequires: perl(File::LoadLines)             >= 1.021
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Hash::Util)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Image::Info)                 >= 1.41
BuildRequires: perl(JSON::PP)                    >= 2.27203
BuildRequires: perl(PDF::API2)                   >= 2.043
BuildRequires: perl(String::Interpolate::Named)  >= 1.03
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Layout)                >= 0.028
BuildRequires: perl(List::Util)                  >= 1.33
BuildRequires: perl(Storable)                    >= 3.08
BuildRequires: perl(base)
BuildRequires: perl(constant)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
ChordPro will read a text file containing the lyrics of one or many
songs plus chord information. ChordPro will then generate a
photo-ready, professional looking, impress-your-friends sheet-music
suitable for printing on your nearest printer.

To learn more about ChordPro, look for the man page or do
chordpro --help for the list of options.

ChordPro is a rewrite of the Chordii program.

For more information about ChordPro, see https://www.chordpro.org.

%package gui

Summary: ChordPro graphical user interface
AutoReqProv: 0

Requires: %{name} = %{version}-%{release}
Requires: perl(Wx) >= 0.99

%description gui
This package contains the wxWidgets (GUI) extension for %{name}.

%package abc

Summary: Support for ChordPro ABC embedding 
AutoReqProv: 0

Requires: %{name} = %{version}-%{release}
Requires: abcm2ps
Requires: ImageMagick

%description abc
This packages installs the requirements for ABC support for ChordPro.

%package lilypond

Summary: Support for ChordPro LilyPond embedding
AutoReqProv: 0

Requires: %{name} = %{version}-%{release}
Requires: lilypond
Requires: ImageMagick

%description lilypond
This packages installs the requirements for LilyPond support for ChordPro.

%prep
%setup -q -n %{FullName}-%{version}

# Remove some stuff.
rm lib/App/Music/ChordPro/res/linux/setup_desktop.sh
rm lib/App/Music/ChordPro/Output/LaTeX.pm
rm lib/App/Music/ChordPro/Output/Markdown.pm
rm t/73_md.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test

%install

# Short names for our libraries.
%global share %{_datadir}/%{name}-%{version}

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
echo "# Placeholder" > %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
mkdir -p %{buildroot}%{share}/lib
mkdir -p %{buildroot}%{_bindir}

# Create lib dirs and copy files.
find blib/lib -type f -name .exists -delete
find blib/lib -type d -printf "mkdir %{buildroot}%{share}/lib/%%P\n" | sh -x
find blib/lib ! -type d -printf "install -p -m 0644 %p %{buildroot}%{share}/lib/%%P\n" | sh -x

for script in chordpro wxchordpro
do

  # Create the main scripts.
  sed -e "s;use lib ..FindBin.*/lib.;use lib qw(%{share}/lib);" \
           -e "/FindBin.*CPAN/d;" \
    < script/${script} >> %{buildroot}%{_bindir}/${script}
  chmod 0755 %{buildroot}%{_bindir}/${script}

  # And its manual page.
  mkdir -p %{buildroot}%{_mandir}/man1
  pod2man blib/script/${script} > %{buildroot}%{_mandir}/man1/${script}.1

done

# Desktop file, icons, ...
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
install -p -m 0664 \
    lib/App/Music/ChordPro/res/icons/chordpro.png \
    lib/App/Music/ChordPro/res/icons/chordpro-doc.png \
    %{buildroot}%{_datadir}/pixmaps/
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    lib/App/Music/ChordPro/res/linux/%{name}.desktop

mkdir -p %{buildroot}%{_metainfodir}
cp -p lib/App/Music/ChordPro/res/linux/%{name}.metainfo.xml \
    %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%{_fixperms} %{buildroot}/*
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

# End of install section.

%files
%doc Changes README.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/chordpro
%{share}/lib/App/Music/ChordPro.pm
%{share}/lib/App/Music/ChordPro
%exclude %{share}/lib/App/Music/ChordPro/Wx.pm
%exclude %{share}/lib/App/Music/ChordPro/Wx
%exclude %{share}/lib/App/Music/ChordPro/Delegate
%{_mandir}/man1/chordpro*

%files gui
%{_bindir}/wxchordpro
%{share}/lib/App/Music/ChordPro/Wx.pm
%{share}/lib/App/Music/ChordPro/Wx/
%{_mandir}/man1/wxchordpro*
%{_datadir}/applications/chordpro.desktop
%{_datadir}/pixmaps/chordpro.png
%{_datadir}/pixmaps/chordpro-doc.png
%{_metainfodir}/chordpro.metainfo.xml

%files abc
%doc README.ABC
%{share}/lib/App/Music/ChordPro/Delegate/ABC.pm

%files lilypond
%doc README.LilyPond
%{share}/lib/App/Music/ChordPro/Delegate/Lilypond.pm

%post gui
xdg-desktop-menu install --novendor %{share}/lib/App/Music/ChordPro/res/linux/chordpro.desktop
xdg-icon-resource install --context mimetypes --size 256 %{share}/lib/App/Music/ChordPro/res/icons/chordpro-doc.png x-chordpro-doc
xdg-mime install --novendor %{share}/lib/App/Music/ChordPro/res/linux/chordpro.xml
update-desktop-database
update-mime-database %{_datadir}/mime
gtk-update-icon-cache %{_datadir}/icons/hicolor

%postun
[ $1 = 0 ] && rm -rf %{share}

%postun gui
if [ $1 = 0 ]; then
xdg-icon-resource uninstall --context mimetypes --size 256 x-chordpro-doc
fi
update-desktop-database
update-mime-database %{_datadir}/mime
gtk-update-icon-cache %{_datadir}/icons/hicolor

%changelog
* Thu Dec 29 2022 Johan Vromans <jvromans@squirrel.nl> - 6.000-1
- Upgrade to upstream.

* Tue Nov 08 2022 Johan Vromans <jvromans@squirrel.nl> - 5.990-2
- Remove some experimental stuff from being installed.

* Fri Nov 04 2022 Johan Vromans <jvromans@squirrel.nl> - 5.990-1
- Upgrade to upstream.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.987-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.987-2
- Perl 5.36 rebuild

* Tue Feb 08 2022 Johan Vromans <jvromans@squirrel.nl> - 5.987-1
- Upgrade to upstream.

* Fri Feb 04 2022 Johan Vromans <jvromans@squirrel.nl> - 5.986-1
- Upgrade to upstream.
- Split ABC and LilyPond support into separate packages.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.982-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Johan Vromans <jvromans@squirrel.nl> - 5.982-1
- Upgrade to upstream.
- Split GUI into separate package.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.977-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.977-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.977-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Johan Vromans <jvromans@squirrel.nl> - 0.977.1-1
- Upgrade to upstream.

* Thu Aug 13 2020 Johan Vromans <jvromans@squirrel.nl> - 0.975.1-8
- Upgrade to upstream.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.974.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.974.1-6
- Perl 5.32 rebuild

* Mon Mar 23 2020 Johan Vromans <jvromans@squirrel.nl> - 0.974.1-5
- Add perl(Hash::Util) build dep for Rawhide.

* Sun Mar 22 2020 Johan Vromans <jvromans@squirrel.nl> - 0.974.1-4
- Incorporate reviewer feedback.
- Upgrade to upstream.

* Thu Feb 27 2020 Johan Vromans <jvromans@squirrel.nl> - 0.974-3
- Incorporate reviewer feedback.

* Tue Feb 25 2020 Johan Vromans <jvromans@squirrel.nl> - 0.974-2
- Incorporate reviewer feedback.

* Sun Feb 02 2020 Johan Vromans <jvromans@squirrel.nl> - 0.974-1
- Initial Fedora package.
