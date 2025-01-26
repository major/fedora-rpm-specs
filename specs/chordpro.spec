# -*- rpm-spec -*-

%global FullName App-Music-ChordPro

Name: chordpro
Summary: Print songbooks (lyrics + chords)
License: Artistic-2.0
Version: 6.070
Release: %autorelease
Source: https://cpan.metacpan.org/authors/id/J/JV/JV/%{FullName}-%{version}.tar.gz
Source1: README.ABC
Source2: README.LilyPond
Source3: README.WX
Source9: config.tmpl
Patch1: chordpro-abc.patch
Patch2: chordpro-fonts.patch
Obsoletes: chordpro-abc == 6.050.4
URL: https://www.chordpro.org

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

# This package would provide many (perl) modules, but these are
# not intended for general use.
%global __provides_exclude_from /*\\.pm$
%global __requires_exclude ChordPro|SVGPDF|JSON

Requires: perl(:VERSION) >= 5.26.0

Requires: perl(SVGPDF)                      >= 0.088
Requires: gnu-free-fonts-common
Requires: gnu-free-mono-fonts
Requires: gnu-free-sans-fonts
Requires: gnu-free-serif-fonts
Requires: perl(Data::Printer)               >= 1.001001
Requires: perl(File::HomeDir)               >= 1.004
Requires: perl(File::LoadLines)             >= 1.044
Requires: perl(FindBin)
Requires: perl(HarfBuzz::Shaper)	    >= 0.026
Requires: perl(Hash::Util)
Requires: perl(Image::Info)                 >= 1.41
Requires: perl(JSON::PP)                    >= 2.27203
Requires: perl(JSON::XS)                    >= 4.03
Requires: perl(LWP::Protocol::https)
Requires: perl(List::Util)                  >= 1.46
Requires: perl(Object::Pad)                 >= 0.78
Requires: perl(PDF::API2)                   >= 2.044
Requires: perl(Ref::Util)		    >= 0.204
Requires: perl(Scalar::Util)		    >= 1.63
Requires: perl(Storable)                    >= 3.08
Requires: perl(String::Interpolate::Named)  >= 1.03
Requires: perl(Text::Layout)                >= 0.038

# BuildRequires for ChordPro.
BuildRequires: desktop-file-utils
BuildRequires: gnu-free-fonts-common
BuildRequires: gnu-free-mono-fonts
BuildRequires: gnu-free-sans-fonts
BuildRequires: gnu-free-serif-fonts
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Data::Printer)               >= 1.001001
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)         >= 7.24
BuildRequires: perl(File::HomeDir)               >= 1.004
BuildRequires: perl(File::LoadLines)             >= 1.021
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(HarfBuzz::Shaper)
BuildRequires: perl(Hash::Util)
BuildRequires: perl(Image::Info)                 >= 1.41
BuildRequires: perl(JSON::PP)                    >= 2.27203
BuildRequires: perl(JSON::XS)                    >= 4.03
BuildRequires: perl(List::Util)                  >= 1.33
BuildRequires: perl(Object::Pad)                 >= 0.78
BuildRequires: perl(PDF::API2)                   >= 2.044
BuildRequires: perl(Ref::Util)			 >= 0.204
BuildRequires: perl(Scalar::Util)		 >= 1.63
BuildRequires: perl(Storable)                    >= 3.08
BuildRequires: perl(String::Interpolate::Named)  >= 1.03
BuildRequires: perl(SVGPDF)                      >= 0.088
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Layout)                >= 0.038
BuildRequires: perl(base)
BuildRequires: perl(constant)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl-libs

%description
ChordPro will read a text file containing the lyrics of one or many
songs plus chord information. ChordPro will then generate a
photo-ready, professional looking, impress-your-friends sheet-music
suitable for printing on your nearest printer.

To learn more about ChordPro, look for the man page or do
chordpro --help for the list of options.

To use the integrated support for ABC, please install CPAN module
JavaScript::QuickJS.

For more information about ChordPro, see https://www.chordpro.org.

%package gui

Summary: ChordPro graphical user interface

Requires: %{name} = %{version}-%{release}
Requires: perl(Wx) >= 0.99

%description gui
This package installs the requirements for the wxWidgets (GUI) version
of ChordPro.

To run the GUI version it is better (though not strictly necessary) to
install an updated version of the perl Wx module. See
https://github.com/sciurius/wxPerl for instructions.

%package lilypond

Summary: Support for ChordPro LilyPond embedding

Requires: %{name} = %{version}-%{release}
Requires: lilypond

%description lilypond
This packages installs the requirements for LilyPond support for ChordPro.

%prep
%setup -q -n %{FullName}-%{version}

%patch -P 1 -p0 -b .abc
%patch -P 2 -p0 -b .fonts

# Update outdated READMEs.
cp -a %{SOURCE1} .
cp -a %{SOURCE2} .
cp -a %{SOURCE3} .

# Add possible missing file.
test -f lib/ChordPro/res/config/config.tmpl \
     || cp -a %{SOURCE9} lib/ChordPro/res/config/config.tmpl

# Remove some stuff.
rm lib/ChordPro/res/linux/setup_desktop.sh
# LaTeX (not yet supported).
rm lib/ChordPro/Output/LaTeX.pm
rm lib/ChordPro/res/templates/*.tt
rm t/74_latex.t
# MarkDown (not yet supported).
rm lib/ChordPro/Output/Markdown.pm
rm t/73_md.t
# Use system package.
rm -fr lib/ChordPro/lib/SVGPDF*
# Fonts (use system fonts).
rm lib/ChordPro/res/fonts/Free*.ttf

%build

# Main build.
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
    lib/ChordPro/res/icons/chordpro.png \
    lib/ChordPro/res/icons/chordpro-doc.png \
    %{buildroot}%{_datadir}/pixmaps/
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    lib/ChordPro/res/linux/%{name}.desktop

mkdir -p %{buildroot}%{_metainfodir}
cp -p lib/ChordPro/res/linux/%{name}.metainfo.xml \
    %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%{_fixperms} %{buildroot}/*
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

# End of install section.

%files
%doc Changes README.md README.ABC
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/chordpro
%{share}/lib/ChordPro.pm
%{share}/lib/ChordPro
%exclude %{share}/lib/ChordPro/Wx.pm
%exclude %{share}/lib/ChordPro/Wx
%{_mandir}/man1/chordpro*
# Exclude Lilypond files.
%exclude %{share}/lib/ChordPro/Delegate/Lilypond.pm

%files gui
%doc README.WX
%{_bindir}/wxchordpro
%{share}/lib/ChordPro/Wx.pm
%{share}/lib/ChordPro/Wx
%{_mandir}/man1/wxchordpro*
%{_datadir}/applications/chordpro.desktop
%{_datadir}/pixmaps/chordpro.png
%{_datadir}/pixmaps/chordpro-doc.png
%{_metainfodir}/chordpro.metainfo.xml

%files lilypond
%doc README.LilyPond
%{share}/lib/ChordPro/Delegate/Lilypond.pm

%post gui
xdg-desktop-menu install --novendor %{share}/lib/ChordPro/res/linux/chordpro.desktop
xdg-icon-resource install --context mimetypes --size 256 %{share}/lib/ChordPro/res/icons/chordpro-doc.png x-chordpro-doc
xdg-mime install --novendor %{share}/lib/ChordPro/res/linux/chordpro.xml
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
%autochangelog
