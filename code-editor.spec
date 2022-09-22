Name:           code-editor
Version:        2.8.1
Release:        29%{?dist}
Summary:        Lightweight and cross-platform text and code editor based on Qt Creator

License:        LGPLv2
URL:            http://qt.gitorious.org/~ilyesgouta/qt-creator/code-editor
Source0:        code-editor-src-20140511.tar.bz2

Source1:        code-editor.desktop

Requires:       hicolor-icon-theme
Requires:       xdg-utils

BuildRequires:  desktop-file-utils
BuildRequires:  botan-devel qtsingleapplication-devel

BuildRequires: qt4-devel >= 4.8
BuildRequires: make
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

# see https://bugzilla.redhat.com/show_bug.cgi?id=652971
%{?filter_setup:
%filter_provides_in %_libdir/code-editor/
%filter_from_requires /\(libAggregation\|libCPlusPlus\|libExtensionSystem\|libLanguageUtils\|libQtConcurrent\|libUtils\|libDebuggingHelper\|libptracepreload\|libQtcSsh\)\.so.*/d
%filter_from_requires /\(libBinEditor\|libClassView\|libCore\|libCppEditor\|libCppTools\|libDiffEditor\|libFakeVim\|libFind\|libGit\|libLocator\|libProjectExplorer\|libTaskList\|libTextEditor\|libVcsBase\)\.so.*/d
%filter_setup
}

%description
CodeEditor is a slimmed down, customized version of Qt Creator that focuses on bringing
its text/code modern editing capabilities to users looking for just a simple and beautiful editor.

%prep
%setup -q -n %{name}

%build
%{qmake_qt4} code-editor.pro IDE_LIBRARY_BASENAME=%{_lib} USE_SYSTEM_BOTAN=1
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}%{_prefix}

desktop-file-install                                    \
--add-category="Development"                            \
--dir=%{buildroot}%{_datadir}/applications              \
%{SOURCE1}

rm -rf %{buildroot}%{_datadir}/code-editor/translations
rm -rf %{buildroot}%{_datadir}/code-editor/templates
rm -rf %{buildroot}%{_datadir}/code-editor/snippets
rm -rf %{buildroot}%{_datadir}/code-editor/rss
rm -rf %{buildroot}%{_datadir}/code-editor/qmlicons
rm -rf %{buildroot}%{_datadir}/code-editor/qmldesigner
rm -rf %{buildroot}%{_datadir}/code-editor/qml
rm -rf %{buildroot}%{_datadir}/code-editor/gdbmacros
rm -rf %{buildroot}%{_datadir}/code-editor/designer
rm -rf %{buildroot}%{_datadir}/code-editor/qml-type-descriptions
rm -rf %{buildroot}%{_datadir}/doc
rm -f %{buildroot}%{_bindir}/qtcreator_process_stub
rm -f %{buildroot}%{_bindir}/qtpromaker

%files
%doc README LICENSE.LGPL LGPL_EXCEPTION.TXT
%{_bindir}/code-editor
%{_libdir}/code-editor/
%{_datadir}/code-editor/
%{_datadir}/icons/hicolor/*/*/codeeditor.*
%{_datadir}/applications/code-editor.desktop

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.1-19
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.8.1-16
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 08 2016 Rex Dieter <rdieter@fedoraproject.org> 2.8.1-13
- rebuild (botan)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.8.1-11
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.8.1-9
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Ilyes Gouta <ilyes.gouta@gmail.com> - 2.8.1-6
- Bugzilla 1091671: unbundle qtsingleapplication and qtlockedfile

* Sun Nov 17 2013 Ilyes Gouta <ilyes.gouta@gmail.com> - 2.8.1-5
- Bump release version for fixing f19 build

* Tue Oct 15 2013 Ilyes Gouta <ilyes.gouta@gmail.com> - 2.8.1-3
- Rebased on origin-2.8 7165378
- Fix a crash on codestylesettings when closing the editor

* Tue Oct 01 2013 Dan Horák <dan[at]danny.cz> - 2.8.1-2
- use system botan (see also #912367)

* Sun Sep 29 2013 Ilyes Gouta <ilyes.gouta@gmail.com> - 2.8.1-1
- Rebased on Qt Creator v2.8.1 (a1fbcf7)
- Fixed previous spec versions 2 and 8 release dates

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 21 2012 Ilyes Gouta <ilyes.gouta@gmail.com> - 2.3.1-13
- Disable unused plugins causing build failures following Fedora_17_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Ilyes Gouta <ilyes.gouta@gmail.com> - 11
- Rebased against a recent Qt Creator code base v2.3.1-5-gdd324e0

* Thu Oct 13 2011 Ilyes Gouta <ilyes.gouta@gmail.com> - 10
- Imported in Fedora's SCM, bumped release number for building in Koji

* Sat Sep 03 2011 Ilyes Gouta <ilyes.gouta@gmail.com> - 9
- Rebased against a recent Qt Creator code base v2.3.0-9-g204f6bc

* Mon Aug 29 2011 Ilyes Gouta <ilyes.gouta@gmail.com> - 8
- Rebased against a recent Qt Creator code base v2.3.0-rc-60-gbc7abeb

* Sun Jul 24 2011 Ilyes Gouta <ilyes.gouta@gmail.com> - 7
- Rebased against a recent Qt Creator code base v2.3.0-beta-332-g0f38dba

* Sun Jul 17 2011 Ilyes Gouta <ilyes.gouta@gmail.com> - 6
- Rebased against a recent Qt Creator code base v2.3.0-beta-190-gfcf2dfa

* Sat Mar 19 2011 Ilyes Gouta <ilyes.gouta@gmail.com> - 5
- Rebased against a recent Qt Creator code base v2.2.1-1510-g79c2e22

* Sat Mar 19 2011 Ilyes Gouta <ilyes.gouta@gmail.com> - 4
- Rebased against a recent Qt Creator code base - commit f671b30

* Fri Dec 31 2010 Ilyes Gouta <ilyes.gouta@gmail.com> - 3
- Rebased against a recent Qt Creator code base v2.1.0-rc1-1374-gd963563

* Mon Nov 08 2010 Ilyes Gouta <ilyes.gouta@gmail.com> - 2
- Packaged for Fedora 14

* Wed Oct 06 2010 Ilyes Gouta <ilyes.gouta@gmail.com> - 1
- First package for Fedora
