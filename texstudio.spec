Name:           texstudio
Version:        4.3.1
Release:        1%{?dist}

Summary:        A feature-rich editor for LaTeX documents
# texstudio binary: GPLv3 due to static linkage of bundled qcodeedit
# texstudio data and image files: GPLv2+
License:        GPLv2+ and GPLv3
URL:            https://www.texstudio.org

Source0:        https://github.com/texstudio-org/texstudio#/archive/%{name}-%{version}.tar.gz
Source1:        texstudio.desktop
Patch1:         texstudio-use-system-qtsingleapplication-instead-of-bundled-on.patch
Patch2:         texstudio-disable-update-check.patch
# don't muck with default build flags
Patch3:         texstudio-wtf_flags.patch

BuildRequires: make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttools-static
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  hunspell-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  poppler-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  poppler-cpp-devel
BuildRequires:  qtsingleapplication-devel
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  qtsinglecoreapplication-devel
BuildRequires:  qtsinglecoreapplication-qt5-devel
BuildRequires:  qtermwidget-devel
BuildRequires:  quazip-qt5-devel
BuildRequires:  zlib-devel

Requires:       tex(latex)
Requires:       tex(preview.sty)
Requires:       tex-dvipng
Requires:       qt5-qtsvg
Requires:       qtermwidget
Provides:       bundled(qcodeedit) 
Provides:       texmakerx = %{version}-%{release}
Obsoletes:      texmakerx < 2.2-1
%description
TeXstudio gives you an environment where you can 
easily create and manage LaTeX documents.
It provides modern writing support, like interactive spell checking, 
code folding, syntax highlighting, integrated pdf viewer
and various assistants. 
Also it serves as a starting point from where you can easily run 
all necessary LaTeX tools.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .qtsingle
%patch2 -p1 -b .update_check
%patch3 -p1 -b .wtf_flags

rm -rf {hunspell,qtsingleapplication,quazip}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} \
%ifnarch %{ix86} x86_64 %{arm}
    NO_CRASH_HANDLER=1 \
%endif
    USE_SYSTEM_HUNSPELL=1 \
    USE_SYSTEM_QTSINGLEAPPLICATION=1 \
    INTERNAL_TERMINAL=1 \
    USE_SYSTEM_QUAZIP=1 QUAZIP_LIB=-lquazip5 QUAZIP_INCLUDE=%{_includedir}/quazip5/ \
    ../texstudio.pro
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT -C %{_target_platform}

install -Dp -m 0644 utilities/texstudio16x16.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio22x22.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio32x32.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio48x48.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio64x64.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/46x46/apps/texstudio.png


rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,COPYING,*.desktop,tex*.png,CHANGELOG.txt}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{*.dic,*.aff}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/qt_*.qm

%find_lang %{name} --with-qt

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files -f %{name}.lang
%{_bindir}/texstudio
%dir %{_datadir}/texstudio/
%{_datadir}/texstudio/*.png
%{_datadir}/texstudio/usermanual.css
%{_datadir}/texstudio/latex2e.*
%{_datadir}/texstudio/*.stopWords
%{_datadir}/texstudio/*.stopWords.level2
%{_datadir}/texstudio/de_DE.badWords
%{_datadir}/texstudio/template_*.tex
%{_datadir}/texstudio/template_*.zip
%{_datadir}/texstudio/*.json
%{_datadir}/texstudio/*.js
%{_datadir}/texstudio/th_*.dat
%{_datadir}/texstudio/usermanual_*.html
%{_datadir}/applications/texstudio.desktop
%{_datadir}/metainfo/texstudio.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg

%doc utilities/AUTHORS utilities/COPYING utilities/manual/CHANGELOG.txt

%changelog
* Fri Aug 26 2022 Johannes Lips <hannes@fedoraproject.org> 4.3.1-1
- Update to latest upstream release 4.3.1

* Mon Aug 08 2022 Johannes Lips <hannes@fedoraproject.org> 4.3.0-1
- Update to latest upstream release 4.3.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 23 2022 Johannes Lips <hannes@fedoraproject.org> 4.2.3-1
- Update to latest upstream release 4.2.3

* Mon Apr 18 2022 Miro Hrončok <mhroncok@redhat.com> - 4.2.2-2
- Rebuilt for quazip 1.3

* Sun Feb 20 2022 Johannes Lips <hannes@fedoraproject.org> 4.2.2-1
- Update to latest upstream release 4.2.2

* Fri Jan 28 2022 Johannes Lips <hannes@fedoraproject.org> 4.2.1-1
- Update to latest upstream release 4.2.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Johannes Lips <hannes@fedoraproject.org> 4.2.0-1
- Update to latest upstream release 4.2.0

* Mon Jan 03 2022 Ian McInerney <ian.s.mcinerney@ieee.org> 4.0.4-2
- Rebuild due to qtermwidget soname bump (fixes rhbz: 2036642)

* Sun Nov 07 2021 Johannes Lips <hannes@fedoraproject.org> 4.0.4-1
- Update to latest upstream release 4.0.4

* Sat Oct 23 2021 Johannes Lips <hannes@fedoraproject.org> 4.0.2-1
- Update to latest upstream release 4.0.2

* Mon Oct 11 2021 Johannes Lips <hannes@fedoraproject.org> 4.0.1-1
- Update to latest upstream release 4.0.1

* Wed Sep 29 2021 Christian Dersch <lupinix@mailbox.org> - 4.0.0-2
- Use quazip-qt5, fix include and linker variables for quazip5

* Sun Sep 26 2021 Johannes Lips <hannes@fedoraproject.org> 4.0.0-1
- Update to latest upstream release 4.0.0

* Thu Aug 19 2021 Björn Esser <besser82@fedoraproject.org> - 3.1.2-3
- Rebuild (quazip)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Johannes Lips <hannes@fedoraproject.org> 3.1.2-1
- Update to latest upstream release 3.1.2

* Mon Feb 22 2021 Johannes Lips <hannes@fedoraproject.org> 3.1.1-1
- Update to latest upstream release 3.1.1

* Wed Feb 17 2021 Johannes Lips <hannes@fedoraproject.org> 3.1.0-1
- Update to latest upstream release 3.1.0

* Tue Feb 16 2021 Johannes Lips <hannes@fedoraproject.org> 3.0.5-1
- Update to latest upstream release 3.0.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Johannes Lips <hannes@fedoraproject.org> 3.0.4-2
- fixed runtime requirements for internal terminal

* Sat Jan 02 2021 Johannes Lips <hannes@fedoraproject.org> 3.0.4-1
- Update to latest upstream release 3.0.4

* Sun Sep 06 2020 Johannes Lips <hannes@fedoraproject.org> 3.0.1-2
- enabled internal terminal

* Wed Sep 02 2020 Johannes Lips <hannes@fedoraproject.org> 3.0.1-1
- Update to latest upstream release 3.0.1

* Tue Aug 25 2020 Johannes Lips <hannes@fedoraproject.org> 3.0.0-1
- Update to latest upstream release 3.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Johannes Lips <hannes@fedoraproject.org> 2.12.22-1
- Update to latest upstream bugfix release 2.12.22

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> 2.12.20-2
- Rebuild for poppler-0.84.0

* Tue Jan 14 2020 Johannes Lips <hannes@fedoraproject.org> 2.12.20-1
- Update to latest upstream bugfix release 2.12.20

* Thu Dec 26 2019 Johannes Lips <hannes@fedoraproject.org> 2.12.18-1
- Update to latest upstream bugfix release 2.12.18
