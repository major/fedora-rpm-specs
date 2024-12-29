%global forgeurl https://github.com/ralph-irving/squeezelite/
%global commit   262994a989dc29ce3be4390c57c6a43373dfdca2
%forgemeta

# Allow AAC to be played directly in the client rather than
# first being transcoded on the server.  Requires libraries not included
# in Fedora for legal reasons.
%bcond_with      faad


Name:            squeezelite
Version:         2.0.0.1517
Release:         %autorelease
Summary:         Headless music player for streaming from Lyrion Music Server

# Squeezelite is released under the GPLv3 licence.
# It incorporates dsd2pcm, which is BSD licenced.
License:         GPL-3.0-only AND BSD-2-Clause-Views

URL:             %{forgeurl}
Source0:         %{forgesource}
Source1:         %{name}.system.service
Source2:         %{name}.user.service
Source3:         %{name}.service.7.md
Source4:         %{name}.sysconfig

BuildRequires: make
BuildRequires:   alsa-lib-devel
%if %{with faad}
BuildRequires:   faad2-devel
%endif
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

Requires(pre):   shadow-utils
%{?systemd_requires}


%description
Squeezelite is a headless client for Lyrion Music Server, and can be
used in place of dedicated Squeezebox network music playing hardware.


%prep
%forgesetup


%build
%set_build_flags

export OPTS="-DDSD -DLINKALL -DRESAMPLE -DVISEXPORT -DIR -DGPIO -DRPI -DFFMPEG %{?!with_faad:-DNO_FAAD} -DUSE_LIBOGG -DUSE_SSL -DOPUS"
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


%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -G audio -d %{_sharedstatedir}/%{name} \
        -s /sbin/nologin -c "Squeezelite headless streaming music client" \
        %{name}
exit 0


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
