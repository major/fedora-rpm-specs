Name:           vokoscreenNG
Version:        3.4.0
Release:        %autorelease
Summary:        Powerful screencast creator in 41 languages to record the screen

License:        GPLv2
URL:            https://github.com/vkohaupt/vokoscreenNG
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# AppData manifest
Source1:        https://raw.githubusercontent.com/flathub/com.github.vkohaupt.%{name}/master/%{name}.appdata.xml

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make

BuildRequires:  cmake(Qt5) >= 5.14
BuildRequires:  cmake(Qt5LinguistTools) >= 5.14
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5X11Extras)

BuildRequires:  pkgconfig(gstreamermm-1.0)
BuildRequires:  pkgconfig(x11)

%description
vokoscreenNG for Windows and Linux is a powerful screencast creator in 41
languages to record the screen, an area or a window (Linux only). Recording of
audio from multiple sources is supported. With the built-in camera support,
you can make your video more personal. Other tools such as systray, magnifying
glass, countdown, timer, Showclick and Halo support will help you do a good
job.


%prep
%autosetup
mkdir -p src/%{_target_platform}


%build
pushd src/%{_target_platform}
%qmake_qt5 ..
popd
%make_build -C src/%{_target_platform}


%install
%make_install -C src/%{_target_platform}
install -Dpm 0755 src/%{_target_platform}/%{name} \
    %{buildroot}%{_bindir}/%{name}

# Desktop file
install -Dpm 0644 src/applications/%{name}.desktop \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

# AppData manifest
install -Dpm 0644 %{SOURCE1} -t %{buildroot}%{_metainfodir}/

# Icon
install -Dpm 0644 src/applications/%{name}.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING
%doc .github/README.md info-licences-changelog-install/CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_metainfodir}/*.xml


%changelog
%autochangelog
