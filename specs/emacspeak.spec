Summary: Emacs Speech interface
Name: emacspeak
Version: 60.0
Release: %autorelease
# main lisp files are GPL2+
License: GPL-2.0-or-later AND BSD-3-Clause
Source: https://github.com/tvraman/emacspeak/releases/download/%{version}/%{name}-%{version}.tar.bz2
URL: http://emacspeak.sourceforge.net/
BuildRequires: emacs
BuildRequires: espeak-ng-devel
BuildRequires: gcc-c++
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: texinfo
BuildRequires: tcl-devel < 1:9
BuildRequires: make
Requires: emacs(bin) >= %{_emacs_version}
Requires: tclx

%description
Emacspeak is a speech interface that allows visually impaired users to
interact independently and efficiently with the computer. Emacspeak has
dramatically changed how the author and hundreds of blind and visually
impaired users around the world interact with the personal computer and
the Internet. A rich suite of task-oriented speech-enabled tools provides
efficient speech-enabled access to the evolving semantic WWW.
When combined with Linux running on low-cost PC hardware,
Emacspeak/Linux provides a reliable, stable speech-friendly solution that
opens up the Internet to visually impaired users around the world.

%prep
# https://github.com/tvraman/emacspeak/issues/141
%setup -q

chmod a-x etc/COPYRIGHT

%build
# use set_build_flags when available for F27 etc
CXXFLAGS="${CXXFLAGS:-%__global_cxxflags}" ; export CXXFLAGS ; \
LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS
make emacspeak
make espeak


%install
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/emacspeak
cp -pr bash-utils etc lisp media servers sounds stumpwm xsl %{buildroot}%{_datadir}/emacs/site-lisp/emacspeak/

make -C servers/native-espeak install LIBPARENTDIR=%{buildroot}%{_libdir}
ln -sf %{_libdir}/emacspeak/servers/native-espeak/tclespeak.so %{buildroot}%{_datadir}/emacs/site-lisp/emacspeak/servers/native-espeak/

mkdir -p %{buildroot}%{_bindir}
sed -e "s/FLAVOR/emacs/" -e "s!ELCDIR!%{_datadir}/emacs/site-lisp/emacspeak!" etc/emacspeak.sh > %{buildroot}%{_bindir}/emacspeak
chmod 0755 %{buildroot}%{_bindir}/emacspeak

mkdir -p %{buildroot}%{_infodir}
cp -p info/*.info* %{buildroot}%{_infodir}

# remove unwanted data files
( cd %{buildroot}%{_datadir}/emacs/site-lisp/emacspeak
  rm etc/bootstrap.sh
  rm -r etc/pickup-c
  rm -r servers/*outloud*
  rm servers/mac
  rm servers/native-espeak/tclespeak.{cpp,o}
  rm etc/COPYRIGHT
  chmod a-x servers/.servers servers/tts-lib.tcl
  find \( -name .nosearch -o -name Makefile \) -delete
)

%files
%license etc/COPYRIGHT
%doc README*
%{_bindir}/emacspeak
%{_datadir}/emacs/site-lisp/emacspeak/
%{_libdir}/emacspeak
%{_infodir}/*


%changelog
%autochangelog
