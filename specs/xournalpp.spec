%global         __cmake_in_source_build 0
%global         with_cppunit 1
%global	        gtest 1
%global         profiling 1

Name:           xournalpp
Version:        1.2.6
Release:        %autorelease
Summary:        Handwriting note-taking software with PDF annotation support
License:	GPL-2.0-or-later
URL:            https://github.com/%{name}/%{name}
Source:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.10
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  help2man
BuildRequires:  libappstream-glib
%if 0%{?with_cppunit}
BuildRequires:  pkgconfig(cppunit) >= 1.12-0
%endif
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
%if 0%{?gtest}
BuildRequires:  pkgconfig(gtest)
%endif
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.9
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0.0
BuildRequires:  pkgconfig(librsvg-2.0)
%if 0%{?profiling}
BuildRequires:  pkgconfig(libprofiler) >= 2.5
BuildRequires:  pkgconfig(libtcmalloc) >= 2.5
%endif
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0.0
BuildRequires:  pkgconfig(libzip) >= 1.0.1
BuildRequires:  pkgconfig(lua) >= 5.3
BuildRequires:  pkgconfig(poppler-glib) >= 0.41.0
BuildRequires:  pkgconfig(portaudiocpp) >= 12
BuildRequires:  pkgconfig(sndfile) >= 1.0.25
Recommends:     texlive-latex-bin
Requires:       hicolor-icon-theme
Requires:       %{name}-plugins = %{version}-%{release}
Requires:       %{name}-ui = %{version}-%{release}

%description
Xournal++ is a handwriting note-taking software with PDF annotation support.
Supports Pen input like Wacom Tablets

%package	plugins
Summary:        Default plugin for %{name}
BuildArch:      noarch

%description	plugins
The %{name}-plugins package contains sample plugins for  %{name}.

%package	ui
Summary:        User interface for %{name}
BuildArch:      noarch

%description	ui
The %{name}-ui package contains a graphical user interface for  %{name}.


%prep
%autosetup -p1

%build
%cmake \
        -DDISTRO_CODENAME="Fedora Linux" \
        -DENABLE_GTEST=%{gtest} \
        -DENABLE_PROFILING=%{profiling}

%cmake_build

%install
%cmake_install

%find_lang %{name}

# REMOVE UNNECESSARY SCRIPTS
find %{buildroot}%{_datadir}/%{name} -name update-icon-cache.sh -delete -print
%fdupes %{buildroot}%{_datadir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.github.%{name}.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.github.%{name}.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}-thumbnailer
%{_bindir}/%{name}
%{_datadir}/applications/com.github.%{name}.%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.github.%{name}.%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/*
%{_datadir}/mime/packages/com.github.%{name}.%{name}.xml
%{_datadir}/thumbnailers/com.github.%{name}.%{name}.thumbnailer
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources/*_template.tex
%{_mandir}/man1/%{name}*.gz
%{_metainfodir}/com.github.%{name}.%{name}.appdata.xml

%files plugins
%{_datadir}/%{name}/plugins

%files ui
%{_datadir}/%{name}/ui

%changelog
%autochangelog
