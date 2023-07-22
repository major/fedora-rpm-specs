Name:		ibus-bogo

%global commit ce44b961de5a0f82a4a2d8fc0e487e8fcb29289d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Version:	0.4
Release:	30%{?dist}
Summary:	Vietnamese engine for IBus input platform

License:	GPLv3
URL:		http://github.com/BoGoEngine/ibus-bogo-python

Source0:	http://github.com/BoGoEngine/ibus-bogo-python/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# fix the run scripts folder to /usr/libexec since upstream developers put it in /usr/lib
Patch0:		ibus-bogo-fix-libexec-folder-name.patch
# patch to disable mouse dedector function
Patch1:		ibus-bogo-disable-mouse-detector-function.patch
Patch2:		ibus-bogo-crash-f22-bug-1204029.patch

BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	ibus-devel
BuildRequires:	python3-devel
BuildRequires:	python3-gobject
BuildRequires:	python3-PyQt4-devel
BuildRequires:	/usr/bin/lrelease-qt4

BuildArch:	noarch

Requires:	ibus
Requires:	python3
Requires:	python3-PyQt4
Requires:	python3-gobject
Requires:	libwnck3


%description
A Vietnamese engine for IBus input platform that uses BoGoEngine.


%prep
%setup -qn %{name}-python-%{commit}
%patch0 -p1
%patch1 -p1
%patch2 -p1 -b .3-resolving-crash-in-engine

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-install \
--add-category="Settings" \
--delete-original \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
${RPM_BUILD_ROOT}%{_datadir}/applications/ibus-setup-bogo.desktop

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/bogo.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>bogo.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>BoGo</name>
  <summary>Vietnamese input method</summary>
  <description>
    <p>
      The BoGo input method is designed for entering Vietnamese text.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">http://github.com/BoGoEngine/ibus-bogo-python</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <languages>
    <lang percentage="100">vi</lang>
  </languages>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF


%files
%doc README.md AUTHORS COPYING
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/ibus-setup-bogo.desktop
%{_datadir}/ibus/component/bogo.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_libexecdir}/%{name}/
%exclude %{_datadir}/%{name}/bogo/*.pyc
%exclude %{_datadir}/%{name}/bogo/*.pyo
%exclude %{_datadir}/%{name}/gui/*.pyc
%exclude %{_datadir}/%{name}/gui/*.pyo
%exclude %{_datadir}/%{name}/ibus_engine/*.pyc
%exclude %{_datadir}/%{name}/ibus_engine/*.pyo
%exclude %{_datadir}/%{name}/vncharsets/*.pyc
%exclude %{_datadir}/%{name}/vncharsets/*.pyo


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Parag Nemade <pnemade AT redhat DOT com> - 0.4-24
- Update for new cmake macros (out of source builds)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-18
- Drop Python 2 dependency (PyQt4 package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-16
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4-14
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4-11
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 16 2015 Richard Hughes <rhughes@redhat.com> - 0.4-8
- Increase AppStream search result weighting when using the 'vi' locale.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Pravin Satpute <psatpute@redhat.com> - 0.4-6
- Resolves bug #1204029 - Crashing in F22 Alpha with updates
- Patch from Fujiwara <tfujiwar@redhat.com>

* Wed Mar 25 2015 Richard Hughes <rhughes@redhat.com> - 0.4-5
- Register as an AppStream component.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.4-3
- Add cmake to BuildRequires.

* Thu Jan 23 2014 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.4-2
- Disable Mouse Detector function using Xlib.

* Wed Jan 22 2014 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.4-1
- Update to new release 0.4 from upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 6 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.3-5
- Add python3-gobject, libwnck3 as Requires.

* Mon Apr 29 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.3-4
- Add pyside-tools as a BuildRequires (missing).

* Wed Apr 24 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.3-3
- Add pyside-tools as a BuildRequires.
- Add BuildArch = noarch
- Add commands to update icon cache
- Add INSTALL="install -p" to preserve timestamps of installed files

* Mon Apr 22 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.3-2
- Add qt3-devel as a BuildRequires and qt3 as a Requires.

* Sat Mar 30 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.3-1
- Update to new release 0.3 from upstream.

* Mon Mar 25 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.2-11.eba2b22
- Update eba2b22 from develop branch (0.3-rc).

* Wed Mar 13 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.2-10.006cf12
- Remove BuildRoot and defattr and clean tags.
- Add comment for Patch1
- Update 006cf12 from develop branch.

* Wed Mar 13 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.2-9.a564b30
- Add a patch to fix the python2 version to run GUI settings because of
python3-pyside not available at this moment (obsolete).

* Wed Mar 13 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0.2-8.a564b30
- Update a564b30 from develop branch.
- Update release number to 0.2.x for more suitable with upstream.

* Mon Mar 11 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-7.d5b92ec
- Update d5b92ec from develop branch.

* Sat Mar 2 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-6.6b003a1
- Add a patch to fix the program files location to /usr/libexec.

* Sat Mar 2 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-5.6b003a1
- Update 6b003a1 from develop branch.

* Fri Mar 1 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-4.c65e3f9
- Update c65e3f9 from develop branch.

* Thu Feb 28 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-3.7163ca3
- Update 7163ca3 from develop branch.

* Wed Feb 27 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-2.2b8ffb4
- Update 2b8ffb4 from develop branch.

* Tue Feb 26 2013 Truong Anh Tuan <tuanta@iwayvietnam.com> - 0-1.92b2013
- Initial release getting from develop branch.

