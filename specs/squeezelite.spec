%global forgeurl https://github.com/ralph-irving/squeezelite/
%global commit   72e1fd8abfa9b2f8e9636f033247526920878718
%forgemeta


Name:            squeezelite
Version:         2.0.0.1541
Release:         %autorelease
Summary:         Headless music player for streaming from Lyrion Music Server

# Squeezelite is released under the GPLv3 licence.
# It incorporates dsd2pcm, which is BSD licenced.
License:         GPL-3.0-only AND BSD-2-Clause-Views

URL:             https://lyrion.org/players-and-controllers/squeezelite/
Source0:         %{forgesource}
Source1:         %{name}.system.service
Source2:         %{name}.user.service
Source3:         %{name}.service.7.md
Source4:         %{name}.sysconfig
Source5:         org.lyrion.%{name}.metainfo.xml
Source6:         https://raw.githubusercontent.com/CDrummond/squeezelite/refs/tags/0.8.0/fastlane/metadata/android/en-US/images/icon.png


BuildRequires:   /usr/bin/appstream-util
BuildRequires: make
BuildRequires:   alsa-lib-devel
BuildRequires:   faad2-devel
BuildRequires:   ffmpeg-free-devel
BuildRequires:   flac-devel
BuildRequires:   gcc
BuildRequires:   libgpiod-devel >= 2
BuildRequires:   libmad-devel
BuildRequires:   libogg-devel
BuildRequires:   libvorbis-devel
BuildRequires:   lirc-devel
BuildRequires:   mpg123-devel
BuildRequires:   openssl-devel
BuildRequires:   opus-devel
BuildRequires:   opusfile-devel
BuildRequires:   pandoc
BuildRequires:   pulseaudio-libs-devel
BuildRequires:   soxr-devel
BuildRequires:   systemd

%{?systemd_requires}


%description
Squeezelite is a headless client for Lyrion Music Server, and can be
used in place of dedicated Squeezebox network music playing hardware.


%prep
%forgesetup

# Create a sysusers.d config file
cat >squeezelite.sysusers.conf <<EOF
u squeezelite - 'Squeezelite headless streaming music client' %{_sharedstatedir}/%{name} -
m squeezelite audio
EOF


%build
%set_build_flags

export OPTS="-DDSD -DLINKALL -DRESAMPLE -DVISEXPORT -DIR -DGPIO -DRPI -DFFMPEG -DUSE_LIBOGG -DUSE_SSL -DOPUS"
%make_build CPPFLAGS+="-I%{_includedir}/ffmpeg" CPPFLAGS+="-I%{_includedir}/ogg" CPPFLAGS+="-I%{_includedir}/opus" EXECUTABLE=%{name}-alsa
%make_build clean

export OPTS="$OPTS -DPULSEAUDIO"
%make_build CPPFLAGS+="-I%{_includedir}/ffmpeg" CPPFLAGS+="-I%{_includedir}/ogg" CPPFLAGS+="-I%{_includedir}/opus" EXECUTABLE=%{name}-pulse

pandoc --to=man --standalone --output=%{name}.service.7 %{SOURCE3}


%install
install -p -D -t %{buildroot}/%{_bindir} %{name}-alsa
ln -s %{name}-alsa %{buildroot}/%{_bindir}/%{name}
install -p -D -t %{buildroot}/%{_bindir} %{name}-pulse
install -p -D -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}/%{_userunitdir}/%{name}.service
install -p -D -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install -p -D -t %{buildroot}/%{_mandir}/man1 -m 0644 doc/%{name}.1
install -p -D -t %{buildroot}/%{_mandir}/man7 -m 0644 %{name}.service.7
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}
install -p -D -m 0644 %{SOURCE5} \
        %{buildroot}/%{_metainfodir}/org.lyrion.%{name}.metainfo.xml
install -p -D -m 0644 %{SOURCE6} \
        %{buildroot}/%{_datadir}/icons/hicolor/512x512/%{name}.png

install -m0644 -D squeezelite.sysusers.conf %{buildroot}%{_sysusersdir}/squeezelite.conf


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %attr(-,%{name},%{name}) %{_sharedstatedir}/%{name} 
%doc %{_mandir}/*/*
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-alsa
%{_bindir}/%{name}-pulse
%{_unitdir}/%{name}.service
%{_userunitdir}/%{name}.service
%{_sysusersdir}/squeezelite.conf
%{_datadir}/icons/hicolor/512x512/%{name}.png
%{_metainfodir}/org.lyrion.%{name}.metainfo.xml


%post
%systemd_post %{name}.service
%systemd_user_post %{name}.service


%preun
%systemd_preun %{name}.service
%systemd_user_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%changelog
%autochangelog
