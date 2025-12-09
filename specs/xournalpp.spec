%bcond cppunit  1
%bcond gtest 1
%bcond profiling 1
%bcond qpdf 1
%global forgeurl https://github.com/xournalpp/xournalpp

Name:           xournalpp
Version:        1.2.10
Release:        %autorelease
Summary:        Handwriting note-taking software with PDF annotation support
License:        GPL-2.0-or-later
%forgemeta
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  cmake >= 3.10
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  help2man
BuildRequires:  libappstream-glib

%if %{with cppunit}
BuildRequires:  pkgconfig(cppunit) >= 1.12
%endif
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
%if %{with gtest}
BuildRequires:  pkgconfig(gtest)
%endif
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.9
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0.0
BuildRequires:  pkgconfig(librsvg-2.0)
%if %{with profiling}
BuildRequires:  pkgconfig(libprofiler) >= 2.5
BuildRequires:  pkgconfig(libtcmalloc) >= 2.5
%endif
%if %{with qpdf}
BuildRequires:  pkgconfig(libqpdf) >= 10.6.0
%endif
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0
BuildRequires:  pkgconfig(libzip) >= 1.0.1
BuildRequires:  pkgconfig(lua) >= 5.3
BuildRequires:  pkgconfig(poppler-glib) >= 0.41
BuildRequires:  pkgconfig(portaudiocpp) >= 12
BuildRequires:  pkgconfig(sndfile) >= 1.0.25

Recommends:     texlive-latex-bin
Requires:       hicolor-icon-theme
Requires:       %{name}-plugins = %{version}-%{release}
Requires:       %{name}-ui = %{version}-%{release}

%description
Xournal++ is a handwriting note-taking application with PDF annotation support.
It is optimized for pen input such as Wacom tablets.

%package plugins
Summary:        Default plugins for %{name}
BuildArch:      noarch

%description plugins
This package contains sample plugins for %{name}.

%package ui
Summary:        User interface files for %{name}
BuildArch:      noarch

%description ui
This package contains user interface resources for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -DDISTRO_CODENAME="Fedora Linux" \
    -DENABLE_GTEST=%{with gtest} \
    -DENABLE_PROFILING=%{with profiling}

%cmake_build

%install
%cmake_install
%find_lang %{name}

# Remove unnecessary scripts and duplicate files
find %{buildroot} -name "*.sh" -delete
%fdupes %{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.github.%{name}.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.github.%{name}.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer
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

