%global debug_package %{nil}
%bcond_without  gui

Name:           ansifilter
Version:        2.19
Release:        1%{?dist}
Summary:        ANSI terminal escape code converter
License:        GPLv3+
URL:            http://www.andre-simon.de/doku/ansifilter/ansifilter.php
Source0:        http://www.andre-simon.de/zip/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
%if %{with gui}
Source1:        ansifilter.desktop
Source2:        http://www.andre-simon.de/img/af_icon.png
%endif

%description
Ansifilter handles text files containing ANSI terminal escape codes. The
command sequences may be stripped or be interpreted to generate formatted
output (HTML, RTF, TeX, LaTeX, BBCode).

%if %{with gui}
%package        gui
Summary:        GUI for %{name} based on Qt5
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel
BuildRequires: make

%description    gui
Ansifilter handles text files containing ANSI terminal escape codes. The
command sequences may be stripped or be interpreted to generate formatted
output (HTML, RTF, TeX, LaTeX, BBCode).

This is a GUI of %{name} based on Qt5.
%endif

%prep
%autosetup

# Preserve timestamps.
sed -i 's|install -m|install -pm|g' makefile

%if %{with gui}
# Remove pre-configured files which may cause errors during building.
rm -frv src/qt-gui/moc_*.cpp
rm -frv src/qt-gui/Makefile*
%endif

# CRLF quickfix
find . -type f -exec sed -i 's/\r$//' {} + -print

%build
# Upstream embeds the cli code in gui so no need to require cli to use GUI
# program, in order to achieve this we need to preserve the objects with -c.
%make_build CFLAGS+="%{optflags} -c" LDFLAGS="%{?__global_ldflags}"

%if %{with gui}
# %%_qt5_qmake will respect the redhat-rpm-config
%make_build all-gui QMAKE="%{_qt5_qmake}"
%endif

%install
%make_install

%if %{with gui}
make install-gui DESTDIR=%{buildroot}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:1}
install -pDm644 %{S:2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%endif

# Use %%doc and %%license to handle docs.
rm -frv %{buildroot}%{_docdir}

%files
%doc ChangeLog* README*
%license COPYING
%{_bindir}/ansifilter
%{_mandir}/man1/ansifilter.1*
%{_datadir}/bash-completion/completions/ansifilter
%{_datadir}/fish/vendor_completions.d/ansifilter.fish
%{_datadir}/zsh/site-functions/_ansifilter

%if %{with gui}
%files gui
%doc ChangeLog* README*
%license COPYING
%{_bindir}/ansifilter-gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ansifilter.*
%endif

%changelog
* Fri Mar 31 2023 Filipe Rosset <rosset.filipe@gmail.com> - 2.19-1
- Update to 2.19 fixes rhbz#2178834

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 05 2021 Filipe Rosset <rosset.filipe@gmail.com> - 2.18-1
- Update to 2.18 fixes rhbz#1925318

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.17-1
- Update to 2.17 fixes rhbz#1884414

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.15-3
- Update to 2.16 fixes rhbz#1796175

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Filipe Rosset <rosset.filipe@gmail.com> - 2.15-1
- Update to 2.15 fixes rhbz#1771191

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Filipe Rosset <rosset.filipe@gmail.com> - 2.14-1
- Updated to new 2.14 upstream version, fixes rhbz #1702469

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 01 2019 Filipe Rosset <rosset.filipe@gmail.com> - 2.13-1
- Updated to new 2.13 upstream version

* Thu Nov 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.12-1
- Updated to new 2.12 upstream version

* Sat Oct 27 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.11-1
- Updated to new 2.11 upstream version
- upstream changelog http://www.andre-simon.de/doku/ansifilter/en/changelog.php

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.10-2
- added gcc-c++ as BR

* Fri Mar 30 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.10-1
- Updated to new 2.10 upstream version, fixes rhbz #1552957

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.8-1
- Updated to new 2.8 upstream version, fixes rhbz #1463860
- Remove upstreamed patch

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.6-1
- Updated to new 2.6 upstream version, fixes rhbz #1463860
- Added patch to fix build issues with fpic and disable debug info packages

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Filipe Rosset <rosset.filipe@gmail.com> - 2.4-1
- Updated to new 2.4 upstream version, fixes rhbz #1409270

* Thu Nov 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.3-1
- Updated to new 2.3 upstream version, fixes rhbz #1380049

* Fri Sep 16 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.2-1
- Updated to new 2.2 upstream version, fixes rhbz #1376619

* Tue Sep 13 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.1-1
- Updated to new 2.1 upstream version, fixes rhbz #1352252 #1359434

* Mon Jul 04 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.18-1
- Updated to new 1.18 upstream version, fixes rhbz #1352252

* Tue May 24 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.17-1
- Updated to new 1.17 upstream version, fixes rhbz #1339022

* Wed May 18 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.16-1
- Updated to new 1.16 upstream version, build against qt5 instead of qt4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.12-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 31 2015 Christopher Meng <rpm@cicku.me> - 1.12-1
- Update to 1.12

* Mon Feb 16 2015 Christopher Meng <rpm@cicku.me> - 1.11-1
- Update to 1.11

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 Christopher Meng <rpm@cicku.me> - 1.8-2
- Correct the license.
- desktop file added for gui program.

* Mon Apr 21 2014 Christopher Meng <rpm@cicku.me> - 1.8-1
- Update to 1.8

* Tue Dec 31 2013 Christopher Meng <rpm@cicku.me> - 1.7-1
- Initial Package.
