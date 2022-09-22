Name:       icebreaker
Version:    2.2.1
Release:    %autorelease
Summary:    An addictive action-puzzle game involving bouncing penguins
License:    GPLv2+

Source:     https://mattdm.org/icebreaker/2.2.x/icebreaker-%{version}.tar.xz
URL:        http://www.mattdm.org/icebreaker/

BuildRequires:  gcc, make
BuildRequires:  SDL-devel, SDL_mixer-devel
BuildRequires:  gawk, sed, grep
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
IceBreaker is an action-puzzle game in which you must capture penguins from
an Antarctic iceberg so they can be shipped to Finland, where they are
essential to a secret plot for world domination. To earn the highest Geek
Cred, trap them in the smallest space in the shortest time while losing the
fewest lives. IceBreaker was inspired by (but is far from an exact clone of)
Jezzball by Dima Pavlovsky.


%prep
%setup -q

%build
%set_build_flags
%make_build prefix=%{_prefix}

%install
%make_install prefix=%{buildroot}%{_prefix}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications icebreaker.desktop
mkdir %{buildroot}%{_datadir}/metainfo
cp -p metainfo.xml %{buildroot}%{_datadir}/metainfo/org.mattdm.icebreaker.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSE
%doc README README.themes TODO ChangeLog
%{_bindir}/icebreaker
%{_datadir}/applications/icebreaker.desktop
%{_datadir}/metainfo/org.mattdm.icebreaker.metainfo.xml
%{_datadir}/icebreaker/
%{_mandir}/man6/*


%changelog
%autochangelog
