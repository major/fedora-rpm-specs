%ifnarch s390x
%bcond_without check
%else
# some tests fail on s390x
%bcond_with check
%endif

%if 0%{?fedora} || 0%{?rhel} < 8
%bcond_without docs
%else
# TODO: package rubygem-asciidoctor
%bcond_with docs
%endif

%if 0%{?rhel} && 0%{?rhel} < 9
%undefine __cmake_in_source_build
%endif
%global __provides_exclude_from ^%{_libdir}/weechat/plugins/.*$

%if %{?_pkgdocdir:1}0
%if 0%{?rhel}
%global _doc %{name}-%{version}
%else
%global _doc %{name}
%endif
%else
%global _doc %{name}-%{version}
%global _pkgdocdir %{_docdir}/%{_doc}
%endif

Name:      weechat
Version:   3.5
Release:   %autorelease
Summary:   Portable, fast, light and extensible IRC client
Group:     Applications/Communications
URL:       http://weechat.org
License:   GPLv3

Source:    http://weechat.org/files/src/%{name}-%{version}.tar.xz
# /usr/bin/ld: CMakeFiles/charset.dir/charset.o:
# relocation R_X86_64_PC32 against symbol `weechat_charset_plugin'
# can not be used when making a shared object; recompile with -fPIC
Patch0:    weechat-1.0.1-plugins-fPIC.patch
Patch1:    weechat-3.4-tests-fPIC.patch
# this fails on too many tests, we want to let them finish anyway
Patch2:    weechat-3.4-disable-memleak-detection.patch

BuildRequires: gcc
%if %{with check}
BuildRequires: cpputest-devel
BuildRequires: glibc-langpack-en
%endif
%if %{with docs}
BuildRequires: asciidoctor
%endif
BuildRequires: ca-certificates
BuildRequires: cmake
BuildRequires: docbook-style-xsl
BuildRequires: enchant-devel
BuildRequires: gettext
BuildRequires: gnutls-devel
%if 0%{?fedora} >= 30 || 0%{?rhel} > 8
BuildRequires: guile22-devel
%else
BuildRequires: guile-devel
%endif
BuildRequires: libcurl-devel
BuildRequires: libgcrypt-devel
BuildRequires: lua-devel
BuildRequires: ncurses-devel
BuildRequires: perl-ExtUtils-Embed
BuildRequires: perl-devel
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: source-highlight
BuildRequires: tcl-devel
BuildRequires: libzstd-devel
%ifarch %{ix86} x86_64 %{arm}
# https://bugzilla.redhat.com/show_bug.cgi?id=1338728
# https://github.com/weechat/weechat/issues/360
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: v8-devel
%endif
%endif
BuildRequires: zlib-devel
%if 0%{?rhel}
BuildRequires: cmake3
%endif

Requires:      hicolor-icon-theme

%description
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

%package devel
Summary: Development files for weechat
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
WeeChat (Wee Enhanced Environment for Chat) is a portable, fast, light and
extensible IRC client. Everything can be done with a keyboard.
It is customizable and extensible with scripts.

This package contains include files and pc file for weechat.


%prep
%autosetup -p1 -n %{name}-%{version}
find doc/ -type f -name 'CMakeLists.txt' \
    -exec sed -i -e 's#${PROJECT_NAME}#%{_doc}#g' '{}' \;

sed -i 's/NAMES python3.7/NAMES python%{python3_version}m python%{python3_version}/' cmake/FindPython.cmake


%build
%cmake3 \
  -DPREFIX=%{_prefix} \
  -DLIBDIR=%{_libdir} \
  -DENABLE_ENCHANT=ON \
  -DENABLE_PYTHON3=ON \
  -DENABLE_PHP=OFF \
%if %{with check}
  -DENABLE_TESTS=ON \
%else
  -DENABLE_TESTS=OFF \
%endif
%if %{with docs}
  -DENABLE_DOC=ON \
  -DENABLE_MAN=ON \
%else
  -DENABLE_DOC=OFF \
  -DENABLE_MAN=OFF \
%endif
  -DENABLE_JAVASCRIPT=OFF \
  -DCA_FILE=/etc/pki/tls/certs/ca-bundle.crt \
  %{nil}
%cmake_build


%install
%cmake_install

%find_lang %name


%if %{with check}
%ctest -- -V
%endif


%files -f %{name}.lang
%doc AUTHORS.adoc ChangeLog.adoc Contributing.adoc
%doc README.adoc ReleaseNotes.adoc
%license COPYING
%{_bindir}/%{name}-curses
%{_bindir}/%{name}
%{_bindir}/%{name}-headless
%{_libdir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%if 0%{?fedora} || 0%{?rhel} < 8
%{_pkgdocdir}/weechat_*.html
%{_mandir}/man1/weechat.1*
%{_mandir}/*/man1/weechat.1*
%{_mandir}/man1/%{name}-headless.1*
%{_mandir}/*/man1/%{name}-headless.1*
%endif

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/weechat-plugin.h
%{_libdir}/pkgconfig/*.pc


%changelog
%autochangelog
