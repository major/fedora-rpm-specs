Name:           sweep
Version:        0.9.3
Release:        32%{?dist}
Summary:        An audio editor and live playback tool
License:        GPLv2+
URL:            http://www.metadecks.org/software/sweep/index.html

Source:         http://prdownloads.sourceforge.net/sweep/%{name}-%{version}.tar.gz
Patch0:         sweep-0.9.3-multithread.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  libogg-devel
BuildRequires:  libmad-devel
BuildRequires:  sed
BuildRequires:  alsa-lib-devel
BuildRequires:  gtk2-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  speex-devel
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

%description
Sweep is an audio editor and live playback tool for GNU/Linux, BSD and
compatible systems. It supports many music and voice formats including
WAV, AIFF, Ogg Vorbis, Speex and MP3, with multichannel editing and
LADSPA effects plugins.


%package devel
Summary:        Development files for Sweep
Requires:       glib2-devel
Requires:       gtk2-devel

%description devel
Header files and libraries for Sweep development.


%prep
%setup -q
%patch0 -p1 -b .multithread
# fix for wrongly set plugin dir on 64-bit
sed -i 's/sweep_plugin_dir=.*/sweep_plugin_dir="$PACKAGE_PLUGIN_DIR"/' configure


%build
LDFLAGS="-lX11 -lgmodule-2.0"
export LDFLAGS
%configure --disable-rpath
make %{?_smp_mflags} V=1


%install
make DESTDIR=$RPM_BUILD_ROOT install

# rename binary and manpage because of name conflict with lam package
(cd $RPM_BUILD_ROOT%{_bindir}; mv sweep sweep-audio-editor)
(cd $RPM_BUILD_ROOT%{_mandir}/man1; 
  mv sweep.1 sweep-audio-editor.1
  sed -i -e 's|.B sweep|.B sweep-audio-editor|' sweep-audio-editor.1
)

cat > sweep.desktop << EOF
[Desktop Entry]
Name=Sweep
GenericName=Sound Editor
Comment=Audio editor and live playback tool
Exec=sweep-audio-editor
Icon=sweep.svg
Terminal=false
Type=Application
MimeType=audio/x-wav;audio/x-aiff;audio/x-aifc;application/ogg;audio/x-mp3;audio/mpeg;audio/basic
Encoding=UTF-8
X-Desktop-File-Install-Version=0.9.4
StartupWMClass=Sweep
EOF

rm -f $RPM_BUILD_ROOT%{_datadir}/applications/sweep.desktop
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
        --vendor fedora \
%endif
        --add-category Application \
        --add-category AudioVideo \
        --add-category AudioVideoEditing \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        sweep.desktop

find $RPM_BUILD_ROOT%{_libdir}/sweep -name "*.la" | xargs rm -f
find $RPM_BUILD_ROOT%{_libdir}/sweep -name "*.a" | xargs rm -f

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/sweep*
%{_libdir}/sweep
%{_datadir}/pixmaps/sweep.svg
%{_datadir}/sweep
%{_datadir}/applications/*
%{_mandir}/man*/*
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/plugin_writers_guide.txt


%files devel
%doc doc/plugin_writers_guide.txt
%{_includedir}/sweep


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.9.3-22
- Enable mp3 loading support

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.3-13
- Remove --vendor from desktop-file-install. https://fedorahosted.org/fesco/ticket/1077

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.3-12
- Fix FTBFS, cleanup spec

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.3-9
- Rebuild for new libpng

* Sun Feb 13 2011 Gérard Milmeister <gemi@bluewin.ch> - 0.9.3-8
- fix DSO problem, add -lX11 to LDFLAGS

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.3-6
- Update desktop file according to F-12 FedoraStudio feature

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  1 2009 Gerard Milmeister <gemi@bluewin.ch> - 0.9.3-4
- fix for crash while saving

* Sat Feb 28 2009 Gerard Milmeister <gemi@bluewin.ch> - 0.9.3-3
- fix for plugins on 64-bit platforms
- really enable alsa

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Apr 14 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.9.3-1
- new release 0.9.3

* Wed Feb  7 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.9.2-1
- new version 0.9.2

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.9.1-5
- Rebuild for FE6

* Sun Mar 26 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.9.1-3
- do not compile in experimental features

* Thu Mar 16 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.9.1-1
- new version 0.9.1

* Fri Jan 20 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.9.0-1
- new version 0.9.0

* Mon Oct  3 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.8.4-1
- First Fedora release

* Mon Mar  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.8.3-1
- First Fedora release
