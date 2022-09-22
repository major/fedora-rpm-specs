%global wingsdir $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{name}-%{version}


Name:           wings
Version:        2.2.9
Release:        1%{?dist}
Summary:        3D Subdivision Modeler
License:        MIT
URL:            http://www.wings3d.com
VCS:		scm:git:https://github.com/dgud/wings.git
Source0:	https://github.com/dgud/wings/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	https://sourceforge.net/projects/wings/files/manual/1.6.1/wings3d_manual1.6.1.pdf
Source3:	wings.png
Source4:	wings.desktop
Source5:	wings.sh
# Fedora/EPEL specific patch
Patch1:		wings-0001-Respect-CFLAGS.patch
# Adjust include paths
Patch2:		wings-0002-Fix-include-paths.patch
# Will be proposed to upstream
Patch3:		wings-0003-Don-t-assume-we-have-installed-Wings.patch
# Fedora/EPEL specific patch
Patch4:		wings-0004-Don-t-build-release.patch
Patch5:		wings-0005-Don-t-handle-external-dependencies.patch
Patch6:		wings-0006-add-igl-template-library.patch
%if 0%{?fedora} >= 37
Patch7:		wings-0007-Don-t-redefine-wx-macros.patch
%endif
BuildRequires:	desktop-file-utils
BuildRequires:	eigen3-devel
BuildRequires:	erlang-cl
BuildRequires:	erlang-erts
BuildRequires:	erlang-kernel
BuildRequires:	erlang-lfe
BuildRequires:	erlang-rpm-macros
BuildRequires:	erlang-stdlib
BuildRequires:	erlang-tools
BuildRequires:	erlang-wx
BuildRequires:	erlang-xmerl
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	make

Provides:       wings-povray = %{version}-%{release}
Obsoletes:      wings-povray


%description
Wings 3D is a subdivision modeler with an user interface that is easy
to use for both beginners and advanced users (inspired by Nendo and
Mirai from Izware).


%package docs
Summary:	Documentation for Wings 3D


%description docs
Documentation for Wings 3D.


%prep
%autosetup -p1
cp %{SOURCE1} .
cp %{SOURCE4} .
# Add version info
echo %{version} > ./version
# Setup link to eigen
ln -s %{_includedir}/eigen3 _deps/eigen


%build
# %%{?_smp_mflags} breaks the build
CFLAGS="%{optflags}" make unix


%install
# Install the wings binaries
mkdir -p %{wingsdir}/plugins/default
cp -rf ebin %{wingsdir}
cp -rf icons %{wingsdir}
cp -rf plugins/* %{wingsdir}/plugins/default
cp -rf priv %{wingsdir}
cp -rf shaders %{wingsdir}
cp -rf textures %{wingsdir}
cp intl_tools/tools.beam %{wingsdir}/ebin

# See - https://bugzilla.redhat.com/664148
rm -f %{wingsdir}/ebin/user_default.beam

find $RPM_BUILD_ROOT -name 'README' | xargs rm -f
find $RPM_BUILD_ROOT -name '*.txt' | xargs chmod 0644
find $RPM_BUILD_ROOT -name '*.auv' | xargs chmod 0644
find $RPM_BUILD_ROOT -name '*.fs' | xargs chmod 0644
find $RPM_BUILD_ROOT -name '*.vs' | xargs chmod 0644

# Install main startup script
install -D -p -m 0755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/wings

# Install icon
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/pixmaps/wings.png

# Install desktop entry
desktop-file-install  \
    --add-category Graphics \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    wings.desktop

# Register as an application to be visible in the software center
install -D -p -m 0644 unix/wings.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%{_bindir}/wings
%{_libdir}/erlang/lib/%{name}-%{version}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%doc AUTHORS OLD-NOTES README.md README-22.txt README.jp
%license license.terms


%files docs
%doc wings3d_manual1.6.1.pdf


%changelog
* Wed Jul 20 2022 Peter Lemenkov <lemenkov@gmail.com> - 2.2.9-1
- Ver. 2.2.9

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Peter Lemenkov <lemenkov@gmail.com> - 2.2.7-1
- Ver. 2.2.7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.2.6.1-1
- Ver. 2.2.6.1

* Sun Apr 19 2020 Peter Lemenkov <lemenkov@gmail.com> - 2.2.5-1
- Ver. 2.2.5

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.2.4-3
- Rebuilt with fixed Rebar

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.2.4-1
- Ver. 2.2.4

* Mon Mar 25 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.2.3-1
- Ver. 2.2.3

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.2.1-1
- Ver. 2.1.7
- Fixes issues with Wayland (by forcing GDK to use X11 for now)

* Tue Nov 20 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.7-1
- Ver. 2.1.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.1.5-1
- Ver. 2.1.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 11 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.4-1
- Ver. 2.0.4

* Sat Apr 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.3-1
- Ver. 2.0.3

* Wed Apr  6 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.2-2
- Rebuild with Erlang 18.3

* Wed Feb 10 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.2-1
- Ver. 2.0.2
- Rebuild with Erlang 18.2.3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.5.3-3
- Add an AppData file for the software center

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.5.3-2
- Rebuild with Erlang 17.3.3

* Fri Aug 29 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.5.3-1
- Ver. 1.5.3
- Fix building with Erlang 17.x.x

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.5.2-4
- Rebuild with Erlang 17.2.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 27 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.5.2-2
- Ver. 1.5.2

* Sat Nov 02 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.5.1-1
- Ver. 1.5.1
- Dropped upstreamed patches
- Restored OpenCL support

* Fri Oct 25 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.4.1-8.git9a2473e
- Rebuild with new __erlang_drv_version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-7.git9a2473e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.4.1-6.git9a2473e
- Actually remove user_default.beam file from distribution (see rhbz #664148).

* Fri Mar 22 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.4.1-5.git9a2473e
- Added localizations (closes rhbz #698630).
- Added requires on Erlang driver's API version
- Remove user_defaults.beam file from distribution (see rhbz #664148).

* Fri Mar 15 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.4.1-4.git9a2473e
- Fixed missing function
- Cleaned up spec-file

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.4.1-3.git9a2473e
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2.git9a2473e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 10 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.4.1-1.git9a2473e
- Ver. 1.4.1.git9a2473e (post-release shapshot for 1.4.1)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec  9 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-3
- Explicitly use erl installed into /usr/bin

* Tue Nov 16 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-2
- Drop erlang-wx dependency
- Fixed startup failure (rhbz #653720)

* Mon Jul 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0
- Docs subpackage no longer requires main package

* Tue Aug 11 2009 Gerard Milmeister <gemi@bluewin.ch> - 1.0.1-1
- new release 1.0.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 30 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.99.05-2
- new release 0.99.05

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.99.02-2
- fix license tag

* Thu Mar 27 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.99.02-1
- new releae 0.99.02

* Sun Apr  8 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.98.36-1
- new version 0.98.36

* Thu Feb 15 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.98.32b-11
- add optflags (bugzilla 228925)

* Sun Dec 10 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.98.32b-10
- split off povray plug-in

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.98.32b-9
- Rebuild for FE6

* Wed Jun  7 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.98.32b-8
- revert to use erlang R10B

* Thu May 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.98.32b-7
- rebuilt for erlang R11B

* Thu Apr 27 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.98.32b-5
- split off docs package

* Tue Apr 25 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.98.32b-3
- build against erlang-esdl-devel

* Sun Dec 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.98.32b-1
- New Version 0.98.32b

* Sun Mar  6 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.98.27b-1
- New Version 0.98.27b

* Sun Feb 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:0.98.27a-1
- New Version 0.98.27a

* Mon Dec 27 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.98.26-0.fdr.1.b
- New Version 0.98.26b

* Sat Jul 17 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.98.24-0.fdr.1
- New Version 0.98.24

* Fri Jun  4 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.98.23a-0.fdr.1
- New Version 0.98.23a

* Thu May  6 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.98.22c-0.fdr.1
- New Version 0.98.22c

* Sun Apr 11 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.98.20c-0.fdr.1
- First Fedora release
